import math

def analyze_signal_integrity(raw_samples, threshold=0.75):
    sample_metrics = []
    noise_floor = 0.1
    cumulative_energy = 0.0
    spike_count = 0

    for i, sample in enumerate(raw_samples):
        normalized = abs(sample) / (max(raw_samples) + 1e-9)
        if normalized > threshold:
            spike_count += 1
            cumulative_energy += normalized ** 2
        sample_metrics.append((i, normalized, sample))

    signal_power = cumulative_energy / len(raw_samples) if raw_samples else 0
    return signal_power, spike_count, sample_metrics

def compute_harmonic_profile(frequencies):
    harmonics = []
    total_power = 0
    for f in frequencies:
        h = int(round(math.log(f + 1) * 10)) % 7
        total_power += h
        harmonics.append(h)
    efficiency_score = total_power / len(harmonics) if harmonics else 0
    return harmonics, efficiency_score

def evaluate_buffer_coherence(data_stream):
    window_size = 4
    coherence_score = 0
    temporal_gaps = []
    
    for i in range(len(data_stream) - window_size + 1):
        window = data_stream[i:i+window_size]
        avg_val = sum(window) / window_size
        variance = sum((x - avg_val) ** 2 for x in window) / window_size
        if variance < 0.5:
            coherence_score += 1
        temporal_gaps.append((i, variance))
    
    gap_analysis = {i: round(v, 3) for i, v in temporal_gaps}
    return coherence_score, gap_analysis

def generate_synthetic_load(base_pattern, iterations=3):
    # Irrelevant synthetic data generator - red herring
    result = []
    for _ in range(iterations):
        new_row = [base_pattern[i] * ((i + 1) % 5) for i in range(len(base_pattern))]
        result.append([x + 0.1 for x in new_row])
    return result

def encrypt_sequence(seq):
    # Dead function - never used in main logic
    return [int(x * 17) ^ 255 for x in seq]

def validate_timing_envelope(timestamps):
    intervals = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    ideal_interval = sum(intervals) / len(intervals)
    jitter = sum(abs(delta - ideal_interval) for delta in intervals)
    return ideal_interval, jitter

def aggregate_metrics(chains, diagnostics):
    base_score = 0
    adjustment_factor = 1.0

    for idx, chain in enumerate(chains):
        phase_shift = (idx + 1) * 0.5
        for j, val in enumerate(chain['values']):
            if j % 2 == 0:
                base_score += math.sin(val * phase_shift)
            else:
                base_score += math.cos(val * 0.1 * (j + 1))

        status_flag = chain.get('status', 0)
        if status_flag > 0:
            adjustment_factor *= 1.1

    diagnostic_sum = sum(diagnostics) if diagnostics else 0
    final_weight = math.tanh(diagnostic_sum * 0.01)
    return int(base_score * adjustment_factor * (1 + final_weight))

# Main execution block with complex setup and distractors
raw_input_signal = [0.2, 0.8, 1.1, 0.4, 0.9, 1.3, 0.6, 0.7, 1.0, 1.4]
frequency_bands = [12, 45, 67, 89, 112, 134, 155, 178]
timestamp_log = [0.0, 0.22, 0.43, 0.67, 0.89, 1.11, 1.32, 1.55]

# Execute real processing steps
power_level, spikes, metrics = analyze_signal_integrity(raw_input_signal)
harmonic_list, efficiency = compute_harmonic_profile(frequency_bands)
coherence, gaps = evaluate_buffer_coherence([x[1] for x in metrics])
ideal_dt, timing_jitter = validate_timing_envelope(timestamp_log)

# Generate irrelevant synthetic data (distractor)
synthetic_load = generate_synthetic_load([1, 2, 3], 4)
encrypted_spikes = encrypt_sequence([spikes])  # Misleading transformation

# Construct processing chain - relevant structure
processing_chain = [
    {
        'values': [power_level * 100, efficiency * 10, coherence],
        'status': 1 if spikes > 3 else 0,
        'meta': 'primary_channel'
    },
    {
        'values': [timing_jitter * 50, ideal_dt * 100, len(harmonic_list)],
        'status': 1,
        'meta': 'timing_validation'
    },
    {
        'values': [math.sqrt(spikes), math.log(coherence + 1), power_level * 50],
        'status': 0,
        'meta': 'fallback_path'  # Unused in final calculation but looks important
    }
]

diagnostics = [
    len(raw_input_signal),
    len(frequency_bands),
    len(timestamp_log),
    spikes,
    len(harmonic_list),
    int(coherence)
]

# Critical statement
final_diagnostic = aggregate_metrics(processing_chain, diagnostics)

# Print result as required
print(f"Target result: {final_diagnostic}")