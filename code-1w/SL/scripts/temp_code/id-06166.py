temperatures_celsius = [23, 19, 27, 31, 16, 22, 25, 28]

# Convert to Fahrenheit as distraction
distraction_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

# Extract high temperatures above 24C
temp_above_threshold = [t for t in temperatures_celsius if t > 24]

# Sort the filtered list
sorted_values = sorted(temp_above_threshold)

# Take every other element starting from index 1 (odd indices)
filtered_sum = sum(sorted_values[1::2])

print(f"Result: {filtered_sum}")