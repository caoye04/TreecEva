temperature = 80
humidity = 35
base_energy = 120
efficiency_factor = 1.25
optimal_energy = base_energy * efficiency_factor
reduced_energy = base_energy * 0.7

# Conditional expression simulating ternary operator using tuple indexing
energy_threshold = (reduced_energy, optimal_energy)[temperature > 75 and humidity < 40]

Result: energy_threshold