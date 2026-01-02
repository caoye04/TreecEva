import math

# Simulate sensor data with noise and valid readings
def generate_sensor_data():
    raw_readings = [12.5, 14.0, 13.8, 15.2, 16.0, 14.3, 13.9, 15.1]
    timestamps = list(range(len(raw_readings)))
    status_flags = ['OK', 'OK', 'ERR', 'OK', 'OK', 'OK', 'ERR', 'OK']
    return list(zip(timestamps, raw_readings, status_flags))

# Filter out erroneous readings and apply calibration
def filter_and_calibrate(data):
    calibrated = []
    error_count = 0
    total_offset = 0.0

    for ts, val, flag in data:
        if flag == 'ERR':  # Skip corrupted data
            error_count += 1
            continue
        # Apply non-linear calibration curve
        calibrated_val = val * (1 + 0.05 * math.sin(ts)) + 0.2
        calibrated.append((ts, calibrated_val))
    
    # Distraction: unused computation
    avg_offset = total_offset / (len(calibrated) or 1) if calibrated else 0.0
    scaling_factor = 1.05  # Unused in final path

    return calibrated

# Process time-series chunks and extract statistical features
def extract_features(calibrated_data):
    values = [val for _, val in calibrated_data]
    n = len(values)
    
    # Compute moving average over window size 3
    moving_averages = []
    for i in range(2, n):
        ma = (values[i-2] + values[i-1] + values[i]) / 3
        moving_averages.append(ma)
    
    # Compute variance from moving average trend
    if moving_averages:
        mean_ma = sum(moving_averages) / len(moving_averages)
        variance = sum((x - mean_ma) ** 2 for x in moving_averages) / len(moving_averages)
        trend_strength = math.sqrt(variance)
    else:
        trend_strength = 0.0

    # Additional distraction variables
    peak_value = max(values) if values else 0.0
    normalized_energy = sum(x**2 for x in values) * 0.01  # Not used later

    return {
        'trend_strength': trend_strength,
        'stability_index': 100 / (1 + trend_strength),
        'sample_count': n
    }

# Apply domain-specific weighting to derive final score
def compute_final_score(features):
    base_weight = 10
    stability_bonus = features['stability_index'] * 0.7
    count_penalty = max(0, 10 - features['sample_count']) * 0.5
    
    # Core calculation
    score = base_weight + stability_bonus - count_penalty
    
    # Red herring computations
    hypothetical_max = base_weight + 100 * 0.7
    efficiency_ratio = score / hypothetical_max if hypothetical_max > 0 else 0
    adjusted_score = score * (1.0 + 0.01 * features.get('extra', 0))  # No effect
    
    return int(round(score))

# Main execution flow
data = generate_sensor_data()
filtered_data = filter_and_calibrate(data)
processed_data = extract_features(filtered_data)
final_score = compute_final_score(processed_data)
print(f"Result: {final_score}")