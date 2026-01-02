from collections import defaultdict
import math

# Simulate employee performance metrics across departments
def analyze_department_stats(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']
    
    # Irrelevant aggregation (distractor)
    total_depts = len(stats)
    avg_per_dept = sum(v['output'] for v in stats.values()) / total_depts if total_depts else 0
    
    return stats

# Calculate risk based on error rate and overtime
risk_calculator = lambda errors, tasks, overtime: (
    (errors / tasks) * 100 + (overtime * 0.5) if tasks > 0 else 100
)

# Secondary helper that computes efficiency but with red herring logic
def compute_efficiency(tasks, time_spent, threshold=8):
    base_rate = tasks / time_spent if time_spent > 0 else 0
    bonus = 1.2 if tasks > threshold else 1.0
    penalty = 0.8 if time_spent > 12 else 1.0  # Unusual overtime penalty
    adjusted = base_rate * bonus * penalty
    
    # Distractor: unused efficiency bands
    if adjusted < 0.5:
        band = 'low'
    elif adjusted < 1.0:
        band = 'medium'
    else:
        band = 'high'
    
    return adjusted  # Only this matters

# Core evaluation function combining multiple factors
def evaluate_performance(productivity, risk_factor):
    # Normalize productivity to a 0-100 scale
    normalized_prod = min(max(productivity * 10, 0), 100)
    
    # Apply non-linear risk penalty
    if risk_factor < 20:
        risk_modifier = 1.0
    elif risk_factor < 50:
        risk_modifier = 0.85
    else:
        risk_modifier = 0.6
    
    # Hidden adjustment based on modular pattern
    hidden_offset = (int(productivity) % 7) * 0.3
    
    # Final score calculation
    final_score = (normalized_prod * risk_modifier) + hidden_offset
    
    # Dead code branch (never executed due to logic above)
    if False and normalized_prod > 100:
        final_score = 100
    
    return final_score

# Employee dataset (real data used in computation)
employees = [
    {'name': 'Alice', 'department': 'Engineering', 'tasks_completed': 8, 'mistakes': 1, 'time_worked': 9},
    {'name': 'Bob', 'department': 'Engineering', 'tasks_completed': 6, 'mistakes': 2, 'time_worked': 8},
    {'name': 'Charlie', 'department': 'Design', 'tasks_completed': 5, 'mistakes': 0, 'time_worked': 7},
    {'name': 'Diana', 'department': 'Design', 'tasks_completed': 7, 'mistakes': 3, 'time_worked': 10}
]

# Step 1: Analyze department statistics (produces intermediate result)
department_data = analyze_department_stats(employees)

# Step 2: Compute aggregate productivity (used)
total_tasks = sum(emp['tasks_completed'] for emp in employees)
total_mistakes = sum(emp['mistakes'] for emp in employees)
total_time = sum(emp['time_worked'] for emp in employees)

# Step 3: Derive key metrics
productivity = total_tasks / len(employees)  # Average tasks per employee

# Step 4: Calculate risk factor using lambda (critical path)
risk_factor = risk_calculator(total_mistakes, total_tasks, overtime=total_time - 32)

# Step 5: Compute efficiency (semi-relevant, not directly used)
efficiency = compute_efficiency(total_tasks, total_time)

# Step 6: Evaluate final performance score (target assignment)
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")