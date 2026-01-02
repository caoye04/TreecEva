def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    efficiency_ratio = 0.0

    for day, log in enumerate(logs):
        daily_total = sum([h for h in log if h > 0])
        daily_idle = len([h for h in log if h == 0])
        total_hours += daily_total
        idle_periods += daily_idle

        if daily_total > 8:
            overtime = daily_total - 8
            total_hours -= overtime * 0.25  # Adjust for fatigue

    if total_hours > 0:
        efficiency_ratio = (total_hours - idle_periods) / total_hours
    return total_hours, efficiency_ratio


def calculate_rating(contribs, penalties):
    base_score = 0
    adjustment = 0.0
    tier_bonus = [0, 5, 10, 15]

    severity_map = {1: 1, 2: 2, 3: 4, 4: 8}
    penalty_deduction = sum(severity_map.get(p, 0) for p in penalties)

    for i, count in enumerate(contribs):
        contribution_value = (i + 1) * count
        base_score += contribution_value

        # Irrelevant complexity: tracking phase multipliers
        phase_multiplier = 1.0
        if i % 2 == 0:
            phase_multiplier = 1.1
        elif i % 3 == 0:
            phase_multiplier = 0.9

    # Dummy loop with no effect (distractor)
    temp_vals = []
    for x in range(3):
        temp_vals.append(x ** 3 - 2 * x)

    final_adjustment = base_score - penalty_deduction
    return int(final_adjustment)

# Simulated weekly work logs (hours worked per shift)
work_logs = [
    [8, 7, 0, 9, 6],
    [8, 8, 0, 0, 7],
    [9, 6, 8, 0, 5],
    [7, 7, 7, 8, 0],
    [6, 0, 8, 9, 7]
]

# Project contributions: [minor, medium, major, critical]
contributions = [12, 8, 5, 3]

# Penalty incidents: levels 1-4
penalties = [2, 3, 1, 2, 4]

# Unused but plausible computation (distractor)
data_points = list(zip(work_logs, [len(log) for log in work_logs]))
expanded = [item for sublist in work_logs for item in sublist]
zero_count = sum(1 for x in expanded if x == 0)

# Key analysis step (moderately relevant)
total_hrs, efficiency = analyze_productivity(work_logs)

# Core calculation with interference from above
final_score = calculate_rating(contributions, penalties)

print(f"Result: {final_score}")