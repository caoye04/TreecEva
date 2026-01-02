from itertools import compress

# System configuration parameters
devices = ["sensor", "actuator", "controller", "transmitter", "receiver"]
base_power = [12, 18, 25, 14, 20]
efficiency = [0.9, 0.75, 0.88, 0.82, 0.77]
operational = [True, True, False, True, True]

# Calculate effective capacity per device
adjusted_power = [base * eff for base, eff in zip(base_power, efficiency)]

# Filter only operational devices
active_power = list(compress(adjusted_power, operational))

# Apply optimization factor based on quartile performance
optimization_factor = 1.1 if len(active_power) > 3 else 1.0
optimized_units = [power * optimization_factor for power in active_power]

# Final summation of optimized units
total_capacity = sum(optimized_units)

# Print result for evaluation
print(f"Result: {total_capacity}")