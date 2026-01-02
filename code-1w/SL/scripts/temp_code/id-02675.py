def analyze_trends(values, window_size=3):
    trends = []
    for i in range(len(values) - window_size + 1):
        segment = values[i:i + window_size]
        avg = sum(segment) / window_size
        trend = 'up' if segment[-1] > segment[0] else 'down'
        trends.append((avg, trend))
    return trends

# Irrelevant helper function (dead code path)
def deprecated_normalize(data):
    max_val = max(data)
    return [x / max_val * 100 for x in data]

# Another red herring: complex-looking but unused transformation
twist_map = lambda x: (x ** 2 + 3 * x + 1) % 97

# Simulate sensor readings with noise filtering
def filter_outliers(raw_data, threshold=2.5):
    mean_val = sum(raw_data) / len(raw_data)
    variance = sum((x - mean_val) ** 2 for x in raw_data) / len(raw_data)
    std_dev = variance ** 0.5
    filtered = [x for x in raw_data if abs(x - mean_val) <= threshold * std_dev]
    return filtered, mean_val

# Core logic obscured by auxiliary computations
def calculate_final_score(dataset, limits):
    # Step 1: Filter and preprocess
    clean_data, base_ref = filter_outliers(dataset)
    
    # Step 2: Compute rolling statistics
    rolling_stats = analyze_trends(clean_data, 2)
    
    # Step 3: Count directional changes
    direction_changes = 0
    prev = None
    for _, trend in rolling_stats:
        if prev and prev != trend:
            direction_changes += 1
        prev = trend
    
    # Step 4: Apply modular arithmetic on index patterns
    indexed_sum = 0
    for idx, val in enumerate(clean_data):
        if idx % 2 == 0:
            indexed_sum += val * (idx + 1)
    
    # Step 5: Use bitwise to mask certain contributions
    masked_contribution = (int(base_ref) & 15) << 2  # Lower 4 bits, shifted
    
    # Step 6: Aggregate score components
    score_components = [
        len(clean_data) * 3,
        direction_changes * 10,
        indexed_sum // 5,
        masked_contribution
    ]
    
    # Distractor: unused intermediate aggregation
    weighted_avg = sum(i * v for i, v in enumerate(score_components)) / len(score_components) if score_components else 0
    
    # Final computation
    total_score = sum(score_components)
    
    # Additional distraction: conditional that never triggers in this case
    if any(x < 0 for x in dataset):
        total_score -= 100  # Not applicable here
    
    return int(total_score)

# Simulated input data from system telemetry
data_stream = [12, 15, 14, 18, 17, 20, 19, 22]

# Thresholds for processing (used in core logic)
threshold_config = {'sensitivity': 2.5, 'window': 2}

# Secondary unused data structure to increase cognitive load
diagnostic_log = {
    'start': min(data_stream),
    'end': max(data_stream),
    'range': max(data_stream) - min(data_stream),
    'checksum': sum(twist_map(x) for x in data_stream)  # Unused
}

# Key execution point
final_score = calculate_final_score(data_stream, threshold_config)

# Output result as required
print(f"Result: {final_score}")