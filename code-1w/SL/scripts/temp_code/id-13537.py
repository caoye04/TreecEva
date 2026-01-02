def analyze_readings(sensor_readings):
    filtered = [x for x in sensor_readings if x > 20 and x < 80]
    avg = sum(filtered) / len(filtered) if filtered else 0
    outliers = [x for x in sensor_readings if x >= 80]
    return avg, len(outliers)


def transform_sequence(raw_sequence):
    shifted = [(x * 2 + 3) % 100 for x in raw_sequence]
    reversed_seq = shifted[::-1]
    cumulative = [sum(reversed_seq[:i+1]) for i in range(len(reversed_seq))]
    temp_result = cumulative[-1] if cumulative else 0
    padding = [0] * (10 - len(cumulative))
    extended = cumulative + padding  # dead code path, not used later
    return shifted, temp_result


def validate_range(values, min_val=10, max_val=90):
    count_in_range = sum(1 for v in values if min_val <= v <= max_val)
    total = len(values)
    ratio = count_in_range / total if total else 0
    return ratio > 0.7


def calculate_final_score(data_chunk):
    base = data_chunk.get('base_value', 0)
    multiplier = data_chunk.get('multiplier', 1)
    penalty = data_chunk.get('penalty', 0)
    adjustment_factor = data_chunk.get('adjustment', 1.0)
    
    intermediate = (base + penalty) * adjustment_factor
    if data_chunk.get('active'):
        intermediate -= penalty
    score = intermediate * multiplier
    return int(score)

# Main execution
sensor_inputs = [15, 25, 30, 85, 45, 70, 90, 60]
sequence_input = [12, 18, 25, 33, 40]

# Step 1: Analyze sensor readings
average_reading, anomaly_count = analyze_readings(sensor_inputs)

# Step 2: Transform sequence
distorted_sequence, sequence_sum = transform_sequence(sequence_input)

# Step 3: Validate transformed data
valid_transmission = validate_range(distorted_sequence)

# Step 4: Prepare processed data with multiple fields (some irrelevant)
processed_data = {
    'base_value': int(average_reading),
    'multiplier': 7,
    'penalty': anomaly_count * 3,
    'adjustment': 1.25,
    'active': valid_transmission,
    'debug_checksum': sequence_sum + anomaly_count,  # unused field
    'timestamp': 1678899000  # irrelevant metadata
}

# Step 5: Calculate final score
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")