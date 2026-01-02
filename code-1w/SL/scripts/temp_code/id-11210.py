from collections import defaultdict

# Simulate employee performance analysis with distraction metrics
def analyze_employee_data(employees):
    stats = defaultdict(int)
    distractions = [0.1, 0.5, None, 0.3]
    total_focus = 0.0

    for emp in employees:
        name = emp['name']
        hours_worked = emp['hours']
        tasks_completed = emp['tasks']
        error_rate = emp['errors'] / tasks_completed if tasks_completed > 0 else 0

        # Real metric: productivity score
        base_productivity = hours_worked * 2.5
        adjusted_productivity = base_productivity * (1 - error_rate)

        # Distractor computation: irrelevant focus score with dead logic
        focus_score = sum([d for d in distractions if d]) * 0.2
        if focus_score > 1:
            total_focus += focus_score  # Dead code path (never reached)

        stats[name] = adjusted_productivity

    return dict(stats)

# Auxiliary function with red herring parameters
def calculate_risk(market_volatility, unused_threshold=999):
    # This function includes complex-looking but ultimately unused logic
    trend = [i**2 for i in range(5) if i % 2 == 0]
    adjustment = 0
    for t in trend:
        adjustment += t // 2
    # Actual simple result despite complex buildup
    return market_volatility * 0.7  # Simple linear mapping, others are distractions

# Core evaluation logic
def evaluate_performance(productivity, risk_factor):
    base = productivity * 0.8
    penalty = risk_factor * 15
    bonus = 10 if productivity > 40 else 0
    # Multiple steps with intermediate variables (some redundant)
    intermediate = base - penalty + bonus
    normalized = round(intermediate, 2)
    final_score = int(normalized)  # Final answer derived here
    return final_score

# Main execution block
if __name__ == '__main__':
    team_data = [
        {'name': 'Alice', 'hours': 35, 'tasks': 20, 'errors': 2},
        {'name': 'Bob', 'hours': 40, 'tasks': 25, 'errors': 4},
        {'name': 'Charlie', 'hours': 30, 'tasks': 15, 'errors': 1}
    ]

    # Step 1: Analyze productivity (only Alice's data used later)
    productivity_map = analyze_employee_data(team_data)
    alice_productivity = productivity_map['Alice']

    # Step 2: Compute risk factor (distractions present)
    market_turbulence = 8
    risk_factor = calculate_risk(market_turbulence)

    # Step 3: Evaluate final score — KEY STATEMENT
    final_score = evaluate_performance(alice_productivity, risk_factor)

    # Irrelevant post-processing (dead computations)
    summary_report = {k: f'{v:.1f}' for k, v in productivity_map.items()}
    scaling_factor = len(summary_report) * 1.5  # Unused

    print(f"Result: {final_score}")