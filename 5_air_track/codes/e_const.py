import matplotlib.pyplot as plt
import matplotlib

# Update font and LaTeX settings
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "CMU Serif",
})
plt.rcParams['mathtext.fontset'] = 'stix'

# Given data
x = [10, 15, 20, 25, 30]  # Position (cm)
Ek = [0.2138, 0.2023, 0.1718, 0.1397, 0.0900]  # Kinetic energy (J)
Ep = [0.0166, 0.0372, 0.0662, 0.1035, 0.1490]  # Potential energy (J)
E = [0.2304, 0.2396, 0.2380, 0.2432, 0.2390]  # Total energy (J)

# Create the figure
plt.figure(figsize=(8, 6))

# Plot Kinetic energy, Potential energy, and Total energy
plt.plot(x, Ek, label='Kinetic Energy (Ek)', marker='o', color='b')
plt.plot(x, Ep, label='Potential Energy (Ep)', marker='s', color='r')
plt.plot(x, E, label='Total Energy (E)', marker='^', color='g')

# Set title and labels
plt.title('Kinetic, Potential, and Total Energy vs. Position')
plt.xlabel('Position (x) [cm]')
plt.ylabel('Energy (J)')
plt.legend()

# Display grid
plt.grid(True)

# Show the plot
plt.show()
