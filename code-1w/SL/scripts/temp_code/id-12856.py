from collections import defaultdict

# Simulate sensor data processing with noise filtering and threshold logic
def process_sensor_readings(readings):
    filtered_data = []
    noise_counter = 0
    cumulative_noise = 0

    for val in readings:
        if abs(val - 50) < 5:  # Assume 50 is baseline, filter near-baseline noise
            noise_counter += 1
            cumulative_noise += val
        elif val > 60:
            filtered_data.append(val - 5)  # Adjust for calibration drift
        else:
            filtered_data.append(val)

    # Irrelevant aggregation (distractor)
    avg_noise = cumulative_noise / noise_counter if noise_counter else 0

    return filtered_data

# Analyze pattern complexity using bitwise fingerprint
def compute_pattern_fingerprint(data):
    fingerprint = 0
    weight = 1
    for num in data:
        fingerprint ^= (num * weight) & 255  # Use only lower byte
        weight = (weight * 3) % 10
    return fingerprint

# Main evaluation logic
def evaluate_performance(sensor_id, raw_readings):
    readings_map = defaultdict(list)
    temp_buffer = []

    # Preprocess: segment readings by modulo pattern (semi-relevant)
    for r in raw_readings:
        readings_map[r % 4].append(r)
        temp_buffer.append(r * 0.98)  # Logging simulation (dead code)

    # Extract primary channel (remainder 0)
    primary_channel = readings_map[0]

    # Apply noise filtering
    clean_data = process_sensor_readings(primary_channel)

    # Compute derived metrics
    base_metric = sum(clean_data) // len(clean_data) if clean_data else 0
    volatility = sum(abs(clean_data[i] - clean_data[i-1]) 
                   for i in range(1, len(clean_data))) if len(clean_data) > 1 else 0

    # Secondary irrelevant transformation chain
    transformed_seq = list(map(lambda x: (x ** 0.5) * 2, temp_buffer))
    smoothed_value = sum(transformed_seq) / len(transformed_seq) if transformed_seq else 0

    # Core logic: combine base metric with fingerprint
    fingerprint = compute_pattern_fingerprint(clean_data)
    security_token = (sensor_id ^ 219) & 255  # Simple obfuscation key

    # Decision logic with short-circuiting (modular arithmetic + boolean logic)
    if base_metric > 45 and (volatility < 30 or (fingerprint % 7 == 0)):
        confidence_factor = 1.7
    else:
        confidence_factor = 0.85

    # Final score computation (target)
    raw_score = base_metric * confidence_factor
    adjustment = (fingerprint & 15) - (security_token >> 4)  # Net small offset
    final_score = int(raw_score + adjustment)

    # Dead code: logging irrelevant state
    debug_state = {
        'buffer_len': len(temp_buffer),
        'smoothed': smoothed_value,
        'noise_ratio': len([x for x in raw_readings if abs(x - 50) < 5]) / len(raw_readings)
    }

    return final_score

# Input data
data_stream = [52, 64, 48, 70, 50, 58, 49, 72, 51, 68, 53, 66, 47, 74, 50, 60]
sensor_identifier = 137

# Execute
target_result = evaluate_performance(sensor_identifier, data_stream)
print(f"Result: {target_result}")