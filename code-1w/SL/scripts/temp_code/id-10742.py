def analyze_signal(samples, threshold=0.75):
    amplitude_map = [abs(x) for x in samples]
    peak = max(amplitude_map)
    normalized = [x / peak for x in amplitude_map]

    # Irrelevant transformation (distractor)
    inverted = [1 - x for x in normalized if x < 1]
    entropy_approx = sum([x * x for x in inverted])

    # Core logic: find dominant frequency band index
    band_energy = [0] * 4
    for val in normalized:
        if val < 0.25:
            band_energy[0] += val
        elif val < 0.5:
            band_energy[1] += val
        elif val < 0.75:
            band_energy[2] += val
        else:
            band_energy[3] += val

    dominant_band = band_energy.index(max(band_energy))

    # Dead code path (misleading)
    if dominant_band == 4:
        return -1  # unreachable

    return dominant_band


def validate_phase_coherence(sequence):
    coherence_score = 0
    for i in range(1, len(sequence)):
        if sequence[i] * sequence[i-1] > 0:
            coherence_score += 1
    return coherence_score / (len(sequence) - 1) if len(sequence) > 1 else 0

# Simulated sensor data (realistic context: signal processing)
sensor_readings = [0.1, -0.3, 0.6, 0.8, -0.75, 0.2, 0.9, -0.15, 0.4, 0.7]

# Distractor variables (irrelevant computations)
baseline_offset = sum(sensor_readings) / len(sensor_readings)
fluctuation_index = max(sensor_readings) - min(sensor_readings)
dc_component = abs(baseline_offset) * 100
rms_noise = (sum([x**2 for x in sensor_readings]) / len(sensor_readings)) ** 0.5

# Conditional expression usage (required feature)
calibration_mode = 'high_gain' if fluctuation_index > 0.5 else 'low_gain'

# Enumerate and zip usage (required feature)
indices = list(enumerate([x for x in sensor_readings if x > 0]))
pairs = list(zip([i for i, _ in indices], [0.5, 0.6, 0.8, 0.9, 0.7]))

# Primary processing chain (nested logic)
processing_stages = {
    'raw': sensor_readings,
    'filtered': [x for x in sensor_readings if abs(x) >= 0.1],
    'classified': ['high' if abs(x) >= 0.75 else 'low' for x in sensor_readings]
}

# Misleading diagnostic flag (red herring)
spike_detected = any(abs(x) >= 0.99 for x in sensor_readings)

# Real but obscured core computation
band_distribution = [0] * 4
for x in processing_stages['filtered']:
    idx = int(abs(x) * 4)  # maps to 0–3
    if idx == 4: idx = 3
    band_distribution[idx] += 1

# Tuple unpacking (required concept)
(primary_load, secondary_load, _, _) = (band_distribution[0]*2, band_distribution[1]*1.5, band_distribution[2], band_distribution[3]*0.8)

# Decoy function call (no side effects)
def audit_integrity(data):
    checksum = 0
    for item in data:
        if isinstance(item, float):
            checksum ^= int(abs(item) * 100) % 255
    return checksum

_ = audit_integrity(sensor_readings)
_ = audit_integrity(['placeholder'])  # unused

# Complex data transformation with nested conditionals
diagnostics = {}
for i, val in enumerate(processing_stages['filtered']):
    category = 'critical' if abs(val) >= 0.75 else ('moderate' if abs(val) >= 0.5 else 'low')
    tag = f"{category}_{i}"
    if category not in diagnostics:
        diagnostics[category] = []
    diagnostics[category].append(tag)

# Key irrelevant dictionary (distractor)
metadata_log = {
    'version': '2.1.0',
    'samples_processed': len(sensor_readings),
    'calibration_valid': True,
    'redundant_flag': False,
    'debug_trace': [audit_integrity(sensor_readings)]
}

# Actual answer derivation path (non-obvious due to distractions)
stage_weights = {
    'raw': 1.0,
    'filtered': 1.8,
    'classified': 0.5
}

aggregate_score = 0
for key, weight in stage_weights.items():
    if key == 'raw':
        aggregate_score += len(processing_stages[key]) * weight
    elif key == 'filtered':
        valid_count = len([x for x in processing_stages[key] if x > 0])
        aggregate_score += valid_count * weight
    elif key == 'classified':
        high_count = processing_stages['classified'].count('high')
        aggregate_score += high_count * weight

# Recursive helper (required abstraction layer)
def recursive_amplify(value, depth):
    if depth <= 0 or value > 20:
        return value
    return recursive_amplify(value + (value * 0.1), depth - 1)

scaled_aggregate = recursive_amplify(aggregate_score, 3)

# Final computation buried in noise
final_diagnostic = 0
if scaled_aggregate > 15:
    analysis_band = analyze_signal(sensor_readings)
    phase_score = validate_phase_coherence(sensor_readings)
    adjustment_factor = 1 + (phase_score * 0.25)
    
    # Critical statement
    final_diagnostic = int(scaled_aggregate * adjustment_factor + analysis_band * 10)
else:
    final_diagnostic = 5000  # decoy branch (not taken)

print(f"Result: {final_diagnostic}")