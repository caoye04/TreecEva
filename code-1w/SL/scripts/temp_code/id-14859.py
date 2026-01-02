def normalize_sensor(value, min_val=0, max_val=1023):
    """Irrelevant normalization function for sensor data."""
    return (value - min_val) / (max_val - min_val)


def decode_signal(signal_sequence):
    """Decodes a binary signal sequence – red herring function."""
    decoded = 0
    for bit in signal_sequence:
        decoded = (decoded << 1) | bit
    return decoded

# Simulated raw sensor readings (voltage levels)
raw_readings = [512, 768, 256, 896, 128, 384, 640, 1000]

# Irrelevant signal pattern (dead code path)
signal_pattern = [1, 0, 1, 1, 0]
decoded_value = decode_signal(signal_pattern)  # Distractor computation

# Normalize all readings (distractor transformation)
normalized_readings = [normalize_sensor(x) for x in raw_readings]

# Filter significant readings above midpoint
significant_readings = [x for x in raw_readings if x > 512]

# Misleading intermediate: average of normalized values (not used in final result)
norm_avg = sum(normalized_readings) / len(normalized_readings)
threshold_flag = norm_avg > 0.5  # Another misleading boolean

# Apply non-linear transformation: square root of doubled value
transformed_readings = []
for val in significant_readings:
    transformed_readings.append(int(val ** 0.5 * 2))

# Unrelated string processing (distractor block)
data_tag = "THM-LOG-2023"
parts = data_tag.split('-')
log_type = '-'.join(parts[:2])  # Unused
year_label = int(parts[2]) if parts[2].isdigit() else 0

# Create reading metadata using enumerate and zip (required feature)
indices = list(range(len(transformed_readings)))
reading_metadata = {}
for i, (idx, val) in enumerate(zip(indices, transformed_readings)):
    reading_metadata[f'entry_{i}'] = {
        'index': idx,
        'value': val,
        'flagged': val > 30
    }

# Extract only values into a list
metadata_values = [entry['value'] for entry in reading_metadata.values()]

# Secondary filtering: only values less than 40
filtered_temp_vals = [v for v in metadata_values if v < 40]

# Simulate thermal hysteresis effect with lagged differences
hysteresis_deltas = []
for i in range(1, len(filtered_temp_vals)):
    hysteresis_deltas.append(filtered_temp_vals[i] - filtered_temp_vals[i-1])

# Compute moving average of deltas (irrelevant)
moving_avg_deltas = []
window_size = 2
for i in range(len(hysteresis_deltas) - window_size + 1):
    window = hysteresis_deltas[i:i+window_size]
    moving_avg_deltas.append(sum(window) / len(window))

# Key function: calculates effective thermal capacity
# Based on sum of filtered transformed values multiplied by count offset
def calculate_thermal_capacity(readings):
    base_sum = sum(readings)
    count_factor = len(readings) + 3  # Artificial offset
    return base_sum * count_factor

# Critical execution point
thermal_capacity = calculate_thermal_capacity(filtered_temp_vals)

# Output required format
print(f"Result: {thermal_capacity}")