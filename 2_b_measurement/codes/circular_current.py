import numpy as np
import matplotlib.pyplot as plt

# Data for X, measured B, and calculated B
X = np.array([-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25])  # Axial Distance X (mm)
B_measured = np.array([0.1314, 0.1361, 0.1404, 0.1436, 0.1456, 0.1473, 0.1478, 0.1470, 0.1451, 0.1424, 0.1390])  # Measured B (mT)
B_calculated = np.array([0.1321, 0.1361, 0.1393, 0.1416, 0.1431, 0.1435, 0.1431, 0.1416, 0.1393, 0.1361, 0.1321])  # Calculated B (mT)

# Calculate percentage error
error = ((B_measured - B_calculated) / B_calculated) * 100  # Percentage error (%)

# Plotting B-X curve for measured and calculated B values
plt.figure(figsize=(12, 7))
plt.plot(X, B_measured, 'bo-', label='Measured B', markersize=6)
plt.plot(X, B_calculated, 'rs--', label='Calculated B', markersize=6)

# Annotate percentage error on the plot
for i, (x, err) in enumerate(zip(X, error)):
    plt.annotate(f"{err:.2f}%", (x, B_measured[i]), textcoords="offset points", xytext=(0, 10),
                 ha='center', fontsize=10, color='green')

# Graph title and labels
plt.title('Magnetic Flux Density $B$ vs Axial Distance $X$', fontsize=16)
plt.xlabel('Axial Distance $X$ (mm)', fontsize=14)
plt.ylabel('Magnetic Flux Density $B$ (mT)', fontsize=14)

# Display grid, legend, and plot
plt.grid(True)
plt.legend(fontsize=12)
plt.show()
