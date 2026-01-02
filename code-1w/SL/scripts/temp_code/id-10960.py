def evaluate_performance(output, risk):
    base_efficiency = output * 0.85
    penalty = 0
    if output < 100:
        penalty += 15
    elif output >= 200:
        bonus = 10
        penalty -= bonus  # Only affects high output

    adjusted = base_efficiency - penalty

    # Distractor: unused calculation for 'theoretical_max'
    theoretical_max = (output + 50) * 0.95 if risk < 0.5 else (output + 50) * 0.7
    scaling_factor = 1.1 if risk < 0.4 else 0.9

    return int(adjusted * scaling_factor)

# Simulated team metrics
task_completion_rate = 230
error_rate = 0.38
hours_worked = 160  # Irrelevant metric

productivity = task_completion_rate - (error_rate * 100)
risk_factor = error_rate / 0.9

# Dummy variables to increase cognitive load
baseline_projection = productivity * 1.05
drift_correction = baseline_projection - productivity
if drift_correction > 10:
    drift_adjusted = drift_correction * 0.75
else:
    drift_adjusted = 0

# Key computation point
final_score = evaluate_performance(productivity, risk_factor)

# Additional red herring: unused set operation
historical_scores = {180, 195, 210, 225}
projected_range = {x * 0.9 for x in historical_scores if x > 200}
overlap = historical_scores & projected_range  # Not used

# Print result as required
print(f"Result: {final_score}")