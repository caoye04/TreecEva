# Weather analysis for temperature data
temperatures = [12, 15, 9, 23, 18, 22, 17, 8, 14, 19]
base_threshold = 15
offset = 2

# Apply adjustment factor to temperatures
adjusted_temps = [t + 1 for t in temperatures]

# Filter temperatures above threshold
filtered_temps = [temp for temp in adjusted_temps if temp > base_threshold + offset]

# Calculate sum of filtered temperatures
filtered_sum = sum(filtered_temps)

print(f"Result: {filtered_sum}")