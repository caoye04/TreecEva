from itertools import cycle

# Simulate daily work metrics over a biweekly period
days = 14
hours_worked = [8.5, 7.0, 9.5, 10.0, 8.0, 0.0, 0.0, 9.0, 8.5, 11.0, 7.5, 8.0, 10.5, 9.0]
pomodoros_completed = [4, 3, 6, 7, 5, 0, 0, 6, 4, 8, 3, 5, 7, 6]
bugs_introduced = [1, 0, 2, 1, 0, 0, 0, 1, 1, 3, 2, 1, 2, 1]

# Distractor: Irrelevant health tracking
daily_steps = [8200, 6500, 9100, 7300, 10500, 3200, 2800, 8700, 7600, 11300, 5400, 8100, 9500, 8900]
hydration_level = [2.1, 1.8, 2.4, 2.0, 2.7, 1.2, 1.0, 2.3, 1.9, 2.5, 1.7, 2.0, 2.6, 2.4]

# Helper function to compute efficiency factor
def compute_efficiency(hours, pomos):
    base = sum(p for p in pomos) * 25
    time_cost = sum(h ** 0.5 for h in hours) * 10
    return (base - time_cost) / 100

# Compute productivity index using list comprehension and lambda
productivity_data = list(map(lambda h: max(0, h - 1), hours_worked))
efficiency_ratio = compute_efficiency(hours_worked, pomodoros_completed)
productivity = efficiency_ratio * len([p for p in pomodoros_completed if p >= 4])

# Risk assessment based on error rate and overtime
overtime_days = len([h for h in hours_worked if h > 9.0])
error_rate = sum(bugs_introduced) / len(bugs_introduced)
risk_factor = overtime_days * 1.5 + error_rate * 10

# Distractor: unused performance tiers
tier_labels = ['Basic', 'Standard', 'Advanced', 'Expert']
tier_thresholds = {t: (i+1)*10 for i, t in enumerate(tier_labels)}

def calculate_wellness_index(steps, hydration):
    # Irrelevant wellness calculation (dead logic path)
    step_avg = sum(steps) / len(steps)
    hyd_avg = sum(hydration) / len(hydration)
    return (step_avg / 1000) * hyd_avg

# Unused helper: misleading function
compute_stress_level = lambda bugs, hours: sum(b * h for b, h in zip(bugs, hours) if h > 8) / 5

# Core evaluation logic with interdependent steps
def evaluate_risk_adjusted_productivity(p):
    if p > 30:
        return p * 0.9
    elif p > 20:
        return p * 1.1
    else:
        return p * 1.3

# Introduce cycling pattern over work rhythm
work_rhythm = cycle([1, -1, 0, 1, 1])
rhythm_adjustment = sum([next(work_rhythm) for _ in range(len(hours_worked))])

# Final performance score computation
adjusted_productivity = evaluate_risk_adjusted_productivity(productivity)
penalty = abs(rhythm_adjustment) * 2
final_score = adjusted_productivity - penalty - risk_factor

# Print result as required
print(f"Target result: {final_score}")