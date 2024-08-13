clear; close all; clc;
A = readmatrix('6H_1304-1316_201steps_20s.dat');

subplot(2,2,1)
X = A(:,1)';
Y = (A(:,2)'-min(A(:,2)))/max(A(:,2)'-min(A(:,2)));
plot(X,Y)
xlabel('Wavelength (nm)')
ylabel('PL (Arbt. Units)')