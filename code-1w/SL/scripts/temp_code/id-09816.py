def analyze_readings(sensor_values):
    threshold = 50
    high_readings = []
    low_readings = []
    cumulative = 0
    temp_sum = 0  # Distractor: used in irrelevant computation

    for idx, val in enumerate(sensor_values):
        if val > threshold:
            high_readings.append((idx, val))
            cumulative += val * (idx + 1)
        else:
            low_readings.append(val)
            temp_sum += val ** 2  # Distractor: not used later

    stats = {}
    for i, reading in enumerate(high_readings):
        pos, value = reading
        stats[pos] = value % 7

    # Irrelevant transformation
    normalized = [x / (max(low_readings) + 1) for x in low_readings] if low_readings else [0]
    avg_normalized = sum(normalized) / len(normalized)  # Dead-end variable

    return cumulative, stats


def transform_mapping(indices_map):
    # Complex but partially irrelevant mapping operation
    shifted = {}
    for k, v in indices_map.items():
        shifted[(k + 3) % 10] = v * 2 + 1
    return shifted


def calculate_final_score(data_packet):
    raw_value, metadata = data_packet
    base = raw_value % 1000
    
    # Unnecessary dictionary aggregations
    aux_data = {i: base + i*3 for i in range(5)}
    inverted = {v: k for k, v in aux_data.items()}
    
    # Core logic hidden among distractions
    bonus = 0
    for key, val in metadata.items():
        if val > 3:
            bonus += key * val

    multiplier = len(metadata.keys()) if metadata else 1
    intermediate = base + bonus
    scaling_factor = 2 if intermediate > 400 else 1.5
    
    # Actual answer depends on these steps
    final_score = int(intermediate * scaling_factor)
    
    # Red herring: complex bitwise but unused
    decoy_flag = (final_score ^ 255) & 15 > 7
    if decoy_flag:
        final_score -= 10  # This never triggers due to fixed data

    return final_score

# Main execution
sensor_inputs = [45, 67, 58, 42, 73, 55, 88, 33]
sensor_inputs_zipped = list(zip(sensor_inputs[::2], sensor_inputs[1::2]))
processed = analyze_readings(sensor_inputs)
processed_data = processed  # Rename for semantic clarity

# Additional distracting structure
validation_check = any(x[1] > 60 for x in processed[1].items())  # True but unused downstream
summary_report = {'entries': len(processed[1]), 'flag': validation_check}

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")