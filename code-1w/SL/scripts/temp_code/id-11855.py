def calculate_final_score(records):
    base_points = 0
    bonuses = []
    for entry in records['items'][1:4]:
        if entry['performance'] > 75:
            base_points += entry['base']
            bonuses.append(entry['bonus'])
    total_bonus = sum(bonuses)
    final_score = base_points + (total_bonus * 0.1)
    return final_score

# Irrelevant auxiliary data
temp_log = {'status': 'inactive', 'retry_count': 3}
data = {
    'items': [
        {'base': 10, 'bonus': 20, 'performance': 60},
        {'base': 25, 'bonus': 50, 'performance': 80},
        {'base': 30, 'bonus': 70, 'performance': 90},
        {'base': 20, 'bonus': 40, 'performance': 85},
        {'base': 15, 'bonus': 30, 'performance': 70}
    ]
}

final_score = calculate_final_score(data)
print(f"Result: {final_score}")