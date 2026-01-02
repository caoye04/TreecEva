def analyze_sensor_readings(readings):
    valid_ranges = set(range(10, 91))
    adjusted_values = []
    outlier_count = 0

    for idx, val in enumerate(readings):
        if val < 0:
            corrected = abs(val)
        elif val > 100:
            corrected = 100
        else:
            corrected = val
        
        if corrected not in valid_ranges:
            outlier_count += 1
            continue
            
        adjusted_values.append(corrected * 0.95)

    avg_base = sum(adjusted_values) / len(adjusted_values) if adjusted_values else 0
    return adjusted_values, avg_base, outlier_count


def filter_and_weight(data_list, weights):
    # Irrelevant transformation
    temp_result = [x * 1.1 for x in data_list]
    weighted_sum = sum(x * w for x, w in zip(data_list, weights))
    normalization_factor = max(weighted_sum, 1)
    return weighted_sum / normalization_factor


def calculate_composite_index(vals):
    magnitude = sum(v ** 2 for v in vals) ** 0.5
    peak_noise = 0
    for i in range(len(vals)):
        if i % 3 == 0:
            peak_noise += vals[i] * 0.05  # Minor distortion
    return magnitude + peak_noise


def calculate_final_score(input_data):
    processed_data = []
    temp_cache = {}
    
    for i, segment in enumerate(input_data):
        a, b, c = segment
        computed = (a + b) * c
        temp_cache[f'entry_{i}'] = computed
        if computed > 500:
            processed_data.append(computed // 10)
        else:
            processed_data.append(computed // 20)
    
    # Dead code: this block is never reached due to logic above
    redundant_check = any(x < 0 for x in temp_cache.values())
    if redundant_check:
        fallback = sum(temp_cache.values())

    base_scores, mean_val, outliers = analyze_sensor_readings(processed_data)
    
    # Apply weighting with dummy weights
    importance_weights = [0.8, 1.2, 0.9, 1.1, 1.0, 0.7, 1.3]
    normalized_score = filter_and_weight(base_scores[:7], importance_weights)
    
    index_value = calculate_composite_index(base_scores)
    
    # Key distraction: complex but unused calculation
    phantom_aggregate = 0
    for x in base_scores:
        for y in base_scores:
            if x != y and (x + y) % 2 == 0:
                phantom_aggregate += (x - y) * 0.1

    final_score = int((normalized_score * 1.5) + (index_value * 0.4) + mean_val)
    return final_score

# Main execution
raw_input_data = [
    (15, 25, 10),
    (8, 12, 20),
    (30, 40, 5),
    (5, 10, 30),
    (20, 20, 15),
    (10, 10, 10),
    (40, 10, 8)
]

result_data = []
for item in raw_input_data:
    result_data.append(item)

final_score = calculate_final_score(result_data)
print(f"Target result: {final_score}")