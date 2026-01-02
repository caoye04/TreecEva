def evaluate_performance(metrics):
    base_weight = 0.8
    bonus_factor = 1.2
    penalty_rate = 0.9
    
    # Irrelevant metrics (distractors)
    unused_metric_a = sum([i**2 for i in range(5)])
    temp_buffer = [x * 0.1 for x in metrics if x > 30]
    debug_log = len(temp_buffer) + 100
    
    # Core logic begins
    filtered_metrics = [m for m in metrics if m >= 20]
    adjusted_values = [val * base_weight for val in filtered_metrics]
    
    # Simulate conditional bonuses using bitwise logic on index parity
    enhanced_values = []
    for idx, val in enumerate(adjusted_values):
        if idx % 2 == 0:
            enhanced_values.append(val * bonus_factor)
        else:
            # Use XOR to toggle small adjustment (bitwise operation)
            bit_flag = idx ^ 1
            enhanced_values.append(val * (1 + 0.05 * bit_flag))
    
    # Aggregate using set operations to remove near-duplicates within tolerance
    rounded_set = {round(v, 1) for v in enhanced_values}  # Set deduplication
    total_contribution = sum(rounded_set)
    
    # Secondary filter: exclude values above a dynamic threshold
    max_limit = sum(rounded_set) / len(rounded_set) + 10 if rounded_set else 0
    compliant_values = {v for v in rounded_set if v <= max_limit}
    
    # Final computation with red herring intermediate
    phantom_offset = sum([i * 0.01 for i in range(len(compliant_values))])  # Unused
    scaling_factor = 0.95 + 0.05 * (len(compliant_values) > 3)
    
    final_score = int(sum(compliant_values) * scaling_factor)
    return final_score

# Input data
metric_data = [25, 30, 15, 45, 22, 18, 40]

# Misleading pre-processing (not used in final path)
shadow_copy = metric_data.copy()
shadow_copy.append(999)
processed_hint = [x for x in shadow_copy if x < 50]

# Key execution point
final_score = evaluate_performance(metric_data)
print(f"Result: {final_score}")