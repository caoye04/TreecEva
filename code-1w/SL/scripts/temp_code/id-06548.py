from itertools import cycle

# Simulate daily work metrics over a sprint
hours_worked = [8, 7, 9, 6, 10, 8, 7]
tasks_completed = [3, 2, 4, 1, 5, 3, 2]
bugs_introduced = [1, 0, 2, 1, 3, 0, 1]

# Distractor: Irrelevant health tracking data
daily_steps = [8200, 6500, 9100, 5400, 10200, 7800, 6900]
hydration_level = [2.1, 1.8, 2.5, 1.7, 3.0, 2.2, 1.9]  # liters

# Productivity scoring with non-linear weighting
productivity = sum(t * (h / 8) ** 0.5 for h, t in zip(hours_worked, tasks_completed))

# Risk factor based on bug rate and inconsistency
avg_hours = sum(hours_worked) / len(hours_worked)
fluctuation_penalty = sum(abs(h - avg_hours) for h in hours_worked)
bug_severity = sum(b ** 1.5 for b in bugs_introduced)
risk_factor = fluctuation_penalty * 0.3 + bug_severity * 2.5

# Distractor: unused function
calculate_wellness_index = lambda steps, water: sum(s / 1000 + w * 0.8 for s, w in zip(steps, water))

# Distractor: dead code path
temperature_readings = [22.1, 23.5, 21.8, 24.0, 22.7, 23.1, 22.4]
if False:
    climate_stability = sum(1 for t in temperature_readings if 22 <= t <= 23)

# Core evaluation logic
def evaluate_performance(efficiency, risk):
    base_score = efficiency * 10
    deduction = risk * 1.75
    bonus = 0
    
    # Conditional bonus for high-effort days
    effort_flags = [h >= 9 and t >= 4 for h, t in zip(hours_worked, tasks_completed)]
    if any(effort_flags):
        bonus += 15 * sum(effort_flags)
    
    # Adjustment using lambda-based normalization
    normalize = lambda x: (x - min(hours_worked)) / (max(hours_worked) - min(hours_worked) + 1e-5)
    consistency_bonus = 10 * (1 - sum(map(normalize, hours_worked)) / len(hours_worked))
    
    return base_score - deduction + bonus + consistency_bonus

# Evaluate final outcome
final_score = evaluate_performance(productivity, risk_factor)

# Print result for extraction
print(f"Result: {final_score}")