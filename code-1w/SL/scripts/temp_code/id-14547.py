def calculate_final_score(results, multiplier):
    base_scores = [res['value'] for res in results if res['active']]
    penalties = sum([res['penalty'] for res in results])
    adjusted_scores = [score * multiplier for score in base_scores]
    total = sum(adjusted_scores) - penalties
    return int(total)

# Irrelevant auxiliary data (minor distraction)
data_log = [{'timestamp': '12:01', 'event': 'start'}, {'timestamp': '12:05', 'event': 'load'}]
config_params = {'version': '2.1', 'debug': False}

# Main computation input
results = [
    {'value': 85, 'penalty': 5, 'active': True},
    {'value': 90, 'penalty': 3, 'active': True},
    {'value': 78, 'penalty': 0, 'active': False},
    {'value': 92, 'penalty': 7, 'active': True}
]

bonus_multiplier = 1.2
final_score = calculate_final_score(results, bonus_multiplier)
print(f"Result: {final_score}")