import math

# Simulated system telemetry data with mixed signal types
def fetch_telemetry():
    raw_signals = {
        'voltage': [3.3, 3.4, 3.2, 3.5, 3.6],
        'current': [0.8, 0.9, 0.75, 0.83, 0.91],
        'temp_c': [45, 47, 46, 49, 51],
        'timestamp': [1680001, 1680002, 1680003, 1680004, 1680005]
    }
    return raw_signals

# Legacy function - unused but looks relevant
def calculate_power_legacy(signals):
    power_vals = []
    for i in range(len(signals['voltage'])):
        p = signals['voltage'][i] * signals['current'][i] * 1.1  # inefficiency factor
        power_vals.append(round(p, 2))
    return power_vals

# Signal normalization (distractor - not used in final path)
def normalize_signal(data, key):
    min_val, max_val = min(data[key]), max(data[key])
    return [(x - min_val) / (max_val - min_val) for x in data[key]]

# Core diagnostic logic
def detect_anomalies(temps):
    anomalies = []
    baseline = sum(temps) / len(temps)
    for i, t in enumerate(temps):
        if abs(t - baseline) > 3 and t > 48:
            anomalies.append(i)
    return anomalies

# Red herring: complex frequency analysis (never called)
def analyze_frequency_domain(signal):
    fft_magnitude = []
    for i in range(len(signal)):
        val = 0
        for j in range(len(signal)):
            angle = 2 * math.pi * i * j / len(signal)
            val += signal[j] * math.cos(angle)
        fft_magnitude.append(abs(val))
    normalized_fft = [round(x / len(signal), 3) for x in fft_magnitude]
    threshold = sum(normalized_fft) / len(normalized_fft)
    peaks = [i for i, x in enumerate(normalized_fft) if x > threshold * 1.5]
    return peaks

# Misleading intermediate processing
telemetry_data = fetch_telemetry()
scaled_temp = normalize_signal(telemetry_data, 'temp_c')
legacy_power = calculate_power_legacy(telemetry_data)

# Unused diagnostic flags
diag_flags = {
    'overvoltage': any(v > 3.5 for v in telemetry_data['voltage']),
    'overcurrent': any(c > 0.9 for c in telemetry_data['current']),
    'thermal_spike': any(t > 50 for t in telemetry_data['temp_c'])
}

# Real-time event buffer (simulated)
event_buffer = [{'type': 'temp_rise', 'value': t} for t in telemetry_data['temp_c'] if t > 46]
buffer_sum = sum(e['value'] for e in event_buffer)

# Critical state tracker (partially relevant)
system_state = {
    'health_score': 92,
    'active_alarms': [],
    'last_update': 1680005,
    'version': '2.1.5'
}

# Log entry generator with dictionary operations and list comprehensions
def generate_log_entries(telemetry, state):
    timestamps = telemetry['timestamp']
    temps = telemetry['temp_c']
    
    # Complex dictionary construction with filtering
    logs = [
        {
            'ts': ts,
            't': temp,
            'risk': 'high' if temp > 48 else 'normal',
            'delta': round(temp - 45 - (ts - 1680001) * 0.5, 2)
        }
        for ts, temp in zip(timestamps, temps) if (ts % 2 == 1)
    ]
    
    # Additional metadata injection
    for log in logs:
        log['diagnostics'] = {
            'stability': 'stable' if log['delta'] < 2 else 'unstable',
            'priority': 1 if log['risk'] == 'high' else 0
        }
    
    # Irrelevant transformation
    reversed_logs = logs[::-1]
    sorted_by_delta = sorted(reversed_logs, key=lambda x: x['delta'])
    
    return logs  # Original order is used

# Main metric aggregator
def aggregate_metrics(log_entries, sys_state):
    # Extract high-risk entries
    high_risk = [e for e in log_entries if e['risk'] == 'high']
    
    # Compute weighted impact
    impact_weights = []
    for entry in high_risk:
        base_weight = entry['t'] * 0.3
        priority_bonus = entry['diagnostics']['priority'] * 5
        stability_penalty = 10 if entry['diagnostics']['stability'] == 'unstable' else 0
        total_weight = base_weight + priority_bonus - stability_penalty
        impact_weights.append(max(total_weight, 0))
    
    # Aggregate with health score modulation
    base_impact = sum(impact_weights)
    modulation_factor = sys_state['health_score'] / 100.0
    
    # Secondary correction based on count
    anomaly_count = len(high_risk)
    correction_term = anomaly_count ** 2 * 0.8
    
    # Final non-linear transformation
    raw_value = (base_impact * modulation_factor) + correction_term
    final_value = int(math.floor(raw_value * 1.25))
    
    # Dead code branch - looks important but unused
    if final_value > 100:
        final_value = 99  # capped for legacy display
    
    return final_value

# Execute main workflow
log_entries = generate_log_entries(telemetry_data, system_state)
final_diagnostic = aggregate_metrics(log_entries, system_state)

# Print result
print(f"Target result: {final_diagnostic}")