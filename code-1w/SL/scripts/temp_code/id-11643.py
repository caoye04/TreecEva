def calculate_performance(flags, data_map):
    base = data_map['init']
    multiplier = 1
    
    if flags['speed'] and flags['accuracy']:
        multiplier += 0.5
    
    if not flags['errors']:
        multiplier += 0.3

    base = base * (1 + data_map['growth'])
    adjustment = data_map['penalty'] if flags['errors'] else 0
    return int(base * multiplier - adjustment)

# Irrelevant auxiliary variable (minor distraction)
temp_log = {'timestamp': '2023-09-15', 'user': 'dev'}

# Input data
bonus_flags = {
    'speed': True,
    'accuracy': True,
    'errors': False
}

metrics = {
    'init': 80,
    'growth': 0.25,
    'penalty': 10
}

final_score = calculate_performance(bonus_flags, metrics)
print(f"Result: {final_score}")