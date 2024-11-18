
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data
X = np.array([42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16])  # Position (mm)
B = np.array([45.0, 87.0, 136.4, 142.2, 143.8, 143.2, 143.9, 142.7, 144.0, 143.9, 143.2, 143.8, 142.8, 143.9])  # Magnetic Flux Density (mT)

# Sort data by X to ensure proper plotting
sorted_indices = np.argsort(X)
X = X[sorted_indices]
B = B[sorted_indices]

# Interpolation for smooth curve
X_smooth = np.linspace(X.min(), X.max(), 300)  # Generate smooth X values
B_smooth = make_interp_spline(X, B)(X_smooth)  # Smooth B values using spline interpolation

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(X, B, 'bo', label='Experimental Data')  # Data points
plt.plot(X_smooth, B_smooth, 'r-', label='Interpolated Curve')  # Smooth curve

# Set chart title and labels
plt.title('Magnetic Flux Density $B$ vs Horizontal Position $X$', fontsize=14)
plt.xlabel('Horizontal Position $X$ (mm)', fontsize=12)
plt.ylabel('Magnetic Flux Density $B$ (mT)', fontsize=12)

# Show legend
plt.legend()

# Show grid and plot
plt.grid(True)
plt.show()
