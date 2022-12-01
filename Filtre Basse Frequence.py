# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 14:54:09 2022

@author: dubuc
"""

import numpy as np
from scipy.signal import filtfilt , butter , freqz
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams.update({'font.size': 12})


# Filter requirements.
order = 10
fs = 200       # sample rate, MHz
cutoff = 30  # desired cutoff frequency of the filter, MHz

# Get the filter coefficients so we can check its frequency response.
N = 10
Wn = 0.05
b, a = butter(N, Wn, 'low')

# Plot the frequency response.
w, h = freqz(b, a, fs=fs, worN=8000)
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(h), 'b')
#plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
#plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.grid()


# Demonstrate the use of the filter.
# First make some data to be filtered.
B0 = 1 #Tesla
B1 = 1.0e-3 #Tesla
hbar = 1.054571818e-34
gamma = 267.513e6 
f_n = 40.0
f_ref = 40.5
tau = 1500e-3
T = 10         # seconds
n = int(T * fs) # total number of samples
t = np.linspace(0, T, n, endpoint=False)
# "Noisy" data.  We want to recover the 1.2 Hz signal from this.
data = np.sin(2*np.pi*f_n*t)*np.exp(-t/tau)*np.cos(2*np.pi*f_ref*t)

# Filter the data, and plot both the original and filtered signals.
y = filtfilt(b, a, data)

plt.subplot(2, 1, 2)
plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=4, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()