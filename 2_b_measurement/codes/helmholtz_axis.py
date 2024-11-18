import numpy as np
import matplotlib.pyplot as plt

# Data for X and measured B
X = np.array([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25])  # Axial Distance X (mm)
B_measured = np.array([0.2104, 0.2109, 0.2112, 0.2112, 0.2112, 0.2112, 0.2112, 0.2112, 0.2112, 0.2109, 0.2109])  # Measured B (mT)

# Plotting B-X curve
plt.figure(figsize=(10, 6))
plt.plot(X, B_measured, 'bo-', label='Measured B', markersize=6)

# Graph title and labels
plt.title('Magnetic Flux Density $B$ vs Axial Distance $X$ (Helmholtz Coil)', fontsize=16)
plt.xlabel('Axial Distance $X$ (mm)', fontsize=14)
plt.ylabel('Magnetic Flux Density $B$ (mT)', fontsize=14)

# Display grid, legend, and plot
plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
