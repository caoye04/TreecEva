def analyze_signal(data, threshold=5.0):
    filtered = [x for x in data if abs(x) > threshold]
    magnitude = sum(abs(x) for x in filtered)
    count = len(filtered)
    return magnitude / count if count else 0.0

# Irrelevant helper function (decoy)
def compute_entropy(sequence):
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = -sum((count / total) * log(count / total) for count in freq.values())
    return entropy

# Unused transformation chain (dead code path)
def transform_readings(readings):
    processed = readings[::2]  # slicing every other element
    processed = [x * 1.5 for x in processed]
    return set(processed)  # set conversion

# Simulated sensor inputs (distraction data)
sensor_log = [-2.3, 4.1, 6.8, -7.2, 9.5, 0.3, -1.2, 8.8, 3.4, -6.1, 5.9]
noise_floor = [abs(x) % 1.0 for x in sensor_log]
smoothed = [round(x + y, 2) for x, y in zip(sensor_log, noise_floor)]

# Real computation begins here — metrics derived from signal analysis
primary_metrics = [
    analyze_signal(sensor_log, 5.0),
    analyze_signal([x * 2 for x in sensor_log], 9.0),
    len([x for x in sensor_log if x > 0]),
    sum(1 for x in sensor_log if x < 0)
]

# Auxiliary but irrelevant metric (red herring)
dummy_metric = compute_entropy([int(abs(x)) for x in sensor_log])

# Weight configuration for evaluation (meaningful only in context)
weights = [0.4, 0.3, 0.2, 0.1]  # Aligned with primary_metrics

# Secondary transformations (distractor list operations)
temp_data = [x for x in smoothed if x > 4]
shifted = temp_data[-3:] + temp_data[:-3]  # slicing rotation
unique_values = set(shifted)  # set operation (irrelevant)

# Core logic: performance evaluator





def evaluate_performance(metrics, importance_weights):
    # Normalize metrics to prevent scale bias (actual relevant logic)
    normalized = []
    for m in metrics:
        if m > 10:
            normalized.append(m / 10.0)
        elif m == 0:
            normalized.append(0.1)
        else:
            normalized.append(m)
    
    # Apply weights and compute weighted score
    weighted_sum = sum(m * w for m, w in zip(normalized, importance_weights))
    
    # Additional adjustment based on pattern in metrics (bitwise distraction)
    pattern_flag = 0
    for m in metrics:
        if int(abs(m)) & 1:  # bitwise AND check for oddness
            pattern_flag += 1
    
    # Final adjustment factor — only depends on weighted_sum
    adjustment = 1.0
    if weighted_sum > 5:
        adjustment = 0.95
    elif weighted_sum < 2:
        adjustment = 1.05
    else:
        adjustment = 1.0
    
    # This part is crucial: metrics[0] represents dominant signal strength
    base_influence = metrics[0] * 0.5
    
    final_value = (weighted_sum + base_influence) * adjustment
    
    # Dead code block (never executed)
    if False:
        fallback = 0
        for val in metrics:
            fallback ^= int(val)  # XOR accumulation (unused)
        final_value = fallback
    
    return final_value

# Execute core evaluation
evaluation_set = primary_metrics  # clearly defined subset
final_score = evaluate_performance(evaluation_set, weights)

# Print result as required
print(f"Result: {final_score}")