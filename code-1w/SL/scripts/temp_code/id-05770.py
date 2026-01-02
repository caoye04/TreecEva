def calculate_final_score(data):
    base = 0
    bonus = 10
    penalty = 5
    temp_result = []

    for item in data:
        if item['type'] == 'A':
            base += item['value'] * 2
        elif item['type'] == 'B':
            base += item['value']
        else:
            base -= penalty

    adjustment_factor = 1.5 if base > 100 else 1.0
    
    # Irrelevant transformation (distractor)
    reversed_names = [name[::-1].upper() for name in ['alice', 'bob', 'charlie']]
    name_sum = sum([len(name) for name in reversed_names])  # Unused

    # Semi-relevant filtering
    valid_entries = [x for x in data if x['value'] > 10]
    extra_points = 0
    for entry in valid_entries:
        if entry['type'] == 'A':
            extra_points += 3

    # Another distraction: dead logic with no effect
    temp_offset = 0
    for i in range(3):
        for j in range(2):
            temp_offset += i - j  # This does not affect final result

    # Accumulate final score
    final_score = int((base * adjustment_factor) + extra_points)
    
    # Additional misleading computation
    outlier_check = [x for x in data if x['value'] < 0]
    if len(outlier_check) > 1:
        final_score -= 20  # Not triggered in this case

    return final_score

# Data setup
raw_data = [
    {'name': 'item1', 'type': 'A', 'value': 45},
    {'name': 'item2', 'type': 'B', 'value': 30},
    {'name': 'item3', 'type': 'A', 'value': 60},
    {'name': 'item4', 'type': 'C', 'value': 25},
    {'name': 'item5', 'type': 'B', 'value': 15}
]

# Preprocessing step with distractor variables
processed_data = []
sum_of_squares = 0
for d in raw_data:
    processed_item = {
        'type': d['type'],
        'value': d['value'],
        'tag': d['name'].replace('item', '').lower()
    }
    sum_of_squares += d['value'] ** 2  # Computed but unused later
    processed_data.append(processed_item)

# Key execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")