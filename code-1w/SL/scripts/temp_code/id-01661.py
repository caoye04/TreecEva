def analyze_phase_shift(readings):
    adjusted = [r * 1.73 for r in readings if r > 0]
    normalized = [a / sum(adjusted) for a in adjusted]
    return sum(n ** 2 for n in normalized)


def evaluate_resonance(sequence):
    magnitude = sum(abs(s) for s in sequence)
    peak = max(sequence)
    threshold = magnitude * 0.1
    active_bands = [s for s in sequence if abs(s) > threshold]
    return len(active_bands), magnitude


def generate_checksum(data_stream):
    xor_sum = 0
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            xor_sum ^= (val % 256)
    return xor_sum

# Irrelevant telemetry processing (red herring)
def process_telemetry(packets):
    errors = 0
    for p in packets:
        if p < 0:
            errors += 1
    return errors

# Unused function — dead code path
def deprecated_filter(values):
    return [v for v in values if v & 1]

# Core diagnostic logic
system_log = [3, 7, -1, 4, 8, 0, 12, 5]
baseline = {1, 2, 3, 4, 5}
reference_frame = set(range(0, 10))
overlap = baseline & reference_frame

temporal_weights = []
for idx, val in enumerate(system_log):
    if val > 0 and idx % 2 == 1:
        temporal_weights.append(val * 2.5)

aggregated_signal = sum(temporal_weights)
scaling_factor = len(overlap) * 0.5

# Simulated sensor array input
sensor_readings = [0.1, 0.4, 0.9, 0.2]
phase_diagnostic = analyze_phase_shift(sensor_readings)

# Resonance evaluation with distractor outputs
band_count, total_power = evaluate_resonance([-3, 7, 1, 8, -5, 2])
useless_ratio = total_power / (band_count + 1) if band_count else 0

# Data stream checksum (misleading relevance)
data_stream = [255, 128, 64, 32, 16]
checksum = generate_checksum(data_stream)

# Consistency validation using set difference (actual relevant logic)
expected_nodes = {1, 2, 3, 4, 5, 6, 7}
active_nodes = {2, 4, 5, 7}
failed_nodes = expected_nodes - active_nodes
consistency_check = len(failed_nodes) <= 2

# Secondary validation: average signal strength
avg_signal = aggregated_signal / len(temporal_weights) if temporal_weights else 0
signal_threshold_met = avg_signal > 10.0

# Tertiary check: phase stability
phase_stable = phase_diagnostic < 0.6

# Final integrity computation — depends only on consistency_check and system_log length
def compute_integrity_score(valid, log):
    base = len(log) * 100
    penalty = 300 if not valid else 0
    return base - penalty

# Execution point of interest
final_diagnostic = compute_integrity_score(consistency_check, system_log)

# Output result
print(f"Result: {final_diagnostic}")