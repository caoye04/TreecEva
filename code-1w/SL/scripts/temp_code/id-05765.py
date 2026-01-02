def analyze_metrics(data_map):
    temp_results = {}
    for key, values in data_map.items():
        if len(values) == 0:
            temp_results[key] = 0
            continue
        avg_val = sum(values) / len(values)
        max_val = max(values)
        min_val = min(values)
        # Distractor: irrelevant transformation
        transformed = [v ** 0.5 for v in values if v > 0]
        temp_results[key] = (avg_val + max_val - min_val) / 2
    return temp_results

# Simulated sensor calibration readings
calibration_log = {
    'sensor_a': [12, 15, 14, 13, 16],
    'sensor_b': [8, 9, 10, 8, 11],
    'sensor_c': [20, 18, 19, 21],
    'sensor_d': []
}

processed = analyze_metrics(calibration_log)

# Secondary processing with conditional expressions and distractors
baseline_shift = 3.5
adjusted_scores = {}
for k, v in processed.items():
    # Real adjustment
    adjusted_scores[k] = v * 1.1 if v > 10 else v * 0.9
    
# Distractor: unused computation chain
shadow_metrics = {k: (v * 2 + baseline_shift) ** 0.3 for k, v in processed.items()}

# Composite aggregation using dictionary lookups and arithmetic
aggregated = 0
weights = {'sensor_a': 0.4, 'sensor_b': 0.2, 'sensor_c': 0.3, 'sensor_d': 0.1}
for sensor, score in adjusted_scores.items():
    aggregated += score * weights.get(sensor, 0)

# Final performance calculation with embedded logic and red herrings
def calculate_performance(raw_data):
    intermediate_sum = sum(len(v) for v in raw_data.values())
    dummy_offset = intermediate_sum * 0.01  # Unused offset
    
    # Key logic path
    base_perf = sum(adjusted_scores.values())
    penalty_factor = len([v for v in raw_data.values() if len(v) == 0]) * 1.5
    
    # Conditional expression used appropriately
    bonus = 5.0 if all(len(v) > 0 for v in raw_data.values()) else 0.0
    
    # Distractor: complex but unused formula
    unused_complexity = (base_perf ** 2 + penalty_factor) / (intermediate_sum or 1)
    
    # Final score computation — only this matters
    final_score = base_perf - penalty_factor + bonus
    
    return final_score

# Execute main logic
target_result = calculate_performance(calibration_log)
print(f"Target result: {target_result}")