from collections import Counter

# Simulate sensor readings with some duplicate noise
temperature_readings = [20, 22, 24, 22, 23, 24, 25, 26, 25, 24, 27, 28, 27, 26, 25]

# Count frequency of each reading
reading_freq = Counter(temperature_readings)

# Filter out readings that appear less than twice (likely transient)
stable_readings = {temp for temp, count in reading_freq.items() if count >= 2}

# Extract consecutive temperatures from stable set
min_temp, max_temp = min(stable_readings), max(stable_readings)
expected_sequence = set(range(min_temp, max_temp + 1))

# Find missing values in sequence (potential sensor gaps)
missing_in_sequence = expected_sequence - stable_readings

# Final data: all original readings in stable set
filtered_data = [val for val in temperature_readings if val in stable_readings]

# Compute sum of filtered data
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")