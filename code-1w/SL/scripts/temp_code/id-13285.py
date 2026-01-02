def analyze_efficiency(values):
    weighted_sum = sum([v * (i + 1) for i, v in enumerate(values)])
    normalization_factor = len(values) * (len(values) + 1) / 2
    return weighted_sum / normalization_factor if normalization_factor else 0

# Simulate daily work metrics over a week
daily_focus_levels = [0.8, 0.6, 0.9, 0.4, 0.7]
daily_task_completion = [5, 3, 6, 2, 4]

# Compute efficiency scores
efficiency_scores = []
for i in range(len(daily_focus_levels)):
    score = daily_focus_levels[i] * daily_task_completion[i]
    efficiency_scores.append(score)

baseline_efficiency = sum(efficiency_scores) / len(efficiency_scores)
adjusted_baseline = baseline_efficiency * 1.1 if baseline_efficiency > 4 else baseline_efficiency * 0.9

# Hidden debug check (irrelevant to final result)
temp_debug_data = [x for x in efficiency_scores if x > 3.0]
dropped_entries = len(efficiency_scores) - len(temp_debug_data)  # unused distraction

# Calculate productivity index using list comprehension
productivity_index = [x / adjusted_baseline for x in efficiency_scores]
productivity = sum(productivity_index) / len(productivity_index)

# Risk assessment based on inconsistency
peak_fluctuation = max(efficiency_scores) - min(efficiency_scores)
risk_factor = 0.5 if peak_fluctuation > 2.0 else 0.2

# Unused but misleading intermediate calculation (dead computation)
phantom_risk_adjustment = peak_fluctuation * 0.3 + 1.2  # not used later

# Core evaluation function
def evaluate_performance(prod, risk):
    if prod < 0.8:
        return int(50 - 10 * risk)
    elif prod < 1.2:
        base = 75
        penalty = 20 * risk
        return int(base - penalty)
    else:
        base = 90
        bonus = int(10 * prod)
        extra_noise = bonus * 0.1  # red herring
        return int(base + bonus - (risk * 5))

# Final performance score
temporary_interim_result = evaluate_performance(productivity, risk_factor)
final_score = evaluate_performance(productivity, risk_factor)

# Logging irrelevant summary
summary_report = {"entries": len(efficiency_scores), "version": "2.1", "valid": True}

print(f"Result: {final_score}")