import math

# Simulate sensor data processing with noise filtering and threshold analysis
def preprocess_data(raw_readings):
    filtered = [x for x in raw_readings if x > 0]  # Remove invalid (non-positive) readings
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized

# Identify anomalies based on dynamic thresholds
def find_anomalies(values, lower=0.1, upper=0.9):
    anomalies = []
    for i, v in enumerate(values):
        if v < lower or v > upper:
            anomalies.append((i, v))
    return anomalies

# Compute entropy as a measure of data unpredictability
def compute_entropy(values):
    frequency_map = {}
    for v in values:
        rounded = round(v, 2)
        frequency_map[rounded] = frequency_map.get(rounded, 0) + 1

    total = len(values)
    entropy = 0.0
    for count in frequency_map.values():
        prob = count / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 4)

# Main evaluation function combining multiple metrics
def evaluate_performance(data_points, thresholds):
    # Preprocess the input data
    clean_data = preprocess_data(data_points)
    
    # Misleading distraction: calculate average but not used in final logic
    temp_avg = sum(clean_data) / len(clean_data) if clean_data else 0
    temp_variance_proxy = sum([(x - temp_avg)**2 for x in clean_data]) / len(clean_data) if clean_data else 0
    
    # Find out-of-bound values
    anomaly_list = find_anomalies(clean_data, thresholds['low'], thresholds['high'])
    anomaly_count = len(anomaly_list)
    
    # Compute information-theoretic metric
    data_entropy = compute_entropy(clean_data)
    
    # Simulated system health indicator (not directly used but adds complexity)
    health_flags = {"low_signal": False, "high_noise": False}
    if len(clean_data) < 5:
        health_flags["low_signal"] = True
    if data_entropy > 0.8:
        health_flags["high_noise"] = True
    
    # Core logic: score based on entropy and anomaly count
    base_score = 100 - (anomaly_count * 5)
    penalty = int(data_entropy * 10)  # Higher entropy → more randomness → higher penalty
    final_raw_score = base_score - penalty
    
    # Additional red herring: unused transformation
    transformed_scores = {i: (score * 1.1) for i, score in enumerate(clean_data)}
    avg_transformed = sum(transformed_scores.values()) / len(transformed_scores) if transformed_scores else 0
    
    # Final clamping to valid range
    final_score = max(0, min(100, final_raw_score))
    return final_score

# Input data with mixed signal characteristics
data_points = [15, -2, 30, 0, 45, 60, -5, 75, 90, 100, 25]
thresholds = {'low': 0.15, 'high': 0.85}

# Execute main logic
final_score = evaluate_performance(data_points, thresholds)
print(f"Result: {final_score}")