from collections import defaultdict, Counter

# Simulated sensor network data analysis with diagnostic logic

def preprocess_readings(raw_readings):
    processed = {}
    for sensor_id, values in raw_readings.items():
        if not values:
            continue
        avg = sum(values) / len(values)
        variance = sum((x - avg) ** 2 for x in values) / len(values)
        processed[sensor_id] = {
            'mean': avg,
            'variance': variance,
            'status_code': 200 if avg > 0 else -1
        }
    return processed

def build_threshold_map(sensors):
    # Irrelevant mapping for calibration levels (distractor)
    calibrations = {sid: abs(hash(sid)) % 5 + 1 for sid in sensors}
    
    # Real threshold logic buried here
    thresholds = defaultdict(float)
    for sid in sensors:
        base = len(sid) % 7
        adjustment = 0.5 if 'X' in sid else 0.2
        thresholds[sid] = base + adjustment
    
    # Dead code path - never used
    debug_info = []
    for k, v in thresholds.items():
        debug_info.append(f'{k}:{v:.2f}')
    
    return thresholds

def filter_anomalies(data_dict):
    # Misleading function - looks important but unused
    anomalies = []
    for sid, metrics in data_dict.items():
        if metrics['variance'] > 250:
            anomalies.append(sid)
    return anomalies

def consolidate_logs(sensor_data):
    # Unused complex aggregation (red herring)
    log_summary = Counter()
    for sid in sensor_data.keys():
        prefix = sid[0] if sid else 'N'
        log_summary[prefix] += 1
    return dict(log_summary)

def evaluate_stability(readings):
    # Decoy computation chain
    total_fluctuation = 0
    for data in readings.values():
        if isinstance(data, dict) and 'mean' in data:
            total_fluctuation += abs(data['mean']) * 0.1
    normalized_index = total_fluctuation / (len(readings) + 1e-8)
    return normalized_index > 0.5  # Never actually used

def analyze_readings(processed_data, threshold_map):
    result_counter = defaultdict(int)
    diagnostic_flags = set()
    
    # Core logic interwoven with distractions
    for sensor_id, metrics in processed_data.items():
        mean_val = metrics['mean']
        thresh = threshold_map.get(sensor_id, 3.0)
        
        # Actual decision logic
        if mean_val > thresh:
            result_counter['high'] += 1
            diagnostic_flags.add(1)
        elif mean_val < thresh * 0.5:
            result_counter['low'] += 1
            diagnostic_flags.add(-1)
        else:
            result_counter['normal'] += 1
            diagnostic_flags.add(0)
    
    # Irrelevant transformation
    flag_list = sorted(list(diagnostic_flags))
    flag_product = 1
    for f in flag_list:
        flag_product *= (f + 2)
    
    # Critical answer computation
    high_count = result_counter['high']
    low_count = result_counter['low']
    normal_count = result_counter['normal']
    
    # Complex but deterministic formula
    score_component = (high_count * 13) - (low_count * 7)
    stability_factor = 1 + (normal_count / (len(processed_data) + 1e-6))
    
    final_diagnostic = int((score_component * stability_factor) + flag_product)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Simulated input data
    raw_sensor_data = {
        'SENSOR_X1': [12.5, 14.0, 13.2, 16.8],
        'SENSOR_Y2': [2.1, 1.8, 2.5],
        'SENSOR_X3': [8.0, 9.1, 7.6, 8.3, 9.0],
        'SENSOR_Z5': [0.3, 0.1, 0.2],
        'SENSOR_X7': [20.1, 19.8, 21.0, 18.9, 20.5]
    }
    
    # Unused data structures (distractors)
    maintenance_log = [
        {'action': 'calibrate', 'sensor': 'SENSOR_X1', 'timestamp': '2023-01-01'},
        {'action': 'replace', 'sensor': 'SENSOR_Y2', 'timestamp': '2023-01-03'}
    ]
    
    system_config = {
        'version': '2.1.0',
        'mode': 'diagnostic',
        'debug_level': 9,
        'buffer_size': 4096
    }
    
    # Execution pipeline
    processed_data = preprocess_readings(raw_sensor_data)
    
    # Call to unused functions (dead paths)
    anomaly_report = filter_anomalies(processed_data)
    log_consolidation = consolidate_logs(raw_sensor_data)
    system_stable = evaluate_stability(processed_data)
    
    threshold_map = build_threshold_map(raw_sensor_data.keys())
    
    # Key execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)