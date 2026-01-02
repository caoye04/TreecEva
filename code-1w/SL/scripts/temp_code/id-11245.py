def analyze_data_stream(raw_samples):
    # Irrelevant pre-processing: normalize signal (unused later)
    normalized = [round(x * 0.98 + 0.5, 2) for x in raw_samples if x > -1]
    temp_flags = [1 if i % 3 == 0 else 0 for i in range(len(raw_samples))]

    # Decoy statistical analysis (never used)
    avg_sample = sum(raw_samples) / len(raw_samples) if raw_samples else 0
    variance_proxy = sum((x - avg_sample) ** 2 for x in raw_samples) / len(raw_samples) if raw_samples else 0
    outlier_threshold = avg_sample + 1.5 * (variance_proxy ** 0.5)

    # Unused transformation path
    transformed = []
    for idx, val in enumerate(raw_samples):
        if val < 0:
            transformed.append(abs(val) ** 0.5 * -1)
        elif val == 0:
            transformed.append(0)
        else:
            transformed.append(val ** 0.5)

    # Dead function — looks important but unused
    def compute_legacy_hash(data):
        h = 0
        for d in data:
            h = (h * 31 + int(d)) & 0xFFFFFFFF
        return h

    # Actual relevant logic starts here
    valid_entries = [v for v in raw_samples if v >= 0]  # Filter non-negative
    filtered_with_index = list(enumerate(valid_entries))
    paired_data = list(zip([x * 2 for x in valid_entries[::2]], [y // 2 for y in valid_entries[1::2]]))

    # Key state variables
    checksum = 0xAAAA
    sequence_state = [0] * 4
    trigger_mask = 0x5555

    # Main processing loop with critical statement
    for i, val in filtered_with_index:
        if val % 7 == 0:
            # Red herring branch
            temp_offset = (i * 3) % 17
            adjusted = val ^ temp_offset
            processed_value = adjusted >> 1
        elif val % 2 == 0:
            processed_value = val ^ 0xFF
        else:
            processed_value = val << 1

        # Update sequence state (some entries are irrelevant)
        sequence_state[i % 4] = (processed_value ^ checksum) & 0xFF

        # Critical update point — this is where we need the value
        checksum = (checksum << 1) ^ processed_value & 0xFFFF

        # Extra misleading manipulation that doesn't affect final checksum
        if i % 4 == 3:
            checksum = (checksum ^ trigger_mask) & 0xFFFF
            checksum = (checksum >> 2) | ((checksum & 0x03) << 14)

        # Spurious secondary checksum (distractor)
        rolling = 0
        for j in range(min(i+1, 4)):
            rolling = (rolling * 3) ^ sequence_state[j]

    # Final post-processing unrelated to target variable
    if len(valid_entries) > 10:
        checksum = checksum ^ 0xFFFF
    else:
        checksum = checksum & 0x7FFF

    # Output the target variable
    print(f"Result: {checksum}")

# Input data (deterministic)
data_stream = [12, 7, 0, 14, 3, 8, 21, 5, 9, 11, 4, 6, 13, 2, 10]
analyze_data_stream(data_stream)