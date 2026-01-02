from itertools import combinations

# Simulate employee task completion with efficiency and error tracking
def analyze_tasks(completed_tasks, error_log):
    base_efficiency = len(completed_tasks) * 1.5
    error_penalty = sum([len(msg) // 10 for msg in error_log]) * 0.3
    adjusted_efficiency = base_efficiency - error_penalty
    return max(adjusted_efficiency, 0)

# Determine collaboration synergy using set intersections
def compute_synergy(teams):
    total_synergy = 0
    team_sets = [set(members) for members in teams]
    for i in range(len(team_sets)):
        for j in range(i + 1, len(team_sets)):
            overlap = len(team_sets[i] & team_sets[j])
            total_synergy += overlap * 0.7
    return total_synergy

# Assess innovation index based on project diversity
def assess_innovation(projects):
    tech_stack = set()
    for proj in projects:
        tech_stack.update(proj.split('-'))
    diversity_bonus = len(tech_stack) * 0.5
    # Distractor: unused innovation metric
    redundant_calc = sum([len(p) for p in projects]) / (len(projects) + 1)
    return diversity_bonus

# Main evaluation function combining multiple factors
def evaluate_performance(productivity, risk_factor):
    # Intermediate irrelevant computation (distractor)
    shadow_metric = productivity ** 0.5 + risk_factor * 0.1
    adjustment_cycle = 0
    temp_buffer = []
    
    for i in range(3):
        adjustment_cycle += (productivity + i) % 2
        temp_buffer.append(shadow_metric + adjustment_cycle)
    
    # Real logic path
    base_performance = productivity * 1.2
    risk_adjusted = base_performance - (risk_factor * 0.8)
    if risk_adjusted < 0:
        risk_adjusted = 0
    
    # Additional distractor: dead code branch
    if False:
        fallback_mode = True
        risk_adjusted = 10
    
    # Final scoring with fake dependency
    scaling_factor = 1.0
    for factor in [1.1, 0.9, 1.0]:
        scaling_factor *= factor  # Net effect ~1.0
    
    final_score = int(risk_adjusted * scaling_factor)
    return final_score

# Input data
completed_tasks = ['T1', 'T2', 'T3', 'T4']
error_log = ['ERR_BUFFER_OVERFLOW', 'ERR_TIMEOUT', 'ERR_NULL_REF']
project_teams = [['Alice', 'Bob'], ['Bob', 'Charlie'], ['Diana', 'Alice']]
innovation_projects = ['AI-ML', 'ML-API', 'WEB-FRONTEND', 'API-SECURITY']

# Irrelevant preprocessing (distractor)
all_pairs = list(combinations(['A', 'B', 'C', 'D'], 2))
dummy_sum = sum([len(pair[0]) + len(pair[1]) for pair in all_pairs])

# Key execution steps
efficiency = analyze_tasks(completed_tasks, error_log)
synergy = compute_synergy(project_teams)
diversity_score = assess_innovation(innovation_projects)

productivity = int(efficiency + synergy)
risk_factor = 5  # Assessed from external audit

# Critical statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Result: {final_score}")