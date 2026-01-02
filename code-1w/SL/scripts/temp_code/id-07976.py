import math

# Simulated sensor array diagnostics with embedded logic validation
def analyze_sensor_node(node_id, readings):
    if len(readings) < 3:
        return 0
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance)

# Irrelevant helper: computes geometric mean (not used in final result)
def geo_mean(data):
    product = 1
    for x in data:
        product *= x
    return product ** (1 / len(data)) if data else 0

# Misleading preprocessing chain that appears important but leads to dead end
def preprocess_signal(raw_signal):
    filtered = [x for x in raw_signal if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    transformed = [round(x * 100) for x in normalized]
    return transformed

# Core logic: bit manipulation masked as signal processing
def extract_timing_pattern(sequence):
    accumulated = 0
    for val in sequence:
        accumulated ^= (val << 1) | (val >> 2)
    return accumulated & 0xFF

# Decoy function that looks like it's part of the pipeline but isn't called
def compute_entropy(vector):
    total = 0
    for v in vector:
        if v != 0:
            total -= v * math.log(v)
    return total

# High-level orchestration with red herring parameters
def validate_system_integrity(nodes_data, threshold=0.15, mode='strict'):
    scores = []
    for node_id, data in nodes_data.items():
        noise_level = analyze_sensor_node(node_id, data)
        score = int(noise_level < threshold)
        scores.append(score)
    return sum(scores)

# Unused recursive structure to distract from linear flow
def traverse_hierarchy(index, depth):
    if depth == 0:
        return index % 7
    return traverse_hierarchy(index + 1, depth - 1) + traverse_hierarchy(index - 1, depth - 2) if depth > 1 else 0

# Lambda-based dispatcher (actually used)
diagnostic_router = lambda code, seq: (
    (code * seq[0]) ^ (seq[-1] + len(seq))
) % 891

# Primary data inputs (simulated telemetry)
telemetry_stream = [17, 23, 19, 29, 23, 31]
node_diagnostics = {
    'A1': [0.12, 0.14, 0.13],
    'B2': [0.21, 0.19, 0.22],
    'C3': [0.11, 0.10, 0.13]
}

# Dead-end transformation path
processed_signal = preprocess_signal(telemetry_stream)
signal_checksum = sum(processed_signal) * 7  # Distractor variable

# Real computation begins here — obscured by prior noise
base_metric = extract_timing_pattern(telemetry_stream)
logic_signature = base_metric + 33  # Key intermediate value

# Multiple assignments and unpacking to increase cognitive load
calibration_offsets = [7, 11, 13, 17]
alpha, beta, gamma, delta = calibration_offsets
reference_frame = (alpha * gamma) + (beta * delta)

# Construct calibration sequence using list manipulations and filtering
raw_calibration = [logic_signature // 2, reference_frame % 50, len(calibration_offsets)]
calibration_sequence = sorted([x + 2 for x in raw_calibration if x > 10])

calibration_sequence.append(signal_checksum % 100)  # Inject misleading value

# Red herring: complex-looking but unused calculation
entropy_proxy = sum(x * math.log(x + 1e-5) for x in telemetry_stream)
entropy_proxy = round(entropy_proxy, 3)

# Key operation: this lambda is actually used
process_metrics = lambda sig, seq: diagnostic_router(sig, seq) + (seq[1] * 7)

# Critical execution point — question targets this assignment
final_diagnostic = process_metrics(logic_signature, calibration_sequence)

# Print result as required
print(f"Result: {final_diagnostic}")