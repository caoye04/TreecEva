def analyze_metrics(values, threshold=50):
    count_above = 0
    temp_sum = 0
    squared_values = []

    for idx, val in enumerate(values):
        if val > threshold:
            count_above += 1
            temp_sum += val
        squared_value = val ** 2
        if squared_value < 1000:  # Distractor: not used later
            pass
        squared_values.append(squared_value)

    avg_high = temp_sum / count_above if count_above else 0
    return avg_high, count_above


def extract_patterns(data_list):
    pattern_matches = []
    for item in data_list:
        if isinstance(item, str) and 'err' in item.lower():
            pattern_matches.append(True)
        else:
            pattern_matches.append(False)
    return pattern_matches

# Simulate system benchmark readings
diagnostic_logs = ['OK', 'WARN_1', 'OK', 'err_critical', 'OK', 'err_init']
raw_readings = [45, 67, 89, 34, 78, 91, 23, 56]

# Misleading preprocessing
shifted_data = [x + 10 for x in raw_readings if x < 80]
filtered_names = [f"Node_{i}" for i, x in enumerate(raw_readings) if x > 40]

# Key data structure
benchmark_data = {
    'readings': raw_readings,
    'status': diagnostic_logs,
    'version': '2.1.0',
    'calibration': [1.1, 0.9, 1.0, 1.2]
}

# Auxiliary computation with partial relevance
def adjust_readings(readings, factor=1.05):
    adjusted = []
    for r in readings:
        adj_val = r * factor
n        if adj_val > 100:
            adj_val = 100
        adjusted.append(round(adj_val))
    return adjusted

# Another distractor function
def compute_entropy(lst):
    from math import log2
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    total = len(lst)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

entropy_value = compute_entropy([1, 1, 2, 2, 3, 3])  # Dead-end variable

# Core logic chain
def calculate_performance(data):
    readings = data['readings']
    statuses = data['status']
    
    # Step 1: Analyze high-performing readings
    avg_high, count_high = analyze_metrics(readings, threshold=55)
    
    # Step 2: Count successful status entries (non-error)
    valid_statuses = [s for s in statuses if 'err' not in s.lower()]
    success_rate = len(valid_statuses) / len(statuses)
    
    # Step 3: Use enumerate and zip (required features)
    indexed_scores = []
    for i, val in enumerate(readings):
        penalty = 0
        if i < len(statuses) and 'err' in statuses[i].lower():
            penalty = 15
        score = val - penalty
        indexed_scores.append((i, score))
    
    # Step 4: Apply adjustment factor based on calibration length
    base_total = sum(r for r in readings if r > 50)
    adjustment_factor = len(data['calibration']) * 0.5
    
    # Step 5: Compute weighted contribution
    contributions = []
    for idx, (index, score) in enumerate(indexed_scores):
        weight = 1 + (idx * 0.1)  # Increasing weight by position
        contributions.append(score * weight)
    
    # Step 6: Final aggregation with distractor inclusion
    temp_debug = [c for c in contributions if c > 0]  # Semi-relevant filtering
    aggregate = sum(temp_debug)
    
    # Step 7: Main result calculation
    raw_performance = aggregate * adjustment_factor
    stability_bonus = 10 if success_rate >= 0.5 else 0
    final_raw_score = raw_performance + stability_bonus
    
    # Normalize to reasonable range
    normalized_score = int(final_raw_score / 10)
    
    # Critical execution point
    final_score = normalized_score + count_high
    
    return final_score

# Execution
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")