from itertools import combinations

def analyze_trends(data_stream):
    trend_markers = []
    for i in range(1, len(data_stream)):
        if data_stream[i] > data_stream[i-1]:
            trend_markers.append(1)
        elif data_stream[i] < data_stream[i-1]:
            trend_markers.append(-1)
        else:
            trend_markers.append(0)
    return trend_markers

def calculate_entropy(sequence):
    freq_map = {}
    total = len(sequence)
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def filter_outliers(values, factor=1.5):
    sorted_vals = sorted(values)
    q1, q3 = sorted_vals[len(sorted_vals)//4], sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [v for v in values if lower_bound <= v <= upper_bound]

def evaluate_performance(feedback, threshold):
    # Misleading preprocessing
    temp_buffer = []
    for x in feedback:
        if x % 2 == 0:
            temp_buffer.append(x * 1.1)
        else:
            temp_buffer.append(x * 0.9)
    
    # Irrelevant string manipulation
    status_tag = "PERF_EVAL_ACTIVE"
    tag_checksum = sum(ord(c) for c in status_tag) % 100
    
    # Actual logic begins
    base_scores = [x for x in feedback if x >= threshold]
    adjustment_factor = len(base_scores) / len(feedback) if feedback else 0
    
    # Use dictionary to track frequency of high performers
    freq_dict = {}
    for score in base_scores:
        freq_dict[score] = freq_dict.get(score, 0) + 1
    
    # Compute combinatorial uniqueness (distractor but plausible)
    unique_pairs = list(combinations(set(base_scores), 2))
    pair_count = len(unique_pairs)
    
    # Core computation
    raw_total = sum(base_scores)
    final_score = int(raw_total * adjustment_factor) + len(freq_dict)
    
    # Dead code path - never executed under current logic
    if tag_checksum < 0:
        final_score = -1
    
    return final_score

# Simulated input data
system_metrics = [85, 92, 78, 96, 88, 73, 91, 87]
benchmark_threshold = 85

# Distractor: unused transformation
normalized_metrics = [round(x / 100, 2) for x in system_metrics]
feedback_sequence = [x + 5 for x in system_metrics if x % 2 == 1]  # Only odd-indexed base values adjusted

# Additional red herring: unused function call
entropy_value = calculate_entropy(analyze_trends(system_metrics))
trend_analysis = analyze_trends(system_metrics)
filtered_data = filter_outliers(system_metrics)

# Key execution point
final_score = evaluate_performance(feedback_sequence, benchmark_threshold)
print(f"Result: {final_score}")