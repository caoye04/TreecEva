def analyze_signal_sequence(raw_samples, threshold=0.75):
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > 0.1]
    segment_energy = sum(x**2 for x in filtered)

    # Real data path begins here
    binary_pattern = [(1 if x > threshold else 0) for x in raw_samples]
    
    # Misleading energy computation (dead end)
    signal_magnitude = sum(abs(x) for x in raw_samples)
    energy_proxy = signal_magnitude * 0.33

    # Actual logic: find repeating bit pairs using slicing and enumerate
    repeated_pairs = 0
    for i, _ in enumerate(binary_pattern[:-1]):
        if i % 2 == 0 and i + 1 < len(binary_pattern):
            pair = binary_pattern[i:i+2]
            if pair == [1, 0] and i + 3 < len(binary_pattern):
                lookahead = binary_pattern[i+2:i+4]
                if lookahead == [1, 0]:
                    repeated_pairs += 1

    # Use of zip to align with dummy indices (partial distractor)
    index_map = list(enumerate(zip([1]*len(binary_pattern), binary_pattern)))
    active_indices = [idx for idx, (a, b) in index_map if b == 1]

    # Destructuring assignment (real use)
    first_idx, *middle_indices, last_idx = active_indices if len(active_indices) > 2 else (active_indices[0],) * 3

    # Simulated mode flags based on pattern stats (used later)
    mode_flags = {
        'burst_mode': repeated_pairs >= 2,
        'edge_align': first_idx % 2 == 0,
        'legacy_compat': False
    }

    # Dead code path (never executed but looks important)
    if mode_flags['legacy_compat']:
        backup_state = {'checksum': 0, 'version': 'A'}
        for j in range(len(normalized)):
            backup_state['checksum'] ^= j

    # Real processing begins — slice and transform
    processed_data = []
    window_size = 3
    for k in range(len(binary_pattern) - window_size + 1):
        window = binary_pattern[k:k+window_size]
        # Only windows starting with 1 are meaningful
        if window[0] == 1:
            # Convert 3-bit window to decimal
            value = window[0]*4 + window[1]*2 + window[2]*1
            processed_data.append(value)

    # Compute integrity value (answer depends only on this function)
    def compute_integrity_value(data, modes):
        base = sum(data)
        if modes['burst_mode']:
            base += 17
        if modes['edge_align']:
            base *= 2
        return base % 9997

    final_checksum = compute_integrity_value(processed_data, mode_flags)

    # Unrelated telemetry logging (distractor)
    telemetry_log = []
    for sample in raw_samples[:5]:
        log_entry = f"Sample:{sample:.3f} -> Norm:{sample/max(raw_samples):.3f}"
        telemetry_log.append(log_entry)

    # Output required format
    print(f"Result: {final_checksum}")

    return final_checksum

# Input data (deterministic)
samples = [0.8, 0.3, 0.9, 0.1, 0.7, 0.2, 0.95, 0.6, 0.15]
analyze_signal_sequence(samples)