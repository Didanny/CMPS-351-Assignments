import numpy as np
import matplotlib
matplotlib.use("TkAgg")     # for macOS
import matplotlib.pyplot as plt
import scipy.fftpack
import random

n = 2500
m = 250
fs = 8192                              # sampling frequency 
t = np.arange(n) / fs
y = ( np.sin(2*np.pi*521*t) + np.sin(2*np.pi*1233*t) ) /2.0

D = scipy.fftpack.dct(np.eye(n), norm='ortho').transpose()
k = sorted(random.sample(range(n), m)) # Pick m random points for the reconstruction
A = D[k, :]
b = y[k]

plt.figure(figsize=(10.24, 2.56))      # change aspect ratio of plot 
plt.plot(t[k], b, 'ko', markersize=1)  # plot data to use to reconstruct
plt.show()
