from itertools import combinations, chain

def analyze_segments(data):
    segments = []
    temp_segment = []
    threshold = sum(data) / len(data)

    # Irrelevant segmentation logic (not used in final result)
    for val in data:
        if val > threshold:
            temp_segment.append(val)
        else:
            if len(temp_segment) > 0:
                segments.append(temp_segment)
                temp_segment = []
    if temp_segment:
        segments.append(temp_segment)

    # Distractor: unused transformation
    transformed = [list(map(lambda x: x * 0.95, seg)) for seg in segments]

    return segments  # Not actually used

def extract_patterns(seq):
    pattern_counts = {}
    # Generate all possible 3-element subsequences
    for combo in combinations(seq, 3):
        key = tuple(sorted(combo))
        pattern_counts[key] = pattern_counts.get(key, 0) + 1

    # Misleading filtering (no impact on final answer)
    filtered = {k: v for k, v in pattern_counts.items() if v > 1}
    return filtered

def compute_entropy(values):
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

def calculate_final_score(data_dict):
    scores = []n    
    # Real computation path
    values = data_dict['readings']
    base_avg = sum(values) / len(values)
    
    # State tracking with intermediate variables
    deviation_sum = 0
    squared_deviation_sum = 0
    positive_count = 0
    
    for v in values:
        deviation_sum += abs(v - base_avg)
        squared_deviation_sum += (v - base_avg) ** 2
        if v > 0:
            positive_count += 1
    
    mean_deviation = deviation_sum / len(values)
    variance = squared_deviation_sum / len(values)
    
    # Use of set for deduplication (real use)
    unique_increments = set()
    for i in range(len(values) - 1):
        diff = values[i+1] - values[i]
        if diff != 0:
            unique_increments.add(abs(diff))
    
    increment_factor = len(unique_increments)
    
    # Dummy recursive function (dead code path)
    def dummy_recurse(n):
        if n <= 1:
            return 1
        return n * dummy_recurse(n-2)
    
    dummy_result = dummy_recurse(6)  # Computed but not used
    
    # Core scoring logic
    score_component_1 = base_avg * 1.5
    score_component_2 = (variance / (mean_deviation + 1)) * 2.0
    score_component_3 = positive_count * increment_factor * 3.0
    
    final_raw_score = score_component_1 + score_component_2 + score_component_3
    
    # Final adjustment using itertools.chain (actual usage)
    adjustments = list(chain([0.5], [0.1] * 3, [-0.2]))
    adjustment_sum = sum(adjustments[:len(values) % 5])  # Depends on input length
    
    adjusted_score = final_raw_score + adjustment_sum
    
    return int(round(adjusted_score))

# Main execution flow
raw_input = [12, -5, 8, 21, 3, 16, -4, 9]
data_context = {
    'source': 'sensor_array_7',
    'calibration': 'v2.3',
    'readings': raw_input,
    'timestamp': 1719865432
}

# Unused analysis steps (distractions)
analyzed_segments = analyze_segments(raw_input)
pattern_library = extract_patterns(raw_input)
entropy_metric = compute_entropy(raw_input)

# Key processing step
processed_values = [x for x in data_context['readings'] if x != -5]  # Filter out -5
processed_data = {
    'readings': processed_values,
    'meta': data_context['source']
}

# Critical statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")