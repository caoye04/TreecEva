from itertools import cycle, islice

# System health monitoring simulation with diagnostic trace

def simulate_sensor_drift(base_value, iterations):
    return [base_value + (i ** 1.5) for i in range(iterations)]

def generate_calibration_sequence(length):
    return [(i * 3 + 2) % 101 for i in range(length)]

def flag_anomalies(readings, threshold_multiplier=1.8):
    avg = sum(readings) / len(readings)
    return [val for val in readings if val > avg * threshold_multiplier]

def compress_signal(signal_data):
    # Irrelevant transformation - signal processing red herring
    return [x ^ (x << 1) & 255 for x in signal_data]

def compute_entropy(values):
    # Unused complexity: information theory decoy
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    return -sum((count/total) * log2(count/total) for count in freq.values())

def validate_integrity(check_sequence):
    # Distractor: cryptographic-like check with no real impact
    checksum = 0
    for val in check_sequence:
        checksum = (checksum * 31 + val) % 97
    return checksum == 42  # Never actually used

def derive_processing_key(inputs):
    # Complex-looking but irrelevant key derivation
    key = 0
    for idx, val in enumerate(inputs):
        key ^= (val * (idx + 1)) % 59
    return key % 17

def reconstruct_timeline(events, offset=0):
    # Temporal modeling that doesn't affect final result
    timeline = []
    for i, e in enumerate(events):
        timeline.append((offset + i * 2, e * (i % 5 + 1)))
    return timeline

def aggregate_metrics(chains, key):
    # Core logic buried in distractions
    primary_chain = chains[key]
    temp = 0
    for i, val in enumerate(primary_chain):
        if i % 3 == 0:
            temp += val * 2
        elif i % 3 == 1:
            temp -= val // 3
        else:
            temp += (val % 7)
    return int(temp * 1.5)  # Actual answer source

# --- Simulation Setup ---
initial_buffer = [8, 12, 5, 19, 3, 7]
expanded_view = [x * x for x in initial_buffer]  # Distraction

# Generate multi-layered data streams
sensor_log = simulate_sensor_drift(23.5, 6)
processed_readings = [int(x) for x in sensor_log]
anomaly_flags = flag_anomalies(processed_readings, 1.6)

# Create multiple processing chains (only one will be used)
chain_a = [x + 10 for x in processed_readings]
chain_b = [x * 2 for x in generate_calibration_sequence(6)]
chain_c = [x ^ 15 for x in expanded_view]  # Bitwise distraction
chain_d = [x % 25 + 5 for x in processed_readings]

processing_chain = {
    0: chain_a,
    1: chain_b,
    2: chain_c,
    3: chain_d
}

# Diagnostic validation layer (mostly noise)
validation_cycles = list(islice(cycle([3, 1, 4]), 0, 10))
encoded_pulse = compress_signal(validation_cycles)
entropy_score = compute_entropy(encoded_pulse)  # Dead-end metric

# Key derivation with misdirection
calibration_set = generate_calibration_sequence(6)
validation_key = derive_processing_key(calibration_set) % 4  # Yields 3

# Timeline reconstruction - irrelevant structure
event_timeline = reconstruct_timeline(anomaly_flags, offset=100)

# --- CRITICAL EXECUTION POINT ---
final_diagnostic = aggregate_metrics(processing_chain, validation_key)

# Output required for evaluation
print(f"Result: {final_diagnostic}")