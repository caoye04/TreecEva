def analyze_signal(samples, threshold=0.75):
    """Process sensor signal with noise filtering and trend analysis."""
    smoothed = []
    noise_floor = 0.1
    peak_magnitude = 0
    cumulative_energy = 0
    spike_count = 0

    for val in samples:
        if abs(val) > threshold + noise_floor:
            corrected = val * 0.85
            spike_count += 1
        else:
            corrected = val * 0.1 if val > 0 else 0
        
        smoothed.append(corrected)
        cumulative_energy += corrected ** 2
        if abs(corrected) > peak_magnitude:
            peak_magnitude = abs(corrected)

    if len(smoothed) == 0:
        return [0], 0, 0

    # Normalize energy by sample count
    normalized_energy = cumulative_energy / len(smoothed)

    # Compute rolling average over 3 elements
    window_avg = []
    for i in range(len(smoothed) - 2):
        window_avg.append(sum(smoothed[i:i+3]) / 3)
    
    # Irrelevant secondary metric
    coherence_score = sum(1 for x in window_avg if x > 0.2) / len(window_avg) if window_avg else 0

    return smoothed, normalized_energy, peak_magnitude


def detect_phase_shift(waveform, ref_phase=1.57):
    """Detect phase deviation in periodic waveform."""
    total_shift = 0.0
    zero_crossings = []
    amplitude_mod = []

    for i in range(1, len(waveform)):
        if waveform[i-1] <= 0 < waveform[i]:
            zero_crossings.append(i)
        elif waveform[i-1] >= 0 > waveform[i]:
            zero_crossings.append(i)
    
    if len(zero_crossings) < 2:
        return 0.0, 0
    
    avg_interval = sum(j - zero_crossings[i] for i, j in enumerate(zero_crossings[1:])) / (len(zero_crossings) - 1)
    expected_phase_step = 6.28 / avg_interval
    
    for val in waveform:
        modulated = abs(val) ** 0.5 * (1 + 0.1 * total_shift)
        amplitude_mod.append(modulated)
    
    # Secondary modulation index
    modulation_index = sum(amplitude_mod) / len(amplitude_mod)

    estimated_phase = expected_phase_step * len(waveform) // 2
    return estimated_phase - ref_phase, int(modulation_index)

# Simulate telemetry data from satellite sensor array
telemetry_stream = [
    0.12, -0.33, 0.45, 0.67, -0.21, 0.88, -0.05, 0.11, 0.76, -0.54,
    0.32, 0.29, -0.81, 0.93, 0.04, -0.65, 0.72, 0.51, -0.39, 0.87
]

# Filter and extract primary features
filtered_signal, energy_level, max_amplitude = analyze_signal(telemetry_stream)

# Generate time-shifted copy for phase comparison
shifted_wave = [round(x * 0.9 + 0.1, 2) for x in reversed(filtered_signal)]

# Perform phase deviation analysis
phase_deviation, mod_index = detect_phase_shift(shifted_wave)

# Build trend data using slicing and list comprehension
trend_slice = filtered_signal[5:-5]
detrended = [x - energy_level * 0.1 for x in trend_slice]
trend_data = [abs(x) for x in detrended if x != 0]
baseline = sum(trend_data) / len(trend_data) if trend_data else 0.5

# Compute entropy proxy (irrelevant to final result)
entropy_proxy = -sum(p * __import__('math').log(p + 1e-8) for p in trend_data[:5]) if trend_data else 0

# Outlier detection using zip and enumerate
outlier_flags = []
for i, (a, b) in enumerate(zip(trend_data, trend_data[1:])):
    if abs(a - b) > 0.3 and i % 3 == 0:
        outlier_flags.append(i)

outlier_buffer = len(outlier_flags) + 5 if len(outlier_flags) < 3 else 2

# Auxiliary computation - distraction
compression_ratio = len(telemetry_stream) / (len(trend_data) + 1)
efficiency_metric = (energy_level + max_amplitude) / (compression_ratio + 1e-6)

# Critical assignment point
def aggregate_metrics(series, base):
    weighted_sum = 0
    for i, val in enumerate(series):
        if i % 2 == 0:
            weighted_sum += val * base * (i + 1)
        else:
            weighted_sum += val * 1.5
    return weighted_sum * 100

final_diagnostic = aggregate_metrics(trend_data, baseline) // outlier_buffer

# Dead code path - never executed but looks relevant
def legacy_calibrate(x):  # Unused function
    return [e * 0.95 for e in x if e > 0.1]

# Unused variables
reference_map = {i: round(__import__('math').sin(i * 0.5), 2) for i in range(10)}
sync_pattern = telemetry_stream[::4]

# Print final result
print(f"Result: {final_diagnostic}")