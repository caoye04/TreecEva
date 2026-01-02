def process_metrics(entries, scaling_factors):
    base_adjustment = 0.0
    temp_offset = 0
    cumulative = 0
    
    # Irrelevant pre-processing (distractor)
    outlier_flags = [abs(x) > 50 for x in entries]
    valid_count = len([flag for flag in outlier_flags if not flag])
    
    # Real logic begins: apply weights and transform
    weighted_values = []
    for i, entry in enumerate(entries):
        if i % 2 == 0:
            transformed = abs(entry) ** 0.5 * scaling_factors[i % len(scaling_factors)]
        else:
            transformed = (entry // 3) * scaling_factors[i % len(scaling_factors)]
        weighted_values.append(round(transformed, 4))
    
    # Secondary transformation with lambda (required feature)
    enhance = lambda x: x + 1.5 if x < 10 else x - 2.5
    enhanced_values = [enhance(val) for val in weighted_values]
    
    # Case conversion distraction (irrelevant string operations)
    status_labels = ['pass' if v > 0 else 'fail' for v in enhanced_values]
    upper_labels = [label.upper() for label in status_labels]  # Dead code path
    
    # Core accumulation logic
    running_total = 0
    for idx, value in enumerate(enhanced_values):
        if idx % 3 == 0:
            running_total += value * 1.1
        elif idx % 3 == 1:
            running_total -= value * 0.9
        else:
            running_total += value * 0.5
    
    # Final adjustment using logical operations (required paradigm)
    multiplier = (len(entries) > 5) and (valid_count >= 3)
    correction_factor = 1.2 if multiplier else 0.8
    
    final_score = int(running_total * correction_factor)
    
    # Unused intermediate variables (distractors)
    avg_enhanced = sum(enhanced_values) / len(enhanced_values) if enhanced_values else 0
    peak_value = max(weighted_values, default=0)
    normalization_shift = base_adjustment + temp_offset
    
    return final_score

# Input data
data = [25, -45, 64, 81, -16, 100, 144]
weights = [1.2, 0.8, 1.5]

# Execute
target_result = process_metrics(data, weights)
print(f"Result: {target_result}")