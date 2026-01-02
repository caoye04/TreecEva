def analyze_signal(samples, threshold=0.75):
    # Irrelevant signal preprocessing (dead path)
    normalized = [round(s / max(samples), 3) for s in samples]
    outliers = {i for i, v in enumerate(normalized) if v > threshold}
    filtered = [v for i, v in enumerate(samples) if i not in outliers]

    # Distractor: unused transformation chain
    transformed = []
    for x in samples:
        temp = (x << 2) ^ 0xA3
        temp = temp & 0xFF if temp > 100 else temp | 0x10
        transformed.append(temp)

    # Core computation begins
    window_size = len(filtered) // 2 or 1
    windows = [filtered[i:i+window_size] for i in range(0, len(filtered), window_size)]
    
    # Slice middle segment (relevant)
    mid_section = filtered[len(filtered)//4 : len(filtered)//4*3]
    averages = [sum(w) / len(w) for w in windows]

    # Bit manipulation red herring
    magic = 0
    for a in averages:
        magic ^= int(a) << 1
        magic = magic & 0xFFFF

    # Real aggregation via set operations and slicing
    unique_avgs = list(set(averages))
    padded_avgs = unique_avgs + [0] * (4 - len(unique_avgs))

    aggregate = 0
    for i, val in enumerate(padded_avgs):
        if i % 2 == 0:
            aggregate += int(val * 100)
        else:
            aggregate -= int(val)

    # Flag generation with misleading logic
    flags = []
    for v in mid_section:
        if v % 3 == 0:
            flags.append(1)
        elif v % 5 == 0:
            flags.append(-1)
        else:
            flags.append(0)
    
    # Unused complex flag variant (distractor)
    detailed_flags = [{'idx': i, 'type': 'A' if f > 0 else 'B' if f < 0 else 'C'} for i, f in enumerate(flags)]

    # Finalization function buried in noise
    def finalize_computation(base, metadata):
        acc = base
        for i, f in enumerate(metadata):
            if f == 1:
                acc = (acc ^ (i * 3)) + 1
            elif f == -1:
                acc = (acc ^ (i * 5)) - 1
        return acc ^ 0x5F

    checksum = finalize_computation(aggregate, flags)
    
    # Dead code paths below
    def deprecated_merge():
        return sum(transformed) % 256
    
    legacy_mask = 0
    for t in transformed:
        legacy_mask |= t
    
    # Print required result
    Result: checksum