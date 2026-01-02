from itertools import combinations

def analyze_sensor_data(data, threshold=5.0):
    """Analyze sensor readings and compute adjusted metrics."""
    high_readings = []
    low_readings = []
    adjusted_values = []
    
    for i, val in enumerate(data):
        if val > threshold:
            high_readings.append((i, val))
            adjusted_values.append(val * 0.9)
        else:
            low_readings.append((i, val))
            adjusted_values.append(val * 1.1)
    
    # Irrelevant computation: count pairs above threshold
    count_pairs = 0
    for pair in combinations(high_readings, 2):
        if abs(pair[0][1] - pair[1][1]) < 2.0:
            count_pairs += 1

    return adjusted_values, len(high_readings)

def calculate_entropy(values):
    """Calculate approximate entropy-like metric (simplified)."""
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * (p ** 0.5)  # Simulated pseudo-entropy
    return round(entropy, 4)

def calculate_final_score(sensor_inputs):
    """Compute final diagnostic score from sensor inputs."""
    clean_data = [x for x in sensor_inputs if 0 <= x <= 10]
    
    # Misleading transformation
    normalized = [((x - min(clean_data)) / (max(clean_data) - min(clean_data))) * 10 if max(clean_data) != min(clean_data) else 5 for x in clean_data]
    
    adjusted_data, high_count = analyze_sensor_data(normalized)
    
    # Dummy bitwise manipulation (semi-relevant)
    masked_sum = 0
    for i, val in enumerate(adjusted_data):
        mask = (i + 1) & 3
        masked_val = int(val) & mask
        masked_sum += masked_val
    
    # Core logic path
    base_score = sum(adjusted_data) / len(adjusted_data)
    entropy_metric = calculate_entropy(adjusted_data)
    
    # Secondary adjustment using set operations
    unique_adjusted = set(round(x) for x in adjusted_data)
    outlier_check = {x for x in unique_adjusted if x < 3 or x > 8}
    penalty = len(outlier_check) * 0.7 if outlier_check else 0
    
    # Distractor: unused conditional branch
    debug_mode = False
    extra_offset = 0
    if debug_mode:  # Dead code path
        extra_offset = sum(1 for x in adjusted_data if x > 7) * 0.2
    
    # Final composition
    final_score = (base_score * 1.2) + (entropy_metric * 2.0) - penalty + extra_offset
    
    # Key execution point
    final_score = int(round(final_score))
    
    return final_score

# Input data
sensor_input_stream = [3.2, 7.1, 0.5, 9.8, 4.4, 12.1, -1.0, 6.7, 8.3, 2.9]

# Execute
result = calculate_final_score(sensor_input_stream)
print(f"Target result: {result}")