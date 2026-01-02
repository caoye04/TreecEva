def process_metrics(entries, importance):
    total = 0
    base_offset = len(entries) * 2
    temp_result = []

    # Tracking metadata (not used in final score)
    stats_log = {}
    for i, entry in enumerate(entries):
        if 'inactive' in entry and entry['inactive']:
            continue

        # Real computation begins
        magnitude = entry.get('value', 0) ** 0.5
        scaling = importance.get(entry['type'], 1.0)
        adjusted = magnitude * scaling

        # Irrelevant intermediate tracking
        temp_result.append(adjusted * 1.1)  # Slight distraction

        # Core accumulation
        total += int(adjusted) + (i % 3)

        # Fake branch with dead logic
        if i > 100:  # Never reached
            stats_log[i] = 'overflow_case'

    # Secondary loop using zip — relevant but obscured
    cumulative_shift = 0
    for val, weight in zip([e['value'] for e in entries], importance.values()):
        cumulative_shift += (val // (weight * 2 + 1)) & 7

    # Combine actual components
    final_score = total + base_offset - cumulative_shift

    # Unused diagnostic structure
    debug_snapshot = {"total_raw": total, "offset": base_offset}

    return final_score

# Input data
entries = [
    {'type': 'A', 'value': 16},
    {'type': 'B', 'value': 25, 'inactive': True},
    {'type': 'A', 'value': 9},
    {'type': 'C', 'value': 64},
    {'type': 'B', 'value': 36}
]

weights = {'A': 1.5, 'B': 2.0, 'C': 0.5}

# Execute
final_score = process_metrics(entries, weights)
print(f"Result: {final_score}")