def analyze_signal_integrity(raw_samples, threshold=0.75):
    # Irrelevant preprocessing: normalize and reverse (not used in final result)
    normalized = [round(x / max(raw_samples), 3) for x in raw_samples]
    reversed_seq = normalized[::-1]
    cumulative_energy = 0
    spike_count = 0
    phase_shifts = []

    for i, sample in enumerate(raw_samples):
        cumulative_energy += sample ** 2
        if sample > threshold * max(raw_samples):
            spike_count += 1
            if i > 0:
                phase_shifts.append(i % 4)

    # Distractor: complex frequency estimation (unused)
    dominant_freq = len([x for x in raw_samples if x > sum(raw_samples) / len(raw_samples)])
    noise_floor = sum(1 for x in raw_samples if x < 0.1) * 0.01

    # Real path begins: transform via modular arithmetic and bit analysis
    binary_projection = [int(x) & 3 for x in raw_samples]  # AND with 3 (mod 4)
    mod_sum = sum(binary_projection) % 17

    # Tuple unpacking and zip usage (required Python feature)
    indices = list(range(len(raw_samples)))
    paired_data = list(zip(indices, raw_samples))
    weighted_index_sum = 0
    for idx, val in paired_data:
        if val > 0.5:
            weighted_index_sum += idx * (val * 10)

    # Simulate checksum from index-value correlation
    checksum = 0
    for i, (idx, val) in enumerate(paired_data):
        if i % 3 == 0:
            checksum ^= int(val * 100)  # Bitwise XOR as checksum update

    # Secondary distractor: unused recursive function
    def predict_next(seq, depth=2):
        if depth == 0 or len(seq) < 2:
            return seq[-1]
        diff = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
        return seq[-1] + predict_next(diff, depth-1)

    forecast = predict_next([1, 2, 4, 8])  # This returns 16 but is irrelevant

    # Critical data transformation chain
    base_metric = mod_sum * 3 + len(phase_shifts)
    adjustment = 0
    if spike_count > 2:
        adjustment = 5
    elif spike_count == 2:
        adjustment = 2
    else:
        adjustment = -3

    # Simulated environmental correction factor
    environment_log = ['stable', 'minor_noise', 'sync_loss', 'recovered']
    recovery_comp = len(environment_log) - 1  # Always 3

    # Key intermediate variables
    aggregate_score = base_metric + adjustment + recovery_comp
    anomaly_weight = len([x for x in binary_projection if x == 3])
    correction_factor = weighted_index_sum // (checksum or 1)

    # Dead code path - misleading branch
    if noise_floor > 100:
        final_diagnostic = -9999
    else:
        # This is the actual execution path
        final_diagnostic = aggregate_score + correction_factor * anomaly_weight

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
samples = [0.2, 0.8, 1.1, 0.4, 1.3, 0.9, 1.6, 0.7]
analyze_signal_integrity(samples)