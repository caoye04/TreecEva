from collections import defaultdict

# Simulate system performance monitoring with noise
base_metrics = [120, 85, 90, 110, 95]
weights = [0.1, 0.2, 0.4, 0.2, 0.1]

# Irrelevant aggregation (distractor)
temp_aggregate = sum([m * w for m, w in zip(base_metrics, weights)])
baseline_offset = temp_aggregate * 0.05

# Core data processing
raw_efficiency = sum(base_metrics) / len(base_metrics)
error_count = 3
penalty_rate = 2.5

# Misleading secondary calculation (dead code path)
if error_count > 5:
    adjustment_factor = 0.8
else:
    adjustment_factor = 1.0  # Never used

# Data transformation using dictionary operations
efficiency_map = defaultdict(float)
efficiency_map['initial'] = raw_efficiency
efficiency_map['calibrated'] = efficiency_map['initial'] - baseline_offset

# Conditional expression for robustness flag (semi-relevant)
robustness_flag = 'high' if efficiency_map['calibrated'] > 90 else 'medium'
efficiency = efficiency_map['calibrated'] if robustness_flag == 'high' else efficiency_map['initial']

# Spurious intermediate computations
shadow_buffer = [efficiency * (1 + i*0.01) for i in range(5)]
smoothed_efficiency = sum(shadow_buffer) / len(shadow_buffer)  # Not used

# Actual evaluation logic
def evaluate_performance(eff, err):
    base = eff * 0.8
    deduction = err * penalty_rate * 3
    bonus = 5 if eff > 95 else 0
    return int(base - deduction + bonus)

# Key statement
final_score = evaluate_performance(efficiency, error_count)

# Print result as required
print(f"Target result: {final_score}")