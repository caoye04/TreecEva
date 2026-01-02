def calculate_final_score(data):
    base_score = data['attempts'] * 5
    bonus = 10 if data['level'] == 'advanced' else 5
    
    # Apply case conversion to ensure consistent processing
    status = data['status'].lower()
    
    if status == 'completed':
        completion_multiplier = 1.5
    elif status == 'in_progress':
        completion_multiplier = 0.7
    else:
        completion_multiplier = 0.3
    
    raw_score = (base_score + bonus) * completion_multiplier
    
    # Use dictionary lookup for penalty adjustment
    penalties = {'minor': 2, 'moderate': 5, 'severe': 10}
    adjusted_score = raw_score - penalties.get(data['penalty'], 0)
    
    return int(adjusted_score)

# Simulate user data input
test_user = {
    'attempts': 6,
    'level': 'advanced',
    'status': 'Completed',
    'penalty': 'moderate'
}

final_score = calculate_final_score(test_user)
print(f"Result: {final_score}")