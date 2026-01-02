def analyze_compound_sequence(sequence_ids):
    # Irrelevant transformation: base-36 decoding (unused later)
    decoded_shift = sum(int(c, 36) for c in map(str, sequence_ids) if c.isdigit())

    # Decoy statistical analysis (never used)
    mean_id = sum(sequence_ids) / len(sequence_ids)
    variance_proxy = sum((x - mean_id) ** 2 for x in sequence_ids) / len(sequence_ids)

    # Core logic disguised among distractions
    activation_threshold = 42
    signal_chain = [x % 25 for x in sequence_ids if x > activation_threshold]

    # Distractor: complex-looking but unused bit manipulation
    decoy_flags = 0
    for x in sequence_ids:
        decoy_flags ^= (x << 2) | (x >> 3)

    # Real processing begins here
    filtered_signals = list(filter(lambda x: (x + 7) % 11 == 0, signal_chain))

    # Secondary filter based on positional criteria
    indexed_energy = [(i * 3 + val) for i, val in enumerate(filtered_signals)]
    clipped_energy = [min(e, 90) for e in indexed_energy]

    # Red herring: entropy-like calculation (not part of final path)
    pseudo_entropy = sum((e / 90) * ((90 - e) / 90) for e in clipped_energy if e > 0)

    # Critical data transformation chain
    aggregate_impulse = sum(clipped_energy)
    resonance_peak = max(clipped_energy) if clipped_energy else 1
    harmonic_ratio = aggregate_impulse / resonance_peak

    # Simulated calibration offset (used later)
    calibration_log = [abs(hash(str(val)) % 100) for val in sequence_ids]
    avg_calibration = sum(calibration_log[:5]) / 5 if len(calibration_log) >= 5 else 10

    # Key intermediate values
    baseline_normalization = harmonic_ratio / (avg_calibration + 1)
    dynamic_range = len(filtered_signals) + (signal_chain[0] if signal_chain else 0)

    # Efficiency model with lambda-based adaptation
    adapt_function = lambda x: 0.8 + (0.4 / (1 + x / 10))
    efficiency_factor = adapt_function(baseline_normalization)

    # Purity metric derived from processed signals
    purity_score = sum(1 for e in clipped_energy if e > 40)
    fallback_purity = len([x for x in signal_chain if x % 7 == 0])
    net_purity = purity_score or fallback_purity or 1

    # MISLEADING alternate path (dead code)
    if False:  # Never executed
        backup_system = {"yield": 0}
        for k in backup_system:
            backup_system[k] += net_purity * 0.5
        efficiency_factor = 0.6  # Would override, but never reached

    # CRITICAL STATEMENT
    filtration_yield = net_purity * efficiency_factor

    # Output required format
    print(f"Result: {filtration_yield}")

    return filtration_yield

# Input data crafted to produce deterministic outcome
input_sequence = [45, 67, 89, 105, 33, 42, 76, 112, 58, 91]
analyze_compound_sequence(input_sequence)