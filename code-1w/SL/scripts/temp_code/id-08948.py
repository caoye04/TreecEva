from collections import defaultdict, Counter

# Simulate sensor data with noise and metadata
def generate_sensor_readings():
    readings = [15, 22, 18, 24, 31, 19, 25, 28, 30, 21]
    timestamps = list(range(10))
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'OK', 'OK', 'WARNING', 'OK', 'OK', 'ERROR']
    return list(zip(timestamps, readings, statuses))

# Parse and filter valid data
def parse_valid_data(raw_readings):
    valid_entries = []
    error_count = 0
    warning_count = 0
    for t, val, status in raw_readings:
        if status == 'ERROR':
            error_count += 1
        elif status == 'WARNING':
            warning_count += 1
        else:
            valid_entries.append(val)
    
    # Irrelevant aggregation
    stats_log = defaultdict(int)
    stats_log['errors'] = error_count
    stats_log['warnings'] = warning_count
    stats_log['valid_length'] = len(valid_entries)
    
    return valid_entries, stats_log

# Apply moving average filter (unused in final result)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal) - window + 1):
        avg = sum(signal[i:i+window]) / window
        smoothed.append(avg)
    return smoothed

# Analyze trend direction (distractor function)
def detect_trend(data_slice):
    if len(data_slice) < 2:
        return 'STABLE'
    direction = 'UP' if data_slice[-1] > data_slice[0] else 'DOWN'
    magnitude = abs(data_slice[-1] - data_slice[0])
    return f'{direction}_{magnitude}'

# Core evaluation logic
def compute_metric_a(values):
    return sum(v ** 0.5 for v in values if v > 20)

def compute_metric_b(values):
    freq = Counter(values)
    mode_val = freq.most_common(1)[0][1]
    return mode_val * 1.5

def compute_metric_c(values):
    mid_section = values[1:-1]  # slice operation
    if not mid_section:
        return 0
    base = sum(mid_section) / len(mid_section)
    penalty = 2.5 if len(values) % 2 == 0 else 0
    return base - penalty

def evaluate_performance(weights, data):
    a = compute_metric_a(data)
    b = compute_metric_b(data)
    c = compute_metric_c(data)
    
    # Weighted combination
    score = weights['a'] * a + weights['b'] * b + weights['c'] * c
    
    # Distractor computation (not used)
    outlier_ratio = len([v for v in data if v > 25]) / len(data)
    adjusted_outlier_score = outlier_ratio * 100
    
    # Red herring: unused normalization
    max_possible = 100 * sum(weights.values())
    normalized = (score / max_possible) * 100 if max_possible > 0 else 0
    
    return int(score)  # Final answer is integer

# Main execution
if __name__ == '__main__':
    raw_data_tuples = generate_sensor_readings()
    filtered_values, logs = parse_valid_data(raw_data_tuples)
    
    # Unused signal processing
    smoothed_signal = smooth_signal(filtered_values)
    trend_label = detect_trend(smoothed_signal[::2])  # slicing with step
    
    # Metric weights (only these matter)
    metric_weights = {'a': 1.2, 'b': 0.8, 'c': 1.5}
    
    # Key statement
    final_score = evaluate_performance(metric_weights, filtered_values)
    
    # Output result
    print(f"Result: {final_score}")