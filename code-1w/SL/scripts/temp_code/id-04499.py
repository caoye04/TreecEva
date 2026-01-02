from collections import defaultdict

# Simulate employee performance metrics across departments
def analyze_department_metrics(employees):
    stats = defaultdict(lambda: {'output': 0, 'errors': 0})
    noise_counter = 0  # Distractor: not used in final logic

    for emp in employees:
        dept = emp['department']
        stats[dept]['output'] += emp['tasks_completed']
        stats[dept]['errors'] += emp['mistakes']
        
        # Irrelevant computation (distractor)
        if emp['satisfaction'] > 7:
            noise_counter += 1

    return stats

# Evaluate individual productivity with weighted scoring
def compute_productivity(base, bonus_factor=1.0):
    raw = base * 1.2 + bonus_factor * 5
    adjusted = max(raw, 10)  # Threshold adjustment
    penalty = 0
    
    # Nested condition with early exit (semi-relevant)
    if base < 20:
        penalty = 3
        return int(adjusted - penalty)

    return int(adjusted)

# Core evaluation function combining arithmetic and logic
def evaluate_performance(p, r):
    p = p + (p % 7)  # Modular arithmetic twist
    r = abs(r - 5)   # Normalize risk
    score = 0

    # Multi-step reasoning with comparison and branching
    if p > 30:
        score += 15
    elif p > 20:
        score += 8
    else:
        score += 3

    if r == 0:
        score += 10
    elif r < 3:
        score += 5
    else:
        score -= 2

    # Bitwise check for efficiency flag (arbitrary heuristic)
    if (p & 1) == 0:  # If productivity is even
        score += 1

    return score

# Main execution flow
if __name__ == '__main__':
    # Dataset: employee records
    team = [
        {'name': 'Alice', 'department': 'Engineering', 'tasks_completed': 25, 'mistakes': 2, 'satisfaction': 8},
        {'name': 'Bob', 'department': 'Engineering', 'tasks_completed': 18, 'mistakes': 5, 'satisfaction': 6},
        {'name': 'Charlie', 'department': 'QA', 'tasks_completed': 22, 'mistakes': 1, 'satisfaction': 9}
    ]

    # Step 1: Aggregate department stats (used indirectly)
    aggregated = analyze_department_metrics(team)
    eng_output = aggregated['Engineering']['output']  # 43

    # Step 2: Compute individual productivity (core path)
    base_effort = eng_output // 2  # 21
    productivity = compute_productivity(base_effort, bonus_factor=0.8)

    # Step 3: Assess risk profile using set operations (distractor-heavy)
    risky_tasks = {1, 3, 4, 7, 9}
    completed_tasks = {2, 3, 5, 7, 8}
    overlap = risky_tasks & completed_tasks  # {3, 7} -> len=2
    risk_factor = len(overlap) * 2  # 4

    # Step 4: Final performance evaluation
    final_score = evaluate_performance(productivity, risk_factor)

    # Output result
    print(f"Result: {final_score}")