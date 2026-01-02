def calculate_final_score(data):
    base_score = data['exam'] * 0.6
    bonus = 0
    if data['attendance'] >= 90:
        bonus += 5
    if data['projects'] > 2:
        bonus += 3
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_warning = "Low project count" if data['projects'] < 2 else "OK"
    
    adjusted_score = base_score + bonus
    
    # Apply performance multiplier based on participation
    multiplier = data['participation_map'].get('multiplier', 1.0)
    final = adjusted_score * multiplier
    
    return int(final)

# Main data input
current_student = {
    'exam': 88,
    'attendance': 95,
    'projects': 3,
    'participation_map': {
        'level': 'high',
        'multiplier': 1.1
    }
}

final_score = calculate_final_score(current_student)
print(f"Result: {final_score}")