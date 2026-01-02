def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    internal_offset = 0.05
    temp_result = 0
    final_score = 0
    
    # Irrelevant tracking variables (distractors)
    sample_count = len(data)
    outlier_flags = [False] * sample_count
    cumulative_noise = 0.0
    
    for i, entry in enumerate(data):
        raw_value = entry['value']
        quality_flag = entry['quality']
        
        # Distraction: noise accumulation that isn't used
        if i % 3 == 0:
            cumulative_noise += raw_value * 0.01
        
        # Real computation begins
        adjusted_value = raw_value * base_multiplier
        if quality_flag > 1:
            adjusted_value *= penalty_factor
        
        # Conditional expression for dynamic weighting
        weight = 1.2 if adjusted_value >= bonus_threshold else 0.8
        
        temp_result += adjusted_value * weight
        
        # Dead code path (misleading)
        if quality_flag < 0:
            outlier_flags[i] = True
            temp_result -= 5  # Never executed due to data constraints

    # Dictionary-based mapping for correction factors (semi-relevant)
    correction_map = {0: 0.95, 1: 1.0, 2: 0.85}
    status_codes = [entry['status'] for entry in data]
    avg_status = sum(status_codes) / len(status_codes) if status_codes else 0
    
    # Unused correction lookup
    _ = correction_map.get(int(avg_status), 1.0)
    
    # Actual final calculation
    stability_adjustment = 0.9 + internal_offset
    final_score = temp_result * stability_adjustment
    
    # Extra irrelevant transformation
    normalized_score = final_score / sample_count if sample_count else 0
    _ = round(normalized_score, 2)  # Not used
    
    return int(final_score)

# Main execution
benchmark_data = [
    {'value': 70, 'quality': 1, 'status': 1},
    {'value': 90, 'quality': 2, 'status': 2},
    {'value': 88, 'quality': 1, 'status': 1},
    {'value': 95, 'quality': 1, 'status': 0},
    {'value': 82, 'quality': 2, 'status': 1}
]

# Intermediate distraction: unused preprocessing
processed = list(zip(
    [d['value'] for d in benchmark_data],
    [d['quality'] for d in benchmark_data]
))
index_map = {i: val[0] for i, val in enumerate(processed)}

# Key statement
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")