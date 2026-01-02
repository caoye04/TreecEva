import math

# Simulated telemetry data from a distributed sensor network
def fetch_telemetry():
    return [
        {'id': 'S1', 'readings': [23.5, 24.1, 22.9, 25.0], 'status': 'active'},
        {'id': 'S2', 'readings': [19.2, 20.0, 18.7, 19.8], 'status': 'active'},
        {'id': 'S3', 'readings': [31.3, 32.0, 30.8, 31.7], 'status': 'active'},
        {'id': 'S4', 'readings': [], 'status': 'inactive'}
    ]

# Legacy function – not actually used in current logic (red herring)
def calculate_legacy_score(data):
    total = 0
    for entry in data:
        if entry['status'] == 'active':
            total += sum(entry['readings']) * 0.85
    return int(total) // 4

# Misleading utility – computes irrelevant average
def compute_thermal_baseline(sensors):
    temps = []
    for s in sensors:
        if s['readings']:
            avg = sum(s['readings']) / len(s['readings'])
            temps.append(avg + 2.5)  # artificial offset
    return sum(temps) / len(temps) if temps else 0

# Unused helper – decoy function with plausible name
def normalize_readings(readings_list):
    if not readings_list:
        return []
    max_val = max(readings_list)
    return [x / max_val for x in readings_list]

# Core processing pipeline
def extract_features(telemetry):
    features = {}
    for sensor in telemetry:
        sensor_id = sensor['id']
        readings = sensor['readings']
        if sensor['status'] != 'active' or len(readings) == 0:
            features[sensor_id] = {'mean': 0, 'variance': 0, 'peak': 0}
            continue
        mean = sum(readings) / len(readings)
        variance = sum((x - mean) ** 2 for x in readings) / len(readings)
        peak = max(readings)
        features[sensor_id] = {
            'mean': round(mean, 2),
            'variance': round(variance, 3),
            'peak': peak
        }
    return features

# System state tracker (simulated)
class SystemState:
    def __init__(self):
        self.timestamp = 1678886400
        self.mode = 'diagnostic'
        self.health_index = 87.3
        self.alert_count = 2
        self.config = {'threshold': 28.0, 'hysteresis': 1.5}

# String-based diagnostic signature generator (distractor)
def generate_signature(state: SystemState):
    parts = []
    parts.append(f"SYS-{int(state.health_index)}")
    parts.append(f"M{state.alert_count}")
    mode_code = ''.join([c.lower() if i % 2 else c.upper() for i, c in enumerate(state.mode)])
    parts.append(mode_code)
    return '-'.join(parts) + f"-{state.timestamp % 1000}"

# Main metric processor – critical path
def process_metrics(sensor_log, sys_state):
    # Extract meaningful features
    extracted = extract_features(sensor_log)
    
    # Irrelevant string manipulation (distractor)
    sig = generate_signature(sys_state)
    tokens = sig.split('-')
    token_lengths = [len(t) for t in tokens]
    avg_token_len = sum(token_lengths) / len(token_lengths)
    
    # Compute composite temperature baseline (unused)
    _ = compute_thermal_baseline(sensor_log)
    
    # Real work begins: find all active sensors with peak > threshold
    threshold = sys_state.config['threshold']
    peaks = []
    for key, data in extracted.items():
        if data['peak'] > 0 and data['peak'] >= threshold:
            peaks.append(data['peak'])
    
    # Calculate anomaly score based on excess over threshold
    excess_values = []
    for p in peaks:
        if p > threshold:
            excess = p - threshold
            excess_values.append(excess)
    
    # Secondary filter: only consider sensors where mean reading also exceeds adjusted threshold
    stable_excess = []
    for key, data in extracted.items():
        adjusted_threshold = threshold - sys_state.config['hysteresis']
        if data['mean'] > adjusted_threshold and data['peak'] in peaks:
            stable_excess.append(data['peak'])
    
    # Final diagnostic is the sum of stable excess peaks, multiplied by alert count
    base_sum = sum(stable_excess)
    final_diagnostic = int(base_sum * sys_state.alert_count)
    
    # Dead code path – never executed due to current state
    if sys_state.mode == 'standby':
        fallback = calculate_legacy_score(sensor_log)
        final_diagnostic = fallback if fallback > 0 else final_diagnostic
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Initialization and execution
telemetry_data = fetch_telemetry()
system_status = SystemState()

# Key statement
final_diagnostic = process_metrics(telemetry_data, system_status)