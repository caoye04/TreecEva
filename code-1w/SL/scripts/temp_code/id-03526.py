from itertools import groupby

def analyze_sequence(seq):
    runs = [len(list(group)) for value, group in groupby(seq) if value == 1]
    return max(runs) if runs else 0

def compute_entropy(s):
    from collections import Counter
    import math
    counts = Counter(s)
    total = len(s)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_outliers(data, factor=1.5):
    if len(data) < 2:
        return data
    sorted_data = sorted(data)
    q1, q3 = sorted_data[len(sorted_data)//4], sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def evaluate_performance(metrics, threshold):
    # Core logic begins
    raw_values = [v['value'] for v in metrics if v['active']]
    
    # Irrelevant transformation (distractor)
    normalized = [round((x - min(raw_values)) / (max(raw_values) - min(raw_values) + 1e-8), 3) for x in raw_values]
    
    # Key computation: count how many exceed threshold
    above_threshold = sum(1 for x in raw_values if x > threshold)
    
    # Dummy grouping logic (semi-relevant but not used)
    grouped_by_value = {k: list(g) for k, g in groupby(sorted(raw_values))}
    
    # Simulated sequence derived from pattern
    binary_pattern = [1 if x % 2 == 0 else 0 for x in raw_values]
    longest_streak = analyze_sequence(binary_pattern)
    
    # Red herring: entropy of string-encoded values
    str_encoded = ''.join(str(int(x))[-1] for x in raw_values)
    entropy_metric = compute_entropy(str_encoded)
    
    # Unused statistical cleanup
    cleaned = filter_outliers(raw_values, factor=2.0)
    
    # Core answer depends only on threshold count and streak
    base_score = above_threshold * 7
    bonus = longest_streak * 2
    final_score = base_score + bonus
    
    # Dead code path (never executed)
    if False:
        fallback = sum(cleaned) / len(cleaned)
        final_score = int(fallback)
    
    return final_score

# Setup input data
metric_data = [
    {'value': 42, 'active': True},
    {'value': 15, 'active': True},
    {'value': 67, 'active': True},
    {'value': 89, 'active': True},
    {'value': 23, 'active': True},
    {'value': 91, 'active': True},
    {'value': 10, 'active': True},
    {'value': 54, 'active': True},
    {'value': 33, 'active': False},  # Inactive, should be filtered
    {'value': 77, 'active': True}
]

base_threshold = 50

# Execute main logic
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")