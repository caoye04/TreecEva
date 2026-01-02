import math

def analyze_pattern(sequence):
    magnitude = sum(x ** 2 for x in sequence) ** 0.5
    normalized = [x / magnitude for x in sequence]
    threshold = 0.5
    significant = [i for i, x in enumerate(normalized) if abs(x) > threshold]
    
    # Distractor: energy computation not used later
    total_energy = sum(math.sin(x) ** 2 + math.cos(x) ** 2 for x in normalized)
    
    return significant if len(significant) > 0 else [0]

def detect_anomalies(data_stream):
    anomalies = []
    window_size = 3
    
    for i in range(len(data_stream) - window_size + 1):
        window = data_stream[i:i + window_size]
        avg = sum(window) / len(window)
        variance = sum((x - avg) ** 2 for x in window) / len(window)
        std_dev = variance ** 0.5
        
        # Use of lambda and conditional expression
        is_spike = (lambda z: abs(z - avg) > 1.8 * std_dev)(data_stream[i + 1])
        
        if is_spike:
            confidence = 0.8 if std_dev > 0.5 else 0.3
            anomalies.append((i + 1, confidence))
    
    # Dead code path - never executed due to logic above
    if len(anomalies) == 0 and False:
        fallback = [x * 1.5 for x in data_stream]
        anomalies.append((len(data_stream), 0.1))
    
    return anomalies

def extract_features(anomaly_list, indices):
    feature_vector = []
    for idx, conf in anomaly_list:
        # Semi-relevant transformation
        mapped_index = idx % 7
        if mapped_index in indices:
            transformed = int(conf * 100) + mapped_index
            feature_vector.append(transformed)
    
    # Irrelevant string processing (distractor)
    status_flags = ['OK' if f > 50 else 'LOW' for f in feature_vector]
    flag_summary = ''.join(status_flags).count('OK')
    
    return feature_vector if len(feature_vector) > 0 else [1]

def process_signals(detections):
    raw_data = [12, 7, 9, 15, 6, 4, 11]
    pattern_result = analyze_pattern(raw_data)
    
    # Simulate detection pipeline
    anomalies = detect_anomalies(raw_data)
    selected_indices = analyze_pattern([3, 1, 4, 1, 5])  # Reusing function for different purpose
    features = extract_features(anomalies, selected_indices)
    
    # Core calculation mixed with distraction
    base_score = sum(features) * pattern_result[0]
    adjustment = len(anomalies) ** 2
    
    # Key variable assignment
    final_output = base_score - adjustment
    
    # Extra unused computation (interference)
    derived_metrics = [math.log(f + 1) for f in features if f > 10]
    summary_ratio = sum(derived_metrics) / (len(derived_metrics) + 1e-5)
    
    return final_output

detections = [(1, 0.8), (3, 0.9), (5, 0.7)]
final_output = process_signals(detections)
print(f"Target result: {final_output}")