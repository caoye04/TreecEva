from itertools import combinations, chain

def analyze_patterns(sequence):
    # Irrelevant pattern analysis (distractor)
    triplet_combinations = list(combinations(sequence, 3))
    sum_triplets = sum(sum(t) for t in triplet_combinations if sum(t) % 2 == 0)
    return len(triplet_combinations)  # Not used in final logic

def transform_case(items):
    # Mixed case transformation with red herring logic
    upper_count = 0
    processed = []
    for item in items:
        if len(item) > 3:
            processed.append(item.upper())
            upper_count += 1
        else:
            processed.append(item.lower())
    excess_info = list(chain.from_iterable([range(len(p)) for p in processed if len(p) > 2]))
    return processed  # Only case matters, not counts or chains

def filter_relevant_entries(data_map):
    # Filtering based on key criteria
    valid_keys = []
    temp_sum = 0
    for k, v in data_map.items():
        if v['active'] and len(k) % 2 == 1:
            temp_sum += v['value']
            valid_keys.append(k)
    adjustment_factor = sum(1 for x in valid_keys if 'a' in x)  # Unused distraction
    return [data_map[k]['value'] for k in valid_keys]

def compute_aggregate(values):
    base_accum = 0
    multiplier = 1
    for i, val in enumerate(values):
        if i % 2 == 0:
            base_accum += val * 1.5
        else:
            base_accum += val * 0.8
        # Simulate intermediate tracking (not affecting result)
        status_flag = 'high' if base_accum > 50 else 'low'
    return round(base_accum, 4)

def calculate_final_score(input_values):
    raw_total = sum(x for x in input_values)
    bonus = 0
    if raw_total > 100:
        bonus = 10
    elif raw_total > 50:
        bonus = 5
    # Core calculation
    penalty = len(input_values) * 0.2
    final_score = raw_total + bonus - penalty
    return round(final_score, 4)

# Main execution flow
if __name__ == '__main__':
    # Initial dataset
    raw_entries = ['alice', 'bob', 'carol', 'dave', 'ellen']
    entry_status = {
        'alice': {'active': True, 'value': 12},
        'bob': {'active': False, 'value': 8},
        'carol': {'active': True, 'value': 18},
        'dave': {'active': True, 'value': 22},
        'ellen': {'active': True, 'value': 15}
    }

    # Step 1: Transform cases (some side effect tracking)
    transformed_names = transform_case(raw_entries)
    
    # Step 2: Analyze combinatorial patterns (entirely irrelevant)
    name_lengths = [len(name) for name in raw_entries]
    _ = analyze_patterns(name_lengths)  # No impact on result

    # Step 3: Filter relevant entries by business rules
    filtered_values = filter_relevant_entries(entry_status)

    # Step 4: Apply weighted aggregation
    aggregated_result = compute_aggregate(filtered_values)

    # Step 5: Final scoring with bonus/penalty logic
    final_score = calculate_final_score(filtered_values)

    print(f"Result: {final_score}")