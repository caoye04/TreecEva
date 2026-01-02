temperatures_celsius = [23, 17, 35, 12, 40, 26, 30]

# Convert to Fahrenheit
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

# Identify high-heat conditions (above 86°F)
high_heat = {temp for temp in temperatures_fahrenheit if temp > 86}

# Extract corresponding Celsius values that led to high heat
high_heat_celsius = {c for c, f in zip(temperatures_celsius, temperatures_fahrenheit) if f > 86}

# Find values within normal range (not in high heat), using slicing to exclude extremes
normal_range_celsius = sorted(set(temperatures_celsius) - high_heat_celsius)[1:-1]

# Select only those that are even, simulating energy efficiency thresholds
energy_efficient = [val for val in normal_range_celsius if val % 2 == 0]

# Apply discount factor for moderate consumption
adjusted_values = [val * 0.9 for val in energy_efficient]

# Simulate data refinement: take middle three if available
refined_values = adjusted_values[len(adjusted_values)//2 - 1 : len(adjusted_values)//2 + 2] if len(adjusted_values) >= 3 else adjusted_values

# Final processing step
relevant_values = [round(val, 1) for val in refined_values]
filtered_sum = sum(relevant_values)
print(f"Result: {filtered_sum}")