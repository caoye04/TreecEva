def calculate_performance(bonus, stats):
    base = sum(stats['points'])
    multiplier = 2 if stats['accuracy'] > 0.8 else 1
    adjustment = -5 if 'penalty' in stats and stats['penalty'] else 0
    
    # Apply conditional expression for consistency bonus
    bonus_factor = 1.5 if all(score >= 70 for score in stats['points']) else 1.0
    
    raw_score = (base * multiplier + adjustment) * bonus_factor
    return int(raw_score + bonus)

# Simulation metrics from user task performance
task_data = {
    'points': [85, 90, 78, 92],
    'accuracy': 0.83,
    'penalty': False,
    'session': 'S04345'
}

# Irrelevant metadata (minimal distraction)
user_info = {'name': 'Alice', 'level': 'Advanced'}
config = {'version': '2.1', 'mode': 'eval'}

bonus_pool = 10
final_score = calculate_performance(bonus_pool, task_data)
print(f"Result: {final_score}")