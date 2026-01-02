import itertools

# Simulated sensor fusion system for predictive maintenance
# The goal is to compute a final diagnostic score based on multi-source health metrics

# Raw sensor inputs (simulated)
sensor_a_readings = [0.85, 0.83, 0.87, 0.90, 0.88]
sensor_b_readings = [42, 38, 45, 40, 44]
sensor_c_flags = [True, False, True, True, False]

timestamps = [1634567890, 1634567950, 1634568010, 1634568070, 1634568130]
dummy_counter = 0

# Irrelevant auxiliary data — distractor
maintenance_logs = {
    'last_service': '2023-08-15',
    'operator': 'AUTO_SYS_7',
    'location_id': 4096,
    'threshold_history': [0.75, 0.78, 0.80]
}

# Decoy function — never called
def analyze_vibration_pattern(data):
    return sum(x ** 2 for x in data) % 100

# Signal conditioning pipeline
filtered_a = list(map(lambda x: round(x * 1.02, 3), sensor_a_readings))  # Calibration adjust
aggregated_b = sum(abs(x - 42) for x in sensor_b_readings)  # Deviation metric

# Bitmask synthesis from boolean flags (real usage)
flag_bitmap = 0
for i, flag in enumerate(sensor_c_flags):
    if flag:
        flag_bitmap |= (1 << i)

# Secondary derived values — some relevant, some not
average_a = sum(filtered_a) / len(filtered_a)
fluctuation_score = max(filtered_a) - min(filtered_a)
dummy_counter += len(timestamps)  # Red herring update

# Baseline reference signature (simulated expected state)
baseline_ref = [
    0.84, 0.86, 0.85, 0.89, 0.87
]

# Health signature generation via pairwise transformation
health_signature = []
for x, y in zip(filtered_a, baseline_ref):
    delta = abs(x - y)
    penalty = 0
    if delta > 0.02:
        penalty = delta * 10
    health_signature.append(1 - penalty)

# Another decoy structure — unused
system_profile = {
    'version': 'v2.3.1',
    'mode': 'diagnostic',
    'cache_size': 256,
    'active_filters': ['kalman', 'median', 'outlier_suppress']
}

# Recursive smoothing function (used once)
def smooth_sequence(seq, depth=2):
    if depth == 0 or len(seq) < 2:
        return seq
    smoothed = [(seq[i] + seq[i+1]) / 2 for i in range(len(seq)-1)]
    return smooth_sequence(smoothed, depth - 1)

# Apply smoothing to health signature
smoothed_diagnostics = smooth_sequence(health_signature + [1.0], depth=1)

# Advanced correlation using itertools — real use
paired_shifts = list(itertools.pairwise(sorted(smoothed_diagnostics)))
correlation_metric = sum(abs(a - b) for a, b in paired_shifts) / len(paired_shifts) if paired_shifts else 0.0

# Auxiliary irrelevant calculation — looks important but isn't used
synthetic_index = (aggregated_b * 1000) // (len(sensor_a_readings) + 1)

# Conditional override simulation (never triggers — misleading)
override_mode = False
if flag_bitmap & 0b11111 == 0b10101 and correlation_metric < 0.05:
    override_mode = True  # This block is dead code under this input

# Core processing function
def process_metrics(metrics, reference):
    base_score = sum(metrics) / len(metrics)
    
    # Nested adjustment logic
    adjustment = 0.0
    for i, val in enumerate(metrics):
        if i % 2 == 0 and val < reference[i % len(reference)]:
            adjustment -= 0.05
        elif val > 0.95:
            adjustment += 0.1
    
    # Bitwise influence from flag_bitmap (real dependency)
    if flag_bitmap & 0b1010:  # Checks specific pattern
        adjustment += 0.08
    
    # Final nonlinear transformation
    final_score = (base_score + adjustment) * 100
    
    # Dead code path — misleading
    if final_score > 120:
        final_score = 120  # Never reached
    
    return int(round(final_score))

# Execute main logic
intermediate_norm = [min(x, 0.99) for x in health_signature]  # Distractor transform
baseline_variance = sum((a - b)**2 for a, b in zip(baseline_ref, sensor_a_readings))  # Unused

# Critical execution point
final_diagnostic = process_metrics(health_signature, baseline_ref)

# Print result as required
print(f"Target result: {final_diagnostic}")