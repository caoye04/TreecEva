def analyze_efficiency(metrics):
    base = sum(metrics) / len(metrics)
    adjustment = 0
    if base > 80:
        adjustment = 10
    elif base > 60:
        adjustment = 5
    else:
        adjustment = -5
    
    # Distractor: irrelevant string processing
    status_msg = "Efficiency: " + ("High" if base > 80 else "Medium" if base > 60 else "Low")
    status_flag = status_msg.replace("High", "H").replace("Medium", "M").replace("Low", "L")
    debug_code = f"[{status_flag}]"

    return base + adjustment


def calculate_stress_level(hours, deadlines):
    stress_index = 0
    for h in hours:
        if h > 12:
            stress_index += 3
        elif h > 8:
            stress_index += 2
        else:
            stress_index += 1
    
    # Dead code path - never executed due to logic above
    if stress_index < 0:
        stress_index = 0  # unreachable

    penalty = 0
    lambda_adjust = lambda x: x * 1.5 if x > 2 else x
    return lambda_adjust(stress_index)

# Simulated team performance data
task_completion = [95, 87, 76, 92, 88]
hours_worked = [10, 14, 12, 9, 13]
deadlines_met = [True, False, True, True, False]

# Irrelevant grouping and counting (distractor)
completion_status = {}
for status in deadlines_met:
    key = str(status)[0].upper()
    completion_status[key] = completion_status.get(key, 0) + 1

productivity = analyze_efficiency(task_completion)
stress_level = calculate_stress_level(hours_worked, deadlines_met)
risk_factor = stress_level * 0.8

# Conditional expression with distractor variables
bonus_weight = 1.2 if productivity >= 85 else 0.9
temp_debug = (len(hours_worked), len(task_completion))  # unused tuple

# Core computation buried among distractions
final_score = 0
def evaluate_performance(efficiency, risk):
    global final_score
    score = efficiency - risk
    if efficiency >= 85 and risk < 10:
        score += 20
    elif efficiency >= 75:
        score += 10
    else:
        score -= 5
    
    # More distraction: unused string formatting
    report_line = f"Performance Score: {score:.1f} ({'Pass' if score >= 80 else 'Review'})"
    
    return int(score)

final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")