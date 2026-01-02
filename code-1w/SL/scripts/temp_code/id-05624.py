from collections import defaultdict, Counter

# Simulated sensor network data processing with diagnostic analysis
def preprocess_readings(raw_readings):
    processed = []
    for item in raw_readings:
        sensor_id = item['sensor']
        value = item['value']
        timestamp = item['time']
        
        # Irrelevant transformation (distractor)
        normalized = (value ** 0.5) if value > 0 else 0
        adjusted = value + (timestamp % 3)  # Misleading adjustment
        
        # Actual relevant logic: filter anomalies
        if 10 <= value <= 95:
            processed.append({'id': sensor_id, 'val': value, 'ts': timestamp})
    
    return processed

# Dead function - never called (red herring)
def legacy_calibrate(data):
    total = sum(d.get('raw', 0) for d in data)
    factor = 0.9 if total > 1000 else 1.1
    return [int(x * factor) for x in data]

# Complex conditional logic with distractors
def classify_environment(avg_temp, humidity_level, pressure):
    if avg_temp < 0:
        return 'FROZEN'
    elif avg_temp < 20:
        if humidity_level > 70:
            return 'HUMID_COLD'
        else:
            return 'DRY_COLD'
    else:
        if pressure < 980:
            return 'LOW_PRESSURE_HOT'
        elif pressure > 1040:
            return 'HIGH_PRESSURE_HOT'
        else:
            return 'STABLE_HOT'

# Unused helper (distractor)
def moving_average(seq, window=3):
    if len(seq) < window:
        return []
    return [sum(seq[i:i+window]) / window for i in range(len(seq)-window+1)]

# Core analysis with bit manipulation red herring
def analyze_readings(data, thresholds):
    stats = defaultdict(int)
    binary_flags = 0
    
    # Meaningless bit accumulation (distraction)
    for entry in data:
        bid = entry['id']
        binary_flags |= (1 << (bid % 8))
    
    # Real logic begins: count per-sensor occurrences
    sensor_counts = Counter(entry['id'] for entry in data)
    
    valid_sensors = 0
    total_sum = 0
    
    for sid, count in sensor_counts.items():
        thresh = thresholds.get(sid, 30)
        
        # Relevant condition
        if count >= thresh:
            valid_sensors += 1
            # Sum all values from qualifying sensors
            for entry in data:
                if entry['id'] == sid:
                    total_sum += entry['val']
    
    # Critical computation path
    if valid_sensors == 0:
        diagnostic_score = 0
    else:
        average_contribution = total_sum / valid_sensors
        # Apply non-linear transformation
        diagnostic_score = int((average_contribution ** 1.5) // valid_sensors)
    
    # Red herring: complex unused calculation
    entropy = 0.0
    for count in sensor_counts.values():
        prob = count / len(data)
        if prob > 0:
            entropy -= prob * (prob).bit_length()
    
    # Final result based on actual logic chain
    final_diagnostic = diagnostic_score + (valid_sensors * 17)
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Simulated input data
    raw_sensor_data = [
        {'sensor': 5, 'value': 15, 'time': 1623},
        {'sensor': 3, 'value': 88, 'time': 1624},
        {'sensor': 5, 'value': 22, 'time': 1625},
        {'sensor': 8, 'value': 12, 'time': 1626},
        {'sensor': 3, 'value': 45, 'time': 1627},
        {'sensor': 5, 'value': 67, 'time': 1628},
        {'sensor': 3, 'value': 33, 'time': 1629},
        {'sensor': 5, 'value': 29, 'time': 1630},
        {'sensor': 8, 'value': 80, 'time': 1631},
        {'sensor': 3, 'value': 90, 'time': 1632},
        {'sensor': 5, 'value': 38, 'time': 1633},
        {'sensor': 3, 'value': 18, 'time': 1634},
        {'sensor': 8, 'value': 44, 'time': 1635},
        {'sensor': 5, 'value': 55, 'time': 1636},
        {'sensor': 3, 'value': 61, 'time': 1637}
    ]

    # Threshold configuration (real parameter)
    threshold_map = {3: 4, 5: 5, 8: 3, 9: 6}  # Sensor 9 not present

    # Processing pipeline
    cleaned = preprocess_readings(raw_sensor_data)
    
    # Intermediate distractor calculations
    temp_readings = [entry['val'] for entry in cleaned if entry['id'] in [3,5]]
    avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
    humidity_level = 65
    pressure = 1013
    
    env_class = classify_environment(avg_temp, humidity_level, pressure)
    
    # Another distraction: unused statistical summary
    time_series = sorted([entry['ts'] for entry in cleaned])
    gaps = [time_series[i] - time_series[i-1] for i in range(1, len(time_series))]
    median_gap = sorted(gaps)[len(gaps)//2] if gaps else 0
    
    # Key statement that produces the answer
    final_diagnostic = analyze_readings(cleaned, threshold_map)
    
    print(f"Result: {final_diagnostic}")