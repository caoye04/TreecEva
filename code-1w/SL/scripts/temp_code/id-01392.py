import math

# Simulated sensor array diagnostics with noise filtering and anomaly detection
def process_sensors(raw_data, threshold=0.75):
    normalized = [x / max(raw_data) for x in raw_data]
    anomalies = []
    running_sum = 0
    weighted_score = 0.0

    for i, val in enumerate(normalized):
        if val > threshold:
            anomalies.append(i)
        running_sum += i * val

    if len(anomalies) > 0:
        weighted_score = running_sum / len(anomalies)
    else:
        weighted_score = running_sum / 1

    return normalized, anomalies, weighted_score


def transform_coordinates(coords):
    # Irrelevant geometric transformation (dead path)
    transformed = []
    for x, y in coords:
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        transformed.append((r, theta))
    return transformed

def aggregate_logs(event_stream):
    # Unused log aggregator (distractor)
    counts = {}
    for event in event_stream:
        name = event['name']
        counts[name] = counts.get(name, 0) + 1
    return counts

def detect_patterns(values):
    # Misleading pattern detector (red herring)
    patterns = 0
    for i in range(len(values) - 2):
        if values[i] < values[i+1] > values[i+2]:
            patterns += 1
    return patterns

def filter_metrics(metrics, criteria_set):
    # Relevant: filters metrics by membership in critical set
    valid_keys = set(criteria_set)
    return {k: v for k, v in metrics.items() if k in valid_keys}

def analyze_readings(data_dict):
    # Core analysis logic: computes diagnostic from filtered data
    base = 0
    multipliers = []
    
    for key, readings in data_dict.items():
        if 'voltage' in key:
            base += sum(readings) * 0.1
        elif 'current' in key:
            avg = sum(readings) / len(readings)
            multipliers.append(avg * 2)
    
    adjustment = 1.0
    for m in multipliers:
        adjustment *= (1 + m / 10)
    
    result = int(base * adjustment)
    
    # Decoy intermediate (misleading)
    temp_diag = sum(multipliers) * base
    
    return result

# Main execution
if __name__ == '__main__':
    # Raw sensor inputs (simulated)
    sensor_array = [88, 53, 92, 77, 61, 98, 44, 85]
    coords_grid = [(1, 2), (3, 4), (5, 6)]
    events = [{'name': 'power_on'}, {'name': 'reset'}, {'name': 'power_on'}]
    
    # Step 1: Process sensors
    norms, flags, score = process_sensors(sensor_array)
    
    # Step 2: Transform coordinates (irrelevant but executed)
    polar_coords = transform_coordinates(coords_grid)
    
    # Step 3: Detect false patterns (distractor call)
    false_pattern_count = detect_patterns(sensor_array)
    
    # Step 4: Aggregate logs (unused side computation)
    log_summary = aggregate_logs(events)
    
    # Step 5: Build metric dictionary
    all_metrics = {
        'voltage_phase_a': [120.1, 119.8, 120.3],
        'voltage_phase_b': [119.5, 120.0, 119.7],
        'current_line_1': [5.2, 5.4, 5.3],
        'current_line_2': [4.8, 4.9, 5.0],
        'temperature_sensor': [32, 33, 31]
    }
    
    # Step 6: Define critical keys (set operation)
    priority_signals = ['voltage_phase_a', 'current_line_1', 'current_line_2']
    
    # Step 7: Filter relevant metrics using set
    filtered_metrics = filter_metrics(all_metrics, priority_signals)
    
    # Step 8: Analyze filtered readings (critical statement)
    final_diagnostic = analyze_readings(filtered_metrics)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")