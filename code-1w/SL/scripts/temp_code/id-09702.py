def analyze_readings(sensor_data):
    # Irrelevant preprocessing: normalize values (not actually used)
    normalized = [round((x - min(sensor_data)) / (max(sensor_data) - min(sensor_data)) * 100) for x in sensor_data]
    threshold = 42
    high_readings = [x for x in sensor_data if x > threshold]
    
    # Distractor: complex-looking but unused transformation
    transformed = []
    for i, val in enumerate(sensor_data):
        if i % 2 == 0:
            transformed.append(val ** 0.5 + i // 3)
    
    # Actual relevant logic: count readings above 50
    valid_count = sum(1 for x in sensor_data if x > 50)

    # Dead code path: never executed due to condition
    if len(sensor_data) < 5:
        return -999  # decoy result

    return valid_count


def extract_features(data_stream):
    # Use of zip and enumerate (required python features)
    indices = list(range(len(data_stream)))
    paired = list(zip(data_stream, indices))
    
    # Misleading feature extraction
    features = []
    for idx, (val, pos) in enumerate(paired):
        if val % 7 == 0:
            features.append(idx * val)
    
    # Relevant: compute average of even-positioned elements
    evens_avg = sum(data_stream[i] for i in range(0, len(data_stream), 2)) / len(data_stream[::2])
    
    # Unused statistical distraction
    variance = sum((x - sum(data_stream)/len(data_stream))**2 for x in data_stream) / len(data_stream)

    return int(evens_avg)


def filter_anomalies(logs):
    # Slicing operations (required)
    window = logs[10:15]  # arbitrary slice
    baseline = logs[:5]
    
    # Red herring: anomaly detection based on deviation
    anomalies = []
    for i in range(len(window)):
        if abs(window[i] - baseline[i % len(baseline)]) > 10:
            anomalies.append(i)
    
    # Actually used: just count how many are divisible by 4
    clean_count = sum(1 for x in logs if x % 4 == 0)
    return clean_count


def aggregate_results(dataset):
    score_a = dataset['count_above_50']
    score_b = dataset['even_index_avg']
    score_c = dataset['divisible_by_4']
    
    # Complex weighting with misleading intermediate names
    weight_a = 3.14159
    weight_b = 2.71828
    weight_c = 1.41421
    
    # Decoy calculation (never used)
    phantom_score = (weight_a + weight_b) * (score_a - score_c) / 100
    
    # Actual final computation
    raw_total = score_a * weight_a + score_b * weight_b + score_c * weight_c
    final_score = int(raw_total // 1)  # floor to integer
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == '__main__':
    # Simulated sensor input
    readings = [34, 56, 78, 23, 67, 89, 12, 91, 44, 55, 61, 73, 82, 39, 50]
    
    # Extract various metrics (some irrelevant)
    count_above_50 = analyze_readings(readings)
    even_index_avg = extract_features(readings)
    divisible_by_4 = filter_anomalies(readings)
    
    # Build dataset for aggregation
    processed_data = {
        'count_above_50': count_above_50,
        'even_index_avg': even_index_avg,
        'divisible_by_4': divisible_by_4,
        'timestamp': 1678886400,  # irrelevant metadata
        'version': 'v2.1'          # distractor field
    }
    
    # Critical execution point
    final_score = aggregate_results(processed_data)
