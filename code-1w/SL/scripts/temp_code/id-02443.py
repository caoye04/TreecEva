from collections import defaultdict, Counter
import math

def preprocess_readings(raw_data):
    # Irrelevant transformation: converts timestamps (not used)
    timestamp_shift = 3600
    adjusted_times = [ts + timestamp_shift for ts in [120, 240, 360]]
    
    # Distractor: complex filtering that doesn't affect final result
    filtered = []
    for x in raw_data:
        if x > 10 and x % 2 == 0:
            filtered.append(x * 0.9)
        elif x <= 10:
            filtered.append(x * 1.1)
    return [round(x, 2) for x in raw_data]  # Key: returns original data rounded

def compute_frequencies(data):
    # Dead function: calculated but never used
    freq = defaultdict(int)
    for item in data:
        freq[item] += 1
    return dict(freq)

def validate_sequence(arr):
    # Misleading validation with side computation
    if len(arr) < 5:
        return False
    checksum = sum(arr[i] * (i + 1) for i in range(len(arr)))
    anomaly_score = 0
    for i in range(1, len(arr)):
        anomaly_score += abs(arr[i] - arr[i-1])
    # This looks important but is discarded
    derived_metric = checksum / (anomaly_score + 1)
    return True

def normalize_readings(data):
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    normalized = [(x - mean_val) / stdev for x in data]
    return [round(x, 3) for x in normalized]

def aggregate_metrics(norm_data):
    # Complex grouping with distractor logic
    groups = defaultdict(list)
    for idx, val in enumerate(norm_data):
        category = 'high' if val > 0.5 else 'low' if val < -0.5 else 'mid'
        groups[category].append(val)
    
    # Compute multiple metrics, most unused
    stats = {}
    for k in groups:
        stats[k + '_count'] = len(groups[k])
        stats[k + '_sum'] = sum(groups[k])
    
    # Red herring: bit manipulation on index sums
    total_index_sum = sum(i for i, x in enumerate(norm_data) if x > 0)
    masked_result = (total_index_sum ^ 255) & 1023  # Looks cryptic, unused
    
    # Actual relevant metric
    mid_count = len(groups['mid'])
    return {'mid_band_usage': mid_count, 'total': len(norm_data)}

def analyze_readings(metrics):
    usage = metrics['mid_band_usage']
    total = metrics['total']
    
    # Core logic hidden among noise
    ratio = usage / total
    score = int(ratio * 1000)
    
    # Multiple decoy transformations
    temp_debug = math.sin(score / 100) * 10000
    debug_flag = (score ^ 512) >> 2
    
    # Final answer embedded here
    final_value = score + 37  # Critical offset
    return final_value

def main():
    # Raw input data
    sensor_readings = [8, 12, 5, 15, 7, 11, 6, 13, 9, 10, 4, 14]
    
    # Step 1: Preprocess (appears complex, just rounds)
    processed_raw = preprocess_readings(sensor_readings)
    
    # Step 2: Validate (returns True, not used)
    is_valid = validate_sequence(processed_raw)
    
    # Step 3: Normalize
    normalized_vals = normalize_readings(processed_raw)
    
    # Step 4: Aggregate metrics
    processed_metrics = aggregate_metrics(normalized_vals)
    
    # Step 5: Analyze readings — KEY EXECUTION POINT
    final_diagnostic = analyze_readings(processed_metrics)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
    
    # Unused variables - red herrings
    freq_table = compute_frequencies(sensor_readings)
    outlier_report = Counter([x for x in sensor_readings if x > 12])
    baseline_shift = sum(sensor_readings) // len(sensor_readings)
    encoded_flag = (baseline_shift << 3) | 7
    
    return final_diagnostic

if __name__ == "__main__":
    main()