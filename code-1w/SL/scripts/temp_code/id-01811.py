def analyze_performance(execution_time, error_count, base_points):
    efficiency_ratio = execution_time / (error_count + 1)
    adjustment_factor = 0.9 if efficiency_ratio > 5 else 1.1
    temp_diagnostic = efficiency_ratio * adjustment_factor  # irrelevant beyond debugging
    return int(base_points * adjustment_factor)


def calculate_adjusted_score(points, penalties):
    raw_score = points - (penalties * 10)
    bonus_applied = False
    if raw_score > 80:
        raw_score += 15
        bonus_applied = True
    elif raw_score > 50:
        raw_score += 5
    else:
        raw_score -= 5
    
    # Simulate conditional scoring rule
    multiplier = 1.2 if bonus_applied and penalties == 0 else 1.0
    intermediate_result = raw_score * multiplier  # semi-relevant, used only if high tier
    final_score = int(intermediate_result) if raw_score > 70 else int(raw_score)
    
    # Dead code - never reached due to logic above
    if final_score < 0:
        final_score = 0
    
    return final_score

# Main simulation
base_points = 75
penalty_count = 3
timing_data = [0.4, 0.6, 0.8]

total_time = sum(timing_data)
avg_time = total_time / len(timing_data)

# Irrelevant preprocessing
normalized_time = avg_time * 100
offset_correction = normalized_time - int(normalized_time)

diagnostic_flag = avg_time > 0.5
auxiliary_value = 42 if diagnostic_flag else 24

# Core computation chain
preliminary_score = analyze_performance(avg_time * 1000, penalty_count, base_points)

# Secondary adjustment using different logic path
final_score = calculate_adjusted_score(base_points, penalty_count)

# Additional distraction: unused aggregation
aggregated_diagnostics = [preliminary_score, auxiliary_value, offset_correction]
summary_stat = sum(aggregated_diagnostics) / len(aggregated_diagnostics)

print(f"Result: {final_score}")