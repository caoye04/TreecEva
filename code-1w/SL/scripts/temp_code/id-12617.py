def calculate_efficiency(data_slice):
    return sum(data_slice) * 0.75

# Sensor data simulation (irrelevant for final result but provides context)
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.2]
humidity_readings = [45, 47, 50, 44, 46, 48, 51]

# Core data used in computation
base_signals = [12, 8, 15, 20, 10, 18, 14]

# Apply transformation using lambda and slicing
process = lambda x: [val ** 2 for val in x]
transformed_data = process(base_signals[1:6])  # Focus on subset

# Key computation step
energy_output = calculate_efficiency(transformed_data)

print(f"Result: {energy_output}")