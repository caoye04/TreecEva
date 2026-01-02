def analyze_sensor_data(raw_readings, calibration_sequence):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.005 for x in raw_readings if x > 0]
    filtered = [y for y in normalized if y < 1000]
    temp_cache = set()
    for val in filtered:
        temp_cache.add(round(val % 7))

    # Meaningful but misleading intermediate (red herring)
    peak_magnitude = max(filtered) if filtered else 0
    decay_rate = 0.98
    smoothed = peak_magnitude
    for _ in range(5):
        smoothed *= decay_rate  # Not actually used later

    # Complex data transformation with conditional logic
    transformed = []
    for i, x in enumerate(calibration_sequence):
        if i % 3 == 0:
            transformed.append(x ** 2)
        elif i % 3 == 1:
            transformed.append(x + 7)
        else:
            transformed.append(abs(x - 15))

    # Set operations and string-based filtering (required python features)
    valid_flags = {'A', 'C', 'D', 'F'}
    status_log = "ACDFB"  # Used to filter via string method
    active_indices = [i for i, c in enumerate(status_log) if c in valid_flags]

    # Destructuring and multiple assignments (variable assignment concept)
    (base_anchor, *remaining_data, fallback) = sorted(transformed)
    offset_value = len(active_indices) * 3

    # Bit manipulation red herring
    bit_accumulator = 0
    for val in raw_readings[:4]:
        bit_accumulator ^= int(val) & 0xF
        bit_accumulator <<= 1
        if bit_accumulator > 255:
            bit_accumulator >>= 4

    # Unused recursive function (dead code path)
    def recursive_sum(n):
        return n + recursive_sum(n - 1) if n > 0 else 0  # Never called

    # Actual relevant computation chain (nested 4 levels)
    aggregate_measure = 0
    for reading in raw_readings:
        if reading < 50:
            continue
        adjusted = reading * 0.9
        for t_val in transformed:
            if t_val <= 0:
                continue
            contribution = (adjusted / t_val) * 100
            if contribution > 200:
                break
            aggregate_measure += contribution

    # Conditional expression and core logic
    correction_factor = 1.75 if 'D' in status_log.upper().strip() else 0.85

    # Key execution point
    final_diagnostic = aggregate_measure * correction_factor + offset_value

    # Print required output
    print(f"Result: {final_diagnostic}")

    # Decoy output variables
    diagnostic_checksum = sum(int(d) for d in str(int(final_diagnostic)) if d != '9')
    print(f"Checksum (irrelevant): {diagnostic_checksum}")

    return final_diagnostic

# Inputs (deterministic)
readings = [65, 88, 42, 91, 77, 53, 95]
calib_seq = [3, 14, 18, 5, 9, 2]

# Execute
result = analyze_sensor_data(readings, calib_seq)