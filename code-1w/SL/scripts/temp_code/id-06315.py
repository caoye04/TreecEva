import math

# Simulated system telemetry data
telemetry_data = {
    'sensor_readings': [0.85, 0.92, 0.78, 0.65, 0.95, 0.88],
    'timestamp_flags': [1, 0, 1, 1, 0, 1],
    'checksums': [234, 567, 891, 234, 567, 891]
}

# Historical performance logs (irrelevant to final result)
historical_stats = {
    'peak_load': 98765,
    'uptime_hours': 4382,
    'error_count': 12,
    'last_maintenance': '2023-11-05',
    'version': 'v2.3.1'
}

# Auxiliary mapping for deprecated subsystems (distractor)
legacy_subsystem_map = {
    'alpha': 'A1', 'beta': 'B2', 'gamma': 'G3',
    'delta': 'D4', 'epsilon': 'E5'
}

# Current active modules (some are unused)
active_modules = ['core_engine', 'io_handler', 'scheduler', 'network_bridge']

# Irrelevant string processing (red herring)
def analyze_version(version_str):
    parts = version_str.split('.')
    major = int(parts[0][1:])  # strip 'v'
    minor = int(parts[1])
    patch = int(parts[2])
    return major * 100 + minor * 10 + patch

# Unused recursive function (dead code path)
def calculate_recursive_depth(n):
    if n <= 1:
        return 1
    return n + calculate_recursive_depth(n - 2)

# Misleading diagnostic check (never called)
def validate_checksums(data_list):
    total = 0
    for val in data_list:
        total = (total + val) % 997
    return total

# Core processing functions
def filter_valid_readings(readings, flags):
    return [r for r, f in zip(readings, flags) if f == 1]

def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return round(entropy, 6)

def detect_anomalies(values):
    mean_val = sum(values) / len(values)
    anomalies = [v for v in values if abs(v - mean_val) > 0.1 * mean_val]
    return len(anomalies)

def build_log_entry(timestamp, value, category='INFO'):
    entry = f"[{timestamp}] {category}: System metric={value:.4f}"
    return entry.upper().replace('SYSTEM', 'CORE')

# Main processing pipeline
def process_metrics(entries, state):
    # Extract relevant sensor data
    raw_readings = telemetry_data['sensor_readings']
    flags = telemetry_data['timestamp_flags']
    
    # Filter valid entries (key step)
    valid_readings = filter_valid_readings(raw_readings, flags)
    
    # Compute statistical metrics (intermediate steps)
    avg_reading = sum(valid_readings) / len(valid_readings)
    squared_dev = sum((x - avg_reading) ** 2 for x in valid_readings)
    variance = squared_dev / len(valid_readings)
    std_dev = math.sqrt(variance)
    
    # Generate log entries (side effect, some distractor usage)
    logs = []
    for i, val in enumerate(valid_readings):
        ts = 1698765000 + i * 60
        log_line = build_log_entry(ts, val, 'DEBUG')
        logs.append(log_line)
    
    # Determine anomaly count
    anomaly_count = detect_anomalies(valid_readings)
    
    # Compute entropy of valid readings
    entropy_value = compute_entropy(valid_readings)
    
    # Apply correction factor based on system state (critical path)
    if state['operational_mode'] == 'high_throughput':
        adjustment = 1.5
    elif state['operational_mode'] == 'low_power':
        adjustment = 0.7
    else:
        adjustment = 1.0  # default mode
    
    # Final diagnostic computation (target result)
    base_score = entropy_value * 1000
    adjusted_score = base_score * adjustment
    final_score = adjusted_score - (anomaly_count * 50)
    
    # Decoy operations (irrelevant)
    temp_checksum = 0
    for c in telemetry_data['checksums']:
        temp_checksum ^= c
    temp_checksum %= 10000
    
    # Another decoy: string manipulation with no effect
    version_code = analyze_version(historical_stats['version'])
    version_flag = version_code & 0xFF
    
    # Final assignment (answer depends only on core logic)
    final_diagnostic = int(round(final_score))
    
    return final_diagnostic

# System state configuration (affects adjustment factor)
system_state = {
    'operational_mode': 'default',
    'load_level': 74,
    'temperature': 68,
    'fan_speed': 2000
}

# Generate log entries list (used in processing)
log_entries = []
for i in range(len(telemetry_data['sensor_readings'])):
    if telemetry_data['timestamp_flags'][i]:
        log_entries.append(f"entry_{i}")

# Execute critical statement
def main():
    final_diagnostic = process_metrics(log_entries, system_state)
    print(f"Result: {final_diagnostic}")

main()