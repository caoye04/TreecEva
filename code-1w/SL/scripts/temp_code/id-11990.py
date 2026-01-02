from collections import defaultdict, Counter

# Simulate sensor data aggregation and anomaly scoring
def process_sensor_readings(raw_readings, window_size=3):
    smoothed = []
    for i in range(len(raw_readings)):
        start = max(0, i - window_size + 1)
        segment = raw_readings[start:i+1]
        avg = sum(segment) / len(segment)
        smoothed.append(round(avg, 2))
    return smoothed

# Misleading auxiliary function (not used in final path)
def legacy_normalize(x):
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

# Core transformation with distractor variables
def extract_features(series):
    features = defaultdict(float)
    n = len(series)
    
    # Relevant feature: peak-to-peak variation
    ptp = max(series) - min(series)
    features['ptp'] = ptp
    
    # Distractor computation: unused frequency stats
    freq_counter = Counter(series)
    most_freq = freq_counter.most_common(1)[0][1]
    avg_freq = sum(freq_counter.values()) / len(freq_counter)
    features['phantom_metric'] = most_freq - avg_freq  # Not used later
    
    # Relevant: zero-crossing rate approximation
    crossings = 0
    for i in range(1, n):
        if (series[i-1] < 0 <= series[i]) or (series[i-1] > 0 >= series[i]):
            crossings += 1
    features['zcr'] = crossings / n
    
    # Irrelevant bit manipulation distraction
    binary_flags = 0
    for val in series[:4]:
        shifted = int(abs(val * 10)) & 0xFF
        binary_flags ^= shifted << 1
        binary_flags = binary_flags & 0xFFFF
    features['checksum'] = binary_flags  # Unused
    
    return features

# Main scoring logic
def calculate_anomaly_weight(feat, thresh=0.5):
    base = 0
    if feat['ptp'] > thresh:
        base += 3
    if feat['zcr'] > thresh * 0.1:
        base += 2
    return base

def calculate_final_score(data, thresholds):
    cumulative = 0
    history = []
    
    for seq in data:
        # Preprocess sequence
        filtered = [x for x in seq if -100 < x < 100]  # Real filtering
        processed = process_sensor_readings(filtered)
        
        # Extract characteristics
        f = extract_features(processed)
        
        # State tracking distraction
        state_log = []
        temp_state = {'seq_len': len(seq), 'processed_len': len(processed)}
        state_log.append(temp_state)  # Collected but not used
        
        # Actual scoring contribution
        weight = calculate_anomaly_weight(f, thresholds['anomaly'])
        magnitude = f['ptp'] * 10
        score_component = weight * magnitude
        
        # Conditional boost (rarely triggered, not in this data)
        if len([x for x in seq if x > 50]) > 5:
            score_component *= 1.5
        
        cumulative += score_component
        history.append(score_component)
    
    # Final adjustment using set logic (relevant)
    unique_contributions = set(round(h, 0) for h in history)
    adjustment = len(unique_contributions) // 2
    final_score = int(cumulative - adjustment)
    
    # Dead code branch (never reached due to prior logic)
    if False and len(history) > 100:
        fallback = sum(history) / len(history)
        final_score = int(fallback)
    
    return final_score

# Generate input data deterministically
raw_data = [
    [1.2, -3.4, 5.6, -2.1, 8.9, -7.0, 0.5],
    [2.3, 1.8, -4.4, 6.7, -5.5, 3.3, -1.1],
    [-0.8, 2.2, 3.3, -6.6, 4.4, 1.1, -3.3]
]

thresholds = {
    'anomaly': 0.45,
    'sensitivity': 0.8  # Unused parameter
}

# Execute main logic
data = [process_sensor_readings(seq) for seq in raw_data]
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")