
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data
I_S = np.array([0.00, 0.50, 1.00, 1.50, 2.00, 2.50, 3.00])  # Current (mA)
V_H = np.array([0.25, 26.25, 52.6, 79.075, 105.275, 131.75, 158.35])  # Hall Voltage (mV)

# Linear Fit
slope, intercept, r_value, p_value, std_err = stats.linregress(I_S, V_H)

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(I_S, V_H, 'bo', label='Experimental Data')  # Plot data points
plt.plot(I_S, slope * I_S + intercept, 'r-', label=f'Fitted Line: $V_H = {slope:.2f} I_S + {intercept:.2f}$')  # Plot fitted line

# Set chart title and labels
plt.title('Hall Voltage $V_H$ vs Current $I_S$', fontsize=14)
plt.xlabel('Current $I_S$ (mA)', fontsize=12)
plt.ylabel('Hall Voltage $V_H$ (mV)', fontsize=12)

# Show legend
plt.legend()

# Show grid and plot
plt.grid(True)
plt.show()

# Print fit parameters
print(f"Fitted line equation: V_H = {slope:.2f} I_S + {intercept:.2f}")
print(f"Slope: {slope:.2f}, Intercept: {intercept:.2f}")
