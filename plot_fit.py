##################################
####        Load Data         ####
##################################

import numpy as np
from numpy import genfromtxt

data = genfromtxt('freq_sweep.csv', delimiter=',', skip_header=1)
freq = data[0:300,0]
magnitude = data[0:300,1]
phase = data[0:300,2]

##################################
####        Curve Fit         ####
##################################

from scipy.optimize import curve_fit

# define variables to make curve-fitting easier
R = 500.0
C = 2e-9
L = 20e-3

w_0_intended = 1 / np.sqrt(L * C)
f_0_intended = w_0_intended / (2 * np.pi)
gamma_intended = R / L

def func(freq, gamma, resonant_freq):
    omega = 2 * np.pi * freq
    resonant_omega = 2 * np.pi * resonant_freq
    return 1 / np.sqrt(1 + (1 / (gamma * omega))**2 * (omega **2 - resonant_omega ** 2) ** 2)

# define limits for curve-fitting
gamma_lower = gamma_intended - 5000
gamma_upper = gamma_intended + 5000
f_0_lower = f_0_intended - 5000
f_0_upper = f_0_intended + 5000


popt, pcov = curve_fit(func, freq, magnitude, bounds=([gamma_lower, f_0_lower],[gamma_upper, f_0_upper]))
best_fit_gamma = popt[0]
best_fit_freq = popt[1]

##################################
####   Plot Data, and Fits    ####
##################################

import matplotlib.pyplot as plt

plt.plot(freq, magnitude, 'g-', label='Recorded Magnitude Response')
plt.plot(freq, func(freq, gamma_intended, f_0_intended), 'b-', label='Intended Magnitude Response')
plt.plot(freq, func(freq, best_fit_gamma, best_fit_freq), 'r-', label='Best Fit Magnitude Response')
plt.legend(loc='best')
plt.xscale("log")
plt.show()

print("Theoretical gamma = {}".format(gamma_intended))
print("Theoretical freq = {}".format(f_0_intended))
print("Best fit gamma = {}".format(best_fit_gamma))
print("Best fit freq = {}".format(best_fit_freq))