import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# Small angle and 50 cm
#t = np.array([26.306, 77.980, 128.842, 251.854])  # t (ms)
#v = np.array([0.380141, 0.384714, 0.388072, 0.397055])  # v (m/s)

# large angle and 50 cm
#t = np.array([19.66, 58.132, 96.246, 187.916])  # t (ms)
#v = np.array([0.508647, 0.516067, 0.519502, 0.532153])  # v (m/s)

# large angle and 60 cm
t = np.array([18.100, 53.660, 88.682, 174.222])  # t (ms)
v = np.array([0.552486, 0.559076, 0.563812, 0.573980])  # v (m/s)

# Perform linear regression (least squares fitting)
slope, intercept, r_value, p_value, std_err = stats.linregress(t, v)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(t, v, 'bo', label='Data points')  # Plot the data points
plt.plot(t, slope * t + intercept, 'r-', label=f'Fit line: $v = {slope:.5f}t + {intercept:.5f}$')

# Add text with slope, intercept, and R^2
plt.text(0.05, 0.8, f'$Slope = {slope:.5f}$', transform=plt.gca().transAxes)
plt.text(0.05, 0.75, f'$Intercept = {intercept:.5f}$', transform=plt.gca().transAxes)
plt.text(0.05, 0.7, f'$R^2 = {r_value**2:.4f}$', transform=plt.gca().transAxes)

# Set title and labels
plt.title(r"$v$ vs $\Delta t$")
plt.xlabel(r"$\Delta t$ (ms)")
plt.ylabel(r"$v$ (m/s)")

# Display legend
plt.legend()

# Display grid
plt.grid(True)

# Show the plot
plt.show()
