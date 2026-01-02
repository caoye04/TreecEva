def calculate_final_score(record):
    base_score = len(record['name']) * 2
    bonus = record['metrics']['alpha'] // 10
    penalty = 0
    
    if record['active']:
        penalty = sum([v for v in record['errors'].values()]) // 2
    
    temp_value = record['metrics']['beta']  # Irrelevant intermediate variable (distractor)
    unused_flag = False  # Distractor variable

    adjusted = base_score + bonus - penalty
    
    if adjusted > 50:
        adjusted *= 0.9
    
    return int(adjusted)

# Main data structure
data = {
    'name': 'Project Phoenix',
    'active': True,
    'metrics': {
        'alpha': 45,
        'beta': 123  # Used elsewhere but not directly in final_score
    },
    'errors': {
        'critical': 3,
        'warnings': 7,
        'info': 5
    }
}

final_score = calculate_final_score(data)
print(f"Result: {final_score}")