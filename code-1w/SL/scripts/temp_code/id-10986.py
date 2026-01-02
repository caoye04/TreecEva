def analyze_signal_integrity(raw_frames, baseline_threshold=0.75):
    # Irrelevant preprocessing stub
    normalized_frames = [f * 0.98 for f in raw_frames if f > 0.1]
    spike_count = sum(1 for x in normalized_frames if x > 1.5)
    
    # Distractor: unused transformation path
    def temporal_shift(data, shift=2):
        return data[-shift:] + data[:-shift]

    shifted_data = temporal_shift(normalized_frames)  # Dead assignment

    # Real processing begins: filter valid pulses
    valid_pulses = [p for p in normalized_frames if p >= baseline_threshold]
    
    # Distractor: fake entropy calculation (never used)
    import math
    def shannon_entropy(seq):
        freqs = {}
        for s in seq:
            freqs[s] = freqs.get(s, 0) + 1
        return -sum(f/len(seq)*math.log2(f/len(seq)) for f in freqs.values())
    
    entropy_metric = shannon_entropy(valid_pulses) if valid_pulses else 0.0  # Unused

    # Chain of relevant transformations
    pulse_energy = sum([e**2 for e in valid_pulses])
    compression_ratio = len(raw_frames) / len(valid_pulses) if valid_pulses else 0

    # Simulated hardware latency compensation (irrelevant but plausible)
    timing_buffer = [0.001 * i for i in range(len(valid_pulses))]
    adjusted_energy = pulse_energy - sum(timing_buffer)

    # Intermediate diagnostic hash based on length patterns
    frame_signatures = [str(int(f * 100)) for f in valid_pulses]
    signature_lengths = [len(s) for s in frame_signatures]
    length_variance = sum((x - sum(signature_lengths)/len(signature_lengths))**2 for x in signature_lengths) / len(signature_lengths) if signature_lengths else 0

    # Fake checksum with string manipulation red herring
    checksum_str = ''.join(frame_signatures).replace('0', 'X').lstrip('X')
    checksum_digit_sum = sum(int(c) for c in checksum_str if c.isdigit())  # Looks important, unused

    # Critical data structure: processing chain history
    processing_chain = {
        'input_size': len(raw_frames),
        'filtered': len(valid_pulses),
        'energy': adjusted_energy,
        'stability': 1 / (length_variance + 0.01),
        'compression': compression_ratio
    }

    # Diagnostic flags with bit-flag pattern (mostly irrelevant)
    DIAG_FLAGS = {
        'NOISE_CLEARED': 1 << 0,
        'PULSES_FOUND': 1 << 1,
        'THRESHOLD_MET': 1 << 2,
        'BUFFER_APPLIED': 1 << 3,
        'ENTROPY_CHECKED': 1 << 4
    }

    active_flags = DIAG_FLAGS['NOISE_CLEARED'] | DIAG_FLAGS['PULSES_FOUND'] | DIAG_FLAGS['THRESHOLD_MET']

    # Distractor: unused flag validation tree
    def validate_diagnostics(flags):
        issues = []
        if not (flags & DIAG_FLAGS['NOISE_CLEARED']):
            issues.append('Noise filter bypassed')
        if not (flags & DIAG_FLAGS['PULSES_FOUND']):
            issues.append('No pulses detected')
        return issues
    
    validation_report = validate_diagnostics(active_flags)  # Computed but unused

    # Actual diagnostics tuple (used later)
    diagnostics = (
        len(valid_pulses) > 0,
        adjusted_energy > 5.0,
        compression_ratio < 10.0,
        length_variance < 0.5
    )

    # Core aggregation function embedded to increase nesting
    def aggregate_metrics(chain, status):
        base_score = chain['energy'] * chain['stability']
        
        # Multi-step weighting logic with red herrings
        modifiers = [0.85, 1.1, 0.95, 1.0]
        adjustment = 1.0
        for i, cond in enumerate(status):
            if cond:
                # Distractor: complex string-based condition that doesn't affect outcome
                cond_str = str(cond).lower()
                if 'r' in cond_str:
                    adjustment += 0.05
                adjustment *= modifiers[i]  # Only this matters
        
        # Decoy calculation
        phantom_score = base_score * (1 + sum(ord(c) for c in checksum_str[:3]) / 1000) if checksum_str else base_score
        
        # Final score (only base_score and adjustment matter)
        return int(base_score * adjustment)

    final_diagnostic = aggregate_metrics(processing_chain, diagnostics)
    print(f"Result: {final_diagnostic}")