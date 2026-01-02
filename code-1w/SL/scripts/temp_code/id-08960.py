def analyze_sensor_stream(raw_input):
    # Irrelevant preprocessing: normalize string format
    cleaned = raw_input.strip().lower().replace('-', '').replace('_', '')
    segments = cleaned.split(',')

    # Distractor variables: parsing unrelated metadata
    version_tag = ''.join([c for c in segments if c.isalpha()])
    timestamp_code = sum(ord(c) for c in version_tag[:3]) if len(version_tag) >= 3 else 0

    # Actual data extraction (mixed with noise)
    readings = []
    for seg in segments:
        if seg.isdigit():
            readings.append(int(seg))
        elif seg.startswith('0x') and len(seg) > 2:
            try:
                readings.append(int(seg, 16))
            except:
                pass

    # Dead code path: never executed due to logic above
    if any(s.startswith('err') for s in segments):
        readings = [0] * len(readings)

    # Redundant transformation chain
    adjusted = [r + 1 for r in readings]
    scaled = [r * 2 for r in adjusted]
    normalized = [r - 2 for r in scaled]  # Cancels previous ops: effectively r*2-2

    # Decoy statistical analysis
    mean_val = sum(normalized) / len(normalized) if normalized else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in normalized) / len(normalized) if normalized else 0
    entropy_approx = len(set(normalized)) / len(normalized) if normalized else 0

    # Critical filtering operation (hidden among distractions)
    threshold = 42
    filtered_data = [x for x in normalized if x > threshold and x % 3 != 1]

    # Unused alternative filter path
    if len(filtered_data) < 5:
        filtered_data = [x for x in normalized if x > 30]

    # Main processing function embedded as inner logic
    def process_readings(data, limit):
        if not data:
            return -1

        # Bit manipulation red herring
        magic_seed = 0b1010
        checksum = 0
        for val in data:
            checksum ^= (val << 1) | (val >> 7)  # Complex-looking but unused

        # Real computation buried here
        valid_count = 0
        temp_result = 1
        for i, val in enumerate(data):
            if i % 2 == 0:  # Only even indices
                temp_result *= (val % 17)  # Non-linear accumulation
            else:
                valid_count += 1

        # Secondary condition with early exit distraction
        if temp_result > 1000:
            temp_result = temp_result // 4

        # Final transformation using string method as pivot
        result_str = f"{temp_result:.0f}"
        digit_sum = sum(int(d) for d in result_str if d.isdigit())
        adjustment = len(result_str.replace('0', ''))  # Counts non-zero digits

        return digit_sum * adjustment  # Actual answer generator

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold)

    # Multiple decoy outputs
    debug_status = f'DIAG-{timestamp_code}-{len(segments)}'
    audit_log = [readings, adjusted, normalized, mean_val]

    # Only this line matters
    print(f"Result: {final_diagnostic}")

# Simulated sensor input with mixed formats and embedded noise
input_stream = "ABC-78,0xFF,xYZ,45,102,0x1A,33,ERR-9,88,0xCD,67"
analyze_sensor_stream(input_stream)