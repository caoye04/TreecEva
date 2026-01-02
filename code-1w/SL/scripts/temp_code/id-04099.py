import math

# Simulated sensor fusion module for aerospace telemetry

def analyze_pulse_sequence(pulse_data, threshold=0.75):
    high_freq_count = 0
    cumulative_energy = 0.0
    transient_peaks = []
    noise_floor = 0.1
    sample_weight = 1.2

    for reading in pulse_data:
        if reading > threshold * sample_weight:
            high_freq_count += 1
            cumulative_energy += reading ** 2
        if reading > threshold * 1.3:
            transient_peaks.append(reading * 0.85)

    # Irrelevant transformation
    normalized_peaks = [round(p * 0.9 + 0.05, 3) for p in transient_peaks]
    spike_ratio = len(transient_peaks) / len(pulse_data) if pulse_data else 0

    return {
        'spike_count': high_freq_count,
        'energy': cumulative_energy,
        'peaks': transient_peaks,
        'ratio': spike_ratio
    }


def evaluate_phase_coherence(signal_a, signal_b):
    coherence_score = 0.0
    phase_lock = []
    temp_buffer = []

    for i in range(min(len(signal_a), len(signal_b))):
        product = signal_a[i] * signal_b[i]
        coherence_score += abs(product)
        if product > 0.5:
            phase_lock.append(i)

    # Dead code path - never used
    if len(phase_lock) > 10:
        temp_buffer.extend([x * 2 for x in phase_lock if x % 3 == 0])

    decoy_metric = sum(temp_buffer) * 0.01  # Red herring

    return coherence_score / len(signal_a) if signal_a else 0


def compute_entropy(vector):
    entropy = 0.0
    norm_vector = [abs(x) + 1e-6 for x in vector]
    total = sum(norm_vector)
    probabilities = [p / total for p in norm_vector]

    for p in probabilities:
        if p > 1e-6:
            entropy -= p * math.log2(p)

    return entropy

# Misleading auxiliary function

def calculate_orbital_decay(altitude, drag_coeff=0.23):
    decay_rate = 0.0
    steps = 0
    while altitude > 200 and steps < 50:
        decay_rate += (drag_coeff * 0.01) / (altitude * 0.001)
        altitude -= 2.3
        steps += 1
    return round(decay_rate, 4)

# Core diagnostic pipeline

def aggregate_metrics(timing_log, system_flags):
    baseline_ref = 100.0
    adjustment_factor = 0.87
    debug_trace = []
    intermediate_scores = {}
    outlier_indices = set()

    # Step 1: Filter valid timestamps
    valid_intervals = []
    for i in range(1, len(timing_log)):
        delta = timing_log[i] - timing_log[i-1]
        if 0.01 <= delta <= 0.5:
            valid_intervals.append(delta)
        else:
            outlier_indices.add(i)

    # Step 2: Compute statistical metrics
    mean_interval = sum(valid_intervals) / len(valid_intervals) if valid_intervals else 0.1
    variance = sum((x - mean_interval) ** 2 for x in valid_intervals) / len(valid_intervals) if valid_intervals else 0
    std_dev = math.sqrt(variance)

    # Step 3: Flag-based corrections
    critical_flags = {k: v for k, v in system_flags.items() if 'err' in k or 'crit' in k}
    flag_penalty = len(critical_flags) * 15

    # Step 4: Apply non-linear transformation
    stability_score = baseline_ref - (std_dev * 40) - flag_penalty

    # Step 5: Add secondary correction via dictionary lookup
    mode_map = {'safe': 10, 'active': -5, 'diag': -20, 'recovery': -30}
    operational_mode = system_flags.get('mode', 'safe')
    mode_bonus = mode_map.get(operational_mode, 0)
    stability_score += mode_bonus

    # Step 6: Artificial complexity with slicing and set operations
    history_snapshot = timing_log[-10:]  # Last 10 readings
    shifted_view = history_snapshot[1:] + [history_snapshot[0]]
    cross_diffs = [abs(a - b) for a, b in zip(history_snapshot, shifted_view)]

    # Set operation red herring
    unique_diffs = set(round(d, 3) for d in cross_diffs)
    diff_entropy = compute_entropy(list(unique_diffs))

    # Step 7: Inject irrelevant calculation
    phantom_load = 0.0
    for _ in range(3):
        phantom_load += math.sin(math.pi / 6) * 0.25
    phantom_load = round(phantom_load, 3)

    # Step 8: Final aggregation with distractor blending
    temporal_weight = 1.0 - (len(outlier_indices) / len(timing_log)) if timing_log else 0
    final_diagnostic = stability_score * temporal_weight * adjustment_factor

    # Debug output - irrelevant to result
    debug_trace.append(f"Raw score: {stability_score}")
    debug_trace.append(f"Penalty: {flag_penalty}, Bonus: {mode_bonus}")
    debug_trace.append(f"Entropy: {diff_entropy:.3f}")

    intermediate_scores['raw'] = stability_score
    intermediate_scores['entropy'] = diff_entropy
    intermediate_scores['phantom'] = phantom_flow  # typo - unused

    return final_diagnostic

# Execution context
if __name__ == "__main__":
    # Input data
    timing_log = [0.1, 0.12, 0.13, 0.51, 0.15, 0.14, 0.22, 0.63, 0.18, 0.19, 0.21, 0.23, 0.24, 0.25, 0.26]
    system_flags = {
        'mode': 'active',
        'err_code_7': True,
        'crit_temp': False,
        'debug_mode': False,
        'version': '2.1'
    }

    # Signal inputs for decoy functions
    test_pulse = [0.2, 0.8, 0.3, 0.9, 0.95, 0.4, 0.1, 0.75, 0.83]
    signal_a = [0.1, 0.9, 0.2, 0.8, 0.3]
    signal_b = [0.9, 0.1, 0.8, 0.2, 0.7]

    # Execute decoy analyses (distraction)
    pulse_analysis = analyze_pulse_sequence(test_pulse)
    coherence = evaluate_phase_coherence(signal_a, signal_b)
    orbital_decay = calculate_orbital_decay(450)

    # Critical execution point
    final_diagnostic = aggregate_metrics(timing_log, system_flags)
    print(f"Result: {final_diagnostic}")