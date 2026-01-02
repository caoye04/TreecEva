def compute_diagnostic_score():
    # Simulate a system health diagnostic with embedded logic chain
    raw_signals = [12, 45, 23, 67, 89, 34, 56, 78, 91, 103]
    
    # Irrelevant signal smoothing (dead-end computation)
    smoothed = [raw_signals[i] + (raw_signals[i-1] + raw_signals[(i+1) % len(raw_signals)]) // 2 
                for i in range(len(raw_signals))]
    normalized = [val / max(smoothed) * 100 for val in raw_signals]  # Distractor normalization

    # Key parameters (some are decoys)
    threshold = 42
    prime_base = 101  # Used in final step
    scaling_factor = 3.14159  # Unused red herring
    fallback_mode = False  # Misleading flag
    debug_trace = []  # Dead data collection path

    # Complex preprocessing with conditional expressions
    filtered = [x for x in raw_signals if x > threshold]
    shifted = [((val << 2) & 0xFF) ^ 17 for val in filtered]  # Bit manipulation red herring

    # Real computation begins: accumulation with slicing-dependent logic
    segment = shifted[1:6]  # Critical slice — depends on filtered/shifted
    backup_accum = sum([x * 2 for x in segment if x % 2 == 0])  # Distractor sum

    # Core logic chain (8–12 steps)
    accumulated = 0
    for index, value in enumerate(segment):
        if index % 2 == 0:
            accumulated += value * (index + 1)
        else:
            accumulated -= (value >> 1)
        
        # Conditional expression used idiomatically
        status_flag = 'valid' if accumulated > 0 else 'recovery'
        debug_trace.append(f'{status_flag}:{accumulated}')  # Logged but unused

        # Early termination red herring
        if accumulated > 1000:
            accumulated = 999  # Never reached due to values
            break

    # Decoy transformation chain
    temp_result = ''.join([chr(val % 90 + 32) for val in segment[:3]])
    hash_candidate = sum([ord(c) * (i+1) for i, c in enumerate(temp_result)])  # Fake checksum

    # Offset derived from original raw signal properties (relevant)
    offset = len([x for x in raw_signals if x % 2 == 1]) * 7  # Count odd values

    # Final critical statement
    checksum = (accumulated ^ offset) % prime_base

    # Output requirement
    print(f"Result: {checksum}")

compute_diagnostic_score()