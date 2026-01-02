def calculate_final_score(records, importance_weights):
    total = 0
    bonus = 10
    penalty = 5
    temp_sum = 0  # distractor: used only for intermediate logging
    adjustment_factor = 0.95

    # Irrelevant preprocessing: case conversion and string padding (distractor)
    processed_labels = [label.upper().strip() for label in records.keys()]
    
    # Semi-relevant accumulation with zip and enumerate
    for i, (key, value) in enumerate(zip(records.keys(), records.values())):
        if i % 2 == 0:
            temp_sum += value * 1.1  # minor adjustment not affecting final result
        else:
            temp_sum += value * 0.9

    # Core logic: weighted sum with conditional scaling
    scale = 1.0
    if sum(records.values()) > 100:
        scale = 1.2

    for idx, (k, v) in enumerate(records.items()):
        weight = importance_weights.get(k, 0.5)
        contribution = v * weight
        if contribution > 20:
            contribution *= scale  # amplification based on threshold
        total += contribution

    # Distractor: unused loop over zipped data
    debug_info = []
    for label, val in zip(processed_labels, records.values()):
        debug_info.append(f'{label}:{val}')

    # Final adjustment with fixed offset and factor
    final_score = int((total * adjustment_factor) + bonus - penalty)
    return final_score

# Input data
metrics = {
    'response_time': 45,
    'throughput': 60,
    'accuracy': 88,
    'latency': 30,
    'reliability': 75
}

weights = {
    'response_time': 0.8,
    'throughput': 1.1,
    'accuracy': 1.3,
    'latency': 0.6,
    'reliability': 0.9
}

# Execution point
final_score = calculate_final_score(metrics, weights)
print(f'Result: {final_score}')