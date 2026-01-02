from collections import defaultdict
import math

# Simulate employee performance metrics across departments
def analyze_department_stats(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']
    
    # Compute efficiency scores (distraction: not directly used later)
    efficiency = {}
    for dept, data in stats.items():
        raw_efficiency = data['output'] / (data['errors'] + 1)
        efficiency[dept] = round(raw_efficiency, 2)
    
    return stats

# Auxiliary function to calculate risk based on error distribution
def calculate_risk_profile(employee_list):
    total_mistakes = sum(e['mistakes'] for e in employee_list)
    high_risk_count = len([e for e in employee_list if e['mistakes'] > 3])
    avg_experience = sum(e['experience'] for e in employee_list) / len(employee_list)
    
    # Irrelevant transformation (distractor)
    penalty_factor = 1.0
    if high_risk_count > 2:
        penalty_factor = 1.5
    elif avg_experience < 2:
        penalty_factor = 1.2
    
    # Actual risk score computation
    base_risk = total_mistakes * penalty_factor / len(employee_list)
    return round(base_risk, 3)

# Core evaluation logic
def evaluate_performance(output_sum, risk):
    # Normalize productivity with logarithmic scaling
    normalized_output = math.log(output_sum + 1) if output_sum > 0 else 0
    
    # Apply risk adjustment
    adjusted_score = normalized_output * (5.0 - min(risk, 4.5))
    
    # Red herring: unused compensation logic
    bonus_eligibility = adjusted_score > 3.5
    review_cycle = "quarterly" if bonus_eligibility else "monthly"
    
    return int(round(adjusted_score * 10))  # Scale up for final metric

# Main execution block
if __name__ == "__main__":
    # Dataset: engineering team performance
    team_employees = [
        {'name': 'Alice', 'department': 'backend', 'tasks_completed': 23, 'mistakes': 2, 'experience': 5},
        {'name': 'Bob', 'department': 'backend', 'tasks_completed': 19, 'mistakes': 4, 'experience': 4},
        {'name': 'Charlie', 'department': 'frontend', 'tasks_completed': 15, 'mistakes': 1, 'experience': 3},
        {'name': 'Diana', 'department': 'frontend', 'tasks_completed': 28, 'mistakes': 3, 'experience': 6},
        {'name': 'Evan', 'department': 'devops', 'tasks_completed': 12, 'mistakes': 5, 'experience': 7}
    ]

    # Step 1: Analyze department-level stats (produces distractor data)
    department_data = analyze_department_stats(team_employees)

    # Step 2: Calculate cross-team risk factor
    risk_factor = calculate_risk_profile(team_employees)
    
    # Step 3: Aggregate total output (key input for answer)
    total_tasks = sum(emp['tasks_completed'] for emp in team_employees)
    
    # Step 4: Evaluate final performance score (critical point)
    final_score = evaluate_performance(total_tasks, risk_factor)
    
    # Step 5: Print result (required format)
    print(f"Target result: {final_score}")
    