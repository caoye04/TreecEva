from collections import defaultdict

# Simulate employee performance evaluation across departments
def analyze_department_stats(employees):
    stats = defaultdict(lambda: {'count': 0, 'total_output': 0})
    temp_buffer = [0] * len(employees)  # Unused preallocation - distractor

    high_performers = 0
    phantom_sum = 0  # Distractor accumulator

    for emp in employees:
        dept = emp['department']
        output = emp['output']
        stats[dept]['count'] += 1
        stats[dept]['total_output'] += output

        if output > 80:
            high_performers += 1

        # Meaningless computation - red herring
        for i in range(3):
            phantom_sum += (output % (i + 1)) if (i + 1) != 0 else 0

    avg_outputs = {}
    for dept, data in stats.items():
        avg_outputs[dept] = data['total_output'] / data['count']

    return avg_outputs, high_performers


def calculate_baseline(workload):
    # Irrelevant baseline logic with unused branching
    if workload > 1000:
        return workload * 0.05
    elif workload > 500:
        return workload * 0.07
    else:
        return workload * 0.1


def evaluate_productivity_shift(base, overtime):
    shift_factor = 1.0
    if overtime > 40:
        shift_factor = 1.2
    elif overtime > 20:
        shift_factor = 1.1

    adjusted = base * shift_factor

    # Fake correction mechanism - irrelevant
    correction = 0
    for _ in range(5):
        correction += (adjusted % 7) * 0.01
    adjusted -= correction  # Not actually used meaningfully

    return int(adjusted)


def evaluate_risk_level(complexity, fatigue):
    if complexity > 90:
        return 3
    elif complexity > 70 and fatigue > 50:
        return 2
    elif complexity > 50 or fatigue > 60:
        return 1
    else:
        return 0


def evaluate_performance(productivity, risk_factor):
    modifier = 1.0
    if risk_factor >= 3:
        modifier = 0.6
    elif risk_factor == 2:
        modifier = 0.8
    elif risk_factor == 1:
        modifier = 0.9

    score = productivity * modifier

    # Padding operation - misleading adjustment
    adjustment_log = []
    temp_val = score
    for i in range(4):
        temp_val = (temp_val + i) / (i + 2)
        adjustment_log.append(temp_val)

    return int(score)

# Main execution flow
if __name__ == '__main__':
    workforce = [
        {'name': 'Alice', 'department': 'Engineering', 'output': 95, 'overtime': 25},
        {'name': 'Bob', 'department': 'Engineering', 'output': 70, 'overtime': 15},
        {'name': 'Charlie', 'department': 'Design', 'output': 88, 'overtime': 35},
        {'name': 'Diana', 'department': 'Design', 'output': 65, 'overtime': 10},
        {'name': 'Eve', 'department': 'Marketing', 'output': 77, 'overtime': 5}
    ]

    # Step 1: Analyze department averages and count high performers
    department_averages, top_count = analyze_department_stats(workforce)

    # Step 2: Calculate total workload (sum of outputs)
    total_work = sum(emp['output'] for emp in workforce)

    # Step 3: Compute baseline threshold (unused in final logic)
    floor_limit = calculate_baseline(total_work)  # Distractor

    # Step 4: Aggregate adjusted productivity using overtime factor
    raw_productivity = sum(emp['output'] for emp in workforce)
    overtime_hours = sum(emp['overtime'] for emp in workforce)
    enhanced_productivity = evaluate_productivity_shift(raw_productivity, overtime_hours)

    # Step 5: Assess project risk based on arbitrary thresholds
    project_complexity = 75
    team_fatigue = 45
    risk_level = evaluate_risk_level(project_complexity, team_fatigue)

    # Step 6: Final performance score with risk adjustment
    final_score = evaluate_performance(enhanced_productivity, risk_level)

    # Output result
    print(f"Result: {final_score}")