import math

# Simulated sensor data processing for environmental monitoring system
def collect_sensor_data():
    raw_values = [23.4, 19.5, 20.1, 25.3, 18.7, 22.0, 19.8, 24.6]
    timestamps = list(range(1000, 1008))
    metadata = {'unit': 'Celsius', 'location': 'Zone_7', 'version': '2.1'}
    
    # Irrelevant transformation (distractor)
    squared_offsets = [round((x - 20)**2, 2) for x in raw_values]
    
    # Relevant: Normalize around baseline
    normalized = [round(x - 19.0, 2) for x in raw_values]
    return dict(data=raw_values, norm=normalized, time=timestamps, meta=metadata)


def filter_anomalies(logs):
    readings = logs['norm']
    anomalies = []
    filtered = []
    
    threshold = 5.5  # Upper limit for normal fluctuation
    recovery_buffer = []  # Tracks recent values post-anomaly
    
    for i, val in enumerate(readings):
        if val > threshold:
            anomalies.append(i)
            if len(recovery_buffer) > 0:
                recovery_buffer.pop()
        else:
            filtered.append(val)
            # Misleading logic: appending to unused buffer
            if val < 2.0:
                recovery_buffer.append(val * 1.5)
    
    # Dead code path (never accessed due to structure)
    if len(anomalies) == 0 and False:
        backup_repair = [x + 0.5 for x in readings]
        return backup_repair
    
    logs['filtered_norm'] = filtered
    logs['anomaly_count'] = len(anomalies)
    return logs


def compress_data(payload):
    # Unused compression function (decoy)
    if isinstance(payload, list):
        return [round(x * 31 % 17, 2) for x in payload]
    return payload


def generate_summary(features):
    # Complex but irrelevant summary stats
    f_data = features.get('filtered_norm', [])
    total_energy = sum([x**2 for x in f_data])
    phase_shift = math.sin(len(f_data)) * math.cos(f_data[0] if f_data else 1)
    entropy_proxy = -sum([math.log(abs(x)+1e-5) for x in f_data[:4]])
    
    # Distractor variables
    spectral_score = total_energy * phase_shift - entropy_proxy
    temporal_weight = len(f_data) / (features.get('anomaly_count', 1) + 1)
    
    # Relevant reduced feature
    avg_magnitude = round(sum(f_data) / len(f_data), 2) if f_data else 0.0
    return {'average': avg_magnitude, 'count': len(f_data)}


def process_corrections(signal):
    correction_map = lambda x: x * 1.08 if x < 3.0 else x * 0.97
    adjusted = list(map(correction_map, signal))
    drift_compensated = [round(x - 0.15, 2) for x in adjusted]
    
    # String-based tagging (uses string method - required feature)
    tags = [f"CALIB_{str(round(x)).zfill(2)}" for x in drift_compensated]
    valid_tags = [t for t in tags if t.endswith('5') or t.startswith('CALIB_03')]
    
    # Red herring: unused statistical moment
    fourth_moment = sum([(x - sum(drift_compensated)/len(drift_compensated))**4 for x in drift_compensated]) / len(drift_compensated) if drift_compensated else 0
    
    return drift_compensated


def analyze_readings(diagnostic_log):
    base_readings = diagnostic_log.get('filtered_norm', [])
    if not base_readings:
        return -999
    
    # Apply corrections
    corrected = process_corrections(base_readings)
    
    # Secondary filtering (irrelevant for final result)
    noise_floor = 0.5
    cleaned = [x for x in corrected if abs(x) > noise_floor]
    
    # Core calculation: weighted trend analysis
    weights = [0.8, 0.9, 1.0, 1.1, 1.2]  # Dynamic weighting window
    trend_window = corrected[-5:] if len(corrected) >= 5 else [0] * (5 - len(corrected)) + corrected
    
    weighted_sum = 0.0
    for i in range(len(trend_window)):
        weighted_sum += trend_window[i] * weights[i]
    
    # Final diagnostic score
    final_score = round(weighted_sum / sum(weights[:len(trend_window)]), 2)
    
    # Decoy aggregation (not used)
    set_a = set([int(x) for x in corrected if x > 0])
    set_b = set([int(x+1) for x in corrected if x < 4])
    intersection_size = len(set_a.intersection(set_b))
    
    return final_score

# Main execution flow
sensor_log = collect_sensor_data()
processed_logs = filter_anomalies(sensor_log)
summary_features = generate_summary(processed_logs)
# Extraneous intermediate step
encoded_stream = compress_data(processed_logs['data'])
final_diagnostic = analyze_readings(processed_logs)
print(f"Result: {final_diagnostic}")