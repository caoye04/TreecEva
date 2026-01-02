from collections import defaultdict, Counter

# Simulated sensor data processing with error correction and redundancy checks
def process_sensor_readings(raw_data):
    readings = [x for x in raw_data if 0 <= x <= 1023]
    filtered = sorted(readings, reverse=True)[:512]  # Top 512 values

    # Frequency analysis (distractor: not used in final result)
    freq_map = Counter(filtered)
    mode_val = freq_map.most_common(1)[0][0]

    # Segment into high and low bands (partially relevant)
    high_band = [x for x in filtered if x > 512]
    low_band = [x for x in filtered if x <= 256]
    
    # Redundant transformations (distractors)
    scaled_high = [h >> 2 for h in high_band]
    shifted_low = [l << 1 for l in low_band]
    merged_ghost = [scaled_high[i] ^ shifted_low[i % len(shifted_low)] for i in range(min(len(scaled_high), len(shifted_low)))]
    ghost_sum = sum(merged_ghost)  # Dead-end computation

    # Core logic path (4-5 steps)
    base_accum = 0
    for i, val in enumerate(filtered):
        if i % 7 == 0:  # Every 7th element
            base_accum ^= val  # Bitwise accumulation
    
    # Secondary transformation chain
    temp_seq = [filtered[j] for j in range(0, len(filtered), 13)][:100]  # Stride sampling
    running_prod = 1
    for t in temp_seq:
        running_prod = (running_prod * t) % 9973
    
    # Tertiary path: statistical decoy
    avg_val = sum(filtered) / len(filtered) if filtered else 0
    variance_proxy = sum((x - avg_val) ** 2 for x in filtered) / len(filtered) if filtered else 0
    entropy_ghost = 0
    for k in freq_map.values():
        if k > 0:
            entropy_ghost -= (k / len(filtered)) * ((k / len(filtered)) ** 0.5)

    # Actual critical computation path
    valid_sequence = base_accum ^ running_prod
    
    # Misleading adjustment from irrelevant path
    decoy_adjust = int(variance_proxy + entropy_ghost)
    real_adjust_source = [temp_seq[i] for i in range(len(temp_seq)) if i & 1]  # Odd indices
    adjustment = sum(real_adjust_source) & 0xFFFF  # Bit-masked sum
    
    # Final modulus from prime sequence (precomputed)
    primes = [1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091]
    modulus = primes[len(temp_seq) % len(primes)]

    # Key statement
    checksum = (valid_sequence ^ adjustment) % modulus

    # Irrelevant output formatting block (dead code)
    report = defaultdict(str)
    report['status'] = 'OK'
    report['samples'] = len(filtered)
    report['outliers'] = len(readings) - len(filtered)

    # Only this print matters
    print(f"Result: {checksum}")

# Input data generated via deterministic pattern
raw_input_data = [(i * 97) % 1024 + (i * 3) % 7 for i in range(700)]
process_sensor_readings(raw_input_data)