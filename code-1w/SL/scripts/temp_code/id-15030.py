def analyze_sequence(data, threshold):
    count_valid = 0
    temp_sum = 0
    outliers = []
    squared_cache = [x ** 2 for x in range(20)]  # Precomputed squares (partially used)

    for i, val in enumerate(data):
        if val < 0:
            continue  # Skip negatives
        if val > threshold:
            outliers.append(val)
            continue

        temp_sum += val
        count_valid += 1

    avg = temp_sum / count_valid if count_valid else 0

    # Distractor: complex but unused logic
    secondary_flags = []
    for idx, (a, b) in enumerate(zip(data, data[1:])):
        if a == 0 or b == 0:
            continue
        ratio = abs(a / b) if b != 0 else 0
        if 0.5 < ratio < 1.5:
            secondary_flags.append(idx)

    # Another distractor: dead code path
    metadata_log = {}
    if len(outliers) > 100:
        metadata_log['overflow'] = True  # Never reached

    return avg, len(outliers)


def calculate_entropy(values):
    from math import log
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)


def evaluate_performance(records, limit):
    raw_values = [r[1] for r in records]
    filtered_scores = [x for x in raw_values if 10 <= x <= 100]

    # Use of tuple unpacking and enumerate
    adjustments = []
    for index, score in enumerate(raw_values):
        adjustment_factor = (index % 3) + 1
        adjusted = score / adjustment_factor
        adjustments.append(adjusted)

    base_avg, outlier_count = analyze_sequence(raw_values, limit)

    # Real computation chain
    aggregate = sum(adjustments[:len(filtered_scores)])
    size_factor = len(filtered_scores) + len([x for x in raw_values if x < 10])
    entropy_metric = calculate_entropy(filtered_scores)

    # Key distraction: irrelevant set and sorting
    unique_set = set(raw_values)
    sorted_vals = sorted(unique_set, reverse=True)
    midpoint = sorted_vals[len(sorted_vals)//2] if sorted_vals else 0

    # Unused intermediate computations
    phantom_total = 0
    for item in sorted_vals:
        if item % 2 == 0:
            phantom_total += item ** 0.5

    # Final logic with dependency on prior steps
    scaling_factor = 2.5 if entropy_metric > 2.0 else 1.8
    intermediate_result = (aggregate * scaling_factor) / (size_factor + 1)
    penalty = outlier_count * 0.7
    final_score = int(intermediate_result - penalty + base_avg)

    # This print is required for traceability
    print(f"Result: {final_score}")
    return final_score

# Main execution
record_data = [
    ('A', 85), ('B', 92), ('C', 78), ('D', 63), ('E', 95),
    ('F', 88), ('G', 52), ('H', 73), ('I', 90), ('J', 105)
]

threshold_limit = 100
result_var = evaluate_performance(record_data, threshold_limit)