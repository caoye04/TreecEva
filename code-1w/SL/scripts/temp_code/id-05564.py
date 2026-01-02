from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    'CPU_TEMP:78,FAN_SPEED:1500,VOLTAGE:3.2,STATUS:OK',
    'CPU_TEMP:85,FAN_SPEED:1600,VOLTAGE:3.3,STATUS:WARNING',
    'CPU_TEMP:92,FAN_SPEED:1800,VOLTAGE:3.4,STATUS:WARNING',
    'CPU_TEMP:99,FAN_SPEED:2000,VOLTAGE:3.5,STATUS:CRITICAL',
    'CPU_TEMP:88,FAN_SPEED:1700,VOLTAGE:3.3,STATUS:WARNING'
]

# Irrelevant statistical counters (distractor)
cpu_mode_count = defaultdict(int)
voltage_transitions = []
spurious_flag_log = set()

# Core processing variables
temperature_readings = []
fan_response_curve = []
system_health_bins = [0] * 4

# Parse and extract relevant metrics
for entry in telemetry_stream:
    parts = entry.split(',')
    kv = {p.split(':')[0]: p.split(':')[1] for p in parts}
    
    temp = int(kv['CPU_TEMP'])
    fan = int(kv['FAN_SPEED'])
    voltage = float(kv['VOLTAGE'])
    status = kv['STATUS']
    
    temperature_readings.append(temp)
    fan_response_curve.append(fan / max(1, temp))  # normalized response
    
    # Bin health levels: 0=OK, 1=WARNING, 2=CRITICAL, 3=UNKNOWN
    if status == 'OK':
        system_health_bins[0] += 1
    elif status == 'WARNING':
        system_health_bins[1] += 1
    elif status == 'CRITICAL':
        system_health_bins[2] += 1
    else:
        system_health_bins[3] += 1

    # Distractor: collect mode-like behavior (not used later)
    rounded_temp = (temp // 5) * 5
    cpu_mode_count[rounded_temp] += 1

    # Distractor: track voltage changes
    voltage_transitions.append(voltage)

# Dead code path - never invoked (red herring)
def calculate_stability_index(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.exp(-variance)

# Unused transformation (misleading intermediate result)
transformed_temps = [math.log(t + 273) for t in temperature_readings]
avg_transformed = sum(transformed_temps) / len(transformed_temps)

# Simulate flag accumulation from distributed sensors (some irrelevant)
sensor_flags = {
    'overheat_alert': max(temperature_readings) > 95,
    'fan_anomaly': any(f < 1550 for f in [1500,1600,1800,2000,1700]),
    'voltage_drift': abs(voltage_transitions[-1] - voltage_transitions[0]) > 0.2,
    'load_spike': True,  # Simulated
    'clock_throttling': False
}

# Additional decoy structure
historical_analysis = {
    'peak_temp_rate': (max(temperature_readings) - min(temperature_readings)) / 4,
    'expected_failures': 0.0,
    'recovery_count': 2
}

# Real processing begins here — aggregate logs
log_summary = {
    'avg_temp': sum(temperature_readings) / len(temperature_readings),
    'max_temp': max(temperature_readings),
    'total_entries': len(temperature_readings),
    'warning_count': system_health_bins[1],
    'critical_count': system_health_bins[2]
}

# Extract system-wide flags
system_flags = []
if sensor_flags['overheat_alert']:
    system_flags.append('OVHT')
if sensor_flags['voltage_drift']:
    system_flags.append('VDRIFT')
if sensor_flags['fan_anomaly']:
    system_flags.append('FAN_ERR')
if log_summary['critical_count'] >= 1:
    system_flags.append('SEVERE')

# Auxiliary function — string manipulation red herring
def analyze_flag_pattern(flags):
    joined = ''.join(sorted(set(flags)))
    char_freq = Counter(joined)
    entropy = 0
    for freq in char_freq.values():
        p = freq / len(joined)
        entropy -= p * math.log(p) if p > 0 else 0
    return entropy

# Another decoy: unused prediction model
predicted_failure_window = None
if 'OVHT' in system_flags and 'SEVERE' in system_flags:
    predicted_failure_window = '0-2h'
else:
    predicted_failure_window = '24h+'

# Critical computation chain
baseline_risk = 10
if log_summary['avg_temp'] > 85:
    baseline_risk += 15
if log_summary['max_temp'] > 95:
    baseline_risk += 25
if log_summary['warning_count'] >= 2:
    baseline_risk += 10
if 'SEVERE' in system_flags:
    baseline_risk += 30

adjustment_factor = 1.0
if 'OVHT' in system_flags:
    adjustment_factor *= 1.2
if 'VDRIFT' in system_flags:
    adjustment_factor *= 1.15
if len(system_flags) >= 3:
    adjustment_factor *= 0.9  # instability reduces predictability

# Secondary adjustment via distractor-derived value (but not really)
flag_entropy = analyze_flag_pattern(system_flags)
if flag_entropy > 0.5:
    adjustment_factor *= 1.05  # minor boost

# Final diagnostic calculation
raw_score = baseline_risk * adjustment_factor
final_diagnostic = int(round(raw_score + (log_summary['total_entries'] * 2)))

# Output target result
Target result: {final_diagnostic}