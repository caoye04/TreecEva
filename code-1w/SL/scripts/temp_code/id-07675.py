from collections import defaultdict

# Simulate employee performance metrics across departments
def analyze_department_metrics(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    error_rate_threshold = 0.05
    phantom_counter = 0  # Distractor: not used in final logic

    for emp_id, data in employees.items():
        dept = data['department']
        stats[dept]['output'] += data['tasks_completed']
        stats[dept]['errors'] += data['errors_made']
        if data['errors_made'] > 0:
            consistency_ratio = data['tasks_completed'] / (data['errors_made'] + 1)
            if consistency_ratio > 10:
                phantom_counter += 1  # Dead code path: doesn't impact result

    return stats

# Determine team efficiency with conditional weighting
def calculate_efficiency(metrics):
    efficiency_map = {}
    total_output = 0
    total_error_penalty = 0

    for dept, values in metrics.items():
        raw_output = values['output']
        error_count = values['errors']
        baseline_effort = raw_output * 1.5

        # Apply penalty only if error rate exceeds threshold
        error_rate = error_count / (raw_output + 1)
        adjusted_output = raw_output * (0.9 if error_rate > 0.04 else 1.0)

        # Complex but irrelevant scaling factor
        scaling_factor = 1.0
        if raw_output > 50:
            scaling_factor *= 1.1
        if error_rate < 0.03:
            scaling_factor *= 1.05

        efficiency_map[dept] = adjusted_output * scaling_factor
        total_output += adjusted_output
        total_error_penalty += error_count * 2

    aggregate_efficiency = total_output - total_error_penalty
    return efficiency_map, aggregate_efficiency

# Evaluate overall performance with risk adjustment
def evaluate_performance(productivity, risk_factor):
    base_score = productivity * 1.2
    adjusted_score = base_score

    if risk_factor > 0.5:
        adjusted_score *= 0.85
    elif risk_factor < 0.2:
        adjusted_score *= 1.1
    else:
        adjusted_score *= 1.0

    volatility_buffer = 0
    for i in range(3):  # Loop with no effect (distractor)
        volatility_buffer += (i * 0.01) % 0.01

    final_score = int(adjusted_score - volatility_buffer)  # Final assignment point
    return final_score

# Main execution flow
if __name__ == "__main__":
    employee_data = {
        'E101': {'department': 'Engineering', 'tasks_completed': 85, 'errors_made': 3},
        'E102': {'department': 'Engineering', 'tasks_completed': 72, 'errors_made': 5},
        'M205': {'department': 'Marketing', 'tasks_completed': 60, 'errors_made': 8},
        'M208': {'department': 'Marketing', 'tasks_completed': 67, 'errors_made': 4},
        'S312': {'department': 'Sales', 'tasks_completed': 94, 'errors_made': 12},
        'S316': {'department': 'Sales', 'tasks_completed': 88, 'errors_made': 9}
    }

    # Step 1: Analyze department-level metrics
    department_stats = analyze_department_metrics(employee_data)
    
    # Step 2: Compute efficiency scores
    _, net_productivity = calculate_efficiency(department_stats)
    
    # Step 3: Assess organizational risk based on error clustering
    high_error_depts = 0
    for dept, vals in department_stats.items():
        err_rate = vals['errors'] / (vals['output'] + 1)
        if err_rate > 0.1:
            high_error_depts += 1

    risk_factor = high_error_depts / len(department_stats)

    # Step 4: Evaluate final performance score
    final_score = evaluate_performance(net_productivity, risk_factor)
    
    # Output result
    print(f"Result: {final_score}")