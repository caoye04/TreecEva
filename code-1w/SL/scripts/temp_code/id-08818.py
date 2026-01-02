def calculate_total(data):
    base = sum(data['values'])
    bonus = data['multiplier'] * len(data['flags'])
    return base + bonus if base > 0 else -bonus

# Irrelevant auxiliary data
user_preferences = {'theme': 'dark', 'language': 'en', 'notifications': True}

# Main computation data
raw_input = [3, 7, -2, 4]
processed_data = {
    'values': [x for x in raw_input if x > 0],
    'multiplier': 5,
    'flags': [True, False, True],
    'timestamp': 1712345678
}

# Additional logic using lambda
validate = lambda x: len(x['values']) >= 3
if validate(processed_data):
    processed_data['multiplier'] += 1

final_score = calculate_total(processed_data)
print(f"Result: {final_score}")