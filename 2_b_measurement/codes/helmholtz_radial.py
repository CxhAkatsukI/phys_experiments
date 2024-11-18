import numpy as np
import matplotlib.pyplot as plt

# Data for X and measured B (Radial Direction)
X_radial = np.array([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25])  # Radial Distance X (mm)
B_measured_radial = np.array([0.2112, 0.2112, 0.2114, 0.2114, 0.2114, 0.2114, 0.2114, 0.2112, 0.2112, 0.2109, 0.2104])  # Measured B (mT)

# Plotting B-X curve
plt.figure(figsize=(10, 6))
plt.plot(X_radial, B_measured_radial, 'ro-', label='Measured B (Radial)', markersize=6)

# Graph title and labels
plt.title('Magnetic Flux Density $B$ vs Radial Distance $X$ (Helmholtz Coil)', fontsize=16)
plt.xlabel('Radial Distance $X$ (mm)', fontsize=14)
plt.ylabel('Magnetic Flux Density $B$ (mT)', fontsize=14)

# Display grid, legend, and plot
plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
