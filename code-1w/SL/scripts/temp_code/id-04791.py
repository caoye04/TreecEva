def evaluate_performance(records, limit):
    count = 0
    total = 0.0
    temp_sum = 0  # distractor variable
    offset = len(records) // 2  # misleading computation

    for i in range(len(records)):
        if i < offset:
            temp_sum += i * 2  # irrelevant accumulation

        entry = records[i]
        if 'status' in entry and entry['status'] == 'active':
            value = entry.get('value', 0)
            flagged = entry.get('flagged', False)

            if not flagged and value > limit:
                total += value
                count += 1

    if count == 0:
        return 0.0

    average = total / count

    # Simulate bonus logic based on string pattern
    tag_summary = ''.join([r.get('tag', '') for r in records if 'tag' in r])
    bonus_multiplier = 1.5 if 'high_priority' in tag_summary else 1.0

    # Distractor: slicing with no effect
    unused_slice = tag_summary[::2]
    debug_check = len(unused_slice) % 7  # unused but computed

    raw_score = average * bonus_multiplier

    # Additional filtering: only consider entries where id is even
    filtered_ids = [r['id'] for r in records if r.get('id', 0) % 2 == 0]
    id_correction = len(filtered_ids) * 0.1  # minor adjustment factor

    final_score = raw_score + id_correction
    return final_score


# Main data setup
user_data = [
    {'id': 1, 'value': 120, 'status': 'active', 'flagged': False, 'tag': 'normal'},
    {'id': 2, 'value': 150, 'status': 'active', 'flagged': False, 'tag': 'high_priority'},
    {'id': 3, 'value': 90, 'status': 'inactive', 'flagged': True, 'tag': 'low_risk'},
    {'id': 4, 'value': 200, 'status': 'active', 'flagged': False, 'tag': 'high_priority'},
    {'id': 5, 'value': 80, 'status': 'active', 'flagged': True, 'tag': 'normal'},
    {'id': 6, 'value': 180, 'status': 'active', 'flagged': False, 'tag': 'medium_risk'}
]

# Parameters
threshold = 100

# Irrelevant pre-processing
shadow_copy = user_data[::-1]  # reversed copy not used in logic
audit_log = [entry['id'] for entry in shadow_copy if 'status' in entry]  # distractor list

# Key execution point
final_score = evaluate_performance(user_data, threshold)

# Output result
print(f"Result: {final_score}")