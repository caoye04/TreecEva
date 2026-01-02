import math

# Simulated sensor data processing with red herrings and complex flow
def preprocess_input(raw_stream, scaling_factor):
    processed = []
    accumulator = 0
    for val in raw_stream:
        if val % 7 == 0:
            accumulator += int(math.sqrt(abs(val)) + 1)
        elif val % 3 == 0:
            accumulator -= val // 5
    # Irrelevant aggregation (red herring)
    temp_sum = sum(x ** 0.5 for x in raw_stream if x > 0)
    normalization = max(temp_sum, 1)
    return [int(x / scaling_factor) for x in raw_stream]

# Distractor function: looks important but unused in final path
def compute_entropy(data):
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Another decoy: matrix transformation with no downstream use
def generate_transformation_matrix(dim, key):
    matrix = [[0]*dim for _ in range(dim)]
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = (i * j + key) % 17
    trace = sum(matrix[i][i] for i in range(dim))
    return matrix, trace

# Core logic buried in distractions
def filter_anomalies(seq, limits):
    result = []
    anomalies_detected = 0
    for idx, x in enumerate(seq):
        if limits[0] < x < limits[1]:
            if x % 4 == 2:
                result.append(x * 2)
            else:
                result.append(x)
        else:
            anomalies_detected += 1
            if anomalies_detected > 3:
                break
    # Dead code branch (never reached due to break above)
    if anomalies_detected == 10:
        result.extend([999] * 5)
    return result[:len(seq)]

# Critical function — actual contributor to final result
def evaluate_stability_index(values):
    if not values:
        return 0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    stability = math.exp(-variance / (abs(mean_val) + 1))
    return round(stability * 1000)

# Key analysis function that produces answer
def analyze_signal(buffer, config_map):
    segment_a = buffer[:len(buffer)//2]
    segment_b = buffer[len(buffer)//2:]
    
    # Use list comprehension and slicing
    transformed_a = [x + config_map['offset'] for x in segment_a if x in config_map['valid_set']]
    transformed_b = [x - config_map['offset'] for x in segment_b]
    
    # Redundant bit manipulation distraction
    magic_key = 0
    for x in transformed_b:
        magic_key ^= (x << 1) | (x >> 2)
    magic_key &= 0xFFFF
    
    # Real computation
    combined = transformed_a + transformed_b
    if len(combined) > 5:
        sliced_part = combined[1::2]  # Every second element
        score_1 = evaluate_stability_index(sliced_part)
        score_2 = min(sliced_part) * max(sliced_part)
        # Final deterministic outcome
        return abs(score_1 - score_2) + len(transformed_a)
    return evaluate_stability_index(combined)

# --- Main execution with heavy interference ---
if __name__ == '__main__':
    # Irrelevant initialization (distractors)
    calibration_data = [12, 15, 22, 27, 30, 35, 40, 45, 50, 53]
    baseline = sum(calibration_data) / len(calibration_data)
    adjustment_factor = math.sin(math.pi / 6) * baseline

    # Unused signal modes
    mode_config = {
        'high_res': {'gain': 2.1, 'filter': 'butterworth'},
        'low_noise': {'gain': 1.3, 'filter': 'chebyshev'}
    }

    # Actual input data
    raw_pattern = [8, 14, 21, 16, 25, 9, 18, 32]
    scale = 2
    
    # Step 1: Preprocess (has side effects but only output matters)
    pattern_buffer = preprocess_input(raw_pattern, scale)
    
    # Distractor: unused transformation
    transform_matrix, trace_value = generate_transformation_matrix(4, 257)
    
    # Distractor: entropy calculation on irrelevant data
    entropy_metric = compute_entropy(calibration_data)
    
    # Threshold configuration actually used later
    threshold_map = {
        'offset': 3,
        'valid_set': {4, 7, 8, 9, 16},
        'bounds': (5, 45)
    }
    
    # Step 2: Filter anomalies (modifies buffer via filtering)
    filtered_buffer = filter_anomalies(pattern_buffer, threshold_map['bounds'])
    
    # Step 3: Critical analysis
    final_diagnostic = analyze_signal(filtered_buffer, threshold_map)
    
    # Print required result
    print(f"Result: {final_diagnostic}")