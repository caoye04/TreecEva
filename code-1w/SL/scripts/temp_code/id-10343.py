import math

# Simulated sensor data processing with diagnostic analysis
def collect_telemetry():
    raw_readings = [24, 18, 57, 43, 29, 71, 65, 38]
    calibration_offset = 1.05
    adjusted = [x * calibration_offset for x in raw_readings]
    return adjusted

# Irrelevant helper: format timestamp (dead utility)
def format_timestamp(ts):
    hours = int(ts // 3600)
    mins = int((ts % 3600) // 60)
    secs = int(ts % 60)
    return f'{hours:02}:{mins:02}:{secs:02}'

# Unused transformation path
def legacy_normalize(data):
    max_val = max(data)
    return [round(x / max_val, 4) for x in data]  # never called

# Bit manipulation red herring
def scramble_bits(value):
    if value < 32:
        return (value << 3) & 0xFF
    else:
        return (value >> 2) ^ 0xAA

# Distractor: complex but unused entropy estimator
def shannon_entropy(data):
    total = sum(data)
    probabilities = [x / total for x in data if x > 0]
    return -sum(p * math.log2(p) for p in probabilities)

# Real logic begins here — pattern analyzer using set and dict operations
def build_frequency_map(seq):
    freq_map = {}
    for item in seq:
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

def detect_anomalies(readings):
    threshold = sum(readings) / len(readings) + 2.5
    anomalies = []
    for i, val in enumerate(readings):
        if val > threshold and i % 2 == 1:
            anomalies.append(i)
    return anomalies

def generate_state_registry(anomaly_indices):
    registry = {}
    states = ['ERROR', 'OK', 'WARN', 'FAULT']
    for i in range(8):
        if i in anomaly_indices:
            registry[i] = states[(i * 3) % 4]
        else:
            registry[i] = states[i % 4]
    return registry

# Core function that contributes to final answer
def compute_checksum(values):
    checksum = 0
    for v in values:
        temp = int(v)
        while temp:
            checksum += (temp & 1)
            temp >>= 1
    return checksum

def filter_critical_events(freq_dict):
    critical_set = set()
    for k, v in freq_dict.items():
        if v >= 2 and k > 40:
            critical_set.add(k)
    return critical_set

def derive_entropy_vector(buffer):
    vector = []
    for x in buffer:
        if x % 2 == 0:
            vector.append(int(math.sqrt(x)) if x > 0 else 0)
        else:
            vector.append(int(math.log2(x)) if x > 1 else 0)
    return vector

def analyze_pattern(buffer):
    # Step 1: Build frequency map
    freq = build_frequency_map(buffer)
    
    # Step 2: Extract critical events as set
    critical_events = filter_critical_events(freq)
    
    # Step 3: Derive entropy-based features
    entropy_features = derive_entropy_vector(list(critical_events)) if critical_events else [0]
    
    # Step 4: Compute checksum from original buffer
    base_checksum = compute_checksum(buffer)
    
    # Step 5: Create state registry based on fake anomaly detection
    anomalies = detect_anomalies(buffer)
    system_states = generate_state_registry(anomalies)
    active_errors = sum(1 for s in system_states.values() if s in {'ERROR', 'FAULT'})
    
    # Step 6: Apply dictionary lookup chain
    mapping_key = len(critical_events) + active_errors
    transform_map = {0: 5, 1: 3, 2: 7, 3: 4, 4: 8, 5: 6}
    factor = transform_map.get(mapping_key, 2)
    
    # Step 7: Combine via weighted contribution
    entropy_sum = sum(entropy_features)
    intermediate = (base_checksum * factor) + entropy_sum
    
    # Step 8: Final adjustment using decimal precision
    final_score = round(intermediate + 0.175, 3)
    
    # Red herring: irrelevant bit scrambling
    decoy_result = 0
    for val in buffer[:3]:
        decoy_result += scramble_bits(int(val))
    
    # Final result
    return int(final_score)

# Main execution flow
if __name__ == '__main__':
    # Collect and preprocess sensor data
    sensor_data = collect_telemetry()
    processed_data = [max(1, int(x)) for x in sensor_data]  # sanitize

    # Dead code path: formatting unused timestamps
    timestamps = [12345, 12346, 12347]
    time_labels = [format_timestamp(t) for t in timestamps]  # irrelevant

    # Normalize (not used in main path)
    normalized = legacy_normalize(processed_data)

    # Real pipeline
    entropy_buffer = [x + (i * 2) for i, x in enumerate(processed_data)]
    final_diagnostic = analyze_pattern(entropy_buffer)
    
    # Output target result
    print(f"Result: {final_diagnostic}")