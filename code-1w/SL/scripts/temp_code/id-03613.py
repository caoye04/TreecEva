def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    efficiency_ratio = 0.0

    for day in logs:
        daily_total = sum(day['work_blocks'])
        total_hours += daily_total
        if daily_total < 4:
            idle_periods += 1

    if total_hours > 0:
        efficiency_ratio = (total_hours - idle_periods * 2) / total_hours

    return total_hours, efficiency_ratio


def calculate_rating(entries, multiplier):
    base_score = 0
    bonus_pool = 100
    deductions = 0

    stats = {}
    for i, entry in enumerate(entries):
        task_complexity = len(entry['name']) % 5 + 1
        completion_rate = entry['completed'] / entry['attempts'] if entry['attempts'] > 0 else 0
        
        # Relevant calculation
        base_score += task_complexity * completion_rate
        
        # Distractor: tracking unused metrics
        stats[f'task_{i}'] = {
            'stdev': (completion_rate * task_complexity) ** 0.5,
            'weight': task_complexity * 1.5
        }
        
        if completion_rate == 1.0:
            bonus_pool -= 5  # Unused bonus mechanism

    # Irrelevant data transformation
    stat_values = [v['weight'] for k, v in stats.items() if 'task' in k]
    average_weight = sum(stat_values) / len(stat_values) if stat_values else 0

    # Core logic with conditional expression
    adjustment = 1.2 if average_weight > 4 else 0.9

    final_score = int((base_score * adjustment - multiplier * 2) + 0.5)
    
    # Dead code path (never executed due to logic)
    if bonus_pool < 0:
        final_score += abs(bonus_pool)

    return final_score

# Simulated dataset
activity_log = [
    {'date': '2023-01-01', 'work_blocks': [2, 1.5, 3], 'breaks': 4},
    {'date': '2023-01-02', 'work_blocks': [1, 2, 1], 'breaks': 6},
    {'date': '2023-01-03', 'work_blocks': [3, 3.5], 'breaks': 3}
]

contributions = [
    {'name': 'frontend', 'completed': 8, 'attempts': 10},
    {'name': 'backend', 'completed': 9, 'attempts': 9},
    {'name': 'database', 'completed': 4, 'attempts': 6},
    {'name': 'testing', 'completed': 5, 'attempts': 5}
]

# Extract from auxiliary analysis (not directly used but looks relevant)
hours_worked, efficiency = analyze_productivity(activity_log)
penalty_factor = 3 if efficiency < 0.7 else 1

# Key computation
final_score = calculate_rating(contributions, penalty_factor)

Result: {final_score}