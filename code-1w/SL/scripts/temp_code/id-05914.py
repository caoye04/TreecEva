def analyze_efficiency(metrics):
    efficiency = sum(metrics) / len(metrics)
    adjusted = efficiency * 0.9 if efficiency > 80 else efficiency * 1.1
    return adjusted

productivity = [75, 82, 91, 67, 88]
baseline = 80

# Irrelevant string processing (distractor)
tags = ['high', 'medium', 'low']
label_map = {tag: idx for idx, tag in enumerate(tags)}
status_flags = set([tag.upper() for tag in tags])
flag_check = 'MEDIUM' in status_flags

# Simulate risk factors with dictionary operations
department_risk = {'dev': 0.1, 'ops': 0.3, 'qa': 0.05}
risk_factor = department_risk.get('dev', 0.2)

# Additional irrelevant list manipulation
temp_data = [x % 10 for x in productivity]
filtered = [x for x in temp_data if x > 5]
avg_remainder = sum(filtered) / len(filtered) if filtered else 0

# Real computation path
productivity_avg = sum(productivity) / len(productivity)
adjusted_productivity = analyze_efficiency(productivity)

# Complex conditional with red herring variables
if adjusted_productivity > baseline:
    bonus_weight = 1.2
    penalty = 0  # Dead code branch
else:
    bonus_weight = 1.0
    penalty = 5

project_count = len(productivity)
weight_ratio = project_count / (project_count + 1)

# Core logic embedded with distractors
raw_score = adjusted_productivity * (1 - risk_factor)
scaling_factor = weight_ratio * bonus_weight
interim = raw_score * scaling_factor

# Multiple assignment and tuple unpacking (irrelevant to final result)
stats = (min(productivity), max(productivity), sum(productivity))
lowest, highest, total = stats
deviation = highest - lowest

# Final evaluation using dictionary lookup and set operation
modifiers = {'bonus': bonus_weight, 'penalty': penalty}
active_mods = set(modifiers.keys())

if 'bonus' in active_mods:
    final_score = interim + modifiers['bonus'] * 2
else:
    final_score = interim

Result: {final_score}