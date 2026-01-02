def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    return sum(adjusted) // len(adjusted) if adjusted else 0

productivity = [8, 7, 9, 3, 6]
overhead_costs = [200, 150, 300]  # Irrelevant data

# Simulate environmental factors with no impact on final result
temperature_fluctuations = [23.5, 24.1, 22.7]
calibration_offset = sum(t ** 0.5 for t in temperature_fluctuations) / len(temperature_fluctuations)

baseline = analyze_efficiency(productivity)

risk_set_a = {1, 2, 3, 4, 5}
risk_set_b = {4, 5, 6, 7}
risk_intersection = risk_set_a & risk_set_b  # Size used later

# Dummy transformation chain
buffer_data = []
for val in productivity:
    temp = val + 2
    buffer_data.append(temp * 0.9)

mean_buffer = sum(buffer_data) / len(buffer_data)
drift_correction = mean_buffer - baseline  # Computed but unused

flags = [True, False, True]
status_summary = any(f for f in flags)  # Always True, not used

scaling_factor = len(risk_intersection)  # Should be 2

if baseline > 7:
    scaling_factor += 1
else:
    scaling_factor -= 1

# Secondary metric with partial relevance
efficiency_ratio = (baseline * scaling_factor) / 10.0

outlier_scores = set()
for i in range(1, 6):
    if i % 2 == 0:
        outlier_scores.add(i * scaling_factor)

# Unused collection
deprecated_tags = {x for x in range(3) if x != 1}  # {0, 2}

risk_factor = len(outlier_scores) + calibration_offset * 0  # Only length matters

# Core logic
prev_adjustment = 0
for i in range(len(productivity)):
    if productivity[i] >= 8:
        prev_adjustment += 1

intermediate = baseline + prev_adjustment

# Final evaluation function
def evaluate_performance(perf_metrics, risk):
    base_perf = sum(perf_metrics) / len(perf_metrics)
    penalty = 0
    if risk > 3:
        penalty = 5
    elif risk == 2:
        penalty = 2
    else:
        penalty = 0
    return int(base_perf) + penalty

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")