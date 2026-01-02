def calculate_final_score(data):
    base_points = 0
    bonuses = {}
    
    for category, values in data.items():
        if category == 'math':
            base_points += sum(values) * 1.5
            bonuses['math_bonus'] = len(values) >= 3
        elif category == 'logic':
            base_points += sum(v ** 0.5 for v in values)  # sqrt of each
            bonuses['logic_streak'] = max(values) > 8
    
    adjustment = 0
    if bonuses.get('math_bonus') and bonuses.get('logic_streak'):
        adjustment = 10
    
    return int(base_points + adjustment)

# Irrelevant auxiliary variable (minor distraction)
user_preferences = {'theme': 'dark', 'notifications': True}

results = {
    'math': [6, 7, 8],
    'logic': [4, 9, 7]
}

final_score = calculate_final_score(results)
print(f"Target result: {final_score}")