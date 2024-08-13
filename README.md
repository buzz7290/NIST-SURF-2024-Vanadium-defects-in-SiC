# Confocal microscope and spectroscopy with Thorlabs Piezo Controllers, Santec Tunable Filter, and Swabian Time Tagger
## Background
Quantum network promises applications that are beyond the reach of classical network, including distributed quantum computing, secure quantum communication, and distributed quantum sensing. The major challenge in quantum network is developing intermediate nodes that could reliably distribute entangled photons over long distances. Among other solid-state qubit platforms, vanadium doped silicon carbide has emerged as a particularly attractive candidate for quantum nodes due to its telecom range emission, mature growth and fabrication technique, and long coherence time.   
    
Essential steps in full characterization of color centers in SiC include spatial mapping and determining resonant frequencies of the defects. Here we share Python codes specifically to control Thorlabs Piezo Controllers, Santec tunable filter, and Swabian Time Tagger for both 2d spatial mapping and spectroscopy. Additionally, data visualization MATALB codes are provided.

## What these codes will do
- 2d Spatial Mapping
- Spectroscopy
- Data Visualization
## Equipment:
- 3x Thorlabs Piezo Controllers KPZ101 (KPC101 preferred for closed-loop operation)
- 1x Thorlabs NanoMax Stage MAX311D
- 1x Swabian Instruments Time Tagger 20
- 1x Single Photon Detector (SPD)
- Santec Tunable Filter OTF-980 (O-Band)
- Optical cage systems
- Objective
## Setup:
![Confocal_setup](https://github.com/user-attachments/assets/a2afae36-5b12-409a-bf0f-a798d91bbbfd)


### Key Requirements
- Light must be properly focused on the sample and into the SPD.
- Appropriate modules must be downloaded in your Python environment.

## 2d Spatial Mapping Example Result
![4H-SiC_one](https://github.com/user-attachments/assets/45b78ec4-d306-40b9-b689-9d14731eca2a)

## Spectroscopy Example Result
![image](https://github.com/user-attachments/assets/5d878638-9ab2-40a4-aeda-fd9f6129baf1)

## References
[1] Calusine, Greg, Alberto Politi, and David D. Awschalom. "Cavity-enhanced measurements of defect spins in silicon carbide." Physical Review Applied 6.1 (2016): 014019.  
[2] Rančić, Miloš, et al. "Coherence time of over a second in a telecom-compatible quantum memory storage material." Nature Physics 14.1 (2018): 50-54. 
[3] Diler, Berk, et al. "Coherent control and high-fidelity readout of chromium ions in commercial silicon carbide." NPJ quantum information 6.1 (2020): 11.    
[4] Heremans, F. Joseph, Christopher G. Yale, and David D. Awschalom. "Control of spin defects in wide-bandgap semiconductors for quantum technologies." Proceedings of the IEEE 104.10 (2016): 2009-2023.  
[5] Ahn, Jonghoon, et al. "Extended spin relaxation times of optically addressed telecom defects in silicon carbide." arXiv preprint arXiv:2405.16303 (2024).   
[6] Babin, Charles, et al. "Fabrication and nanophotonic waveguide integration of silicon carbide colour centres with preserved spin-optical coherence." Nature materials 21.1 (2022): 67-73.   
[7] Wolfowicz, Gary, et al. "Quantum guidelines for solid-state spin defects." Nature Reviews Materials 6.10 (2021): 906-925.   
[8] Nagy, Roland, et al. "High-fidelity spin and optical control of single silicon-vacancy centres in silicon carbide." Nature communications 10.1 (2019): 1-8. 
[9] Nomura, Masahiro, et al. "Highly efficient optical pumping of photonic crystal nanocavity lasers using cavity resonant excitation." Applied physics letters 89.16 (2006).   
[10] Spindlberger, Lukas, et al. "Optical properties of vanadium in 4 H silicon carbide for quantum technology." Physical Review Applied 12.1 (2019): 014015.   
[11] Bayliss, S. L., et al. "Optically addressable molecular spins for quantum information processing." Science 370.6522 (2020): 1309-1312. 
[12] Tissot, Benedikt, and Guido Burkard. "Spin structure and resonant driving of spin-1/2 defects in SiC." Physical Review B 103.6 (2021): 064106. 
[13] Gottscholl, Andreas, et al. "Superradiance of spin defects in silicon carbide for maser applications." Frontiers in Photonics 3 (2022): 886354.    
[14] Cilibrizzi, Pasquale, et al. "Ultra-narrow inhomogeneous spectral distribution of telecom-wavelength vanadium centres in isotopically-enriched silicon carbide." Nature Communications 14.1 (2023): 8448.  
[15] Wolfowicz, Gary, et al. "Vanadium spin qubits as telecom quantum emitters in silicon carbide." Science advances 6.18 (2020): eaaz1192. 
