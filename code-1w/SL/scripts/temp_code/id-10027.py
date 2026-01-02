from collections import defaultdict
from itertools import combinations

# Simulate employee performance metrics across departments
def analyze_department_metrics(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    error_threshold = 5
    bonus_eligibility = []

    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']

        # Irrelevant logic for distraction (dead path)
        if emp['seniority'] > 10 and emp['mistakes'] == 0:
            hidden_bonus = True  # Unused variable

        if emp['tasks_completed'] > 20:
            bonus_eligibility.append(emp['name'])

    return stats, bonus_eligibility

# Evaluate individual productivity with risk adjustment
def calculate_productivity(base_output, experience_years):
    base_multiplier = 1.0
    if experience_years < 2:
        base_multiplier = 0.6
    elif 2 <= experience_years <= 5:
        base_multiplier = 0.8
    else:
        base_multiplier = 1.1

    adjusted = base_output * base_multiplier

    # Dummy calculation - doesn't affect final result
    hypothetical_max = base_output * 1.5
    efficiency_ratio = adjusted / hypothetical_max if hypothetical_max > 0 else 0

    return adjusted

# Assess risk based on error rate and consistency
def assess_risk(error_count, attendance_rate):
    if attendance_rate < 0.8:
        base_risk = 3
    elif error_count > 10:
        base_risk = 2
    else:
        base_risk = 1

    # Extra computation for confusion
    risk_profile = 'high' if base_risk >= 3 else 'medium' if base_risk == 2 else 'low'
    risk_profile_code = ord(risk_profile[0])  # Distractor

    return base_risk

# Main evaluation function combining multiple factors
def evaluate_performance(output, risk):
    base_score = output * 10
    penalty = risk * 15
    final_score = base_score - penalty

    # Additional unused logic to increase interference
    if final_score > 100:
        level = 'excellent'
    elif final_score > 70:
        level = 'good'
    elif final_score > 50:
        level = 'average'
    else:
        level = 'poor'

    # More irrelevant processing
    performance_label = f"Performance: {level.upper()}"
    normalized = round(final_score / 150 * 100, 2)  # Not used

    return final_score

# Dataset initialization
employee_data = [
    {'name': 'Alice', 'department': 'Engineering', 'tasks_completed': 25, 'mistakes': 3, 'seniority': 6, 'experience_years': 7, 'attendance_rate': 0.95},
    {'name': 'Bob', 'department': 'Engineering', 'tasks_completed': 18, 'mistakes': 12, 'seniority': 4, 'experience_years': 3, 'attendance_rate': 0.75},
    {'name': 'Charlie', 'department': 'QA', 'tasks_completed': 22, 'mistakes': 1, 'seniority': 5, 'experience_years': 6, 'attendance_rate': 0.98}
]

# Extract key metrics
all_outputs = sum(emp['tasks_completed'] for emp in employee_data)
max_experience = max(emp['experience_years'] for emp in employee_data)
total_errors = sum(emp['mistakes'] for emp in employee_data)

# Calculate core values with intermediate distractions
productivity = calculate_productivity(all_outputs, max_experience)
risk_factor = assess_risk(total_errors, 0.90)

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Irrelevant combinatorial analysis (distractor)
departments = list(set(emp['department'] for emp in employee_data))
pairings = list(combinations(departments, min(2, len(departments))))
complexity_index = len(pairings) * 10

# Print final answer as required
print(f"Result: {final_score}")