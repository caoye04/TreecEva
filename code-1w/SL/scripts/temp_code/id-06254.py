from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant metrics
def generate_noisy_data():
    raw_readings = [15, 23, 18, 25, 30, 14, 19, 27, 22, 20]
    timestamps = list(range(10))
    statuses = ['OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK', 'ERROR', 'OK', 'OK', 'WARNING']
    
    data_stream = []
    for i in range(len(raw_readings)):
        entry = {
            'time': timestamps[i],
            'value': raw_readings[i],
            'status': statuses[i],
            'retries': 0 if statuses[i] == 'OK' else 2,
            'meta': f'data_{i}'
        }
        data_stream.append(entry)
    return data_stream

def preprocess_and_filter(data_stream):
    # Extract only valid entries (non-error)
    filtered = [d for d in data_stream if d['status'] != 'ERROR']
    
    # Misleading aggregation - not used later
    retry_count_total = sum(d['retries'] for d in data_stream)
    average_retry = retry_count_total / len(data_stream) if data_stream else 0
    
    values_only = [d['value'] for d in filtered]
    time_slices = [d['time'] for d in filtered]
    
    # Slice middle portion (t = 2 to t = 6)
    mid_idx = [i for i, t in enumerate(time_slices) if 2 <= t <= 6]
    mid_values = [values_only[i] for i in mid_idx] if mid_idx else []
    
    return values_only, mid_values, average_retry

def calculate_trend_anomaly(values):
    if len(values) < 2:
        return 0
    diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
    trend = sum(diffs)
    anomaly_score = sum(1 for d in diffs if abs(d) > 5)
    return trend * anomaly_score

def calculate_performance(raw_data):
    all_vals, mid_vals, avg_retry = preprocess_and_filter(raw_data)
    
    # Real computation path
    sorted_vals = sorted(all_vals)
    median = sorted_vals[len(sorted_vals)//2]
    
    # Use slicing and set operations to derive secondary features
    upper_half = sorted_vals[len(sorted_vals)//2:]
    unique_upper = list(set(upper_half))
    
    # Combinatorics: count pairs with sum > 2 * median
    pair_count = 0
    for i in range(len(unique_upper)):
        for j in range(i+1, len(unique_upper)):
            if unique_upper[i] + unique_upper[j] > 2 * median:
                pair_count += 1
    
    # Additional feature from mid-segment
    mid_avg = sum(mid_vals) / len(mid_vals) if mid_vals else 0
    mid_peak = max(mid_vals) if mid_vals else 0
    
    # Misleading complex structure
    stats_summary = defaultdict(int)
    for v in all_vals:
        if v > mid_avg:
            stats_summary['above_avg'] += 1
        else:
            stats_summary['below_or_equal'] += 1
    
    # Unused but plausible computation
    entropy_proxy = 0
    counts = Counter(all_vals)
    total = len(all_vals)
    for count in counts.values():
        p = count / total
        entropy_proxy -= p * p  # Simplified squared entropy
    
    # Final score calculation (only some components are relevant)
    base_score = sum(all_vals) // len(all_vals)  # integer average
    trend_score = calculate_trend_anomaly(all_vals)
    bonus = pair_count * 2
    penalty = len([v for v in all_vals if v < 18]) * 3
    
    final_score = base_score + trend_score + bonus - penalty
    
    # This print is required to expose the answer
    print(f"Result: {final_score}")
    return final_score

# Generate input and execute
data = generate_noisy_data()
final_score = calculate_performance(data)