
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data
I_M = np.array([0.00, 50, 100, 150, 200, 250, 300])  # Excitation Current (mA)
B = np.array([1.375, 26.0, 71.5, 107.9, 142.55, 180.4, 214.375])  # Magnetic Flux Density (mT)

# Linear Fit
slope, intercept, r_value, p_value, std_err = stats.linregress(I_M, B)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(I_M, B, 'bo', label='Experimental Data')  # Plot data points
plt.plot(I_M, slope * I_M + intercept, 'r-', label=f'Fitted Line: $B = {slope:.2f} I_M + {intercept:.2f}$')  # Plot fitted line

# Set chart title and labels
plt.title('Magnetic Flux Density $B$ vs Excitation Current $I_M$', fontsize=14)
plt.xlabel('Excitation Current $I_M$ (mA)', fontsize=12)
plt.ylabel('Magnetic Flux Density $B$ (mT)', fontsize=12)

# Show legend
plt.legend()

# Show grid and plot
plt.grid(True)
plt.show()

# Print fit parameters
print(f"Fitted line equation: B = {slope:.2f} I_M + {intercept:.2f}")
print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")
