def analyze_efficiency(metrics):
    adjusted = 0
    base_factor = metrics.get('output', 0) / (metrics.get('time_spent', 1) + 0.1)
    stress_level = metrics.get('overtime_hours', 0) * 1.5
    bonus_eligibility = metrics.get('innovation_score', 0) > 7
    
    if base_factor > 5:
        adjusted += 10
        if bonus_eligibility:
            adjusted += 5
    elif base_factor > 3:
        adjusted += 6
    else:
        adjusted -= 2
        
    distraction_value = stress_level * 0.3  # Not used in final logic
    return adjusted

productivity_data = {
    'output': 48,
    'time_spent': 8,
    'overtime_hours': 3,
    'innovation_score': 8
}

risk_profile = {
    'error_rate': 0.02,
    'compliance_score': 95,
    'audit_trail': True
}

# Simulate team performance across shifts
team_shifts = ['morning', 'evening', 'night']
summary_stats = {}
for shift in team_shifts:
    efficiency = analyze_efficiency(productivity_data)
    summary_stats[shift] = efficiency

# Set-based analysis for operational coverage
tasks_completed = {1, 2, 3, 5, 8, 13}
tasks_required = {1, 2, 3, 4, 5, 6}
pending_tasks = tasks_required - tasks_completed
escalated_tasks = {8, 13} & tasks_completed

coverage_ratio = len(tasks_completed & tasks_required) / len(tasks_required)
penalty = len(pending_tasks) * 3

# Redundant computation - misleading path
project_health = 100
if len(escalated_tasks) > 0:
    project_health -= 10

# Simulated risk adjustment
risk_factor = 0
if risk_profile['error_rate'] < 0.03:
    risk_factor += 5
if risk_profile['compliance_score'] >= 90:
    risk_factor += 10

# Core evaluation logic
productivity_set = set()
for k, v in productivity_data.items():
    if isinstance(v, (int, float)) and v > 5:
        productivity_set.add(k)

risk_set = set()
for k, v in risk_profile.items():
    if isinstance(v, (int, float)) and v >= 90:
        risk_set.add(k)
    elif k == 'audit_trail' and v:
        risk_set.add(k)

# Key function with logical combination
def evaluate_performance(prod_set, rsk_set):
    base = len(prod_set) * 7
    risk_bonus = len(rsk_set) * 3
    overlap = len(prod_set & rsk_set)
    deduction = len(prod_set - rsk_set) * 2
    temp_adjust = overlap * 4  # Distractor: only used once
    result = base + risk_bonus - deduction
    if overlap >= 2:
        result += 5
    return result

# Unused diagnostic block (dead code path)
if False:
    debug_info = {}
    for key in productivity_data:
        debug_info[key] = hex(id(key))

# Critical statement
final_score = evaluate_performance(productivity_set, risk_set)

print(f"Result: {final_score}")