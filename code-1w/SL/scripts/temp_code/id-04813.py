from collections import defaultdict, Counter

# Simulated sensor data ingestion and preprocessing pipeline
def ingest_sensor_data():
    raw_data = [
        (1, 'temp', 23.5), (2, 'pressure', 1013.2), (3, 'humidity', 45),
        (4, 'temp', 25.1), (5, 'pressure', 1012.8), (6, 'flow', 0.47),
        (7, 'humidity', 48), (8, 'temp', 22.9), (9, 'flow', 0.53)
    ]
    return raw_data

# Irrelevant utility function - dead code path
def legacy_calibrate(x):
    return (x * 1.02) - 0.5

# Data classification by type
sensor_types = ['temp', 'pressure', 'humidity', 'flow']
dummy_flags = {t: False for t in sensor_types}

# Unused accumulator - red herring
running_averages = defaultdict(float)

# Main processing with distractors
def process_data(raw_data):
    grouped = defaultdict(list)
    temp_readings = []  # Distractor list
    pressure_readings = []  # Another distractor

    # Real grouping logic
    for idx, s_type, value in raw_data:
        grouped[s_type].append(value)
        if s_type == 'temp':
            temp_readings.append(value)
        elif s_type == 'pressure':
            pressure_readings.append(value)

    # Complex but irrelevant transformation chain
    scaled_values = []
    for t in grouped.get('temp', []):
        adjusted = t * 1.01 + 0.2
        normalized = abs(adjusted) % 100
        scaled_values.append(round(normalized, 2))

    # Decoy statistical calculation
    if len(scaled_values) > 0:
        fake_mean = sum(scaled_values) / len(scaled_values)
        deviation_score = sum(abs(v - fake_mean) for v in scaled_values)
    
    # Real processed output structure
    result = {}
    for s_type, values in grouped.items():
        result[s_type] = {
            'count': len(values),
            'sum': sum(values),
            'latest': values[-1]
        }
    
    # Inject dummy statistics - misleading intermediate
    result['meta'] = {'version': '2.1', 'calibrated': False}
    
    return result

# Threshold configuration map (used later)
def get_thresholds():
    thresholds = defaultdict(dict)
    thresholds['temp']['upper'] = 30.0
    thresholds['temp']['lower'] = 18.0
    thresholds['pressure']['upper'] = 1020.0
    thresholds['pressure']['lower'] = 1000.0
    thresholds['humidity']['upper'] = 60
    thresholds['humidity']['lower'] = 30
    thresholds['flow']['critical'] = 0.6
    return thresholds

# Diagnostic analysis engine
def analyze_metrics(metrics, config):
    diagnostic_code = 0
    severity_weights = {'temp': 3, 'pressure': 2, 'humidity': 1, 'flow': 4}
    anomaly_count = 0
    critical_flags = []

    # Spurious loop with zip - appears meaningful but not used in final logic
    temp_vals = metrics.get('temp', {}).get('sum', 0)
    press_vals = metrics.get('pressure', {}).get('sum', 0)
    for t, p in zip([temp_vals], [press_vals]):
        stability_index = (t / (p + 1e-5)) * 100
        if stability_index > 2.5:
            diagnostic_code += 5

    # Core diagnostic logic
    for s_type, data in metrics.items():
        if s_type == 'meta':
            continue
        
        weight = severity_weights.get(s_type, 0)
        latest_val = data['latest']
        
        # Actual condition checks using config
        if s_type == 'temp' and (latest_val > config[s_type]['upper'] or latest_val < config[s_type]['lower']):
            anomaly_count += 1
            diagnostic_code += weight * 10
        elif s_type == 'pressure' and (latest_val > config[s_type]['upper'] or latest_val < config[s_type]['lower']):
            anomaly_count += 1
            diagnostic_code += weight * 8
        elif s_type == 'humidity' and (latest_val > config[s_type]['upper'] or latest_val < config[s_type]['lower']):
            anomaly_count += 1
            diagnostic_code += weight * 5
        elif s_type == 'flow' and latest_val >= config[s_type]['critical']:
            anomaly_count += 1
            diagnostic_code += weight * 15
            critical_flags.append(True)

    # Secondary adjustment based on count
    if anomaly_count >= 3:
        diagnostic_code += 25
    elif anomaly_count == 2:
        diagnostic_code += 10

    # Final computation with distractor
    base_score = diagnostic_code
    adjustment_factor = 0.95
    
    # Unused complex calculation - red herring
    history_buffer = []
    for i, val in enumerate([base_score]):
        history_buffer.append((i, val * (1.05 ** i)))
    
    final_score = int(base_score * adjustment_factor)
    
    # Key assignment point
    final_diagnostic = final_score + 17  # Offset added here

    return final_diagnostic

# Execution pipeline
if __name__ == '__main__':
    # Step 1: Ingest data
    data_stream = ingest_sensor_data()
    
    # Step 2: Process data (contains distractions)
    processed_data = process_data(data_stream)
    
    # Step 3: Retrieve configuration
    threshold_map = get_thresholds()
    
    # Step 4: Run diagnostics - key statement
    final_diagnostic = analyze_metrics(processed_data, threshold_map)
    
    # Output result
    print(f"Result: {final_diagnostic}")