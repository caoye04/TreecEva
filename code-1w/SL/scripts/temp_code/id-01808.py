def process_results(entries, importance):
    total = 0
    bonus = 0
    penalty = 0
    temp_result = []

    # Irrelevant pre-processing (distractor)
    magnitude_check = lambda x: abs(x) > 5
    outliers = [e['value'] for e in entries if magnitude_check(e['value'])]

    # Semi-relevant transformation
    normalized = [(e['value'] + 10) / 20 for e in entries]

    for i, entry in enumerate(entries):
        base = entry['value'] * importance[i]
        
        # Conditional logic with side distraction
        if entry['category'] == 'A':
            base *= 1.2
            extra_weight = sum([importance[i] for _ in range(1)])  # Redundant
        elif entry['category'] == 'B':
            base *= 0.9
            temp_result.append(base)
        else:
            base += 5

        # Accumulate only total; bonus/penalty unused
        bonus += len(outliers) * 0.1  # Computed but irrelevant
        penalty -= min(normalized) if normalized else 0  # Dead-end calc

        total += base

    # Another distractor: sorting that isn't used
    sorted_entries = sorted(temp_result, reverse=True)
    adjustment_factor = 0.95 if len(sorted_entries) > 2 else 1.0

    final_score = int(total * adjustment_factor)

    # Print required result
    print(f"Target result: {final_score}")
    return final_score

# Input data
raw_data = [
    {'value': 8, 'category': 'A'},
    {'value': 12, 'category': 'B'},
    {'value': 5, 'category': 'C'},
    {'value': 15, 'category': 'B'},
    {'value': 3, 'category': 'A'}
]

weights_scheme = [0.5, 0.8, 0.3, 1.0, 0.4]

# Execution point
final_score = process_results(raw_data, weights_scheme)