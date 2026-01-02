import math

# Simulated system telemetry data with mixed signal types
telemetry_stream = [
    {'time': 0.0, 'voltage': 3.3, 'temp': 45.0, 'state': 'active'},
    {'time': 0.1, 'voltage': 3.28, 'temp': 46.1, 'state': 'active'},
    {'time': 0.2, 'voltage': 3.25, 'temp': 47.3, 'state': 'active'},
    {'time': 0.3, 'voltage': 3.15, 'temp': 49.0, 'state': 'active'},
    {'time': 0.4, 'voltage': 2.9, 'temp': 55.2, 'state': 'warning'},
    {'time': 0.5, 'voltage': 2.1, 'temp': 65.0, 'state': 'critical'},
    {'time': 0.6, 'voltage': 1.8, 'temp': 70.1, 'state': 'critical'},
    {'time': 0.7, 'voltage': 1.2, 'temp': 74.5, 'state': 'critical'},
    {'time': 0.8, 'voltage': 0.9, 'temp': 77.3, 'state': 'failed'}
]

# Irrelevant transformation: convert timestamps to hex (unused later)
hex_timestamps = [hex(int(entry['time'] * 1000)) for entry in telemetry_stream]

# Decoy statistical analysis on voltage drift (not used in final logic)
voltage_deltas = [telemetry_stream[i+1]['voltage'] - telemetry_stream[i]['voltage'] 
                  for i in range(len(telemetry_stream)-1)]
mean_drift = sum(voltage_deltas) / len(voltage_deltas)
volatility_index = math.sqrt(sum(d**2 for d in voltage_deltas))

# System thresholds for health checks (used in actual logic)
system_thresholds = {
    'overheat_temp': 75.0,
    'min_voltage': 1.0,
    'max_rise_rate': 8.0  # degrees per second
}

# Extract temperature history for analysis
temp_history = [entry['temp'] for entry in telemetry_stream]
time_intervals = [entry['time'] for entry in telemetry_stream]

# Compute rate of temperature change per second (actual relevant metric)
temp_rates = []
for i in range(1, len(temp_history)):
    delta_t = time_intervals[i] - time_intervals[i-1]
    if delta_t > 0:
        rate = (temp_history[i] - temp_history[i-1]) / delta_t
        temp_rates.append(rate)

# Distractor: analyze state transition counts (never used)
state_transitions = 0
for i in range(1, len(telemetry_stream)):
    if telemetry_stream[i]['state'] != telemetry_stream[i-1]['state']:
        state_transitions += 1

# Simulated log entries with metadata and severity levels
log_entries = [
    {'msg': 'SYS_INIT', 'level': 'INFO', 'ts': 0.0, 'code': 0},
    {'msg': 'VOLTAGE_FLUCTUATION_DETECTED', 'level': 'WARN', 'ts': 0.3, 'code': 12},
    {'msg': 'TEMP_RISE_LIMIT_80PCT', 'level': 'WARN', 'ts': 0.5, 'code': 15},
    {'msg': 'COOLER_FAILURE_PREDICTED', 'level': 'ERROR', 'ts': 0.6, 'code': 21},
    {'msg': 'HARDWARE_SAFETY_SHUTDOWN', 'level': 'CRITICAL', 'ts': 0.8, 'code': 99}
]

# Unused function: calculates log entropy (red herring)
calculate_entropy = lambda logs: sum(math.log(len(logs), 2) for l in logs if 'ERROR' in l['level'])
entropy_score = calculate_entropy(log_entries)

# Set operation to identify unique warning types (partially relevant but not decisive)
warning_types = set()
for log in log_entries:
    if 'WARN' in log['level'] or 'ERROR' in log['level']:
        words = log['msg'].split('_')
        for word in words:
            if len(word) > 4 and word.isupper():
                warning_types.add(word)

critical_keywords = {'FAILURE', 'SHUTDOWN', 'ERROR'}
keyword_match_count = len(critical_keywords.intersection(warning_types))

# Core diagnostic processor
# Filters logs and applies threshold-based reasoning
def process_metrics(logs, thresholds):
    # Extract numeric codes from error logs
    error_codes = [log['code'] for log in logs if log['level'] in ['ERROR', 'CRITICAL']]
    
    # Irrelevant string processing: count uppercase consonants in messages
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    letter_count = 0
    for log in logs:
        letter_count += sum(1 for c in log['msg'] if c in consonants)
    
    # Real condition: check if temperature exceeded shutdown threshold
    peak_temp = max(temp_history)
    overheat_event = peak_temp >= thresholds['overheat_temp']
    
    # Check voltage collapse
    min_voltage = min(entry['voltage'] for entry in telemetry_stream)
    voltage_collapse = min_voltage < thresholds['min_voltage']
    
    # Analyze maximum thermal ramp rate
    max_rate = max(temp_rates) if temp_rates else 0
    excessive_rise = max_rate > thresholds['max_rise_rate']
    
    # Hidden rule: only trigger full diagnostic if multiple failure modes coincide
    if overheat_event and voltage_collapse:
        base_score = 42
    elif overheat_event and excessive_rise:
        base_score = 38
    else:
        base_score = 10
    
    # Apply error code multiplier (only if present)
    code_multiplier = 1
    if error_codes:
        avg_code = sum(error_codes) / len(error_codes)
        code_multiplier = math.ceil(avg_code / 10)
    
    # Final computation with decoy influence
    # NOTE: letter_count is large but has no effect due to short-circuit
    final_score = base_score * code_multiplier
    if keyword_match_count > 1 and final_score > 25:
        final_score += 5
    
    # This variable is the true answer
    final_diagnostic = final_score + len(hex_timestamps) % 17  # minor obfuscation
    
    # Dead code path: never reached due to logic above
    if letter_count > 1000:
        final_diagnostic = -999  # decoy assignment
    
    return final_diagnostic

# Execute main diagnostic
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Result: {final_diagnostic}")