from collections import defaultdict, Counter

# Simulated sensor data ingestion with noise and redundancy
def ingest_sensor_stream():
    raw_stream = [
        (0, 'temp', 23.5), (1, 'pressure', 101.3), (2, 'temp', 24.1),
        (3, 'humidity', 45.0), (4, 'temp', 22.8), (5, 'pressure', 102.1),
        (6, 'flow', 12.5), (7, 'humidity', 47.3), (8, 'temp', 25.0),
        (9, 'pressure', 100.7), (10, 'temp', 23.9), (11, 'flow', 13.1)
    ]
    
    # Irrelevant transformation: mapping to string codes
    code_map = {'temp': 'A1', 'pressure': 'B2', 'humidity': 'C3', 'flow': 'D4'}
    coded = [code_map[t] for _, t, _ in raw_stream]
    frequency_stats = Counter(coded)  # Distractor: never used again
    
    # Relevant: group by sensor type
    grouped = defaultdict(list)
    for idx, stype, value in raw_stream:
        grouped[stype].append(value)
    
    return grouped

# Diagnostic filter chain
def apply_calibration(readings, stype):
    if stype == 'temp':
        return [v + 0.7 for v in readings]  # calibration offset
    elif stype == 'pressure':
        return [v * 0.99 for v in readings]  # minor correction
    else:
        return readings

# Redundant health check with misleading intermediate
# (looks important but doesn't affect final result)
def assess_stability_profile(data):
    temp_changes = [abs(data['temp'][i+1] - data['temp'][i]) 
                    for i in range(len(data['temp'])-1)]
    pressure_trend = sum(1 for i in range(len(data['pressure'])-1) 
                         if data['pressure'][i+1] > data['pressure'][i])
    
    stability_score = len(temp_changes) - sum(1 for x in temp_changes if x > 1.0)
    anomaly_flag = stability_score < 2  # Computed but unused later
    return anomaly_flag  # Dead end

# Real processing path
def filter_outliers(values, limit=2.0):
    mean = sum(values) / len(values)
    std_dev = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean) <= limit * std_dev], std_dev

# Core analysis function
def process_readings(data, thresh):
    calibrated = {}
    for sensor_type, readings in data.items():
        calibrated[sensor_type] = apply_calibration(readings, sensor_type)
    
    # Focus on temperature for final decision
    temp_readings = calibrated['temp']
    
    # Filter using threshold
    clean_temps, spread = filter_outliers(temp_readings, limit=thresh)
    
    # Compute weighted diagnostic index
    weights = [1.0, 1.2, 1.4, 1.6, 1.8]  # Increasing weight for recent
    recent_count = min(len(clean_temps), len(weights))
    weighted_sum = sum(temp * weight 
                       for temp, weight in zip(reversed(clean_temps[-recent_count:]), weights[:recent_count]))
    
    # Secondary adjustment based on pressure consistency (distractor branch)
    press = data['pressure']
    variation = max(press) - min(press)
    if variation > 1.5:
        weighted_sum -= 2.5  # Minor penalty
    else:
        baseline_offset = 23.0
        adjustment = (weighted_sum / (spread + 1e-5)) * 0.01  # Looks complex, minimal impact
        weighted_sum += adjustment  # Slight boost
    
    # Final nonlinear transformation
    import math
    final_index = int(math.floor(weighted_sum * 1.08))
    
    # Additional red herring: unused conditional expression
    status_label = 'OK' if final_index > 100 else 'MONITOR' if final_index > 80 else 'ALERT'
    _ = f'Diagnostic {status_label}: reading active'  # No effect
    
    return final_index

# Main execution flow
if __name__ == '__main__':
    # Ingest and parse sensor data
    sensor_data = ingest_sensor_stream()
    
    # Irrelevant aggregation: total point count
    total_points = sum(len(v) for v in sensor_data.values())
    compression_ratio = total_points / (total_points + 5)  # Unused metric
    
    # Stability assessment (called but result ignored)
    _ = assess_stability_profile(sensor_data)
    
    # Filtering operation that modifies data
    filtered_data = {}
    for typ, vals in sensor_data.items():
        # Apply dynamic filtering based on type
        if typ == 'humidity':
            filtered_data[typ] = [v for v in vals if 30 < v < 70]
        elif typ == 'flow':
            filtered_data[typ] = [v * 0.9 for v in vals]  # scaling
        else:
            filtered_data[typ] = vals  # pass through others
    
    # Threshold logic with decoy calculation
    base_thresh = 2.0
    dynamic_factor = len(filtered_data['temp']) * 0.1
    threshold = base_thresh if dynamic_factor < 0.5 else base_thresh * 0.7  # evaluates to 2.0
    
    # Critical statement
    final_diagnostic = process_readings(filtered_data, threshold)
    
    # Output result as required
    print(f"Target result: {final_diagnostic}")