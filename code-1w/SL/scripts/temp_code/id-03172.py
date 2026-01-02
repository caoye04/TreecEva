def process_metrics(entries, scaling_factors):
    base_multiplier = 1.5
    temp_results = []
    cumulative_shift = 0

    for entry in entries:
        raw_value = entry['value']
        category = entry['type']
        
        # Irrelevant transformation (distractor)
        shifted_value = raw_value + (hash(category) % 3) - 1
        normalized = abs(shifted_value) % 100
        
        # Actual relevant logic
        if category == 'critical':
            adjustment = lambda x: int(x * 1.8) if x > 40 else int(x * 1.2)
        elif category == 'standard':
            adjustment = lambda x: int(x * 1.1)
        else:
            adjustment = lambda x: int(x * 0.9)
            
        adjusted = adjustment(normalized)
        temp_results.append(adjusted)

    # Dead code path (distractor)
    outlier_count = 0
    for val in temp_results:
        if val > 90:
            outlier_count += 1
        elif val < 10:
            break  # Misleading early exit

    # Real aggregation
    total_weighted = 0.0
    weight_sum = 0
    for i, val in enumerate(temp_results):
        weight = scaling_factors[i % len(scaling_factors)]
        total_weighted += val * weight
        weight_sum += weight

    average_score = total_weighted / weight_sum

    # Additional distraction: unused sorting and case conversion
    labels = [e['type'].upper() for e in entries]
    sorted_labels = sorted(labels)
    label_hash = sum(ord(c) for c in ''.join(sorted_labels))

    final_score = int(average_score + (label_hash % 5))
    return final_score

# Input data
input_entries = [
    {'value': 45, 'type': 'critical'},
    {'value': 60, 'type': 'standard'},
    {'value': 30, 'type': 'optional'},
    {'value': 50, 'type': 'critical'}
]
weights = [0.4, 0.6, 0.5]

# Execution
final_score = process_metrics(input_entries, weights)
print(f"Result: {final_score}")