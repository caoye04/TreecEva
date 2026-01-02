import math

# Simulated sensor array diagnostics with mixed signal processing
def collect_diagnostics():
    base_frequency = 50.0
    harmonics = [base_frequency * i for i in range(1, 6)]
    phase_shifts = {h: math.sin(h / 10) for h in harmonics}
    
    # Irrelevant environmental metadata
    ambient_temp = 23.5
    humidity_level = 67
    pressure_kpa = 101.3
    timestamp_log = [1623456789 + i*60 for i in range(10)]

    # Real signal data embedded among distractions
    raw_readings = [127, 255, 191, 63, 0, 127]
    processed_signals = []
    for val in raw_readings:
        normalized = (val / 255.0) * 2 - 1
        if abs(normalized) > 0.5:
            processed_signals.append(round(normalized * 100) / 100)
        else:
            processed_signals.append(0)

    # Dead code path - never executed due to prior filtering
    def legacy_filter(x):
        return x if x > 0.7 else 0

    # Unused transformation chain
    fft_buffer = [complex(math.cos(i), math.sin(i)) for i in range(8)]
    fft_magnitude = [abs(x) for x in fft_buffer]
    spectral_peaks = set()
    for i, mag in enumerate(fft_magnitude):
        if mag > 0.9:
            spectral_peaks.add(i)

    # Decoy analysis function that's defined but not used
    def compute_coherence(signal_list):
        coherence_score = 0
        for s in signal_list:
            coherence_score += math.sqrt(abs(s)) if s != 0 else -0.1
        return coherence_score

    # Actual critical computation buried in noise
    threshold_mask = {i: v for i, v in enumerate(processed_signals) if v != 0}
    active_indices = list(threshold_mask.keys())
    index_product = 1
    for idx in active_indices:
        index_product *= (idx + 1)  # Avoid zero multiplication

    # Secondary distraction: power system metrics
    apparent_power = [base_frequency * v for v in processed_signals]
    reactive_power = [p * 0.3 for p in apparent_power]
    power_factor = [0.85] * len(apparent_power)

    # Signal integrity check (unused)
    checksum = sum([int(p * 100) for p in processed_signals if p != 0]) % 256

    # Another red herring: phase alignment simulation
    aligned_phases = []
    for h in harmonics:
        aligned = math.cos(h / 5) + math.sin(h / 7)
        aligned_phases.append(round(aligned, 2))
    
    # Core logic obscured by context
    clipped_signals = [max(-1.0, min(1.0, s)) for s in processed_signals]
    energy_sum = sum([s**2 for s in clipped_signals])
    
    # Distractor: frequency domain approximation (irrelevant)
    freq_weights = {f: math.exp(-f/100) for f in harmonics}
    weighted_spectrum = sum(freq_weights.values())

    # Critical intermediate result
    signal_entropy = 0.0
    for s in clipped_signals:
        if s != 0:
            signal_entropy -= s * math.log(abs(s))

    # Final processing chain
    scaled_entropy = int(abs(signal_entropy) * 100)
    normalized_index_product = index_product % 100
    final_diagnostic = scaled_entropy + normalized_index_product

    # Dead print statements (distractors)
    # print(f"Ambient: {ambient_temp}C, Humidity: {humidity_level}%")
    # print(f"Checksum: {checksum}, Weighted Spectrum: {weighted_spectrum:.2f}")
    
    return final_diagnostic

# Secondary auxiliary function with misleading name
def analyze_readings(signal_data):
    # This function is actually irrelevant - the real calculation happens in collect_diagnostics
    dummy_result = 0
    for i, val in enumerate(signal_data):
        if i % 2 == 0 and val > 0.5:
            dummy_result += int(val * 10)
    return dummy_result * 2  # Never meaningfully contributes

# Execution flow with primary result computed before final assignment
diagnostic_set = collect_diagnostics()
baseline_readings = [-0.8, 0, 0.6, 0, 0, 1.0]
final_diagnostic = analyze_readings(baseline_readings)
final_diagnostic = diagnostic_set  # Correct assignment overwrites previous

print(f"Result: {final_diagnostic}")