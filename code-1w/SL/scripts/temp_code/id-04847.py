from collections import defaultdict, Counter

# Simulated sensor network diagnostic tool
# Analyzes environmental readings and applies fault detection logic

def collect_sensor_data():
    # Real data collection would go here
    return [
        (101, 'temp', 23.4), (102, 'humidity', 45.1), (103, 'temp', 22.8),
        (104, 'pressure', 1013.2), (105, 'temp', 26.9), (106, 'humidity', 52.3),
        (107, 'co2', 415.6), (108, 'temp', 24.1), (109, 'pressure', 1012.8),
        (110, 'humidity', 48.7), (111, 'temp', 25.3), (112, 'co2', 423.1)
    ]

def build_threshold_map():
    # Define acceptable ranges for each sensor type
    thresholds = {
        'temp': (20.0, 25.0),
        'humidity': (30.0, 50.0),
        'pressure': (1000.0, 1020.0),
        'co2': (350.0, 450.0)
    }
    
    # Distractor: irrelevant transformation
    temp_copy = {k: v for k, v in sorted(thresholds.items())}
    processed_copy = [f'{k}:{v[0]}-{v[1]}' for k, v in temp_copy.items()]
    metadata_log = {'version': '2.1', 'calibration': 'passed'}
    
    return thresholds

def analyze_trends(data_points):
    # Advanced trend analysis (mostly unused)
    trends = defaultdict(list)
    for sid, stype, value in data_points:
        trends[stype].append(value)
    
    # Distractor: complex but irrelevant statistical computation
    stats_summary = {}
    for sensor_type, values in trends.items():
        mean_val = sum(values) / len(values)
        variance = sum((x - mean_val) ** 2 for x in values) / len(values)
        stats_summary[f'{sensor_type}_stability'] = 1 / (1 + variance) if variance > 0 else 1
    
    # Another red herring
    coded_flags = [bin(hash(stype))[2:10] for sid, stype, _ in data_points[:5]]
    
    return trends  # Only trends is used downstream

def validate_checksum(record_list):
    # Checksum validation (unused in final logic)
    total = 0
    for item in record_list:
        if isinstance(item, tuple) and len(item) == 3:
            total += hash(str(item))
    return hex(total % 10000)

def generate_report_template():
    # Dead code path - never called
    template = {
        'header': 'Sensor Network Report',
        'sections': ['overview', 'anomalies', 'recommendations'],
        'format': 'PDF'
    }
    return template

def filter_anomalies(sensor_groups, limits):
    anomalies = []
    anomaly_count = defaultdict(int)
    
    # Core logic embedded with distractions
    for stype, readings in sensor_groups.items():
        low, high = limits.get(stype, (-float('inf'), float('inf')))
        for reading in readings:
            # Distractor: redundant flagging
            is_outlier = reading < low or reading > high
            severity = 'high' if is_outlier and abs(reading - (low+high)/2) > 10 else 'low'
            
            if is_outlier:
                anomalies.append((stype, reading, severity))
                anomaly_count[stype] += 1
                
                # Red herring: bit manipulation on sensor type
                shift_key = sum(ord(c) for c in stype) % 8
                masked = (anomaly_count[stype] << 2) ^ (shift_key | 7)

    # Distractor: create unused summary string
    summary_str = ''.join(f'{k}:{v}|' for k, v in anomaly_count.items())
    
    return anomalies, dict(anomaly_count)

def calculate_system_health(anomaly_counts):
    # Health score calculation
    base_score = 100.0
    penalties = 0
    
    # Different penalty weights per sensor type
    weights = {'temp': 1.5, 'humidity': 1.2, 'pressure': 2.0, 'co2': 0.8}
    
    for stype, count in anomaly_counts.items():
        weight = weights.get(stype, 1.0)
        penalties += count * weight * 3.5
    
    health = base_score - penalties
    return max(0, health)  # Clamp to non-negative

def aggregate_diagnostics(readings_by_type):
    # Count occurrences per type (used later)
    counter = Counter()
    for stype, vals in readings_by_type.items():
        counter[stype] += len(vals)
    
    # Distractor: enumerate with filtering
    labeled_items = []
    for idx, (k, v) in enumerate(counter.items()):
        if v > 2:
            labeled_items.append(f'{idx}-{k}'.upper())
    
    return dict(counter)

def process_readings(raw_data, thresholds):
    # Step 1: Group by sensor type
    grouped = defaultdict(list)
    for sensor_id, s_type, value in raw_data:
        grouped[s_type].append(value)
    
    # Step 2: Trend analysis (uses core data)
    trends = analyze_trends(raw_data)
    
    # Step 3: Anomaly detection
    anomalies, counts = filter_anomalies(trends, thresholds)
    
    # Step 4: System health assessment
    health_score = calculate_system_health(counts)
    
    # Step 5: Data volume metrics
    volume_stats = aggregate_diagnostics(grouped)
    
    # Step 6: Final diagnostic synthesis
    total_sensors = len(set(sid for sid, _, _ in raw_data))
    active_types = len(volume_stats)
    
    # Irrelevant string processing distraction
    labels = ['sensor_{}'.format(i) for i in range(total_sensors)]
    encoded_labels = [label.replace('_', '-').title() for label in labels]
    checksum_tag = validate_checksum(raw_data)
    
    # Core formula: weighted combination
    # temp_weight: 0.4, humidity_weight: 0.3, others: 0.15 each
    type_weights = defaultdict(lambda: 0.15)
    type_weights.update({'temp': 0.4, 'humidity': 0.3})
    
    weighted_sum = 0.0
    for stype, count in volume_stats.items():
        weighted_sum += count * type_weights[stype]
    
    # Final diagnostic combines health and volume index
    volume_index = sum(volume_stats.values()) / active_types if active_types else 0
    final_diagnostic = int(health_score + volume_index * 2.5 + weighted_sum)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution flow
if __name__ == '__main__':
    collected_data = collect_sensor_data()
    threshold_map = build_threshold_map()
    
    # Distractor variables
    config_settings = {'debug': False, 'mode': 'diagnostic'}
    audit_trail = [f'init', f'data_collected:{len(collected_data)}']
    
    # Key execution point
    final_diagnostic = process_readings(collected_data, threshold_map)