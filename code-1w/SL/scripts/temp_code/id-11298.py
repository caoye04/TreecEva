def analyze_productivity(metrics, thresholds):
    exceeded = 0
    for val in metrics.values():
        if val > thresholds['target']:
            exceeded += 1
    return exceeded

# Simulate employee performance assessment across multiple dimensions
assessments = {
    'planning': 84,
    'execution': 92,
    'adaptability': 78,
    'collaboration': 88,
    'innovation': 73
}

thresholds_config = {
    'target': 80,
    'minimum': 65,
    'bonus_eligibility': 85
}

# Irrelevant helper: counts how many are below threshold (not used in final logic)
def count_underperforming(data, limit):
    count = 0
    for k, v in data.items():
        if v < limit:
            count += 1
    return count

# Distractor variables
temp_result = [x - 70 for x in assessments.values()]
offset_adjustment = sum(temp_result) // len(temp_result)

baseline_shift = {
    key: val + offset_adjustment for key, val in assessments.items()
}

# Real computation begins
high_performers = analyze_productivity(assessments, thresholds_config)

efficiency_flags = tuple(v > 85 for v in assessments.values())
bonus_awarded = efficiency_flags.count(True) >= 2

scaling_factor = 1.0
if high_performers >= 3:
    scaling_factor = 1.2
elif high_performers == 2:
    scaling_factor = 1.1
else:
    scaling_factor = 0.9

# Secondary distraction: unused weighted calculation
weighted_score = 0
for skill, score in assessments.items():
    weight = 1.0
    if 'tion' in skill:
        weight = 1.3
    elif 'ion' in skill:
        weight = 1.1
    weighted_score += score * weight

# Actual aggregation logic
top_three = sorted(assessments.values(), reverse=True)[:3]
raw_aggregate = sum(top_three)

# Use dictionary and slicing operations
snapshot = list(assessments.items())[1:4]  # middle three as snapshot
snapshot_avg = sum([v for k, v in snapshot]) / len(snapshot)

# Final determination using set operation to deduplicate (though no dups here)
unique_scores = set(assessments.values())
core_stability = len(unique_scores) > 3

final_score = raw_aggregate * scaling_factor

if core_stability and bonus_awarded:
    final_score += 10

# Print result for execution verification
print(f"Result: {final_score}")