def analyze_data_stream(raw_input):
    # Preprocess input: filter and transform
    cleaned = ''.join(ch for ch in raw_input if ch.isdigit() or ch in ['-', '+'])
    segments = cleaned.split('+')

    # Irrelevant transformation branch (dead path)
    if len(segments) > 100:
        normalized = [s[::-1] for s in segments]
    else:
        normalized = segments  # This is always taken

    # Extract numeric values, ignore invalid
    values = []
    for seg in normalized:
        try:
            num = int(seg)
            if -1000 < num < 1000:
                values.append(num)
        except ValueError:
            continue

    # Decoy statistical analysis (unused)
    avg_magnitude = sum(abs(v) for v in values) / len(values) if values else 0
    outlier_threshold = avg_magnitude * 1.5

    # Real logic begins: find first valid subsequence meeting criteria
    candidate = None
    for i in range(len(values) - 4):
        window = values[i:i+5]
        if sum(window) % 7 == 0 and window[2] > 0:
            candidate = window
            break

    # Unused alternate logic path (misleading)
    if not candidate:
        temp = [v for v in values if v % 2 == 0]
        if len(temp) >= 5:
            candidate = temp[:5]

    # Final processing only if candidate found
    if candidate:
        base_value = candidate[0] * candidate[4]
        shift_amount = abs(candidate[2]) % 6

        # Bit manipulation chain
        shifted = base_value << shift_amount
        flipped = shifted ^ 0b101010
        masked = flipped & 0xFFFF

        # Secondary adjustment from string properties
        length_component = len(raw_input.strip()) % 13
        adjustment = (length_component ** 2) + 7

        # Checksum computation with slicing red herring
        reversed_str = raw_input[::-1]
        slice_sum = sum(ord(c) for c in reversed_str[::3])  # Distractor

        # Set operations with irrelevant data
        unique_digits = set(raw_input) - {'+', '-', '0'}
        digit_count_bonus = len(unique_digits) * 3  # Not used

        # Key statement
        mask = 0xFF
        checksum = (masked ^ adjustment) & mask
    else:
        checksum = 0

    # Redundant post-processing (never reached due to structure)
    final_scaling = 1.0
    for factor in [1.1, 1.2, 1.3]:
        final_scaling *= factor
        if final_scaling > 1.5:
            break

    # Output result
    print(f"Result: {checksum}")
    return checksum

# Input with controlled properties
input_data = "+-123+456+789+101+202+303+404"
analyze_data_stream(input_data)