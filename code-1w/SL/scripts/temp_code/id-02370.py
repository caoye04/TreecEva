from itertools import compress, cycle

def analyze_metrics(data, threshold):
    filtered = list(compress(data, (x > threshold for x in data)))
    temp_sum = sum(x * 0.9 for x in filtered)  # Distractor: not used later
    return len(filtered)

# Simulate sensor readings and performance bands
readings = [85, 90, 78, 92, 88, 76, 94, 87]
baseline = 85
reliable_count = analyze_metrics(readings, baseline)

# Redundant transformation (distractor)
distorted_readings = [(r ** 2 + 3) // r for r in readings]

# Core logic: employee assessment with weighted tiers
assessments = [
    {'skill': 'debugging', 'rating': 88, 'weight': 1.2},
    {'skill': 'design', 'rating': 91, 'weight': 1.0},
    {'skill': 'testing', 'rating': 83, 'weight': 0.9},
    {'skill': 'integration', 'rating': 94, 'weight': 1.3}
]

scaling_factor = 0.85 if reliable_count >= 3 else 0.7

# Secondary distractor: unused statistical calculation
variance_proxy = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)

# Use lambda to generate dynamic adjustment based on pattern
adjustment_curve = list(map(lambda x: (x['rating'] * 0.1 + reliable_count * 2), assessments))

total_weighted = 0
max_rating = 0
for item in assessments:
    contribution = item['rating'] * item['weight']
    total_weighted += contribution
    if item['rating'] > max_rating:
        max_rating = item['rating']

average_contribution = total_weighted / len(assessments)

# Introduce tuple unpacking and conditional logic
bonus_tier = 'high' if average_contribution > 88 else 'standard'
bonuses = {'high': 12, 'standard': 5}
base_bonus = bonuses[bonus_tier]

# Complex but partially irrelevant structure
status_flags = [*cycle([True, False]), False, True][:len(assessments)]
diagnostic_info = {f"sensor_{i}": readings[i] * status_flags[i] for i in range(len(status_flags))}

# Key computation with distractors around it
raw_performance = average_contribution * scaling_factor
penalty = 0
if reliable_count < 2:
    penalty = 10
else:
    penalty = 2  # Distractor: constant override

intermediate_score = raw_performance - penalty

# Final aggregation using dictionary operation
summary_stats = {
    'initial': intermediate_score,
    'adjustments': sum(adjustment_curve),
    'bonus': base_bonus
}

final_score = summary_stats['initial'] + summary_stats['bonus']
print(f"Result: {final_score}")