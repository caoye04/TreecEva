from collections import Counter

# Sensor readings with noise and duplicate entries
temperature_readings = [23.5, 24.1, 23.5, 25.0, 24.1, 23.5, 26.3, 25.0]
weight_measurements = [102, 98, 102, 95, 99, 105, 98, 100]

# Count frequency of temperature readings
temp_freq = Counter(temperature_readings)

# Find most common temperature reading
most_common_temp, _ = temp_freq.most_common(1)[0]

# Select weights where temperature was at the most common value
relevant_indices = [i for i, t in enumerate(temperature_readings) if abs(t - most_common_temp) < 0.1]
filtered_weights = [weight_measurements[i] for i in relevant_indices]

# Calculate total adjusted weight
total_weight = sum(filtered_weights)

# Print final result
print(f"Result: {total_weight}")