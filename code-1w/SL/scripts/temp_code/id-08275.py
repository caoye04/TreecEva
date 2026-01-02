from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'sensor': 'temp', 'value': 45, 'status': 'OK', 'timestamp': 1001},
    {'sensor': 'pressure', 'value': 1013, 'status': 'OK', 'timestamp': 1002},
    {'sensor': 'temp', 'value': 52, 'status': 'WARN', 'timestamp': 1003},
    {'sensor': 'flow', 'value': 88, 'status': 'OK', 'timestamp': 1004},
    {'sensor': 'pressure', 'value': 990, 'status': 'OK', 'timestamp': 1005},
    {'sensor': 'temp', 'value': 61, 'status': 'ALERT', 'timestamp': 1006},
    {'sensor': 'flow', 'value': 45, 'status': 'WARN', 'timestamp': 1007},
    {'sensor': 'temp', 'value': 58, 'status': 'OK', 'timestamp': 1008}
]

# Irrelevant helper function (distractor)
def analyze_frequency(signal):
    magnitude = 0
    for i in range(len(signal)):
        magnitude += signal[i] * math.sin(i * 0.5)
    return round(magnitude, 3)

# Unused transformation map (dead code path)
sensor_normalization_map = {
    'temp': lambda x: (x - 32) / 1.8,
    'pressure': lambda x: x * 0.75,
    'flow': lambda x: x ** 0.5
}

# Misleading intermediate diagnostic (red herring)
current_health_index = 0.87
projected_stress_factor = 3.14159

# Real processing begins here
def extract_readings(data, sensor_type):
    return [entry['value'] for entry in data if entry['sensor'] == sensor_type]

def compute_anomaly_score(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    outliers = [v for v in values if abs(v - mean_val) > 1.5 * std_dev]
    return len(outliers), std_dev

def build_status_trace(data):
    trace = defaultdict(list)
    for entry in data:
        trace[entry['status']].append(entry['value'])
    return trace

def calculate_entropy(status_count):
    total = sum(status_count.values())
    entropy = 0
    for count in status_count.values():
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def flag_critical_sequence(values, threshold=55, window=3):
    for i in range(len(values) - window + 1):
        if all(v > threshold for v in values[i:i+window]):
            return True
    return False

def derive_system_phase(temp_vals, pressure_vals):
    temp_trend = 'rising' if temp_vals[-1] > temp_vals[0] else 'stable'
    pressure_delta = pressure_vals[-1] - pressure_vals[0]
    if pressure_delta < -20:
        return 'degradation'
    return temp_trend

def aggregate_diagnostics(metrics):
    base_score = metrics['anomalies'] * -10
    base_score += metrics['entropy'] * 25
    if metrics['critical_sequence']:
        base_score -= 15
    if metrics['phase'] == 'degradation':
        base_score -= 20
    return int(base_score)

def process_metrics(log_data, system_state):
    # Extract relevant sensor data
    temp_readings = extract_readings(log_data, 'temp')
    pressure_readings = extract_readings(log_data, 'pressure')
    
    # Compute core statistics
    anomaly_count, deviation = compute_anomaly_score(temp_readings)
    
    # Build status distribution
    status_log = build_status_trace(log_data)
    status_counter = Counter(dict(status_log))
    entropy_score = calculate_entropy(status_counter)
    
    # Check for dangerous patterns
    has_critical_run = flag_critical_sequence(temp_readings, threshold=50, window=2)
    
    # Determine operational phase
    phase = derive_system_phase(temp_readings, pressure_readings)
    
    # Compile metrics (some fields are red herrings)
    diagnostic_metrics = {
        'anomalies': anomaly_count,
        'entropy': entropy_score,
        'critical_sequence': has_critical_run,
        'phase': phase,
        'deviation': deviation,  # unused in final score
n        'readings_count': len(temp_readings),  # distractor
        'system_mode': system_state.get('mode', 'unknown')  # irrelevant
    }
    
    # Final computation
    final_score = aggregate_diagnostics(diagnostic_metrics)
    
    # Secondary adjustment (looks important but isn't used)
    safety_margin = 100 - abs(final_score) if final_score < 0 else 100
    
    # Actual result
    final_diagnostic = (final_score * 2) + 17
    
    return final_diagnostic

# System state with decoy fields
system_state = {
    'mode': 'high_throughput',
    'uptime': 1247,
    'version': '2.8.1',
    'debug_enabled': False,
    'last_reboot_cause': 'maintenance'
}

# Main execution flow
log_data = telemetry_stream

# Spurious pre-processing (irrelevant)
decoded_signals = [entry['value'] % 128 for entry in log_data if entry['sensor'] == 'temp']
frequency_analysis = analyze_frequency(decoded_signals)

# Key statement
final_diagnostic = process_metrics(log_data, system_state)

# Output result
print(f"Result: {final_diagnostic}")