import math

# System health monitoring simulation with layered diagnostics
def analyze_subsystem(readings, threshold, mode='strict'):
    if mode == 'strict':
        return sum(1 for r in readings if r > threshold * 1.1)
    else:
        return sum(1 for r in readings if r > threshold * 0.9)

# Irrelevant helper - decoy function (never called in critical path)
def legacy_normalization(data):
    max_val = max(data)
    return [x / max_val * 100 for x in data]

# Signal preprocessing chain
def filter_artifacts(signal, window_size=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window_size)
        end = min(len(signal), i + window_size + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Unused transformation (red herring)
def spectral_decomposition(sequence):
    result = []
    for i, val in enumerate(sequence):
        result.append(val * math.sin(i * math.pi / 4))
    return result

# Core diagnostic engine
def generate_calibration_profile(base_freq, harmonics):
    profile = []
    for h in range(1, harmonics + 1):
        profile.append(base_freq * h * math.cos(h * math.pi / 6))
    return [round(p, 3) for p in profile]

# Critical aggregation logic
def aggregate_metrics(metrics_log, calibration):
    base_score = sum(metrics_log) % 773
    adjustment = int(sum([c * 1.2 for c in calibration[:5]]) // 1)
    return (base_score * 2) - adjustment + len(calibration)

# Simulated sensor input (real data)
sensor_readings = [85, 92, 78, 96, 88, 76, 91, 87, 83]

# Generate irrelevant intermediate data
baseline_norm = [x * 0.85 for x in sensor_readings]
denoised_signal = filter_artifacts(baseline_norm, 2)

# Decoy processing branch (dead code path)
if len(denoised_signal) > 10:
    transformed = spectral_decomposition(denoised_signal)
else:
    transformed = None  # This path doesn't affect final result

# Real preprocessing steps
anomaly_count = analyze_subsystem(sensor_readings, threshold=80, mode='strict')
processing_chain = [anomaly_count * 3, 45, 67, 23, 88, 12]

# Generate actual calibration sequence
primary_cal = generate_calibration_profile(base_freq=17.5, harmonics=8)
calibration_sequence = [round(c + 5.2, 2) for c in primary_cal]

# Add noise-like adjustments that don't matter
temp_offset = sum(calibration_sequence) * 0.01
offset_applied = [c + temp_offset for c in calibration_sequence]

# Key computation - this is where the answer comes from
final_diagnostic = aggregate_metrics(processing_chain, calibration_sequence)

# Print final result as required
print(f"Result: {final_diagnostic}")