def analyze_workload(tasks):
    base_load = sum([t['effort'] for t in tasks if t['priority'] > 1])
    adjustment_factor = 0.85 if len(tasks) > 5 else 1.0
    adjusted_load = base_load * adjustment_factor
    
    # Distractor: irrelevant computation on deadlines
    total_deadlines = sum([1 for t in tasks if 'urgent' in t])
    fake_pressure_index = total_deadlines ** 2 if total_deadlines > 0 else 0
    
    return adjusted_load


def evaluate_stress_level(hours_logged):
    stress_threshold = 40
    overtime_penalty = 0
    if hours_logged > stress_threshold:
        overtime_hours = hours_logged - stress_threshold
        overtime_penalty = overtime_hours * 1.5
    
    # Distractor: unused health metric
    theoretical_recovery_time = overtime_hours * 0.5 if 'overtime_hours' in locals() else 0
    
    return overtime_penalty


def calculate_performance_rating():
    tasks = [
        {'effort': 8, 'priority': 2, 'urgent': True},
        {'effort': 5, 'priority': 3},
        {'effort': 12, 'priority': 1},  # low priority, excluded from base_load
        {'effort': 7, 'priority': 4, 'urgent': True},
        {'effort': 3, 'priority': 2},
        {'effort': 9, 'priority': 3}
    ]
    
    hours_logged = 45
    
    # Relevant computations
    workload_score = analyze_workload(tasks)
    stress_deduction = evaluate_stress_level(hours_logged)
    
    # Secondary distractor variables (semi-relevant naming but not used directly)
    nominal_capacity = 50
    efficiency_ratio = workload_score / nominal_capacity if nominal_capacity else 0
    
    # Final score calculation
    raw_score = workload_score - stress_deduction
    scaling_constant = 1.2
    final_score = int(raw_score * scaling_constant)
    
    # Additional misleading variable
    apparent_efficiency = efficiency_ratio * (100 // (final_score % 10 + 1)) if final_score % 10 != 0 else 0
    
    return final_score

# Execution entry point
final_score = calculate_performance_rating()
print(f"Result: {final_score}")