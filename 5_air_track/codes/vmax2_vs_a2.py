import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# Given data
A = np.array([10, 15, 20, 25, 30])  # A values (cm)
Vmax = np.array([39.340, 57.683, 77.190, 94.037, 117.280])  # Vmax values (cm/s)

# Calculate Vmax^2 and A^2
Vmax_squared = Vmax ** 2
A_squared = A ** 2

# Perform linear regression (least squares fitting)
slope, intercept, r_value, p_value, std_err = stats.linregress(A_squared, Vmax_squared)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(A_squared, Vmax_squared, 'bo', label='Data points')  # Plot the data points
plt.plot(A_squared, slope * A_squared + intercept, 'r-', label=f'Fit line: $y = {slope:.2f}x + {intercept:.2f}$')

# Add text with slope, intercept, and R^2
plt.text(0.05, 0.80, f'$Slope = {slope:.2f}$', transform=plt.gca().transAxes)
plt.text(0.05, 0.75, f'$Intercept = {intercept:.2f}$', transform=plt.gca().transAxes)
plt.text(0.05, 0.70, f'$R^2 = {r_value**2:.4f}$', transform=plt.gca().transAxes)

# Set title and labels
plt.title(r"$V_{max}^2$ vs $A^2$")
plt.xlabel(r"$A^2$ (cm$^2$)")
plt.ylabel(r"$V_{max}^2$ (cm$^2$/s$^2$)")

# Display legend
plt.legend()

# Display grid
plt.grid(True)

# Show the plot
plt.show()
