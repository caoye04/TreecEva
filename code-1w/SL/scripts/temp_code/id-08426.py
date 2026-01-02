def process_sensor_data(raw_data, threshold=75.0):
    # Irrelevant preprocessing: character counting and case conversion
    metadata_log = {}
    for entry in raw_data:
        tag = entry.get('tag', '')
        uppercase_count = sum(1 for c in tag if c.isupper())
        metadata_log[tag] = uppercase_count  # Dead code path — never used again

    # Distractor: complex but unused set operations
    unique_tags = {entry['tag'] for entry in raw_data if 'tag' in entry}
    reserved_tags = {'SYS', 'CORE', 'BOOT'}
    conflict_zones = unique_tags & reserved_tags  # Computed but not used

    # Actual relevant data extraction
    readings = [entry['value'] for entry in raw_data if 'value' in entry]

    # Decoy transformation: bit manipulation with no impact
    shifted_mask = 0
    for i in range(len(readings)):
        shifted_mask ^= (int(readings[i]) << (i % 5))  # Red herring
    masked_diagnostic = shifted_mask & 0xFFFF  # Unused

    # Relevant filtering based on threshold
    filtered_readings = [v for v in readings if v > threshold]

    # Distractor: conditional expression with misleading intermediate
    status_flag = 'ACTIVE' if len(filtered_readings) > 3 else 'STANDBY'
    debug_state = 1 if status_flag == 'ACTIVE' else 0
    auxiliary_score = debug_state * len(conflict_zones) * 100  # Looks important, isn't

    # Nested logic with multiple steps
    def classify(v):
        if v > 90.0:
            return 'CRITICAL'
        elif v > 80.0:
            return 'ELEVATED'
        elif v > threshold:
            return 'WARNING'
        else:
            return 'NORMAL'

    classified = [classify(v) for v in filtered_readings]

    # More distraction: tuple unpacking and dummy assignment
    summary_stats = (len(classified), sum(1 for c in classified if c == 'CRITICAL'))
    count_valid, critical_count = summary_stats  # Unpack but partially ignore

    # Create a set from classifications — actual usage begins here
    alert_levels = set(classified)
    severity_map = {'CRITICAL': 4, 'ELEVATED': 3, 'WARNING': 2}
    
    # Real computation: summing mapped severities
    total_risk = 0
    for level in alert_levels:
        if level in severity_map:
            total_risk += severity_map[level]

    # Another decoy: recursive function that's defined but not used
    def compute_entropy(data, base=2):
        from math import log
        if len(data) == 0:
            return 0.0
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        entropy = 0.0
        for f in freq.values():
            p = f / len(data)
            entropy -= p * log(p, base)
        return entropy

    entropy_diagnostic = compute_entropy(classified)  # Computed but irrelevant

    # Core logic hidden among distractions
    adjustment_factor = 1.5 if 'CRITICAL' in alert_levels else 0.8
    base_diagnostic = total_risk * len(filtered_readings)
    final_diagnostic = round(base_diagnostic * adjustment_factor, 4)

    # Final red herring: unused conditional expression
    result_code = 'OK' if final_diagnostic < 100 else ('ALERT' if 'CRITICAL' in alert_levels else 'MONITOR')

    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Additional irrelevant global variables
SYSTEM_MODE = "DEBUG"
MAX_BUFFER_SIZE = 1024
last_processed_id = None

# Simulated sensor input
sensor_input = [
    {'tag': 'SensorA', 'value': 65.0},
    {'tag': 'sensorB', 'value': 82.5},
    {'tag': 'SENSORC', 'value': 88.0},
    {'tag': 'SensorD', 'value': 91.0},
    {'tag': 'sensorE', 'value': 76.0},
    {'tag': 'SensorF', 'value': 70.0},
    {'tag': 'SENSORG', 'value': 95.0}
]

# Key execution point
final_diagnostic = analyze_readings = process_sensor_data(sensor_input)
