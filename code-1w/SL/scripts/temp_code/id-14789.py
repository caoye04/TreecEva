def calculate_final_score(records):
    base_points = 0
    bonuses = []
    penalties = set()

    for entry in records:
        if entry['category'] == 'performance':
            base_points += entry['value']
        elif entry['category'] == 'bonus' and entry['value'] > 0:
            bonuses.append(entry['value'])
        elif entry['category'] == 'penalty':
            penalties.add(entry['value'])

    adjustment = len(bonuses) * 5 - sum(penalties)
    total_bonus = sum(b for b in bonuses if b % 2 == 1)

    final_score = base_points + adjustment + total_bonus

    temp_tracker = {'status': 'processed', 'total_steps': 3}
    return final_score

# Dataset representing evaluation metrics
data = [
    {'category': 'performance', 'value': 42},
    {'category': 'performance', 'value': 18},
    {'category': 'bonus', 'value': 7},
    {'category': 'bonus', 'value': 4},
    {'category': 'penalty', 'value': 3},
    {'category': 'penalty', 'value': 2}
]

result = calculate_final_score(data)
print(f"Result: {result}")