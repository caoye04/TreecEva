def analyze_productivity(log, threshold=5):
    total_entries = len(log)
    valid_count = sum(1 for entry in log if entry > threshold)
    efficiency = valid_count / total_entries if total_entries else 0
    return efficiency

baseline = [3, 7, 8, 4, 9, 6]
activity_log = [5, 6, 2, 8, 7, 3, 9, 4]

# Auxiliary computation - not directly used in final result
temp_weights = [x * 0.5 + 2 for x in baseline]
avg_weight = sum(temp_weights) / len(temp_weights)

# Simulate conditional adjustments based on pattern matching
adjustment_factor = 1.0
if len(activity_log) > 6:
    adjustment_factor = 1.2 if sum(1 for x in activity_log if x >= 7) >= 3 else 1.1

# Secondary metric with partial relevance
effective_units = 0
for val in activity_log:
    if val >= 6:
        effective_units += 1
    elif val == 5:
        effective_units += 0.5

# Distractor: complex-looking but unused transformation
distorted_log = [((x ** 2) % 11) + 1 for x in activity_log if x % 2 == 0]
shadow_index = sum(distorted_log) / (len(distorted_log) or 1)

# Core logic chain
raw_performance = analyze_productivity(activity_log, threshold=4)
scaling_factor = adjustment_factor * (1 + avg_weight / 100)
weighted_score = raw_performance * 100 * scaling_factor

# Conditional expression usage (Python idiom)
penalty = 10 if weighted_score > 80 and len(baseline) % 2 == 1 else 5

# Final aggregation incorporating multiple concepts
def calculate_performance(base, log):
    base_effort = sum(base) / len(base)
    peak_frequency = sum(1 for x in log if x >= 7)
    consistency = peak_frequency / len(log)
    score = (base_effort * 0.3) + (consistency * 100 * 0.7)
    # Apply penalty only if certain combinatorial condition holds
    high_activity_days = sum(1 for x in log if x >= 6)
    is_balanced = abs(len(log) - len(base)) <= 2
    final_modifier = 0.95 if high_activity_days >= 4 and is_balanced else 1.0
    return int((score * final_modifier) - penalty)

final_score = calculate_performance(baseline, activity_log)
print(f"Target result: {final_score}")