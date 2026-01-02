import math

# Simulated system telemetry and health monitoring with extensive red herrings
def analyze_component_health(sensor_readings, config):
    accumulated_risk = 0
    temp_offset = config.get('calibration', 0) - 273.15
    pressure_factor = sensor_readings.get('p', 0) * 0.01
    voltage_spike = (sensor_readings.get('v', 0) > 120)

    if sensor_readings.get('t', 0) > config.get('overheat_limit', 85):
        accumulated_risk += 40
    
    if sensor_readings.get('rpm', 0) > 6000:
        accumulated_risk += 25

    # Irrelevant vibration analysis (dead path due to impossible condition)
    micro_vibrations = sensor_readings.get('vib', [])
    critical_modes = [x for x in micro_vibrations if x > 1000]
    if len(critical_modes) > 5 and False:  # Dead code branch
        accumulated_risk += len(critical_modes) * 2

    return accumulated_risk + int(pressure_factor)

# Decoy function – looks important but never called in execution path
def legacy_diagnostic_scan(data):
    checksum = 0
    for k, v in data.items():
        if isinstance(v, int):
            checksum ^= v
    return checksum % 1000

# Another decoy: complex bit manipulation with no downstream effect
def compute_bit_entropy(value):
    entropy = 0
    while value:
        entropy += (value & 1)
        value >>= 1
    return entropy * 1.5 if entropy % 2 else -entropy * 1.5

# Real processing chain begins here
def evaluate_stability_index(telemetry_packet):
    base_score = 100
    anomalies = 0

    # Distractor variables
    transient_spike_count = 0
    recalibration_needed = False
    decay_rate = 0.98

    for entry in telemetry_packet:
        temp = entry.get('temperature', 0)
        load = entry.get('cpu_load', 0)
        fan_speed = entry.get('fan_rpm', 0)

        if temp > 90:
            anomalies += 1
            transient_spike_count += 1  # Used nowhere

        if load > 95 and fan_speed < 2000:
            anomalies += 2

        # Red herring: unused conditional expression
        status_flag = 'critical' if anomalies > 5 else ('elevated' if anomalies > 2 else 'normal')
        recalibration_needed = (status_flag == 'critical')  # Never used later

    # Actual relevant logic hidden among distractions
    adjusted_anomalies = max(anomalies - 1, 0)
    return base_score - (adjusted_anomalies * 8)

# Central metric processor with dictionary operations and conditional expressions
def process_metrics(log_data, thresholds):
    # Irrelevant preprocessing block (no impact on output)
    filtered_logs = [log for log in log_data if log.get('source') != 'debug']
    error_set = {entry['code'] for entry in log_data if entry.get('type') == 'ERROR'}
    warning_count = sum(1 for entry in log_data if entry.get('type') == 'WARNING')

    # Decoy dictionary transformations
    stats_summary = {
        'errors': len(error_set),
        'warnings': warning_count,
        'priority': 'high' if len(error_set) > 5 else 'medium',
        'timestamp_range': (min(log['ts'] for log in log_data), max(log['ts'] for log in log_data))
    }

    # Core logic buried within noise
    total_weight = 0.0
    severity_cap = thresholds.get('max_severity', 10)

    for log in log_data:
        raw_severity = log.get('severity', 1)
        category_boost = 1.0

        # Conditional expression affecting result
        category_boost = 1.5 if log.get('category') == 'system' else 2.0 if log.get('category') == 'security' else 1.0

        adjusted_severity = min(raw_severity * category_boost, severity_cap)

        # Only security and system logs contribute to final weight
        if log.get('category') in ['security', 'system']:
            total_weight += adjusted_severity

    # Additional distraction: unused recursive-like reduction
    def smooth_value(x, depth=3):
        if depth == 0 or x < 1:
            return x
        return 0.5 * smooth_value(x * 0.9, depth - 1)

    smoothed = smooth_value(total_weight)  # Not used in final computation

    # Final calculation using integer division and rounding
    stability_index = evaluate_stability_index(log_data[:3])  # Uses first 3 entries
    diagnostic_code = (int(total_weight // 3) + (stability_index % 17)) * 2

    # Key assignment: this is the answer variable
    final_diagnostic = int(diagnostic_code * 1.5) - 44

    # More decoys
    metadata_hash = sum(ord(c) for c in thresholds.get('mode', 'default')) % 1000
    entropy_marker = compute_bit_entropy(metadata_hash + 100)

    return final_diagnostic

# Simulated input data with mixed types and irrelevant fields
log_data = [
    {'ts': 1623456780, 'type': 'INFO', 'code': 1001, 'severity': 2, 'category': 'network', 'source': 'driver'},
    {'ts': 1623456781, 'type': 'ERROR', 'code': 2001, 'severity': 5, 'category': 'system', 'source': 'kernel'},
    {'ts': 1623456782, 'type': 'WARNING', 'code': 3001, 'severity': 3, 'category': 'security', 'source': 'firewall'},
    {'ts': 1623456783, 'type': 'ERROR', 'code': 2001, 'severity': 4, 'category': 'system', 'source': 'kernel'},
    {'ts': 1623456784, 'type': 'INFO', 'code': 1002, 'severity': 1, 'category': 'ui', 'source': 'frontend'}
]

system_thresholds = {
    'overheat_limit': 90,
    'max_severity': 8,
    'mode': 'production',
    'calibration': 300
}

# Health check initialization (distractor)
initial_risk = 0
for reading in [{'t': 88, 'p': 1013, 'v': 110, 'rpm': 5500}]:
    config_stub = {'overheat_limit': 85}
    initial_risk = analyze_component_health(reading, config_stub)

# Main execution flow
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Target result: {final_diagnostic}")