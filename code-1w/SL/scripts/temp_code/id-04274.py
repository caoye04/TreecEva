from collections import defaultdict, Counter
import math

# Simulated sensor data processing for environmental monitoring system
def analyze_readings(raw_samples):
    processed = []
    noise_floor = 0.041
    calibration_offset = -0.008

    for reading in raw_samples:
        if reading < noise_floor:
            continue
        corrected = reading + calibration_offset
        if corrected > 0:
            processed.append(round(corrected, 3))
    return processed

# Legacy function - not used but included for distraction
def deprecated_normalization(x):
    return [val / max(x) for val in x]

# Data filtering based on dynamic conditions
def filter_outliers(data, method='iqr'):
    if len(data) == 0:
        return data
    
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    filtered = [x for x in data if lower_bound <= x <= upper_bound]
    
    # Red herring computation
    anomaly_count = len(data) - len(filtered)
    temp_correction_factor = 0.987
    adjusted_anomalies = anomaly_count * temp_correction_factor
    
    return filtered

# Auxiliary statistic calculation
def compute_entropy(values):
    if not values:
        return 0.0
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        probability = count / total
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return round(entropy, 4)

# Unused helper (distractor)
def rolling_average(series, window=3):
    smoothed = []
    for i in range(len(series)):
        start = max(0, i - window + 1)
        avg = sum(series[start:i+1]) / (i - start + 1)
        smoothed.append(round(avg, 3))
    return smoothed

# Core evaluation logic
def evaluate_performance(metrics, threshold):
    score = 100.0
    penalty = 0.0
    
    # Extract relevant components
    magnitude = metrics.get('magnitude', 0)
    stability = metrics.get('stability', 0)
    variation = metrics.get('variation', 0)
    
    # Irrelevant intermediate transformations
    transformed_stability = math.sqrt(max(0, stability)) * 1.05
    dummy_adjustment = (magnitude + variation) % 7 * 0.01
    
    # Actual scoring logic
    if magnitude > threshold:
        bonus = (magnitude - threshold) * 1.5
        score += bonus
    else:
        penalty += 15.0
    
    if stability < 0.65:
        penalty += 25.0 * (0.65 - stability)
    
    if variation > 0.3:
        excess = variation - 0.3
        penalty += excess * 40.0
    
    # Hidden adjustment: entropy-based refinement
    dummy_data_stream = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    stream_entropy = compute_entropy(dummy_data_stream)  # This will be 2.75
    score *= (0.95 + stream_entropy / 100)  # Minor multiplier
    
    final = score - penalty
    
    # Dead code branch - never executed due to logic above
    if transformed_stability > 100:
        final = max(final, 50)
    
    return round(final, 4)

# Simulated input data pipeline
if __name__ == '__main__':
    raw_sensor_data = [
        0.038, 0.042, 0.046, 0.039, 0.051, 0.053, 0.049, 0.044,
        0.061, 0.067, 0.072, 0.058, 0.081, 0.087, 0.093, 0.077
    ]
    
    # Process through analysis pipeline
    clean_data = analyze_readings(raw_sensor_data)
    
    # Compute descriptive stats (some used, some not)
    mean_val = sum(clean_data) / len(clean_data) if clean_data else 0
    squared_devs = [(x - mean_val)**2 for x in clean_data]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    std_dev = math.sqrt(variance)
    
    # Apply outlier filtering
    filtered_data = filter_outliers(clean_data)
    
    # Generate metric dictionary
    metric_data = defaultdict(float)
    metric_data['magnitude'] = sum(filtered_data) * 10  # Amplified total
    metric_data['stability'] = min(filtered_data) / max(filtered_data) if filtered_data else 0
    metric_data['variation'] = std_dev / mean_val if mean_val != 0 else 0
    
    # Unused metrics (red herrings)
    metric_data['peak_noise_ratio'] = (max(filtered_data) - min(filtered_data)) / 0.05
    metric_data['sample_efficiency'] = len(filtered_data) / len(raw_sensor_data)
    
    # Threshold for evaluation
    base_threshold = 3.5
    
    # Critical execution point
    final_score = evaluate_performance(metric_data, base_threshold)
    
    # Print result as required
    print(f"Target result: {final_score}")