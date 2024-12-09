import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# Data
mu = np.array([0.00160, 0.00558, 0.00207, 0.00350, 0.00375])  # Linear density (kg/m)
f1 = np.array([89.29, 55.56, 89.29, 67.57, 64.10])  # Fundamental frequency (Hz)

# Compute ln(μ) and ln(f)
ln_mu = np.log(mu)
ln_f = np.log(f1)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(ln_mu, ln_f)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(ln_mu, ln_f, 'o', label="Data points")  # Plot original data points
plt.plot(ln_mu, slope * ln_mu + intercept, 'r-', label=f"Fit: ln(f) = {slope:.2f} ln($\\mu$) + {intercept:.2f}")  # Fitted line

# Add labels and legend
plt.xlabel(r'$\ln \mu$ (kg/m)', fontsize=14)
plt.ylabel(r'$\ln f$ (Hz)', fontsize=14)
plt.title('Linear Fit of $\\ln f$ vs. $\\ln \\mu$', fontsize=16)
plt.legend()

# Display slope and intercept on the graph
plt.text(0.1, 0.8, f"Fit slope: {slope:.2f}\nFit intercept: {intercept:.2f}", transform=plt.gca().transAxes)

# Show grid and plot
plt.grid(True)
plt.show()

# Print fitted parameters
print(f"Fitted slope: {slope:.2f}")
print(f"Fitted intercept: {intercept:.2f}")
