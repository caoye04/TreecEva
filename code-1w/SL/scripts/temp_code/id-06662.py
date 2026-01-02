def process_signal_chain(raw_input, threshold_level):
    # Irrelevant signal preprocessing (distractor)
    normalized = [x % 256 for x in raw_input if x > 0]
    filtered = [x for x in normalized if x < threshold_level]
    aggregated = sum(filtered) * 0.9

    # Dead code path - never executed due to condition (red herring)
    if len(normalized) > 1000:
        backup_state = {i: normalized[i] for i in range(0, len(normalized), 10)}
        for k in backup_state:
            backup_state[k] = backup_state[k] ** 2

    # Actual relevant computation begins
    signal_map = {}
    for i, val in enumerate(filtered):
        if i % 3 == 0:
            signal_map[i] = val ^ 240  # Bitwise manipulation
        elif i % 5 == 0:
            signal_map[i] = val // 3 + 17

    # Use of set operations (required feature)
    indices_set = set(signal_map.keys())
    multiples_of_3 = {i for i in indices_set if i % 3 == 0}
    multiples_of_5 = {i for i in indices_set if i % 5 == 0}
    overlapping = multiples_of_3.intersection(multiples_of_5)

    # Decoy transformation with string methods (required feature)
    status_log = "Signal analysis complete. Status: OK"
    if status_log.endswith("OK"):
        tokens = status_log.split(' ')
        coded = ''.join([t[0] for t in tokens if len(t) > 0]).lower()
        checksum = hash(coded) % 1000  # Irrelevant derived value

    # Complex but relevant data aggregation
    accumulator = 0
    for idx in sorted(signal_map.keys()):
        if idx in overlapping:
            accumulator += signal_map[idx] * 2
        elif idx in multiples_of_3:
            accumulator += signal_map[idx] + 11
        elif idx in multiples_of_5:
            accumulator -= signal_map[idx]

    return int(accumulator % 97)


def encrypt_sequence(seq, key):
    # Unused encryption function (dead code path)
    rotated = [((x << 2) | (x >> 6)) & 255 for x in seq]
    return [rotated[i] ^ key for i in range(len(rotated))]


def analyze_pattern(signals, key):
    # Core logic with multiple nested steps
    base_value = process_signal_chain(signals, 200)

    # Simulate diagnostic fingerprint using string method and set logic
    fingerprint_str = f"DIAG_{base_value}_{key}"
    char_set = set(fingerprint_str)
    digit_chars = {c for c in char_set if c.isdigit()}
    digit_sum = sum(int(d) for d in digit_chars)

    # Secondary transformation chain
    temp_seq = []
    for i in range(len(digit_chars)):
        temp_seq.append((base_value * (i + 1)) ^ key)

    # Redundant list processing
    processed_temp = [x for x in temp_seq if x % 2 == 1]
    if len(processed_temp) > 3:
        sliced = processed_temp[1:4]
        correction = sum(sliced) // len(sliced)
    else:
        correction = 0

    # Final computation with distractor variables
    noise_floor = 42  # Misleading constant
    calibration_offset = sum(ord(c) for c in fingerprint_str) % 50  # Distractor
    final_diagnostic = (base_value + digit_sum - correction) % 10000

    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


# Main execution context
if __name__ == "__main__":
    # Input signal data
    collected_signals = [
        150, 180, 210, 240, 270, 300, 330, 360,
        120, 140, 160, 190, 220, 250, 280, 310
    ]
    system_key = 83

    # Trigger main analysis
    final_diagnostic = analyze_pattern(collected_signals, system_key)