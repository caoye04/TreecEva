def analyze_temperatures(temps):
    if not temps:
        return 0
    avg = sum(temps) / len(temps)
    deviations = [abs(t - avg) for t in temps]
    return sum(d > avg * 0.1 for d in deviations)


def filter_outliers(values, threshold=2):
    mean_val = sum(values) / len(values)
    sq_diffs = [(v - mean_val)**2 for v in values]
    variance = sum(sq_diffs) / len(sq_diffs)
    std_dev = variance ** 0.5
    filtered = [v for v in values if abs(v - mean_val) <= threshold * std_dev]
    return filtered if len(filtered) > 2 else values[:len(values)//2 + 1]


def compute_entropy(data):
    from math import log
    total = sum(data)
    if total == 0:
        return 0.0
    probabilities = [d / total for d in data if d > 0]
    entropy = -sum(p * log(p) for p in probabilities)
    return round(entropy, 6)


def merge_segments(segments):
    result = []
    for seg in segments:
        result.extend(seg)
    return result


def calculate_baseline(shifts):
    base = 0
    for i, s in enumerate(shifts):
        base += s * (i % 4 + 1)
    return base * 0.75


def process_metrics(data, weights):
    # Irrelevant preprocessing
    temp_snapshot = [x * 1.05 for x in data if x > 0]
    redundant_copy = temp_snapshot.copy()
    
    # Distractor: unused function call
    _ = analyze_temperatures([10, 12, 15, 14, 20, 21, 18])
    
    # Real computation begins
    filtered_data = filter_outliers(data)
    normalized = [x / sum(filtered_data) for x in filtered_data]
    
    # Weight application
    weighted_vals = []
    for val, w in zip(normalized, weights):
        weighted_vals.append(val * w)
    
    # Additional distraction: dead code path
    if len(weighted_vals) < 5:
        placeholder = [0] * 5
        for idx, val in enumerate(weighted_vals):
            placeholder[idx] = val * 2
    else:
        pass  # Simulated branch, no effect

    # Core logic: accumulation with conditional adjustment
    accumulation = 0
    for i, wv in enumerate(weighted_vals):
        if i % 2 == 0:
            accumulation += wv * 1.5
        else:
            accumulation -= wv * 0.5

    # Set operations as per requirement
    index_set_a = set(range(0, len(weighted_vals), 2))
    index_set_b = set(range(1, len(weighted_vals), 2))
    overlap_count = len(index_set_a & index_set_b)
    adjustment_factor = 1 + (overlap_count * 0.1)

    # Final transformation
    final_score = accumulation * adjustment_factor
    
    # Slicing operation
    history_log = [final_score * 0.9, final_score * 0.95, final_score, final_score * 1.05]
    recent = history_log[-2:]
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution
raw_input = [85, 90, 78, 92, 88, 200, 87, 83]
weights = [0.8, 1.2, 0.9, 1.1, 1.0, 0.7, 1.3, 0.6]
data = filter_outliers(raw_input)

# Misleading intermediate
_ = compute_entropy(data)
segments = [[1,2], [3,4], [5,6]]
_ = merge_segments(segments)

final_score = process_metrics(data, weights)