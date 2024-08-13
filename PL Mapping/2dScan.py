import os
import time
import clr
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import logging
from TimeTagger import createTimeTagger, Counter, freeTimeTagger, Countrate
from System import Decimal

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Load the Kinesis DLLs
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("C:\\Program Files\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.KCube.PiezoCLI.dll")
from Thorlabs.MotionControl.DeviceManagerCLI import DeviceManagerCLI
from Thorlabs.MotionControl.KCube.PiezoCLI import KCubePiezo

# Function to initialize and connect to the motor
def initialize_motor(serial_no):
    DeviceManagerCLI.BuildDeviceList()
    
    # create new device
    device = KCubePiezo.CreateKCubePiezo(serial_no)
    
    # connect
    device.Connect(serial_no)
    
    # begin polling and enable
    device.StartPolling(250)  # 250ms polling rate
    time.sleep(15)
    device.EnableDevice()
    time.sleep(0.25)  # Wait for device to enable
    if not device.IsSettingsInitialized():
        device.WaitForSettingsInitialized(10000)  # 10 second timeout
        assert device.IsSettingsInitialized() is True 
    # Load the device configuration
    device_config = device.GetPiezoConfiguration(serial_no)

    # This shows how to obtain the device settings
    device_settings = device.PiezoDeviceSettings
    
    # Get the maximum voltage output of the KPZ
    max_voltage = device.GetMaxOutputVoltage()  # This is stored as a .NET decimal
    
    # set zero point
    device.SetZero()
    return device, max_voltage 

# Function to set motor position
def set_position(device, position, max_voltage):
    
    # Go to a voltage
    dev_voltage = Decimal(float(position))
    print(f'Desired voltage {dev_voltage}')

    if dev_voltage <= max_voltage:
        device.SetOutputVoltage(dev_voltage)
        time.sleep(1.0)
        print(f'Actual Voltage {device.GetOutputVoltage()}')
    else:
        print(f'Voltage must be below or equal to {max_voltage}')
    
    
    device.SetOutputVoltage(Decimal(float(position)))
    
# Function to get counts from Swabian time tagger counter
def get_counts():
    #counter = Counter(tagger, [CH], binwidth=int(1e9), n_values=5000)
    count_rate = Countrate(tagger,[CH])
    time.sleep(30)  # Adjust sleep time to match your integration time
    rate = count_rate.getData()[0]
    return rate

# Define function for 2D scan with real-time plotting and data saving
def scan_2d(x_start, y_start, x_end, y_end, step_size, z_motor, z_position, output_file, max_voltage, iteration):
    set_position(z_motor, z_position, max_voltage)
    time.sleep(0.1)  # Wait for the Z motor to move to the position
    logging.info(f"Set Z position to: {z_position} micrometers")

    x_positions = np.arange(x_start, x_end, step_size)
    y_positions = np.arange(y_start, y_end, step_size)
    
    counts_matrix = np.zeros((len(y_positions), len(x_positions)))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    plt.ion()  # Turn on interactive mode

    # Open a text file to save data
    with open(output_file, 'w') as file:
        file.write('X Position (micrometers)\tY Position (micrometers)\tCounts\n')

        for j, y in enumerate(y_positions):
            set_position(y_motor, y, max_voltage)
            for i, x in enumerate(x_positions):
                set_position(x_motor, x, max_voltage)
                time.sleep(0.1)  # Wait for the motors to move to the position
                counts = get_counts()
                counts_matrix[j, i] = counts
                ax.clear()
                X, Y = np.meshgrid(x_positions, y_positions)
                ax.plot_surface(X, Y, counts_matrix, cmap='viridis')
                ax.set_xlabel('X Position (micrometers)')
                ax.set_ylabel('Y Position (micrometers)')
                ax.set_zlabel('Counts')
                #plt.pause(0.01)  # Allow the plot to update
                logging.info(f"Moved to position: ({x_motor.GetOutputVoltage()}, {y_motor.GetOutputVoltage()}, {z_motor.GetOutputVoltage()}), Counts/s: {counts}, iteration: {iteration}")
                # Save data to text file
                file.write(f'{x}\t{y}\t{counts}\n')

    plt.ioff()  # Turn off interactive mode
    plt.show()

if __name__ == '__main__':
    # Initialize Swabian Instruments Time Tagger
    tagger = createTimeTagger()
    CH = 1
    tagger.setInputDelay(CH, 0.7e6)
    tagger.setDeadtime(CH, 100000)
    tagger.setTriggerLevel(CH, 1)

    # Serial numbers for the motors
    x_motor_serial = "29252405"
    y_motor_serial = "29252395"
    z_motor_serial = "29252397"
    
    # Initialize the motors
    print('initializing x motor')
    x_motor, x_max = initialize_motor(x_motor_serial)
    print("initializing y motor")
    y_motor, y_max = initialize_motor(y_motor_serial)
    print("initializing z motor")
    z_motor, z_max = initialize_motor(z_motor_serial)
    max_voltage = max([x_max,y_max,z_max])

    # Define scan area and step size
    x_start = 0
    y_start = 0
    x_end = 75
    y_end = 75
    step_size = 3.947
    fixed_z_position = 0  # Fixed Z position in micrometers
    num_scans = 4        # Number of scans
    
    # Perform the 2D scan
    for i in range(num_scans):
        n=i
        output_file = f'4H_30s_1330nm_Filter_{n}.txt'
        scan_2d(x_start, y_start, x_end, y_end, step_size, z_motor, fixed_z_position, output_file, max_voltage, i+1)
    
    # initialize positions
    set_position(x_motor, 0, x_max)
    set_position(y_motor, 0, y_max)
    
    # Disable the motors after scanning
    x_motor.StopPolling()
    x_motor.Disconnect()
    y_motor.StopPolling()
    y_motor.Disconnect()
    z_motor.StopPolling()
    z_motor.Disconnect()

    # Free the Time Tagger resources
    freeTimeTagger(tagger)