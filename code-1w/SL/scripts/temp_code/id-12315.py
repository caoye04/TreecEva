from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
raw_data = [15, 23, 8, 42, 19, 37]
weights = [0.1, 0.3, 0.15, 0.25, 0.05, 0.15]

# Irrelevant preprocessing: normalize data (not used in final logic)
normalized = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data)), 3) for x in raw_data]

# Distractor: unused transformation
temp_offsets = list(map(lambda x: (x * 0.01) + 0.5, raw_data))

# Slice relevant segments
primary_inputs = raw_data[1:5]  # 23, 8, 42, 19
secondary_weights = weights[:4]

# Track state with defaultdict (semi-relevant)
metric_contributions = defaultdict(float)
for i, val in enumerate(primary_inputs):
    metric_contributions[f'metric_{i}'] = val * secondary_weights[i]

# Additional distraction: dead computation path
dummy_aggregate = sum([x ** 0.5 for x in temp_offsets if x > 0.7])

# Simulate outcome flags based on thresholds
outcomes = []
for val in primary_inputs:
    if val > 40:
        outcomes.append(3)
    elif val > 20:
        outcomes.append(2)
    elif val > 10:
        outcomes.append(1)
    else:
        outcomes.append(0)

# Introduce misleading cumulative score
running_risk = 0
for flag in outcomes:
    running_risk += flag * 0.1

# Actual core logic begins here
raw_outcomes = [x * 2 for x in outcomes]  # Amplify signals

# Weight mapping (only some are used)
metric_weights = {
    'm0': 0.2,
    'm1': 0.25,
    'm2': 0.3,
    'm3': 0.25
}

# Real computation: weighted combination
weighted_sum = 0
for i in range(len(raw_outcomes)):
    key = f'm{i}'
    if key in metric_weights:
        weighted_sum += raw_outcomes[i] * metric_weights[key]

# Final adjustment based on auxiliary condition
bonus_trigger = sum(primary_inputs) > 90
final_score = weighted_sum + (5 if bonus_trigger else 0)

# Key statement
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Helper function defined after use (semantic confusion)
def evaluate_performance(weights_dict, outcome_values):
    base = 0
    for idx, val in enumerate(outcome_values):
        weight = weights_dict.get(f'm{idx}', 0)
        base += val * weight
    bonus = 5 if sum(outcome_values) >= 10 else 0
    return base + bonus

print(f"Result: {final_score}")