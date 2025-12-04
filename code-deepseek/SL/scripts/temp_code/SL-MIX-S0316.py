from collections import Counter

# Process sensor data readings
sensor_readings = [15, 23, 15, 42, 23, 15, 18, 42, 42, 23]
reading_frequency = Counter(sensor_readings)

# Calculate frequency metrics
most_common_reading = reading_frequency.most_common(1)[0][0]
frequency_sum = sum(reading_frequency.values())

# Create result mapping with some redundant calculations
result_mapping = {}
for reading, count in reading_frequency.items():
    # Some intermediate calculations that don't affect final result
    temp_adjustment = reading * 2 - 10
    redundant_check = temp_adjustment > 30
    
    # Actual relevant calculation
    if count >= 2:
        result_mapping[reading] = reading * count + 5

# Find the maximum key and corresponding value
if result_mapping:
    max_key = max(result_mapping.keys())
    final_output = result_mapping.get(max_key, -1)
else:
    final_output = -1

# Print the target result
print(f"Target result: {final_output}")