import math

# Simulated sensor fusion system for environmental anomaly detection
def analyze_spectral_peak(frequency, amplitude):
    if frequency < 0:
        return 0.0
    intensity = amplitude * math.log(frequency + 1e-5)
    normalized = abs(math.sin(intensity)) ** 2
    return round(normalized * 100, 3)

# Legacy function - not used in current execution path
def deprecated_calibrate(values):
    adjusted = [v * 0.95 for v in values if v > 10]
    return sum(adjusted) // len(adjusted) if adjusted else 0

# Signal preprocessing pipeline
signal_buffer = [
    {'freq': 120.5, 'amp': 42.3, 'type': 'EM'},
    {'freq': 89.1, 'amp': 37.8, 'type': 'ACOUSTIC'},
    {'freq': 150.0, 'amp': 55.2, 'type': 'EM'},
    {'freq': 65.3, 'amp': 29.4, 'type': 'VIBRATION'}
]

# Misleading diagnostic flags (some are decoys)
critical_band_alert = False
baseline_drift_compensated = True
noise_floor_estimation = 0.87
spurious_peak_count = 0
redundant_accumulator = 0

# Threshold configuration map (used in aggregation)
threshold_map = {
    'EM': (120.0, 45.0),
    'ACOUSTIC': (85.0, 35.0),
    'VIBRATION': (60.0, 25.0)
}

# Secondary buffer with irrelevant data (red herring)
auxiliary_readings = []
for i in range(len(signal_buffer)):
    temp_offset = (i + 1) * 0.3
    phase_shift = math.cos(temp_offset)
    auxiliary_readings.append({
        'index': i,
        'shift': phase_shift,
        'offset': temp_offset,
        'status': 'OK' if phase_shift > 0 else 'CALIBRATING'
    })
    redundant_accumulator += phase_shift  # Dead-end computation

# Unused transformation (distractor)
transformed_signals = [
    {**entry, 'enriched': True, 'quality': 'HIGH'} 
    for entry in signal_buffer 
    if entry['amp'] > 30
]

# Diagnostic engine core
active_channels = 0
peak_diagnostics = []
false_positive_mitigation_counter = 0

for signal in signal_buffer:
    f = signal['freq']
    a = signal['amp']
    t = signal['type']
    
    ref_freq, ref_amp = threshold_map[t]
    
    if f > ref_freq and a > ref_amp:
        score = analyze_spectral_peak(f, a)
        peak_diagnostics.append(score)
        active_channels += 1
    else:
        # Simulate false positive suppression logic (not triggered)
        false_positive_mitigation_counter += 1

# Decoy statistical summary (unused)
mean_diagnostic_value = sum(peak_diagnostics) / len(peak_diagnostics) if peak_diagnostics else 0
median_suppression_factor = sorted(peak_diagnostics)[len(peak_diagnostics)//2] if peak_diagnostics else 1.0

# Core aggregation logic with list comprehension and accumulation
intermediate_weights = [math.tanh(x / 100) for x in peak_diagnostics]
weight_sum = sum(intermediate_weights)
size_penalty = 1 / (len(signal_buffer) + 1)

# Final computation using composite factors
if weight_sum > 0 and active_channels >= 2:
    raw_aggregate = sum(
        w * val for w, val in zip(intermediate_weights, peak_diagnostics)
    )
    adjustment_factor = math.exp(-size_penalty)
    filtration_score = int(raw_aggregate * adjustment_factor) + active_channels * 5
else:
    filtration_score = -1

# Spurious post-processing (irrelevant)
final_status_flags = []
for reading in auxiliary_readings:
    if reading['status'] == 'OK':
        final_status_flags.append(True)
    else:
        final_status_flags.append(False)

# Output target result
Result: filtration_score