def analyze_signal_pattern(raw_data):
    # Irrelevant pre-processing: frequency normalization (unused later)
    normalized = [x * 0.987 for x in raw_data if x > 5]
    baseline = sum(normalized) / len(normalized) if normalized else 0

    # Distractor: complex filter that's not used in final computation
    filtered_peaks = [i for i, x in enumerate(raw_data) if x > 10 and i % 2 == 1]
    peak_map = {i: raw_data[i] ** 0.5 for i in filtered_peaks}

    # Real path begins: extract even-indexed values above threshold
    candidates = [x for i, x in enumerate(raw_data) if i % 2 == 0 and x > 7]

    # Misleading transformation chain (partially unused)
    transformed = []
    shift_key = 0
    for val in candidates:
        if val % 3 == 0:
            shift_key += 2
        elif val % 3 == 1:
            shift_key -= 1
        transformed.append((val << 1) ^ 5)

    # Dead code path: never executed due to logic, but looks important
    if len(transformed) > 100:
        transformed = [t + baseline for t in transformed]

    # Core logic hidden among noise: build valid sequence using slicing and conditions
    trimmed = transformed[1:-1] if len(transformed) > 2 else transformed
    valid_sequence = []
    for t in trimmed:
        if t & 1:  # only odd values proceed
            valid_sequence.append(t)

    # Decoy checksum from unused branch
    dummy_checksum = sum(peak_map.values()) * 0.5 if peak_map else 0

    # Adjustment computed via bitwise and logical ops (looks like red herring)
    flags = [shift_key & 1, len(filtered_peaks) > 5, len(candidates) % 4 == 0]
    adjustment = 17
    if flags[0] and not flags[1]:
        adjustment ^= 23
    if not flags[0] or flags[2]:
        adjustment += 19
    adjustment = (adjustment ^ len(valid_sequence)) | 7

    # Key statement — answer depends on this
    checksum = (valid_sequence[-1] ^ adjustment) % 883

    # Final red herring: conditional override that doesn't trigger
    if all(f == False for f in flags) or dummy_checksum > 1000:
        checksum = -1

    # Output target result
    print(f"Result: {checksum}")
    return checksum

# Simulate input with deterministic signal
input_data = [6, 12, 8, 15, 9, 21, 10, 24, 14, 30, 11, 33, 13, 36, 16, 39]
analyze_signal_pattern(input_data)