def analyze_metrics(data):
    baseline = sum(data) / len(data)
    deviations = [abs(x - baseline) for x in data]
    adjusted = [x * 0.9 + baseline * 0.1 for x in data if x > baseline]
    return adjusted

benchmark_results = [85, 92, 78, 96, 88, 76, 94]

# Irrelevant preprocessing
shadow_copy = benchmark_results.copy()
sorted_data = sorted(shadow_copy, reverse=True)
ranked_scores = {i+1: val for i, val in enumerate(sorted_data)}

# Distractor computation: entropy-like measure (not used)
import math
total = sum(benchmark_results)
probabilities = [x / total for x in benchmark_results]
entropy = -sum(p * math.log(p) for p in probabilities if p > 0)

# Real processing begins
filtered_high = [score for score in benchmark_results if score >= 85]
scaling_factor = 1.2 if len(filtered_high) > 4 else 1.0
amplified_scores = [score * scaling_factor for score in filtered_high]

# Secondary distractor: simulate calibration drift
baseline_drift = 0
for i in range(len(amplified_scores)):
    baseline_drift += amplified_scores[i] * 0.01
    amplified_scores[i] += baseline_drift

# Aggregation with conditional logic
temp_sum = 0
for s in amplified_scores:
    if s < 100:
        temp_sum += s
    else:
        temp_sum += s * 0.95

consistency_bonus = 5 if len(filtered_high) == len(set(filtered_high)) else 0

# Key state tracking
performance_log = []
for idx, val in enumerate(amplified_scores):
    performance_log.append(f"Step {idx}: {val:.1f}")

# Final calculation
def calculate_performance(results):
    high_performers = len([r for r in results if r >= 85])
    multiplier = 1.1 if high_performers >= 4 else 1.0
    base_score = sum(results) / len(results)
    return int(base_score * multiplier) + consistency_bonus

final_score = calculate_performance(benchmark_results)
print(f"Result: {final_score}")