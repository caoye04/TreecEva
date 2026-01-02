import math

# Simulated sensor data chunk (irrelevant to final result)
sensor_readings = [0.1, 0.35, 0.67, 0.89, 1.04, 1.21]
offset_correction = sum([math.sin(x) for x in sensor_readings])
adjusted_readings = [x + offset_correction for x in sensor_readings]

# Financial threshold parameters (distractor logic)
def calculate_risk_score(values):
    base = sum(values) / len(values)
    penalty = 0.05 * len([v for v in values if v > 1.0])
    return base - penalty

risk_threshold = calculate_risk_score(adjusted_readings)
alert_mode = risk_threshold > 0.5  # Dead end, never used

# Core data processing chain (relevant logic)
data_stream = [8, 3, 12, 7, 19, 5, 14, 9]
filtered_data = [x for x in data_stream if x % 2 == 1]  # Keep odd numbers
shifted_data = [x << 1 for x in filtered_data]           # Bit-shift left by 1

# Misleading transformation path (red herring)
decoy_map = {i: (i ** 2) % 13 for i in range(1, 20)}
temp_weights = [decoy_map[x % 10] for x in shifted_data if x % 6 != 0]
weighted_sum = sum(temp_weights) // 2  # Looks important, unused later

# Actual computation path
chunk_size = 4
raw_chunk = shifted_data[:chunk_size]  # Take first 4 elements after shift

# Apply conditional transformation based on index parity and magnitude
transformed_chunk = []
for i, val in enumerate(raw_chunk):
    if i % 2 == 0:
        transformed_chunk.append(val * 3)
    else:
        transformed_chunk.append(val + (val >> 2))  # Add quarter via bit shift

# Auxiliary lookup table (partial distractor)
lookup_table = {k: v for k, v in enumerate([10, -5, 8, 12, 3, 7, 1, 9])}
index_bias = sum(lookup_table[i] for i in range(0, len(lookup_table), 2))  # Unused

# Critical processing function
def process_transformed_data(data_list):
    # Nested dictionary operation (required python feature)
    stats = {
        'max': max(data_list),
        'min': min(data_list),
        'range': max(data_list) - min(data_list)
    }
    
    # Conditional expression with slicing (required features)
    mid_slice = data_list[1:-1] if len(data_list) > 2 else [data_list[0]]
    adjustment = stats['range'] // 2 if stats['max'] > 20 else stats['max']
    
    # Composite calculation with interdependent steps
    accumulated = 0
    for idx, item in enumerate(mid_slice):
        factor = adjustment if item > 15 else (adjustment + 2)
        accumulated += item * factor - (idx ** 2)
    
    # Final formula using dictionary-derived values
    result = accumulated + stats['min'] * 3
    return result

# Execution point of interest
final_output = process_transformed_data(transformed_chunk)

# Print required output
print(f"Target result: {final_output}")