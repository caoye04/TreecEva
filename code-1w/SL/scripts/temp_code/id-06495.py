from collections import defaultdict
import math

def analyze_efficiency(metrics):
    efficiency = 0
    adjustments = [0.1, -0.2, 0.3]
    temp_log = []
    for val in metrics:
        if val > 80:
            efficiency += val * 0.15
        elif val > 50:
            efficiency += val * 0.05
        temp_log.append(efficiency)
    return efficiency

def calculate_stress_level(hours):
    stress = 0
    for h in hours:
        if h > 12:
            stress += (h - 12) * 2
        elif h < 6:
            stress += 1
    return max(stress, 1)

def evaluate_performance(output, risk):
    base = sum(output) / len(output)
    penalty = 0
    if risk > 10:
        penalty = risk * 1.5
    elif risk > 5:
        penalty = risk * 0.8
    score = base - penalty
    multiplier = 1.2 if score > 40 else 0.9
    score *= multiplier
    return int(score)

# Simulated dataset
productivity_data = [85, 90, 78, 92, 88]
risk_assessment = [3, 7, 11, 5, 9]
work_hours = [10, 13, 9, 15, 8]

# Irrelevant aggregation (distractor)
task_counter = defaultdict(int)
for i, val in enumerate(productivity_data):
    task_counter[f'week_{i}'] += val // 10

# Unused transformation (dead code path)
normalized = [round(math.log(x + 1), 2) for x in productivity_data if x > 0]

# Compute intermediate values
raw_efficiency = analyze_efficiency(productivity_data)
risk_factor = calculate_stress_level(work_hours)

# Key evaluation logic with distractors
scaling_factor = 1.0
if raw_efficiency > 100:
    scaling_factor = 1.5
elif raw_efficiency > 50:
    scaling_factor = 1.2  # This will be triggered

adjusted_risk = risk_factor * scaling_factor

# Critical statement
final_score = evaluate_performance(productivity_data, adjusted_risk)

# Print result
print(f"Result: {final_score}")