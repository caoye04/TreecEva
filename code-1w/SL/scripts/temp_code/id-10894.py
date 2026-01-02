def transform_signal(x):
    # Irrelevant transformation function (dead code path)
    return (x ** 2 + 3 * x + 1) % 100

def accumulate_values(data_list):
    # Distractor function: looks relevant but unused in final computation
    total = 0
    for val in data_list:
        if val > 50:
            total += val // 3
    return total

def parse_sensor_string(raw):
    # Splits and processes a sensor reading string
    parts = raw.split(':')
    sensor_id = parts[0]
    readings_str = parts[1]
    values = [float(x) for x in readings_str.split(',')]
    return sensor_id, values

def map_severity(level):
    # Simple mapping used later
    severity_map = {1: 'LOW', 2: 'MODERATE', 3: 'HIGH', 4: 'CRITICAL'}
    return severity_map.get(int(level), 'UNKNOWN')

def filter_outliers(data, limit=100):
    # Filters values above limit (used once)
    return [x for x in data if x <= limit]

def recursive_reduce(n):
    # Unused recursive red herring
    if n <= 1:
        return 1
    return n - recursive_reduce(n - 2)

def compute_checksum(text):
    # Unused checksum distraction
    return sum(ord(c) for c in text) % 256

def decode_threshold_config(config_str):
    # Processes threshold configuration string
    items = config_str.split('|')
    threshold_map = {}
    for item in items:
        k, v = item.split('=')
        threshold_map[k] = float(v)
    return threshold_map

def normalize_readings(readings):
    # Normalize using min-max scaling
    min_val, max_val = min(readings), max(readings)
    if min_val == max_val:
        return [0.5 for _ in readings]
    return [(x - min_val) / (max_val - min_val) for x in readings]

def count_transitions(data):
    # Counts upward transitions (distractor)
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            count += 1
    return count

def analyze_readings(data, thresholds):
    # Core logic: counts how many normalized values exceed dynamic threshold
    dynamic_ref = thresholds.get('base', 0.3) * thresholds.get('factor', 1.5)
    count_above = 0
    for val in data:
        if val > dynamic_ref:
            count_above += 1
    # Additional rule: if more than half are above, add bonus
    if count_above > len(data) / 2:
        count_above += int(thresholds.get('bonus', 2))
    return count_above

def main():
    # Simulated sensor input
    raw_input = "SNSR45:87.3,42.1,95.7,68.9,104.2,77.6"
    config_line = "base=0.25|factor=2.4|bonus=3|offset=1.1|padding=999"
    
    # Parse sensor data
    sensor_code, raw_values = parse_sensor_string(raw_input)
    
    # Filter extreme outliers (e.g., faulty sensor spike)
    cleaned_values = filter_outliers(raw_values, limit=100)
    
    # Normalize the valid readings
    normalized = normalize_readings(cleaned_values)
    
    # Decode thresholds
    threshold_map = decode_threshold_config(config_line)
    
    # UNUSED: various distractor variables
    checksum = compute_checksum(sensor_code)
    signal_trace = [transform_signal(i) for i in range(3)]
    accumulated = accumulate_values([120, 200, 85])
    transitions = count_transitions(raw_values)
    recursive_result = recursive_reduce(8)
    
    # Core processing pipeline
    processed_data = normalized  # Final data stream
    baseline_ref = threshold_map['base']
    adjustment = 0.1 * len(signal_trace)  # Red herring calculation
    
    # CRITICAL EXECUTION POINT
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result for evaluation
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()