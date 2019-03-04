# This template generates synthetic data (missing pixels) to use
# in testing the solution of Problem 3 in Assignment 6.
# Unknown pixels are defined by the array called "unknown".
# Obscured image is in the array U1.

import numpy as np
import matplotlib
matplotlib.use("TkAgg")     # for macOS
import matplotlib.pyplot as plt


# Read a sample image
U0 = plt.imread('bwicon.png')
m, n = U0.shape

# Create 50% mask of known pixels and use it to obscure the original
np.random.seed(7592)                 # seed the randonm number generator (for repeatability)
unknown = np.random.rand(m,n) < 0.5
U1 = U0*(1-unknown) + 0.5 *unknown



# Display images
plt.figure(1)
plt.subplot(1, 2, 1)
plt.imshow(U0, cmap='gray')
plt.title('Original image')
plt.subplot(1, 2, 2)
plt.imshow(U1, cmap='gray')
plt.title('Obscured image')
plt.show()

