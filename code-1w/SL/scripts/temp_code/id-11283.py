import math

# Simulated sensor array data from environmental monitoring station
def acquire_sensor_data():
    raw_values = [127, 255, 0, 64, 192, 32, 96, 160]
    timestamps = [1623456780 + i*30 for i in range(len(raw_values))]
    return list(zip(timestamps, raw_values))

# Legacy calibration function (partially deprecated)
def apply_legacy_calibration(signal):
    calibrated = []
    for ts, val in signal:
        adjusted = val * 0.7854 if val > 100 else val * 0.8123
        calibrated.append((ts, round(adjusted)))
    return calibrated

# Modern multi-factor normalization
def normalize_signal(signal):
    base_values = [val for _, val in signal]
    mean_val = sum(base_values) / len(base_values)
    variance = sum((x - mean_val) ** 2 for x in base_values) / len(base_values)
    std_dev = math.sqrt(variance)
    
    normalized = []
    for ts, val in signal:
        z_score = (val - mean_val) / std_dev if std_dev != 0 else 0
        normalized.append((ts, round(z_score * 10 + 50)))
    return normalized

# Signal discretization into bands (distraction: not used in final path)
def discretize_bands(signal):
    band_map = {i: [] for i in range(5)}
    for ts, val in signal:
        if val < 10: band = 0
        elif val < 25: band = 1
        elif val < 50: band = 2
        elif val < 75: band = 3
        else: band = 4
        band_map[band].append(ts)
    return band_map

# Irrelevant auxiliary transformation (red herring)
def compute_spectral_entropy(signal):
    magnitudes = [abs(val - 50) for _, val in signal]
    total = sum(magnitudes)
    if total == 0:
        return 0.0
    probabilities = [m / total for m in magnitudes]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 3)

# Core processing chain
processed_cache = {}
def process_segment(segment_data, method='hybrid'):
    if method == 'legacy':
        return apply_legacy_calibration(segment_data)
    elif method == 'modern':
        return normalize_signal(segment_data)
    else:
        # Hybrid approach: legacy scale then modern norm
        temp_result = apply_legacy_calibration(segment_data)
        return normalize_signal(temp_result)

def integrate_temporal_weights(filtered_signal, decay_factor=0.95):
    weighted_sum = 0.0
    weight = 1.0
    for i, (ts, val) in enumerate(reversed(filtered_signal)):
        weighted_sum += val * weight
        weight *= decay_factor
    return weighted_sum

# Distractor: unused fusion algorithm
def fuse_multi_source(primary, secondary):
    fused = []n    for (ts1, v1), (ts2, v2) in zip(primary, secondary):
        combined = (v1 * 0.7) + (v2 * 0.3)
        fused.append((ts1, round(combined)))
    return fused

# Main pipeline
sensor_log = acquire_sensor_data()

# Apply hybrid processing
processed_signals = process_segment(sensor_log, method='hybrid')

# Dead code path - never invoked but looks important
if __debug__:
    debug_snapshot = processed_signals.copy()
    buffer_checksum = sum(val for _, val in debug_snapshot) % 1000

# Spurious intermediate analysis (distractor)
band_distribution = discretize_bands(processed_signals)
diagnostic_entropy = compute_spectral_entropy(processed_signals)

# Real computation begins here (hidden among distractions)
effective_readings = []
for idx, (ts, val) in enumerate(processed_signals):
    if idx % 2 == 0:
        transformed = val ^ (idx << 2)  # Bit manipulation
    else:
        transformed = val | (idx & 3)
    effective_readings.append(transformed)

# Conditional aggregation with case logic
case_mapped = []
for x in effective_readings:
    if x < 20:
        case_mapped.append(x * 3)
    elif x < 40:
        case_mapped.append(x + 15)
    elif x < 60:
        case_mapped.append(x)
    else:
        case_mapped.append(int(x * 0.9))

# Final diagnostic computation
rolling_window = []
for i in range(len(case_mapped)):
    window_avg = sum(case_mapped[max(0, i-2):i+1]) / (i+1 if i < 2 else 3)
    rolling_window.append(window_avg)

smoothed_final = sum(rolling_window) / len(rolling_window)
final_diagnostic = int(round(smoothed_final * 1.25))

# Output target result
print(f"Result: {final_diagnostic}")