from collections import defaultdict
import itertools

# Simulate employee performance tracking across departments
def analyze_department_stats(employees):
    stats = defaultdict(lambda: {'hours': 0, 'tasks': 0})
    distractions = [0] * len(employees)  # unused array - distractor

    for emp in employees:
        name, hours, tasks, errors = emp
        stats[name]['hours'] += hours
        stats[name]['tasks'] += tasks
        efficiency = (tasks / (hours + 1)) if hours > 0 else 0  # not directly used later

    total_hours = sum(s['hours'] for s in stats.values())
    total_tasks = sum(s['tasks'] for s in stats.values())
    avg_completion = total_tasks / len(stats) if stats else 0

    return total_hours, total_tasks, avg_completion


def calculate_risk_factors(data):
    risk_values = []
    for val in data:
        temp_score = val ** 2 - val * 0.5
        if temp_score > 10:
            risk_values.append(temp_score * 0.1)
        else:
            risk_values.append(temp_score * 0.05)
    
    # Dead code path - never executed due to input range
    if len(risk_values) > 100:
        return sum(risk_values) / 100
        
    return sum(risk_values)

# Helper function with multiple concerns
def evaluate_productivity(hours_list, task_list):
    productivity = 0
    scaling_factor = 1.0
    
    for i, (h, t) in enumerate(itertools.zip_longest(hours_list, task_list, fillvalue=0)):
        if i % 3 == 0:
            scaling_factor = 1.1
        elif i % 3 == 1:
            scaling_factor = 0.9
        else:
            scaling_factor = 1.0
            
        contribution = (t + 1) / (h + 1) * scaling_factor
        productivity += contribution
        
        # Intermediate tracking not used in final result
        debug_msg = f'Step {i}: contrib={contribution:.3f}'

    return productivity

# Core evaluation logic
def evaluate_performance(p_index, r_index):
    base = p_index * 1.5
    penalty = r_index * 0.8
    bonus = 0
    
    # Conditional bonus logic (untriggered due to values)
    if p_index > 100 and r_index < 5:
        bonus = 25
    
    return int(base - penalty + bonus)

# Main execution block
if __name__ == "__main__":
    # Dataset: (name, weekly_hours, tasks_completed, error_count)
    team_a = [
        ('alice', 35, 42, 2),
        ('bob', 40, 38, 5),
        ('charlie', 30, 33, 1),
        ('diana', 45, 50, 3)
    ]
    
    _, total_tasks, avg_comp = analyze_department_stats(team_a)
    
    # Generate auxiliary metrics
    hours_data = [emp[1] for emp in team_a]
    tasks_data = [emp[2] for emp in team_a]
    error_rates = [e[3]/(e[2]+1) for e in team_a]  # computed but not used
    
    productivity = evaluate_productivity(hours_data, tasks_data)
    
    # Artificial signal noise
    smoothed_errors = [round(er * 100, 2) for er in error_rates]
    cumulative_shift = sum(smoothed_errors[i] - smoothed_errors[i-1] 
                          for i in range(1, len(smoothed_errors)))

    risk_factor = calculate_risk_factors([2, 3, 5, 7, 11])
    
    # Key statement
    final_score = evaluate_performance(productivity, risk_factor)
    
    print(f"Result: {final_score}")