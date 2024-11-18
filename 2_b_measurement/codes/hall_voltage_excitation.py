
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data
I_M = np.array([0.00, 50, 100, 150, 200, 250, 300])  # Excitation Current (mA)
V_H = np.array([4.825, 12.9, 26.2, 39.25, 52.675, 66.3, 78.7])  # Hall Voltage (mV)

# Linear Fit
slope, intercept, r_value, p_value, std_err = stats.linregress(I_M, V_H)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(I_M, V_H, 'bo', label='Experimental Data')  # Plot data points
plt.plot(I_M, slope * I_M + intercept, 'r-', label=f'Fitted Line: $V_H = {slope:.2f} I_M + {intercept:.2f}$')  # Plot fitted line

# Set chart title and labels
plt.title('Hall Voltage $V_H$ vs Excitation Current $I_M$', fontsize=14)
plt.xlabel('Excitation Current $I_M$ (mA)', fontsize=12)
plt.ylabel('Hall Voltage $V_H$ (mV)', fontsize=12)

# Show legend
plt.legend()

# Show grid and plot
plt.grid(True)
plt.show()

# Print fit parameters
print(f"Fitted line equation: V_H = {slope:.2f} I_M + {intercept:.2f}")
print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")
