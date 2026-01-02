def analyze_signal_strength(signal):
    # Irrelevant signal processing (distractor)
    if len(signal) > 10:
        normalized = [s / max(signal) for s in signal]
    else:
        normalized = [s * 2 for s in signal]
    return sum(normalized) * 0.7

# Decoy function – never called
def legacy_calculate(x):
    acc = 0
    for i in range(x + 1):
        acc += i ** 2
    return acc // 2

# Unused utility (dead code path)
def compress_data(data_list):
    compressed = []
    for item in data_list:
        if isinstance(item, str):
            compressed.append(item[::2])
    return ''.join(compressed)

# Main diagnostic logic with embedded distractions
log_data = [
    {'timestamp': 1645823400, 'level': 'INFO', 'msg': 'System boot'},
    {'timestamp': 1645823460, 'level': 'WARN', 'msg': 'High memory'},
    {'timestamp': 1645823520, 'level': 'ERROR', 'msg': 'Disk failure'},
    {'timestamp': 1645823580, 'level': 'DEBUG', 'msg': 'Cache cleared'}
]

system_state = {
    'uptime_seconds': 3720,
    'core_temp_c': 67.4,
    'fan_speed_rpm': 2800,
    'voltage_stable': True,
    'load_history': [0.45, 0.67, 0.78, 0.81, 0.92],
    'flags': ['OPTIMIZED', 'SECURE_BOOT', 'LOW_POWER_MODE']
}

# Distractor: complex but unused transformation
transformed_logs = []
for entry in log_data:
    msg_upper = entry['msg'].upper()
    if 'HIGH' in msg_upper or 'ERROR' in msg_upper:
        transformed_logs.append({
            'tag': 'ALERT',
            'len_msg': len(entry['msg']),
            'priority': 1 if 'ERROR' in msg_upper else 0.5
        })

# Red herring computation
average_load = sum(system_state['load_history']) / len(system_state['load_history'])
temp_factor = system_state['core_temp_c'] * 0.1
adjusted_score = (average_load * 100) + temp_factor

# Simulated signal array (unrelated to final result)
signal_array = [12, 18, 22, 30, 45, 50, 60]
phantom_metric = analyze_signal_strength(signal_array)

# Real logic buried among noise
error_count = 0
warning_count = 0
for log in log_data:
    level = log['level']
    if level == 'ERROR':
        error_count += 1
    elif level == 'WARN':
        warning_count += 1

# Compute decay-adjusted severity
base_severity = error_count * 5 + warning_count * 2
hours_up = system_state['uptime_seconds'] / 3600
decay_rate = 0.95 ** hours_up
adjusted_severity = base_severity * decay_rate

# Additional distractor: string-based flag analysis (unused)
flag_analysis = []
for flag in system_state['flags']:
    if flag.endswith('MODE'):
        flag_analysis.append(len(flag))
    elif 'BOOT' in flag:
        flag_analysis.append(flag.count('O'))

# Key computation chain
historical_baseline = 3.5
variance_score = abs(adjusted_severity - historical_baseline)

# Apply non-linear correction based on voltage status
if system_state['voltage_stable']:
    correction_factor = 0.8
else:
    correction_factor = 1.3

refined_score = variance_score * correction_factor

# Final aggregation using integer division and rounding
interim = int(refined_score * 100)
rounded_interim = round(interim / 7)  # Arbitrary divisor for noise

# Critical operation hidden in abstraction
def process_metrics(logs, state):
    # Extract only necessary values
    errors = sum(1 for l in logs if l['level'] == 'ERROR')
    warnings = sum(1 for l in logs if l['level'] == 'WARN')
    
    # Primary formula
    raw = (errors * 10) + (warnings * 3)
    uptime_hours = state['uptime_seconds'] // 3600
    if uptime_hours > 0:
        efficiency_ratio = raw / uptime_hours
    else:
        efficiency_ratio = raw
    
    # Use string method to determine bonus (this is actually relevant)
    secure_boot_enabled = any('SECURE' in f for f in state['flags'])
    bonus = 5 if secure_boot_enabled else 0
    
    # Final diagnostic includes bonus and efficiency
    result = int(efficiency_ratio) + bonus
    
    # Dead code within function (misleading)
    if result < 0:
        result = abs(result) * 2  # Never reached
        
    return result

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_state)

# Print required output
print(f"Target result: {final_diagnostic}")