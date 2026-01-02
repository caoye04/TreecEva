temperatures_celsius = [0, 15, 30, 45, 60, 75, 90]

# Convert to Fahrenheit
temperatures_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures_celsius]

# Apply sensor offset correction
adjusted_temps = [temp + 2.5 for temp in temperatures_fahrenheit]

# Simulate data sampling: every other reading starting from index 1
processed_data = adjusted_temps[::1]  # full copy (neutral operation)

# Extract odd-indexed samples after adjustment
filtered_sum = sum(processed_data[1::2])

Result: filtered_sum