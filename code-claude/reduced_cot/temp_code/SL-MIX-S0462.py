import itertools

# Data representing daily temperature readings in Celsius
temperature_readings = [22, 24, 22, 25, 23, 24, 26, 25, 23, 22]

# Process the data: Keep only temperatures that appear in consecutive days
consecutive_pairs = list(itertools.pairwise(temperature_readings))
temperature_sum = sum(temperature_readings)

# Extract temperatures that repeat in adjacent readings
repeated_adjacent = [pair[0] for pair in consecutive_pairs if pair[0] == pair[1]]

# Apply data transformation: slice to get readings from odd-indexed days
odd_day_readings = temperature_readings[1::2]

# Combine processed datasets
processed_data = repeated_adjacent + odd_day_readings

# Calculate the number of unique temperature values
unique_elements = len(set(processed_data))

print(f"Result: {unique_elements}")