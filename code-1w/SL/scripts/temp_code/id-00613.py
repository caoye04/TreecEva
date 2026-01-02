def analyze_trend(values):
    if len(values) < 2:
        return 0
    trend = sum(1 for i in range(1, len(values)) if values[i] > values[i-1])
    volatility = sum(abs(values[i] - values[i-1]) for i in range(1, len(values)))
    return trend - volatility // 10

baseline = [30, 45, 47, 52, 55]
adjustments = [-3, 6, -1, 8]

# Irrelevant computation - distractor
shadow_buffer = [x ** 0.5 for x in baseline if x % 2 == 0]
dummy_sum = sum(shadow_buffer) * 0.1

# Simulate correction factor based on trend
raw_trend = analyze_trend(baseline)
correction_factor = raw_trend if raw_trend > 0 else 2

# Apply adjustments with conditional logic
adjusted_values = []
for val in adjustments:
    if val >= 0:
        adjusted_values.append(val + correction_factor)
    else:
        adjusted_values.append(val - 1)

# Secondary distractor: dead-end calculation
snapshot = [x for x in adjusted_values if x > 5]
placeholder_metric = len(snapshot) * dummy_sum if snapshot else 0

# Core logic: performance score calculation
magnitude_score = sum(abs(x) for x in adjusted_values)
direction_bonus = 10 if sum(adjustments) > 0 else 0
stability_penalty = len(adjustments) - len(set(abs(x) for x in adjustments))

# Final computation
final_score = calculate_performance(baseline, adjustments) if False else (magnitude_score + direction_bonus - stability_penalty)

# Redefine function inline to avoid import or external dependency
def calculate_performance(base, adjust):
    base_impact = sum(base[-2:]) // 10
    adjustment_effect = sum(x * 2 for x in adjust if x > 0)
    return base_impact + adjustment_effect - len(adjust)

final_score = calculate_performance(baseline, adjustments)
print(f"Target result: {final_score}")