from itertools import combinations

def analyze_workload(employees, tasks):
    # Simulate workload distribution analysis with some irrelevant metrics
    n = len(employees)
    total_pairs = list(combinations(employees, 2))
    interaction_cost = 0
    
    for pair in total_pairs:
        x, y = pair
        interaction_cost += (x['seniority'] + y['seniority']) % 3
    
    # Real computation begins: assign tasks and compute completion likelihood
    assignment_scores = []
    for emp in employees:
        base_skill = emp['skill']
        stress_factor = emp['workload'] / (base_skill + 1)
        adjusted_skill = base_skill * (1 - min(stress_factor, 0.5))
        
        task_performance = 0
        for task in tasks:
            if task['complexity'] <= adjusted_skill:
                task_performance += 1.0
            else:
                task_performance += 0.4  # partial progress
        
        # Irrelevant metric: peer_review_score (not used later)
        peer_review_score = (emp['seniority'] * 2 + interaction_cost) // len(tasks)
        
        assignment_scores.append(task_performance)
    
    avg_completion = sum(assignment_scores) / len(assignment_scores)
    max_possible = len(tasks)
    efficiency_score = (avg_completion / max_possible) * 100
    
    # Distractor: unused normalization
    normalized_efficiency = round(efficiency_score / 10) * 10
    
    return efficiency_score

# Define realistic workforce data
employees = [
    {'name': 'alice', 'skill': 7, 'seniority': 5, 'workload': 8},
    {'name': 'bob', 'skill': 5, 'seniority': 3, 'workload': 6},
    {'name': 'charlie', 'skill': 9, 'seniority': 7, 'workload': 10},
    {'name': 'diana', 'skill': 6, 'seniority': 4, 'workload': 5}
]

tasks = [
    {'id': 1, 'complexity': 4},
    {'id': 2, 'complexity': 6},
    {'id': 3, 'complexity': 8},
    {'id': 4, 'complexity': 5},
    {'id': 5, 'complexity': 7}
]

efficiency_score = analyze_workload(employees, tasks)

# Print result as required
print(f"Result: {efficiency_score}")