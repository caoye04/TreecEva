import math

# Simulated sensor data processing system
def analyze_readings(readings):
    if not readings:
        return 0
    valid_count = sum(1 for r in readings if 0 <= r <= 100)
    total = sum(r for r in readings if r > 0)
    avg = total / len(readings) if readings else 0
    outlier_ratio = sum(1 for r in readings if r > 95) / len(readings)
    return avg * (1 - outlier_ratio) if valid_count > 0 else 0

# Legacy function - not used but looks relevant
def compute_legacy_index(x):
    acc = 0
    for i in range(len(x)):
        acc += x[i] * (i % 7 + 1)
    return acc // 3 if acc > 0 else 0

# Data transformation pipeline
def transform_sequence(seq):
    transformed = []
    for val in seq:
        if val < 0:
            continue
        adjusted = val ** 0.5 if val % 2 == 0 else val * 0.9
        normalized = min(adjusted, 50)
        transformed.append(normalized)
    return [t for t in transformed if t > 5]

# Complex conditional expression with distractors
def calculate_weighted_factor(a, b, c, mode='balanced'):
    temp_x = (a * 1.2 + b * 0.8) / 2
    temp_y = (b * 1.5 + c * 0.6) / 2
    
    # Distractor: complex unused calculation
    shadow_accum = 0
    for i in range(1, 11):
        shadow_accum += (a + i) * (c - i) % 5
    
    # Actual logic uses ternary chain
    factor = temp_x * 1.1 if mode == 'aggressive' else (temp_y * 0.95 if mode == 'conservative' else (temp_x + temp_y) / 2)
    return factor

# Main processing function with nested logic and red herrings
def process_metrics(log_data, threshold):
    # Irrelevant preprocessing block (dead path due to constant guard)
    debug_mode = False
    if debug_mode and 'DEBUG_KEY' in log_data:
        print('Tracing internal states...')
        dump = [x * 2 for x in log_data['values'] if isinstance(x, int)]

    # Extract and filter primary metrics
    raw_values = log_data.get('readings', [])
    base_metrics = analyze_readings(raw_values)
    
    # Transform data using secondary logic
    processed_seq = transform_sequence(raw_values)
    
    # Compute auxiliary stats (some irrelevant)
    peak = max(processed_seq) if processed_seq else 0
    floor = min(processed_seq) if processed_seq else 0
    spread = peak - floor
    
    # Unused statistical moment calculations (distractor)
    mean_sq = sum(x*x for x in processed_seq) / len(processed_seq) if processed_seq else 0
    variance_proxy = mean_sq - (sum(processed_seq)/len(processed_seq))**2 if processed_seq else 0
    
    # Key variables for final computation
    a_val = base_metrics
    b_val = len(processed_seq) * 1.5
    c_val = spread * 0.7
    
    # Weighted combination with conditional expression
    core_index = calculate_weighted_factor(a_val, b_val, c_val, mode='balanced')
    
    # Final efficiency score computation
    reliability = 1 - (sum(1 for x in raw_values if x < 0 or x > 100) / len(raw_values)) if raw_values else 0
    efficiency_score = core_index * reliability
    
    # Dead code: unreachable under normal conditions
    if __debug__ and False:
        efficiency_score *= 1.2
    
    # Critical execution point
    final_output = efficiency_score
    
    # Print result as required
    print(f"Result: {final_output}")
    return final_output

# Simulated input data
sensor_log = {
    'timestamp': 1712345678,
    'readings': [85, 92, 78, -5, 96, 88, 45, 102, 73, 81, 69],
    'source': 'primary_array'
}

# Threshold constant (used in function signature but not directly impactful)
threshold = 0.75

# Execute main function
efficiency_score = process_metrics(sensor_log, threshold)