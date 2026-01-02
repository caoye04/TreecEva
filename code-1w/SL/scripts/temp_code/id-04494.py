def analyze_efficiency(metrics):
    adjusted = [m * 1.1 for m in metrics if m > 5]
    baseline = sum(metrics) / len(metrics)
    bonus = 0
    if len(adjusted) > 2:
        bonus += 15
    return baseline, bonus


def calculate_stress_level(hours, thresholds):
    stress = 0
    for h, t in zip(hours, thresholds):
        if h > t:
            stress += (h - t) * 1.5
    return max(stress, 5)


def evaluate_performance(output, risk):
    score = 0
    if output > 80:
        score += 30
    elif output > 60:
        score += 20
    else:
        score += 10
    
    # Distractor: complex but unused calculation
    temp_values = [output // (i+1) for i in range(3)]
    temp_sum = sum(temp_values) // 2
    adjustment = temp_sum * 0.1  # Not actually used
    
    if risk < 30:
        score += 25
    elif risk < 50:
        score += 15
    else:
        score += 5
        
    multiplier = 1.0
    if output > 70 and risk < 40:
        multiplier = 1.2
    
    return int(score * multiplier)

# Main execution
work_metrics = [8, 9, 7, 10, 6]
working_hours = [9, 8, 10, 11]
threshold_levels = [8, 7, 9, 10]

avg_effort, extra_bonus = analyze_efficiency(work_metrics)

stress_index = calculate_stress_level(working_hours, threshold_levels)
productivity = sum(work_metrics[:3]) * 3.5  # First three days weighted

# Irrelevant slicing and string operations as noise
status_log = "Productivity analysis completed successfully"
diagnostic_tag = status_log[12:21].upper() + "_" + str(len(work_metrics))

# Unused intermediate calculations
phantom_data = [x for x, _ in enumerate(work_metrics)]
dummy_pairs = list(zip(phantom_data, working_hours))

risk_factor = stress_index * 1.8

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

Result: {final_score}