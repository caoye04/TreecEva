from collections import defaultdict

# Simulate employee performance analytics with noise and distractors
def analyze_employee_data(employees):
    stats = defaultdict(int)
    anomalies = []
    temp_buffer = []

    base_threshold = 85
    adjustment_factor = 0.9
    phantom_counter = 0  # Irrelevant tracking

    for emp in employees:
        name = emp['name']
        hours_worked = emp['hours']
        tasks_completed = emp['tasks']
        error_rate = emp['errors'] / tasks_completed if tasks_completed > 0 else 0

        # Real computation branch
        productivity = (tasks_completed * 100) // max(hours_worked, 1)
        risk_factor = 0
        
        if error_rate > 0.2:
            risk_factor += 30
        elif error_rate > 0.1:
            risk_factor += 15

        if hours_worked < 30:
            risk_factor += 20
        elif hours_worked > 60:
            overtime_risk = hours_worked - 60
            risk_factor += overtime_risk // 5 * 5

        # Distractor: complex but unused anomaly detection
        if productivity < base_threshold and hours_worked > 50:
            phantom_counter += 1
            deviation = base_threshold - productivity
            score_rank = 'low' if deviation > 20 else 'moderate'
            temp_buffer.append({'emp': name, 'dev': deviation, 'rank': score_rank})

        # Critical state update: used later
        stats['total_productivity'] += productivity
        stats['risk_sum'] += risk_factor

    # Unused aggregation (distractor)
    avg_anomaly_risk = 0
    if temp_buffer:
        total_dev = sum(item['dev'] for item in temp_buffer)
        avg_anomaly_risk = total_dev / len(temp_buffer)

    # Key variables for final evaluation
    productivity = stats['total_productivity'] // len(employees)
    risk_factor = stats['risk_sum'] // len(employees)

    # Final scoring logic
    baseline = 100
    penalty = 0

    if risk_factor > 40:
        penalty += 25
    elif risk_factor > 25:
        penalty += 15
    else:
        penalty += 5

    # Apply adjustment based on group efficiency
    efficiency_ratio = productivity / 100.0
    adjusted_penalty = int(penalty * (1.1 - efficiency_ratio))

    # Final score calculation (this is the target)
    final_score = baseline - adjusted_penalty

    # Additional irrelevant transformation
    normalized = (final_score - 50) * 2  # Not used
    capped_score = min(max(final_score, 0), 100)  # Redundant safeguard

    return final_score


def evaluate_performance(p, r):
    # Wrapper that applies minor transformation
    modifier = 1
    if p > 90:
        modifier += 0.1
    elif p < 70:
        modifier -= 0.1
    return int((p - r * 0.3) * modifier)

# Dataset initialization (real input)
employee_pool = [
    {'name': 'Alice', 'hours': 45, 'tasks': 40, 'errors': 5},
    {'name': 'Bob', 'hours': 38, 'tasks': 32, 'errors': 8},
    {'name': 'Charlie', 'hours': 62, 'tasks': 50, 'errors': 3},
    {'name': 'Diana', 'hours': 48, 'tasks': 55, 'errors': 6},
    {'name': 'Eve', 'hours': 33, 'tasks': 20, 'errors': 4}
]

# Execute analysis
productivity_agg = 0
risk_total = 0
for e in employee_pool:
    p = (e['tasks'] * 100) // max(e['hours'], 1)
    r = 0
    err_rate = e['errors'] / e['tasks'] if e['tasks'] > 0 else 0
    if err_rate > 0.2:
        r += 30
    elif err_rate > 0.1:
        r += 15
    if e['hours'] < 30:
        r += 20
    elif e['hours'] > 60:
        r += (e['hours'] - 60) // 5 * 5
    productivity_agg += p
    risk_total += r

productivity = productivity_agg // len(employee_pool)
risk_factor = risk_total // len(employee_pool)

# Critical statement
final_score = evaluate_performance(productivity, risk_factor)

print(f"Target result: {final_score}")