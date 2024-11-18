import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data for B-I_M and V_H-I_M curves
I_M = np.array([50, 75, 100, 125, 150, 175, 200])  # Excitation Current I_M (mA)
B = np.array([35.6, 53.5, 71.1, 89.4, 107.2, 125.1, 143.2])  # Magnetic Flux Density B (mT)
V_H_AC = np.array([8.804, 15.228, 21.790, 28.428, 35.087, 41.938, 48.162])  # Hall Voltage V_H (mV)

# Create two subplots for B-I_M and V_H-I_M curves
fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# B-I_M Curve
ax[0].plot(I_M, B, 'bo-', label='Experimental Data', markersize=6)
slope_B, intercept_B, _, _, _ = stats.linregress(I_M, B)
ax[0].plot(I_M, slope_B * I_M + intercept_B, 'r--', label=f'Fitted Line: $B = {slope_B:.2f} I_M + {intercept_B:.2f}$')

ax[0].set_title('Magnetic Flux Density $B$ vs Excitation Current $I_M$', fontsize=14)
ax[0].set_xlabel('Excitation Current $I_M$ (mA)', fontsize=12)
ax[0].set_ylabel('Magnetic Flux Density $B$ (mT)', fontsize=12)
ax[0].legend()
ax[0].grid(True)

# V_H-I_M Curve
ax[1].plot(I_M, V_H_AC, 'go-', label='Experimental Data', markersize=6)
slope_VH, intercept_VH, _, _, _ = stats.linregress(I_M, V_H_AC)
ax[1].plot(I_M, slope_VH * I_M + intercept_VH, 'r--', label=f'Fitted Line: $V_H = {slope_VH:.2f} I_M + {intercept_VH:.2f}$')

ax[1].set_title('Hall Voltage $V_H$ vs Excitation Current $I_M$ (AC)', fontsize=14)
ax[1].set_xlabel('Excitation Current $I_M$ (mA)', fontsize=12)
ax[1].set_ylabel('Hall Voltage $V_H$ (mV)', fontsize=12)
ax[1].legend()
ax[1].grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# Print fit parameters for both plots
print(f"B-I_M fit: B = {slope_B:.2f} I_M + {intercept_B:.2f}")
print(f"V_H-I_M fit: V_H = {slope_VH:.2f} I_M + {intercept_VH:.2f}")
