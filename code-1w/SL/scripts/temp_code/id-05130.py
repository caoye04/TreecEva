def calculate_final_score(records):
    total_points = 0
    penalties = set()
    
    for i, record in enumerate(records):
        action = record['action']
        duration = record['duration']
        category = record['category']
        
        if action == 'submit' and duration < 30:
            total_points += 10
        elif action == 'review' and category in ['critical', 'urgent']:
            total_points += 5
        
        if duration > 60 and category == 'routine':
            penalties.add(i)
    
    adjustment = 0
    for idx, record in enumerate(records):
        if idx in penalties and record['action'] == 'submit':
            adjustment -= 3
    
    completeness_check = [r['action'] for r in records]
    unique_actions = len(set(completeness_check))
    
    bonus = 7 if unique_actions == 3 else 0
    
    final_score = total_points + adjustment + bonus
    return final_score

# Simulated input data
data = [
    {'action': 'submit', 'duration': 25, 'category': 'critical'},
    {'action': 'review', 'duration': 45, 'category': 'urgent'},
    {'action': 'submit', 'duration': 70, 'category': 'routine'},
    {'action': 'log', 'duration': 10, 'category': 'info'}
]

result = calculate_final_score(data)
print(f"Result: {result}")