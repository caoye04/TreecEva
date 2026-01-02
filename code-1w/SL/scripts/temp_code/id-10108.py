def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = {k: v / max(metrics.values()) for k, v in metrics.items()}
    exceeded = set()
    for metric, value in metrics.items():
        if value > thresholds.get(metric, 0):
            exceeded.add(metric)
    
    # Semi-relevant computation
    compliance_rate = len(exceeded) / len(thresholds) if thresholds else 0
    return exceeded, compliance_rate

# Main data
student_scores = {'algebra': 85, 'calculus': 92, 'physics': 78, 'chemistry': 88}
department_caps = {'algebra': 90, 'calculus': 95, 'physics': 80, 'chemistry': 90}

# Distractor variables
weighted_avg = sum(v * 0.25 for v in student_scores.values())
scaled_scores = tuple(s / 100 for s in student_scores.values())
histogram_bins = [0, 80, 85, 90, 95, 100]

# Nested logic with multiple concepts
exceed_set, adherence = analyze_performance(student_scores, department_caps)

# Additional irrelevant intermediate steps
buffer_zone = 5
adjusted_cap = {subj: cap - buffer_zone for subj, cap in department_caps.items()}
marginally_exceeding = set()
for subject in student_scores:
    if student_scores[subject] > adjusted_cap[subject]:
        marginally_exceeding.add(subject)

# Core calculation chain
base_score = sum(1 for s in student_scores.values() if s >= 85)
bonus = len(exceed_set.intersection({'calculus', 'algebra'}))
penalty = 0
if 'physics' not in exceed_set:
    penalty += 2

# Red herring function that's defined but not used
def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Another distractor: dead code path
status_flags = {}
for sub in student_scores:
    if sub in ['algebra', 'calculus']:
        status_flags[sub] = 'priority'
    else:
        status_flags[sub] = 'standard'

# Final aggregation with tuples and set influence
achievement_tier = ('basic', 'intermediate', 'advanced')[min(bonus, 2)]
tier_bonus_map = {'basic': 0, 'intermediate': 1, 'advanced': 3}

temp_debug = [base_score, bonus, penalty]  # Unused debug list

final_score = base_score + tier_bonus_map[achievement_tier] - penalty

# Key output
print(f"Result: {final_score}")