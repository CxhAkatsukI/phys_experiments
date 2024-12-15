import matplotlib.pyplot as plt
import numpy as np

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# Table data
frequencies_khz = [1.88, 2.00, 2.08, 2.15, 2.19, 2.22, 2.240, 2.25, 2.26, 2.275, 2.30, 2.36, 2.43, 2.62, 3.18]
phi_degrees = [-83.37, -67.56, -60.72, -44.70, -28.72, -17.40, -6.035, -1.572, 7.186, 13.85, 30.75, 47.42, 61.43, 70.41, 77.58]

# Plot the curve
plt.figure(figsize=(8, 6))
plt.plot(frequencies_khz, phi_degrees, marker='o', linestyle='-', color='b', label=r'$\varphi - f$ curve')

# Add title and axis labels (in English)
plt.title(r'Series Circuit $\varphi - f$ Curve', fontsize=14)
plt.xlabel('Frequency $f$ (kHz)', fontsize=12)
plt.ylabel(r'Phase Difference $\varphi$ (degrees)', fontsize=12)

# Add grid and legend
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=10)

# Display the plot
plt.show()
