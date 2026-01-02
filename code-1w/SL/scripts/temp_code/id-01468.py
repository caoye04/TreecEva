def process_entry(entry):
    # Irrelevant transformation
    temp_tag = entry['tag'].upper().replace('_', '')
    weight = len(temp_tag) if temp_tag.startswith('X') else 1

    # Distractor: unused computation
    magnitude = sum([ord(c) for c in entry['name']]) % 7

    # Relevant logic: score depends on active status and length
    base_value = len(entry['name']) * 2
    if entry['active']:
        adjustment = 5 if entry['category'] == 'premium' else 2
    else:
        adjustment = -3

    # Conditional expression used
    bonus = 4 if 'special' in entry['features'] else 0

    return base_value + adjustment + bonus


def calculate_final_score(entries):
    scores = []
    total_weighted = 0
    count_processed = 0

    for entry in entries:
        # String method used for filtering
        if entry['tag'].strip().lower().endswith('temp'):
            continue  # Skip temporary entries

        # Valid entry processing
        raw_score = process_entry(entry)
        # Another distractor variable
        normalized = raw_score / (len(entry['name']) + 1)
        total_weighted += raw_score * entry.get('priority', 1)
        scores.append(raw_score)
        count_processed += 1

    # Simulated grouping logic
    grouped_adjustment = 0
    high_priority_count = 0
    for entry in entries:
        if entry.get('priority', 0) > 2:
            high_priority_count += 1

    # Red herring: complex but irrelevant calculation
    if high_priority_count > 0:
        phantom_sum = sum([i * i for i in range(high_priority_count)])
        fake_average = phantom_sum / high_priority_count if high_priority_count else 0

    # Real impact: final score based on weighted sum and count
    final_score = int(total_weighted - (10 - min(count_processed, 10)))

    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Input data
data_entries = [
    {'name': 'Alice', 'tag': 'user_active', 'active': True, 'category': 'premium', 'features': ['special'], 'priority': 3},
    {'name': 'Bob', 'tag': 'user_temp', 'active': True, 'category': 'basic', 'features': [], 'priority': 1},
    {'name': 'Charlie', 'tag': 'user_staging', 'active': False, 'category': 'basic', 'features': [], 'priority': 2},
    {'name': 'Diana', 'tag': 'user_active_x', 'active': True, 'category': 'premium', 'features': ['special'], 'priority': 3},
    {'name': 'Eve', 'tag': 'debug_temp', 'active': True, 'category': 'basic', 'features': ['special'], 'priority': 1}
]

# Execution point
final_score = calculate_final_score(data_entries)