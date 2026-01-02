from collections import defaultdict, Counter

# Simulate sensor data with noise and redundancy
def preprocess_sensor_data(raw_data):
    processed = []
    temp_buffer = []
    for val in raw_data:
        if val < 0:
            temp_buffer.append(abs(val))
        elif val % 2 == 0:
            processed.append(val * 1.5)
        else:
            processed.append(val * 0.8)
    
    # Irrelevant smoothing pass (distractor)
    smoothed = []
    for i in range(len(processed)):
        window = processed[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))
    
    return [round(x, 2) for x in processed]

# Analyze frequency distribution of key signals
def analyze_distribution(clean_data):
    freq = Counter(clean_data)
    mode_val = freq.most_common(1)[0][1] if freq else 0
    
    # Distractor: track rare values that are unused later
    rare_count = sum(1 for v in freq.values() if v == 1)
    threshold = mode_val * 0.7
    
    # Return only relevant metric
    return mode_val + len(freq) // 2

# Core scoring logic with weighted components
def calculate_component_score(arr):
    base_total = sum(x for x in arr if x > 5)
    penalty = 0
    
    # Track transitions (distractor logic)
    direction_changes = 0
    prev_inc = None
    for i in range(1, len(arr)):
        curr_inc = arr[i] > arr[i-1]
        if prev_inc is not None and curr_inc != prev_inc:
            direction_changes += 1
        prev_inc = curr_inc
    
    # Actual penalty based on low-value density
    low_density = sum(1 for x in arr if x < 3)
    if low_density > len(arr) * 0.3:
        penalty += low_density * 1.5
    
    return base_total - penalty

# Final aggregation with weighting
def calculate_final_score(dataset, weight_map):
    scores = defaultdict(float)
    total_weight = sum(weight_map.values())
    
    for key, data in dataset.items():
        clean = preprocess_sensor_data(data)
        dist_metric = analyze_distribution(clean)
        comp_score = calculate_component_score(clean)
        
        # Weighted contribution
        norm_weight = weight_map[key] / total_weight
        scores[key] = (comp_score + dist_metric) * norm_weight
    
    # Misleading entropy calculation (dead code path)
    all_vals = []
    for d in dataset.values():
        all_vals.extend(d)
    entropy = 0
    count = Counter(all_vals)
    for cnt in count.values():
        prob = cnt / len(all_vals)
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    
    final_score = sum(scores.values())
    return round(final_score, 2)

# Input data setup
data = {
    'sensor_a': [12, -3, 8, 14, -7, 6, 2, 11],
    'sensor_b': [9, 5, -2, 13, 4, 4, 6],
    'sensor_c': [7, 7, 8, -5, 3, 1, 15, 10, 10]
}

weights = {
    'sensor_a': 3,
    'sensor_b': 2,
    'sensor_c': 4
}

# Execute main computation
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")