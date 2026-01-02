import math

# Simulated telemetry data from satellite subsystems
telemetry_stream = [
    {'temp': 78, 'voltage': 3.2, 'status': 'OK', 'timestamp': 1625094000},
    {'temp': 85, 'voltage': 3.1, 'status': 'WARN', 'timestamp': 1625094060},
    {'temp': 95, 'voltage': 2.9, 'status': 'FAIL', 'timestamp': 1625094120},
    {'temp': 65, 'voltage': 3.3, 'status': 'OK', 'timestamp': 1625094180}
]

# Irrelevant auxiliary mapping (distractor)
status_weights = {'OK': 1, 'WARN': 0.5, 'ERROR': 0, 'CRITICAL': -1, 'UNKNOWN': 0}

# Decoy function – never called in execution path
def analyze_redundancy(data):
    return sum(d['temp'] * 0.1 for d in data if d['status'] == 'WARN')

# Unused transformation (dead code)
baseline_shift = [abs(entry['temp'] - 70) for entry in telemetry_stream]

# System mode flags
system_mode = {'active': True, 'debug': False, 'override': False}

# Historical cache with obsolete entries (misleading)
cache_records = {
    'prev_cycle': [88, 82, 81],
    'peak_load': 94,
    'stable_avg': 75.5
}

# Primary processing function with multiple concerns
def normalize_readings(stream):
    temps = [entry['temp'] for entry in stream]
    voltages = [entry['voltage'] for entry in stream]
    avg_temp = sum(temps) / len(temps)
    avg_voltage = sum(voltages) / len(voltages)
    
    # Apply damping factor to smooth fluctuations (relevant)
    damped_temp = avg_temp * 0.9 + 25
    
    # Red herring: unused derived value
    fluctuation_index = max(temps) - min(temps)
    
    return damped_temp, avg_voltage

# Secondary validation logic
validation_log = []
for entry in telemetry_stream:
    if entry['voltage'] < 3.0 and entry['status'] != 'OK':
        validation_log.append(False)
    else:
        validation_log.append(True)

# Misdirection: complex but irrelevant bitwise analysis
bit_analysis = 0
for i in range(len(telemetry_stream)):
    bit_analysis ^= int(telemetry_stream[i]['temp']) & 7

# Another decoy structure (unused)
summary_stats = {
    'count': len(telemetry_stream),
    'max_temp': max(t['temp'] for t in telemetry_stream),
    'min_voltage': min(t['voltage'] for t in telemetry_stream),
    'status_count': {s: 0 for s in status_weights.keys()}
}

# Simulate external state injection (partially relevant)
system_state = {
    'mode': 'active',
    'load_factor': 0.68,
    'recovery_attempts': 2,
    'last_reset': 1625093940
}

# Main diagnostic processor
log_data = [entry for entry in telemetry_stream if entry['status'] in ['WARN', 'FAIL']]

# Core calculation chain
base_score = 0
if log_data:
    # Extract and transform relevant data
    durations = [(log_data[-1]['timestamp'] - log_data[0]['timestamp']) // 60]
    temp_rise = log_data[-1]['temp'] - log_data[0]['temp']
    voltage_drop = round(log_data[0]['voltage'] - log_data[-1]['voltage'], 3)
    
    # Compute weighted risk score
    risk_factors = []
    for record in log_data:
        severity = 1 if record['status'] == 'WARN' else 2
        time_factor = (record['timestamp'] - 1625094000) / 3600
        risk_factors.append(severity * time_factor * record['temp'])
    
    base_score = sum(risk_factors)
    
    # Apply conditional correction using dictionary lookup and slicing
    corrections = [0.85, 0.90, 0.95, 1.0]
    window_slice = corrections[1:3]
    adjustment = window_slice[0] if system_state['load_factor'] > 0.6 else window_slice[1]
    
    base_score *= adjustment

# Auxiliary computation – looks important but not used directly
consistency_check = all(math.isclose(t['voltage'], 3.2, abs_tol=0.2) for t in telemetry_stream)

# Final aggregation with conditional expression and dictionary merge
extended_diagnostics = {
    **{'initial_temp': telemetry_stream[0]['temp']},
    **{'final_risk': round(base_score, 4)}
}

# Critical statement: what is the value of final_diagnostic here?
final_diagnostic = process_metrics(log_data, system_state)

# Top-level function defined late to obscure flow
def process_metrics(failures, state):
    # Local helper with closure
    def time_weighted_risk(entry):
        base_time = 1625094000
        hours_elapsed = (entry['timestamp'] - base_time) / 3600
        return entry['temp'] * hours_elapsed * (2 if entry['status'] == 'FAIL' else 1)
    
    raw_risk = sum(time_weighted_risk(entry) for entry in failures)
    
    # Additional modifiers
    modifier = 1.0
    if state['recovery_attempts'] > 0:
        modifier *= 0.8
    
    # Apply logarithmic compression if high risk
    if raw_risk > 50:
        raw_risk = math.log(raw_risk) * 10
    
    raw_risk *= modifier
    
    # Final adjustment using slicing on sorted list
    history_peaks = sorted([94, 88, 82, 78, 65])
    recent_peak = history_peaks[-2:]  # slicing operation
    if failures[-1]['temp'] >= recent_peak[0]:
        raw_risk *= 1.1
    
    return int(round(raw_risk))

# Print result as required
print(f"Target result: {final_diagnostic}")