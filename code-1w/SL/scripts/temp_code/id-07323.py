from itertools import cycle

# Simulate daily work metrics over a 5-day period
daily_hours = [8.5, 7.2, 9.0, 6.5, 10.0]
errors_per_day = [2, 1, 3, 0, 4]
context_switches = [15, 23, 18, 12, 25]  # Distraction metric (not directly used)

# Derived productivity factors
productivity = []
for i, hours in enumerate(daily_hours):
    efficiency = hours / (1 + errors_per_day[i])
    adjusted_efficiency = efficiency * (0.95 ** context_switches[i])  # Diminishing returns
    productivity.append(round(adjusted_efficiency, 3))

# Irrelevant transformation - red herring
temp_analysis = []
for val in productivity:
    if val > 7:
        temp_analysis.append(val * 0.1)
    elif val > 5:
        temp_analysis.append(val * 0.05)
    else:
        temp_analysis.append(0)

# Calculate baseline performance index using slicing and sum
performance_window = productivity[1:4]  # Middle three days
baseline_index = sum(performance_window) / len(performance_window)

# Risk assessment based on error trends
error_trend = 'increasing' if errors_per_day[-1] > errors_per_day[0] else 'decreasing'
risk_factor = 1.2 if error_trend == 'increasing' else 0.8

# Spurious correlation attempt - distractor
fake_correlation = 0
for h, e in zip(daily_hours, errors_per_day):
    fake_correlation += h * e
fake_correlation /= len(daily_hours)

# Core evaluation function
def evaluate_performance(efficiencies, risk):
    peak = max(efficiencies)
    volatility = max(efficiencies) - min(efficiencies)
    
    # Apply risk-weighted smoothing
    smoothed_peak = peak * (1 / risk)
    stability_bonus = 10 * (1 - (volatility / peak))  # Normalize bonus
    
    # Final composite score
    score = (smoothed_peak * 40) + stability_bonus
    
    # Dead code branch - misleading
    if len(efficiencies) > 10:
        score *= 1.1  # Never executed
    
    return int(score)

# Execute main logic
final_score = evaluate_performance(productivity, risk_factor)

# Additional unrelated tracking (distractor)
work_patterns = list(zip(daily_hours, errors_per_day))
cycle_iter = cycle(['focus', 'review', 'break'])
pattern_summary = [next(cycle_iter) for _ in range(len(work_patterns))]

# Print final result as required
print(f"Result: {final_score}")