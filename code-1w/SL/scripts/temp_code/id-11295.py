from collections import defaultdict

# Simulate employee performance tracking with distraction metrics
def analyze_employee_data(records):
    stats = defaultdict(int)
    distractions = []
    temp_buffer = []

    for record in records:
        emp_id, hours, errors, focus = record[:4]
        score = hours * 10 - errors * 5
        if focus < 0.7:
            distractions.append(emp_id)
            score -= 20  # penalty for low focus

        stats[emp_id] += score
        temp_buffer.append(score * 0.1)  # irrelevant accumulation

    # Irrelevant secondary pass: normalize distractions (not used later)
    normalized_distractions = [d % 7 for d in distractions if d > 0]
    overflow = sum(normalized_distractions) * 0.01

    # Relevant data aggregation
    productivity = 0
    risk_factor = 0
    high_risk_count = 0

    for i, record in enumerate(records):
        _, hours, errors, focus, team = record
        efficiency = (hours - errors) / (hours + 1)
        risk_rating = 1 if errors > 5 or focus < 0.5 else 0
        risk_factor += risk_rating

        # Conditional logic with inline expression
        contribution = efficiency * 100 if team == 'A' else efficiency * 80
        productivity += contribution

        if errors > 3:
            high_risk_count += 1

    # Dead code path - never executed due to prior logic
    if len(temp_buffer) > 1000:
        reset_flag = True
        productivity = 0

    # Core evaluation function defined inside
    def evaluate_performance(prod, risk):
        base = prod * 0.75
        adjustment = 0
        if risk > 0:
            adjustment = -risk * 15
        elif prod > 300:
            adjustment = 50
        return int(base + adjustment)  # final integer score

    final_score = evaluate_performance(productivity, risk_factor)
    
    # Unrelated checksum calculation (distraction)
    checksum = 0
    for d in distractions:
        checksum ^= d
    checksum = checksum % 97

    # Output the required result
    print(f"Result: {final_score}")
    return final_score

# Input data: (employee_id, hours_worked, errors_made, focus_level, team)
data = [
    (101, 40, 2, 0.85, 'A'),
    (102, 35, 6, 0.65, 'B'),
    (103, 45, 1, 0.90, 'A'),
    (104, 30, 8, 0.45, 'A'),
    (105, 38, 3, 0.75, 'B')
]

result = analyze_employee_data(data)