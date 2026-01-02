import itertools

def analyze_signal_strength(signal_sequence, noise_floor):
    filtered = [x for x in signal_sequence if x > noise_floor]
    return sum(filtered) // len(filtered) if filtered else 0

def compute_checksum(data_stream):
    checksum = 0
    for byte in data_stream:
        checksum ^= byte * 3
    return checksum % 256

def evaluate_health_status(metrics, baseline):
    score = 0
    for key in metrics:
        if key in baseline:
            if metrics[key] > baseline[key] * 1.2:
                score += 2
            elif metrics[key] < baseline[key] * 0.8:
                score -= 3
    return score

# Irrelevant helper (dead code path)
def deprecated_normalization(vec):
    magnitude = sum(x**2 for x in vec) ** 0.5
    return [x / magnitude for x in vec] if magnitude else vec

# Unused constant (distractor)
MAX_BUFFER_SIZE = 8192

# Simulated telemetry data
raw_readings = [127, 255, 64, 192, 32, 160, 0, 224]
signal_log = [x | 1 for x in raw_readings]  # Artificial bit manipulation

# Noise processing branch (partially irrelevant)
noise_profile = [x & 15 for x in raw_readings]
smoothed_noise = list(itertools.accumulate(noise_profile, lambda a, b: (a + b) // 2))

# System thresholds and baselines
system_thresholds = {
    'voltage': 220,
    'current': 15,
    'temperature': 75
}

baseline_metrics = {
    'voltage': 230,
    'current': 12,
    'temperature': 65
}

# Data transformation pipeline
transformed = list(map(lambda x: (x >> 2) ^ 15, signal_log))
compressed = [transformed[i] for i in range(0, len(transformed), 2)]

# Diagnostic packet generation (red herring)
diag_header = bytes([0xAA, 0x55, 0x0F])
diag_payload = bytes(compressed)
diag_packet = diag_header + diag_payload
packet_checksum = compute_checksum(diag_payload)  # Used only here

# Core logic disguised among distractors
log_data = {
    'voltage': analyze_signal_strength(transformed, 30),
    'current': len([x for x in compressed if x > 20]),
    'temperature': (sum(compressed) // len(compressed)) - 5
}

# Conditional override simulation (irrelevant branch)
if packet_checksum > 100:
    log_data['voltage'] = system_thresholds['voltage']
else:
    adjustment = (packet_checksum // 10)
    log_data['current'] += adjustment  # Misleading modification

# Main evaluation function
def process_metrics(metrics, thresholds):
    diagnostics = []
    for sensor in thresholds:
        if sensor in metrics:
            val = metrics[sensor]
            threshold = thresholds[sensor]
            status = 1 if val >= threshold * 0.9 else -1
            diagnostics.append(status * abs(val - threshold) // 5)
    aggregate = sum(diagnostics)
    health_score = evaluate_health_status(metrics, baseline_metrics)
    # Final fusion (key computation)
    final_value = aggregate * 7 + health_score
    return final_value

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Result: {final_diagnostic}")