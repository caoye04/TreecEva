def analyze_system_health(health_data, weights):
    cumulative_score = 0
    for i, (metric, value) in enumerate(health_data.items()):
        if i % 2 == 0:
            cumulative_score += value * weights.get(metric, 1.0)
        else:
            cumulative_score -= value * 0.5
    return cumulative_score

# Irrelevant helper (dead function - distractor)
def encrypt_log(data):
    encrypted = ''
    for char in str(data):
        encrypted += chr(ord(char) ^ 7)
    return encrypted

# Another decoy: fake anomaly detection with no real impact
class AnomalyDetector:
    def __init__(self, sensitivity):
        self.sensitivity = sensitivity
        self.history = []

    def check(self, val):
        self.history.append(val > self.sensitivity * 2)
        return False  # Always returns False (misleading)

# Unused data structure (distractor)
system_protocols = {
    'TCP': {'port': 80, 'active': True},
    'UDP': {'port': 53, 'active': True},
    'ICMP': {'port': None, 'active': False}
}

# Real input data
log_entries = {
    'cpu_load': 78,
    'memory_usage': 2048,
    'disk_io': 150,
    'network_in': 980,
    'temperature': 67
}

system_thresholds = {
    'critical': 90,
    'warning': 75,
    'info': 50
}

weights = {
    'cpu_load': 1.2,
    'memory_usage': 0.8,
    'disk_io': 0.6,
    'network_in': 0.4,
    'temperature': 1.0
}

# Fake signal processor (unused but plausible)
def process_signal_stream(stream, sample_rate=44100):
    magnitude = 0
    for s in stream:
        magnitude += abs(s) / sample_rate
    return magnitude * 1000

# Simulated sensor array (red herring)
sensor_grid = [[i*j + 2 for j in range(5)] for i in range(5)]
grid_checksum = sum(sum(row) for row in sensor_grid) // 10

# Decoy list for zip usage (partially relevant)
timestamps = [1634567890, 1634567891, 1634567892, 1634567893, 1634567894]
names = ['sensor_A', 'sensor_B', 'sensor_C', 'sensor_D', 'sensor_E']

# Misleading intermediate: looks important but isn't used in final result
baseline_readings = {name: (idx * 17) % 100 for idx, name in enumerate(names)}
combined_telemetry = dict(zip(timestamps, zip(names, baseline_readings.values())))

# Core processing function
def process_metrics(entries, thresholds):
    temp_result = 0
    adjustment_factor = 0.1
    
    # Use enumerate and zip (required features)
    for idx, (key, val) in enumerate(entries.items()):
        # Conditional branching and logical operations
        is_critical = val > thresholds['critical']
        is_warning = val > thresholds['warning'] and not is_critical
        priority_boost = 5 if is_critical else (2 if is_warning else 0)
        
        # Bit manipulation as noise (shifts and XOR - distractor logic)
        obfuscated = (val << 1) ^ 3
        deobf = (obfuscated ^ 3) >> 1  # Recovers val, but unused
        
        # Only even-indexed keys contribute positively
        if idx % 2 == 0:
            temp_result += val + priority_boost
        else:
            temp_result -= val * adjustment_factor
    
    # Nested conditionals with short-circuiting
    if temp_result > 200 and (thresholds.get('critical') or True):
        temp_result *= 0.95
    elif temp_result < 100 or not False:
        temp_result += 10

    # Dictionary operations (required): transformation
    inverted = {v: k for k, v in entries.items()}
    duplicate_check = len(inverted) == len(entries)  # Always true
    
    # Final computation chain
    raw_total = sum(entries.values())
    index_compound = sum(i for i, _ in enumerate(entries))  # 0+1+2+3+4 = 10
    
    # Key line: this is where final_diagnostic is set
    final_diagnostic = int((temp_result + raw_total * 0.1) - index_compound)
    
    # Dead code branch (never reached due to return)
    if False:
        backup = analyze_system_health(entries, weights)
        final_diagnostic = max(final_diagnostic, backup)
    
    return final_diagnostic

# Execution flow
anomaly_detector = AnomalyDetector(sensitivity=0.7)
detector_status = anomaly_detector.check(42)  # Always False

# Signal processing call with dummy data (distractor)
fake_signal = [-1.5, 2.3, 0.0, -4.1]
signal_magnitude = process_signal_stream(fake_signal)

# Actual target execution
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Target result: {final_diagnostic}")