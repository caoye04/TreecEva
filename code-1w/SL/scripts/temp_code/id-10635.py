def process_results(entries, limits):
    warnings = []
    debug_logs = []
    
    # Precompute thresholds for performance (not all used)
    limit_map = {i: val * 1.5 for i, val in enumerate(limits)}
    debug_logs.append(f'Mapped limits: {limit_map}')

    # Filter valid entries using multiple conditions
    valid_entries = []
    for entry in entries:
        if entry['value'] > limits[0] and entry['flag'] is True:
            valid_entries.append(entry)
        elif 'override' in entry and entry['override']:
            temp_val = entry['value'] * 0.8
            if temp_val > limits[1]:
                valid_entries.append({**entry, 'value': temp_val})

    # Misleading aggregation - not part of final result
    avg_misleading = sum(e['value'] for e in entries) / len(entries) if entries else 0
    debug_logs.append(f'Overall average (unused): {avg_misleading}')

    # Actual processing with lambda and list comprehension
    modifiers = [lambda x: x * 1.1, lambda x: x + 5]
    adjusted = [
        (e['value'] * 1.1 + 5) if e.get('priority') else (e['value'] * 1.05)
        for e in valid_entries
    ]

    # Use of zip and enumerate for alignment tracking (partially relevant)
    base_weights = [0.9, 1.0, 1.2]
    weighted = []
    for i, val in enumerate(adjusted):
        weight = base_weights[i % len(base_weights)]
        weighted.append(val * weight)
        if i > len(limits):  # Dead condition due to data size
            warnings.append(f'Index {i} exceeded limit bounds')

    # Final scoring logic
    raw_total = sum(weighted)
    penalty = len(warnings) * 10
    bonus = 25 if len(valid_entries) >= 3 else 0

    # Key variable assignment
    final_score = int(raw_total - penalty + bonus)

    # Simulate logging (irrelevant output)
    print(f'Debug logs: {len(debug_logs)} entries generated')
    return final_score

# Input data
thresholds = [12.0, 18.5, 25.0]
data = [
    {'value': 10.0, 'flag': False},
    {'value': 15.0, 'flag': True, 'priority': True},
    {'value': 20.0, 'flag': True},
    {'value': 8.0, 'override': True, 'flag': False},
    {'value': 22.0, 'flag': True, 'priority': False}
]

# Execute and print result
result = process_results(data, thresholds)
print(f'Target result: {result}')