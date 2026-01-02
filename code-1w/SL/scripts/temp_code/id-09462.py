def analyze_efficiency(metrics):
    base_efficiency = sum([m * 0.85 for m in metrics if m > 2])
    adjustment = len([m for m in metrics if m < 1]) * 1.5
    return base_efficiency - adjustment


def calculate_stress_level(workload):
    stress = 0
    for hour in workload:
        if hour > 6:
            stress += (hour - 6) * 2
    return stress + len(workload)


def evaluate_risk(employee_data):
    risk = 0
    if employee_data['absences'] > 3:
        risk += 2
    if employee_data['errors'] > 5:
        risk += 3
    risk += max(0, employee_data['complaints'] - 2)
    return risk

# Simulated employee performance data
productivity = [3.2, 4.1, 2.8, 5.0, 3.6]
stress_metrics = [7, 5, 8, 6, 9]  # Weekly overtime hours
employee_info = {
    'absences': 2,
    'errors': 7,
    'complaints': 4
}

# Irrelevant distraction variables
baseline_target = 85.0
target_growth_rate = 0.07
project_count = 4
department_code = "DEV-ALPHA"

# Auxiliary computations with partial relevance
workload_stress = calculate_stress_level(stress_metrics)
efficiency_rating = analyze_efficiency(productivity)
risk_factor = evaluate_risk(employee_info)

# Secondary calculations that influence final logic
performance_multiplier = 1.0 if efficiency_rating > 10 else 0.85
risk_penalty = risk_factor * 1.2 if risk_factor > 4 else 0.0

# Main evaluation chain
raw_score = efficiency_rating * performance_multiplier
adjusted_score = raw_score - risk_penalty

# Distraction: unused function call and dead code path
unused_flag = False
if project_count > 10:
    baseline_target *= (1 + target_growth_rate)
    unused_flag = True

# Final scoring logic
final_score = int(round(adjusted_score))

# Output result as required
print(f"Result: {final_score}")