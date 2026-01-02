import math

# Simulated telemetry data from satellite subsystems
telemetry_streams = {
    'power': [12.4, 11.8, 13.1, 12.7, 12.0],
    'temp_core': [67, 72, 65, 70, 68],
    'temp_panel': [45, 50, 48, 55, 52],
    'signal_strength': [88, 91, 85, 89, 90]
}

# Irrelevant calibration map (distractor)
calibration_map = {i: round(math.sin(i * 0.1), 3) for i in range(100)}

# Historical anomaly thresholds (mostly unused)
anomaly_thresholds = {
    'voltage_surge': 14.0,
    'critical_heat': 80,
    'low_signal': 30,
    'safe_margin': 5
}

# Raw log entries with mixed data types (relevant input)
log_entries = [
    {'timestamp': 1001, 'event': 'OK', 'codes': [0, 0, 0], 'meta': {'q': 1}},
    {'timestamp': 1002, 'event': 'WARN', 'codes': [1, 0, 0], 'meta': {'q': 2}},
    {'timestamp': 1003, 'event': 'ERR', 'codes': [3, 2, 1], 'meta': {'q': 3}},
    {'timestamp': 1004, 'event': 'WARN', 'codes': [1, 1, 0], 'meta': {'q': 4}},
    {'timestamp': 1005, 'event': 'OK', 'codes': [0, 0, 0], 'meta': {'q': 5}}
]

# System flags derived from telemetry (some irrelevant)
system_flags = {
    'overvoltage': any(v > 13.0 for v in telemetry_streams['power']),
    'thermal_alert': max(telemetry_streams['temp_core']) > 75,
    'panel_flux': sum(1 for t in telemetry_streams['temp_panel'] if t > 50),
    'sync_lock': len(telemetry_streams['signal_strength']) % 2 == 0,
    'legacy_mode': False
}

# Decoy function - looks important but unused
def compute_checksum(data):
    chk = 0
    for item in str(data):
        chk ^= ord(item) * 3
    return chk % 1000

# Auxiliary transformation (partial red herring)
transformed_logs = [
    {**entry, 'enhanced': True, 'code_sum': sum(entry['codes'])} 
    for entry in log_entries
]

# Dead code path - never executed
def deprecated_analysis(logs):
    total_risk = 0
    for log in logs:
        total_risk += len(log.get('event', '')) * 10
    return total_risk

# Unused aggregation (misleading intermediate)
avg_power = sum(telemetry_streams['power']) / len(telemetry_streams['power'])
peak_temp = max(telemetry_streams['temp_core'] + telemetry_streams['temp_panel'])

# Real processing begins here
flag_weights = {
    'overvoltage': 100,
    'thermal_alert': 200,
    'sync_lock': 50,
    'legacy_mode': 10
}

# Weighted flag score (used later)
weighted_flag_score = sum(
    flag_weights[flag] for flag in system_flags if system_flags[flag] and flag in flag_weights
)

# Event severity mapping
severity_map = {'OK': 0, 'WARN': 30, 'ERR': 300}

def analyze_pattern(logs, flags):
    base_risk = 0
    pattern_score = 0
    
    # Analyze event sequence
    for i, log in enumerate(logs):
        event = log['event']
        codes = log['codes']
        
        # Direct severity contribution
        base_risk += severity_map[event]
        
        # Code-based risk (only first code matters)
        if codes[0] == 1:
            base_risk += 5
        elif codes[0] >= 3:
            base_risk += 25
        
        # Temporal pattern: ERR following WARN increases impact
        if i > 0 and event == 'ERR' and logs[i-1]['event'] == 'WARN':
            pattern_score += 40
        
        # XOR-based obfuscation check (bitwise distractor)
        meta_q = log['meta']['q']
        if meta_q ^ 2 > 3:  # Always true for q >= 1
            pattern_score += 1
    
    # Nested conditional with decoy arithmetic
    adjustment = 0
    if flags['overvoltage']:
        if flags['thermal_alert']:
            adjustment += 75
        else:
            adjustment += 25
    elif flags['sync_lock']:
        adjustment += 15
    
    # Complex but deterministic computation
    raw_diagnostic = base_risk + pattern_score + adjustment + weighted_flag_score
    
    # Final scaling with truncation (key step)
    final_value = int(raw_diagnostic * 1.1)  # Apply fixed multiplier
    
    # Security hash (unused)
    security_token = ''.join(chr((ord('X') + i) % 90 + 32) for i in range(8))
    
    return final_value

# Execution point of interest
final_diagnostic = analyze_pattern(log_entries, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")