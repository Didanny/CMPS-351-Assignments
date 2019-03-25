import numpy as np
import matplotlib
matplotlib.use("TkAgg")     # for macOS
import matplotlib.pyplot as plt


np.random.seed(421)            # seed the random number generator
n = 100
p = 40

# Generate a random p-by-n matrix with independent rows
A = np.random.randn(p, n)

while np.linalg.matrix_rank(A) !=p : 
    print('generating another data set with independent rows')
    A = np.random.rand(p, n)

# Generate a random right hand side  
b = A @ np.random.randn(n)


