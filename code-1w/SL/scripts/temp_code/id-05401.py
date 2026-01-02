def calculate_rating(entries, penalty):
    base = sum([e['points'] for e in entries if e['active']])
    multiplier = len([e for e in entries if e['priority'] > 1])
    adjustment = 0
    for entry in entries:
        if entry['category'] == 'critical' and entry['completed']:
            adjustment += 5
        elif entry['category'] == 'minor':
            adjustment -= 2
    
    # Distractor block: irrelevant computation on metadata
    temp_sum = 0
    for entry in entries:
        for k, v in entry.items():
            if isinstance(v, int) and k != 'points':
                temp_sum += v * 0.1
    normalized_temp = round(temp_sum, 2)

    # Another distractor: unused conditional expression
    status_flag = 'high' if base > 30 else 'low'
    auxiliary_value = 10 if status_flag == 'high' else 5

    raw_score = base * (multiplier + 1) + adjustment
    final_rating = raw_score - penalty * 2
    return int(final_rating)

# Main data structure with mixed relevance fields
contributions = [
    {'points': 10, 'active': True, 'priority': 2, 'category': 'critical', 'completed': True},
    {'points': 8, 'active': True, 'priority': 3, 'category': 'critical', 'completed': False},
    {'points': 5, 'active': False, 'priority': 1, 'category': 'minor', 'completed': True},
    {'points': 12, 'active': True, 'priority': 2, 'category': 'standard', 'completed': True},
    {'points': 7, 'active': True, 'priority': 1, 'category': 'minor', 'completed': True}
]

# Irrelevant helper that's defined but not used
def compute_variance(data_list):
    mean = sum(data_list) / len(data_list)
    return sum((x - mean) ** 2 for x in data_list) / len(data_list)

penalty_factor = 4
intermediate_total = sum(item['points'] for item in contributions)  # Distractor variable
filter_count = len([x for x in contributions if x['active']])  # Semi-relevant but unused later

final_score = calculate_rating(contributions, penalty_factor)
print(f"Result: {final_score}")