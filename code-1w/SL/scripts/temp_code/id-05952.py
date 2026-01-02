from collections import defaultdict, Counter

# Simulate sensor readings over time with some noise
def generate_sensor_data():
    return [42 + i * 3 for i in range(15)]

# Process raw data by filtering anomalies and applying calibration
def process_readings(raw):
    calibrated = [x * 0.98 for x in raw if 30 < x < 100]
    offset = sum([calibrated[i] - calibrated[i-1] for i in range(1, len(calibrated))]) / len(calibrated)
    adjusted = [val + offset * 0.1 for val in calibrated]
    return adjusted

# Analyze trend using lambda-based slope detection
trend_analyzer = lambda seq: sum(seq[i] > seq[i-1] for i in range(1, len(seq)))

# Secondary helper that computes distribution stats (partially irrelevant)
def compute_stats(values):
    freq = Counter(values)
    mode_val = freq.most_common(1)[0][1]
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return avg, variance, mode_val

# Main performance calculator combining multiple factors
def calculate_performance(data_log):
    base_metrics = defaultdict(float)
    
    for idx, entry in enumerate(data_log):
        if idx % 3 == 0:
            base_metrics['peak'] += entry * 0.3
        elif idx % 5 == 0:
            base_metrics['bonus'] += entry * 0.05
        else:
            base_metrics['base'] += entry * 0.1
    
    # Dummy loop to increase nesting and add distraction
    temp_buffer = []
    for _ in range(2):
        for val in data_log:
            temp_buffer.append(val ** 0.5)
    
    smoothing_factor = len(temp_buffer) / 100
    base_metrics['base'] = base_metrics['base'] * (1 + smoothing_factor * 0.01)

    # Critical calculation branch
    trend_strength = trend_analyzer(data_log)
    if trend_strength > 7:
        base_metrics['trend_boost'] = 25.0
    else:
        base_metrics['trend_boost'] = 10.0
    
    # Final score computation
    final_score = (
        base_metrics['base'] + 
        base_metrics['peak'] + 
        base_metrics['bonus'] + 
        base_metrics['trend_boost']
    )
    
    # Irrelevant aggregation (distractor)
    total_pairs = 0
    for i, a in enumerate(data_log):
        for j, b in enumerate(data_log):
            if i < j and abs(a - b) < 5:
                total_pairs += 1

    return int(final_score)  # Discretize for deterministic output

# Generate and process data
raw_sensor_data = generate_sensor_data()
processed_data = process_readings(raw_sensor_data)
avg, var, mode_count = compute_stats(processed_data)

# Key execution point
final_score = calculate_performance(processed_data)
print(f"Result: {final_score}")