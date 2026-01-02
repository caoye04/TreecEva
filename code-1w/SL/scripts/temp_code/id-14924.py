def process_metrics(data_log):
    # Irrelevant transformation - distractor
    temp_data = [x ** 2 for x in data_log if x % 3 == 0]
    offset = sum(temp_data) // len(temp_data) if temp_data else 0

    # Decoy function that's never called
    def decrypt_sequence(seq):
        return [seq[i] ^ (i * 2) for i in range(len(seq))]

    # Unused but plausible-looking aggregation
    baseline = max(data_log) - min(data_log)
    adjustment_factor = round(baseline * 0.15, 3)

    # Relevant logic begins: filtering and scoring
    filtered = list(filter(lambda x: x > 0, data_log))
    if not filtered:
        return 0

    # Bit manipulation red herring
    masked_values = [val & 0xFF for val in filtered]
    checksum = 0
    for v in masked_values:
        checksum ^= v

    # Distracting set operations with no impact
    unique_caps = set([x for x in filtered if x > 50])
    expired_flags = set([x for x in filtered if x < 10])
    interference_set = unique_caps.symmetric_difference(expired_flags)
    dummy_merge = unique_caps.union(expired_flags).difference([checksum])

    # Actual score precursor (hidden among noise)
    raw_total = sum(filtered)
    penalty_rate = len([x for x in filtered if x % 7 == 0])  # subtle condition

    # Another decoy: complex but unused dictionary transformation
    stats_map = {
        'max_val': max(filtered),
        'min_val': min(filtered),
        'range': max(filtered) - min(filtered),
        'outliers': [x for x in filtered if x > 2 * (sum(filtered) / len(filtered))]
    }
    stats_map['enriched'] = {k: (v * 1.1 if isinstance(v, (int, float)) else []) for k, v in stats_map.items()}

    # Core calculation buried in middle
    base_score = raw_total // (penalty_rate + 1)

    # Irrelevant recursive helper (never invoked)
    def trace_decay(val, depth):
        if depth <= 0 or val < 5:
            return val
        return trace_decay(val - (val % 7), depth - 1)

    # Multiple assignments to confuse tracking
    phase, level, tier = 3, base_score % 4, 7
    level_boost = phase * tier // 2

    # Real intermediate values mixed with fake ones
    fudge_factor = 0.85 + (len(interference_set) * 0.01)  # looks influential but isn't
    true_multiplier = 2 if (base_score ^ checksum) & 1 else 1  # uses bit op meaningfully

    provisional = int(base_score * true_multiplier) + level_boost

    # Final ranking depends only on this function call
    def calculate_ranking(points, penalties):
        # Complex but deterministic logic
        scaling = (points + penalties) % 5 + 1
        adjusted = points >> scaling  # right shift based on modulo
        if adjusted == 0:
            return 1
        # Use of dictionary mapping as control flow
        weight_map = {1: 3, 2: 1, 3: 4, 4: 2}
        factor = weight_map.get(scaling, 5)
        return adjusted * factor * (2 if points & 1 else 3)

    points = provisional
    penalties = len([x for x in data_log if x < 0])
    final_score = calculate_ranking(points, penalties)
    
    # Output required format
    print(f"Result: {final_score}")
    return final_score

# Execution entry point with seeded input
log_input = [12, -5, 63, 42, 17, -8, 28, 35, 70, 11, 91, 44]
process_metrics(log_input)