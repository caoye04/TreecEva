def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    performance_log = []
    total_weight = 0.0
    raw_sum = 0.0
    bonus_applied = False

    for i, (name, score, category) in enumerate(data):
        weight = 1.0
        if category == 'critical':
            weight = 2.0
        elif category == 'experimental':
            weight = 0.5

        adjusted_score = score * weight * base_multiplier

        # Irrelevant logging (distractor)
        temp_entry = {
            'index': i,
            'name': name,
            'raw': score,
            'weighted': adjusted_score
        }
        performance_log.append(temp_entry)

        # Actual accumulation
        raw_sum += adjusted_score
        total_weight += weight

        # Bonus logic (only applied once)
        if score > bonus_threshold and not bonus_applied:
            raw_sum += 5.0
            bonus_applied = True  # Prevent multiple bonuses

    # Simulate additional unused computation (distractor)
    avg_log_score = sum(entry['raw'] for entry in performance_log) / len(performance_log) if performance_log else 0
    outlier_count = sum(1 for entry in performance_log if entry['raw'] < 30)

    final_score = raw_sum / total_weight if total_weight > 0 else 0

    # Dead code path (distractor)
    if avg_log_score < 50 and outlier_count > 10:
        final_score *= penalty_factor

    return final_score

# Main data input
dataset = [
    ('module_a', 78, 'standard'),
    ('module_b', 92, 'critical'),
    ('module_c', 45, 'standard'),
    ('module_d', 88, 'critical'),
    ('module_e', 73, 'experimental'),
    ('module_f', 95, 'standard')
]

# Execution flow
temp_result = [x[1] * 1.1 for x in dataset]  # Unused preprocessing
baseline_avg = sum(x[1] for x in dataset) / len(dataset)
scaling_factor = 1.0 if baseline_avg > 70 else 0.85

# Key statement
calibration_offset = 2.5
final_score = calculate_performance(dataset)
final_score += calibration_offset

print(f"Result: {final_score}")