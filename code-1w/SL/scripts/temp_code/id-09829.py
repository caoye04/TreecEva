import itertools

# Simulated signal processing pipeline with diagnostic overhead
def analyze_harmonic_profile(samples):
    # Irrelevant diagnostics
    sample_count = len(samples)
    total_amplitude = sum(abs(s) for s in samples)
    avg_amplitude = total_amplitude / sample_count if sample_count else 0

    # Dead code path - never executed due to filter
    redundant_copy = [x for x in samples if x > 1e5]  
    if len(redundant_copy) > 1000:
        normalization_offset = max(redundant_copy)
    else:
        normalization_offset = 0  # Never used

    # Real computation begins: frequency centroid calculation
    weighted_sum = 0.0
    total_weight = 0.0
    
    for i, amplitude in enumerate(samples):
        freq_bin = i + 1  # Non-zero indexed
        if amplitude <= 0:  # Skip non-positive amplitudes
            continue
        energy = abs(amplitude) ** 2
        weighted_sum += freq_bin * energy
        total_weight += energy

    frequency_centroid = weighted_sum / total_weight if total_weight != 0 else 0.0

    # Distractor: spurious statistical analysis
    squared_deviations = [(x - avg_amplitude)**2 for x in samples]
    variance_proxy = sum(squared_deviations) / len(squared_deviations) if squared_deviations else 0
    entropy_placeholder = 0.0
    for x in samples:
        if x != 0:
            entropy_placeholder -= (x / total_amplitude) * ((x / total_amplitude).__log__())
    # End of irrelevant stats

    # Correction logic based on spectral compactness
    spectral_moment = sum((i+1) * abs(val) for i, val in enumerate(samples[:50]))
    reference_baseline = 127.5
    dynamic_range = max(samples, default=0) - min(samples, default=0)

    compression_ratio = 1.0
    if dynamic_range > 50:
        compression_ratio = 0.87
    elif dynamic_range > 30:
        compression_ratio = 0.92
    else:
        compression_ratio = 0.98

    # Decoy transformation chain
    temp_buffer = []
    for a in samples:
        transformed = abs(a) ** 0.5
n        if transformed > 10:
            temp_buffer.append(transformed * 0.75)
    # Unused buffer accumulates nothing useful

    # Actual correction factor derivation
    peak_index = max(range(len(samples)), key=lambda i: abs(samples[i])) if samples else 0
    index_in_quartile = (peak_index // (len(samples)//4)) if len(samples) > 4 else 0
    quartile_bias = [1.05, 0.98, 0.93, 0.88][index_in_quartile] if index_in_quartile < 4 else 0.85

    correction_factor = compression_ratio * quartile_bias

    # Key statement
    equilibrium_score = round(frequency_centroid * correction_factor, 4)

    # More red herrings: unused data structure manipulations
    zigzag_pairs = list(itertools.combinations(samples[::3], 2))
    cumulative_trend = list(itertools.accumulate(samples, func=lambda x,y: x + y*0.1))
    filtered_cycle = list(itertools.dropwhile(lambda x: x < 10, cumulative_trend))

    # Spurious final check
    if len(filtered_cycle) % 2 == 0 and len(zigzag_pairs) > 10:
        equilibrium_score += 0.001  # Never reached in this case

    return equilibrium_score

# Generate deterministic input
base_frequencies = [3, 7, 12, 18, 25, 30, 28, 22, 15, 10, 6, 4, 2]
signal_harmonics = [amp * (1 + (idx % 3) * 0.1) for idx, amp in enumerate(base_frequencies)]
modulated_signal = [(x * (5 + i)) if i % 2 == 0 else x // (i+1) for i, x in enumerate(signal_harmonics)]
final_samples = [max(1, int(x)) for x in modulated_signal]  # Ensure positivity

# Execute main analysis
result = analyze_harmonic_profile(final_samples)
equilibrium_score = result
print(f"Target result: {equilibrium_score}")