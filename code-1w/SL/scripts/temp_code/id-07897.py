import math

# System telemetry data structure
telemetry_stream = [
    {'timestamp': 1648523400, 'power_draw': 23.5, 'temp_core': 67, 'status_flag': 0},
    {'timestamp': 1648523460, 'power_draw': 24.1, 'temp_core': 69, 'status_flag': 1},
    {'timestamp': 1648523520, 'power_draw': 22.8, 'temp_core': 65, 'status_flag': 0},
    {'timestamp': 1648523580, 'power_draw': 25.3, 'temp_core': 72, 'status_flag': 1},
]

# Auxiliary diagnostic thresholds (irrelevant to final result)
thresholds = {
    'voltage_stability': 4.2,
    'max_cycles_per_sec': 9800,
    'thermal_limit_safe': 85,
    'bandwidth_capacity': 1024
}

# Legacy checksum function (unused red herring)
def calculate_legacy_checksum(data):
    checksum = 0
    for item in data:
        checksum ^= int(item['power_draw'] * 10)
    return checksum % 17

# Simulate sensor drift compensation (distractor logic)
calibration_offset = 0.7
adjusted_readings = []
for entry in telemetry_stream:
    adjusted_entry = entry.copy()
    adjusted_entry['power_draw'] += calibration_offset
    adjusted_entry['temp_core'] += 1  # Simulated correction
    adjusted_readings.append(adjusted_entry)

# Flag analysis with bit manipulation decoy
event_mask = 0
for idx, entry in enumerate(telemetry_stream):
    if entry['status_flag']:
        event_mask |= (1 << idx)
event_mask = event_mask ^ 0b1111  # Irrelevant transformation

# Primary log processing function
def extract_critical_events(logs):
    critical = []
    for log in logs:
        if log['temp_core'] > 70 and log['power_draw'] > 24.0:
            critical.append(log)
    return critical

# Secondary filter using dictionary accumulation (partially relevant)
def accumulate_metrics(events):
    metrics = {
        'total_power_surplus': 0.0,
        'peak_temp_deviation': 0,
        'event_count': len(events)
    }
    baseline_power = 20.0
    baseline_temp = 60
    for e in events:
        metrics['total_power_surplus'] += e['power_draw'] - baseline_power
        deviation = e['temp_core'] - baseline_temp
        if deviation > metrics['peak_temp_deviation']:
            metrics['peak_temp_deviation'] = deviation
    return metrics

# Complex conditional scoring logic
def compute_integrity_score(entries, flags):
    critical_events = extract_critical_events(entries)
    
    # Distractor: unused path based on flag length
    if len(flags) > 10:
        return -999  # Dead code path
    
    if not critical_events:
        return 100.0  # Perfect score if no critical events
    
    # Actual computation begins here
    metrics = accumulate_metrics(critical_events)
    
    base_score = 100.0
    
    # Deduct based on event count (10 points per event)
    base_score -= metrics['event_count'] * 10
    
    # Deduct based on total power surplus (0.5 point per unit)
    base_score -= metrics['total_power_surplus'] * 0.5
    
    # Apply non-linear penalty for peak temperature deviation
    temp_penalty = math.pow(metrics['peak_temp_deviation'], 1.5)
    base_score -= temp_penalty
    
    # Conditional adjustment based on time clustering (unused due to single window)
    timestamps = [e['timestamp'] for e in critical_events]
    if len(timestamps) > 1:
        intervals = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
        if all(t < 60 for t in intervals):
            base_score -= 15  # Cluster penalty (not triggered)
    
    return round(base_score, 4)

# Misleading auxiliary analysis (dead weight)
def analyze_temp_trend(data):
    temps = [d['temp_core'] for d in data]
    avg_temp = sum(temps) / len(temps)
    variance = sum((t - avg_temp) ** 2 for t in temps) / len(temps)
    return {'average': avg_temp, 'variance': variance, 'warning_level': 'moderate'}

# Unused statistical summary
temp_analysis = analyze_temp_trend(telemetry_stream)

# Flags with decoy data (only length matters, content irrelevant)
system_flags = [True, False, True, True, False, False, True, True, True]

# Key execution point
final_diagnostic = compute_integrity_score(telemetry_stream, system_flags)

# Additional distraction: simulate log compression
compressed_size = sum(len(str(v)) for log in telemetry_stream for v in log.values())
compression_ratio = len(str(telemetry_stream)) / compressed_size if compressed_size else 0

# Output the target result
print(f"Result: {final_diagnostic}")