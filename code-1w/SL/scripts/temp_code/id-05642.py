def analyze_pattern(sequence, threshold=3):
    indices = []
    values = []
    temp_sum = 0
    count = 0

    for i, val in enumerate(sequence):
        if val > threshold:
            indices.append(i)
            values.append(val)
            temp_sum += val ** 2
        else:
            temp_sum -= val

    # Distractor: tracking unused stats
    avg_val = sum(values) / len(values) if values else 0
    max_gap = max([indices[i+1] - indices[i] for i in range(len(indices)-1)] + [0])

    running_total = 0
    adjustment_factor = 1.5

    for idx, v in zip(indices, values):
        if idx % 2 == 0:
            running_total += v * adjustment_factor
        else:
            running_total += v / adjustment_factor

    # Secondary distractor computation (not used)
    mirrored_seq = [sequence[-i-1] for i in range(len(sequence))]
    mirror_match = sum(1 for a, b in zip(sequence, mirrored_seq) if a == b)

    def compute_aggregate(data, weight_map):
        base = 0
        for k, d in enumerate(data):
            if k in weight_map:
                base += d * weight_map[k]
            else:
                base += d * 0.5
        return int(base)

    weight_mapping = {i: 2 for i in indices}
    intermediate_result = compute_aggregate(values, weight_mapping)

    scaling_factor = len(indices) / len(sequence) if sequence else 0
    final_score = intermediate_result + int(running_total * scaling_factor)

    # Irrelevant state tracking
    status_log = [{'step': 'processed', 'value': final_score}]
    
    return final_score

# Input data
input_sequence = [1, 4, 2, 5, 6, 3, 7, 8]
result = analyze_pattern(input_sequence)
print(f"Result: {result}")