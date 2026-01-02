from collections import defaultdict, Counter

# Simulate sensor data aggregation in an industrial monitoring system
def collect_telemetry(readings):
    aggregated = defaultdict(float)
    noise_floor = 0.003
    calibration_offset = 0.017

    for sensor_id, value in readings:
        if value < 0.1:  # Likely erroneous reading
            continue
        aggregated[sensor_id] += value + calibration_offset

    return dict(aggregated)

# Analyze temporal patterns in sensor bursts
def detect_anomalies(sequence):
    anomalies = []
    moving_avg = 0.0
    count = 0

    for i, val in enumerate(sequence):
        moving_avg = (moving_avg * count + val) / (count + 1) if count > 0 else val
        count += 1
        if abs(val - moving_avg) > 0.5 and val > 1.0:
            anomalies.append((i, val))
    
    # Red herring: unused transformation
    squared_devs = [x**2 for x in sequence if x > 0.5]
    normalized = [x / (sum(squared_devs) + 1e-8) for x in squared_devs]

    return anomalies

# Core evaluation logic with combinatorics and filtering
def generate_combinations(elements, r):
    if r == 0:
        return [[]]
    if not elements:
        return []
    head, tail = elements[0], elements[1:]
    with_head = [[head] + c for c in generate_combinations(tail, r - 1)]
    without_head = generate_combinations(tail, r)
    return with_head + without_head

# Evaluate system performance based on metric thresholds
def evaluate_performance(metrics, base):
    score = 0.0
    penalty_factor = 1.0
    
    # Real computation path
    valid_metrics = [m for m in metrics.values() if isinstance(m, (int, float)) and m >= 0]
    if len(valid_metrics) < 3:
        return -999.0

    mean_metric = sum(valid_metrics) / len(valid_metrics)
    
    # Distractor block: complex but unused bitwise analysis
    bit_analysis = 0
    for m in valid_metrics:
        truncated = int(m * 10)
        bit_analysis ^= (truncated << 2) | (truncated >> 1)
    temp_result = bit_analysis & 0xFFFF

    # Actual scoring logic
    threshold = base * 1.35
    high_performers = [m for m in valid_metrics if m > threshold]
    
    combination_count = len(generate_combinations(high_performers, 2))
    
    if combination_count > 0:
        score += 45.0 * (combination_count / len(valid_metrics))
    else:
        score -= 10.0
    
    # Additional condition based on distribution
    sorted_vals = sorted(valid_metrics)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    
    if iqr < 0.8 * base:
        score += 23.7
    else:
        score -= 5.2
    
    # Final adjustment using enumerate and zip (required idiom)
    adjustments = [0.3, 0.7, 0.4, 0.9]
    total_adj = 0.0
    for idx, (val, adj) in enumerate(zip(sorted_vals, adjustments)):
        if idx % 2 == 0:
            total_adj += adj * (val / (base + 1))
    
    score += total_adj

    # Dead code path: never executed due to prior conditions
    if False and score > 100:
        backup_tracker = Counter()
        for k, v in metrics.items():
            backup_tracker[k] += int(v)
        score = min(score, 88.8)

    return round(score, 6)

# Irrelevant auxiliary function (decoy)
def calculate_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0.0
    for f in freqs.values():
        p = f / total
        entropy -= p * __import__('math').log(p) if p > 0 else 0.0
    return entropy

# Main execution flow
if __name__ == '__main__':
    raw_readings = [
        ('sensor_A', 0.15), ('sensor_B', 0.08), ('sensor_A', 0.22),
        ('sensor_C', 1.45), ('sensor_B', 0.93), ('sensor_C', 0.11),
        ('sensor_A', 1.87), ('sensor_D', 0.02), ('sensor_B', 1.01)
    ]

    # Process telemetry
    processed_data = collect_telemetry(raw_readings)
    
    # Extract sequences for anomaly detection (distractor usage)
    time_series = [v for k, v in raw_readings if v >= 0.08]
    detected_issues = detect_anomalies(time_series)
    
    # Build metric dictionary for evaluation
    metric_data = {
        'throughput': 4.2,
        'latency': 0.85,
        'jitter': 0.33,
        'bandwidth': 5.1,
        'stability': 3.9,
        'reliability': 4.8
    }
    
    # Unused data structures (red herrings)
    historical_stats = defaultdict(list)
    for key, val in metric_data.items():
        historical_stats[key].append(val * 0.95)
        historical_stats[key].append(val * 1.05)

    baseline = 3.5
    
    # Key statement
    final_score = evaluate_performance(metric_data, baseline)
    
    # Print result as required
    print(f"Target result: {final_score}")