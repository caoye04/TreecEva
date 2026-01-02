def analyze_system_load(usage_data):
    # Irrelevant transformation - distractor
    normalized = [u / max(usage_data) for u in usage_data]
    thresholds = [0.5, 0.75, 0.9]
    alerts = sum(1 for u in normalized if u > thresholds[1])
    return alerts

# Simulated sensor readings (distractor data)
sensor_readings = [23.4, 25.1, 22.8, 26.5, 24.0, 27.3]
avg_temp = sum(sensor_readings) / len(sensor_readings)

def process_metrics(raw):
    # Complex but irrelevant preprocessing chain
    filtered = list(filter(lambda x: x > 0, raw))
    indexed = dict(enumerate(filtered))
    squared_devs = [(v - sum(filtered)/len(filtered))**2 for v in filtered]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    return [round(v + variance, 2) for v in filtered]

# Unused recursive function - red herring
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n-1) + calculate_depth(n-2)

# Core weight adjustment logic using set operations and zip
def adjust_weights(factors, base):
    factor_set = set(factors)
    prime_weights = {2, 3, 5, 7, 11}
    adjusted = []
    for i, w in enumerate(base):
        if (i + 1) in factor_set:
            adjustment = 1.1 if (i + 1) in prime_weights else 0.9
        else:
            adjustment = 0.95
        adjusted.append(w * adjustment)
    return adjusted

# Main evaluation with nested logic and distractors
def evaluate_performance(metrics, weights):
    # Step 1: Process metrics through irrelevant pipeline
    processed = process_metrics(metrics)
    
    # Step 2: Early filtering that looks important but isn't critical
    valid_indices = [i for i, m in enumerate(processed) if m > 1.0]
    if not valid_indices:
        return -1
    
    # Step 3: Real computation begins - accumulation over zip
    temp_results = []
    for val, weight in zip(processed, weights):
        if val < 0: 
            continue
        temp_results.append(val * weight)
    
    # Step 4: Summation with conditional scaling
    raw_sum = sum(temp_results)
    scale_factor = 1.0
    if raw_sum > 50:
        scale_factor = 0.8
    elif raw_sum < 10:
        scale_factor = 1.2
    
    # Step 5: Apply adjustment using set logic
    contribution_set = {int(x) for x in temp_results if x > 5}
    bonus = len(contribution_set.intersection({7, 11, 13})) * 2.5
    
    # Step 6: Final accumulation - this is where answer comes from
    final = raw_sum * scale_factor + bonus
    
    # Dead code path - never executed due to structure above
    if False:
        fallback = 0
        for _ in range(10):
            fallback += calculate_depth(5)
        final = fallback
    
    return final

# Primary data inputs
metrics = [4.5, 6.7, -1.2, 8.3, 5.1, 9.0, 3.2]
weights = [0.8, 1.2, 1.0, 0.9, 1.1, 1.3, 0.7]

# Irrelevant data structures - distractors
dependency_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

task_queue = [(1, 'init'), (2, 'load'), (3, 'run')]

# Additional unused computations
transposed = list(zip(*[(i, i*2) for i in range(5)]))
flat = [item for sublist in [(i,i+1) for i in [1,3,5]] for item in sublist]

# Adjust weights using complex logic
adjusted_weights = adjust_weights([2, 3, 5], weights)

# Analyze system load on fake data (dead end)
load_alerts = analyze_system_load([80, 85, 90, 78, 92, 88])

# Key execution point
final_score = evaluate_performance(metrics, adjusted_weights)

# Output result
print(f"Result: {final_score}")