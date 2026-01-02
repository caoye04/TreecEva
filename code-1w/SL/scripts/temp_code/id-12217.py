def analyze_trends(data_slice):
    trend_value = sum(data_slice) / len(data_slice)
    offset_correction = max(data_slice) - min(data_slice)
    adjusted_trend = trend_value * 0.9 if offset_correction > 10 else trend_value * 1.1
    return adjusted_trend

benchmark_data = [3, 7, 8, 12, 15, 9, 4]

# Irrelevant preprocessing (distractor)
preliminary_scan = [x ** 2 for x in benchmark_data if x % 2 == 1]
duplicate_filter = [x for x in preliminary_scan if x > 20]

subset_window = benchmark_data[1:6]  # Focus on central performance window

evaluation_weights = []
for i in range(len(subset_window)):
    weight = (i + 1) * 0.5
    evaluation_weights.append(weight)

weighted_sum = 0
for i, val in enumerate(subset_window):
    weighted_sum += val * evaluation_weights[i]

raw_metric = weighted_sum / sum(evaluation_weights)

temp_debug_log = f"Raw metric computed: {raw_metric:.2f}"
status_flag = "OK" if raw_metric > 10 else "LOW"

baseline_reference = analyze_trends(benchmark_data)

# Secondary irrelevant check (dead logic path)
consistency_check = True
for x in benchmark_data:
    if x < 0:
        consistency_check = False

scaling_factor = 1.25 if status_flag == "OK" else 0.75
intermediate_score = raw_metric * scaling_factor

penalty_adjustment = 0
if len(duplicate_filter) > 3:
    penalty_adjustment = 5

# Final calculation
final_score = intermediate_score - penalty_adjustment + (baseline_reference * 0.1)

# Output result as required
print(f"Result: {final_score}")