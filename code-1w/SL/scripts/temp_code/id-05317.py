def analyze_sensor_stream(raw_input):
    # Irrelevant preprocessing: format cleaning
    cleaned = raw_input.strip().replace(' ', '').lower()
    segments = cleaned.split(',')

    # Decoy statistical analysis (never used)
    avg_length = sum(len(s) for s in segments) / len(segments) if segments else 0
    outlier_flags = [s for s in segments if 'err' in s]
    temp_registry = {f'entry_{i}': len(s) for i, s in enumerate(segments)}

    # Actual relevant data extraction
    numeric_values = []
    for seg in segments:
        if seg.isdigit():
            numeric_values.append(int(seg))
        elif seg.startswith('0x') and len(seg) > 2:
            try:
                numeric_values.append(int(seg, 16))
            except ValueError:
                pass

    # Misleading transformation chain (partially unused)
    squared_chain = [x**2 for x in numeric_values if x > 0]
    shifted_view = [(x >> 1) for x in squared_chain]
    masked_result = [x & 0xFF for x in shifted_view]  # Only last step matters

    # Dead code path: complex but irrelevant checksum
    def compute_legacy_checksum(data):
        chk = 0
        for val in data:
            chk = (chk << 1) ^ val
            if chk > 255:
                chk = chk % 251
        return chk
    legacy_chk = compute_legacy_checksum(numeric_values)  # Unused

    # Core logic disguised among noise
    filtered_data = [x for x in masked_result if x % 2 == 1]  # Keep odd values

    # Dictionary-based threshold routing (used)
    threshold_map = {
        'low': 15,
        'medium': 45,
        'high': 85
    }

    # Red herring: unused normalization
    normalized = []
    base_offset = min(filtered_data) if filtered_data else 1
    for val in filtered_data:
        norm_val = round((val - base_offset) / base_offset, 3)
        if norm_val > 0.5:
            normalized.append(norm_val)
    scale_factor = len(normalized) if normalized else 1  # Distractor

    # Actual processing function
    def process_readings(data_list, thresholds):
        count_low = len([v for v in data_list if v < thresholds['low']])
        count_med = len([v for v in data_list if thresholds['medium'] >= v >= thresholds['low']])
        count_high = len([v for v in data_list if v > thresholds['high']])

        # Complex weighting with bit manipulation
        weight_a = (count_low << 2)  # Multiply by 4
        weight_b = (count_med * 3) + (count_med & 1)  # Multiply by 3, add parity
        weight_c = count_high ** 2  # Square high counts

        # Combine using XOR to obscure relationship
        intermediate = (weight_a ^ weight_b) + weight_c

        # Final adjustment based on string pattern in original input
        flag_char = raw_input[5] if len(raw_input) > 5 else 'a'
        ascii_offset = ord(flag_char) % 7
        result = intermediate - ascii_offset

        # One more red herring: unused recursive filter
        def deep_filter(arr, depth=0):
            if depth >= 2 or not arr:
                return [0]
            return deep_filter([x-1 for x in arr if x > 1], depth+1)
        decoy_sum = sum(deep_filter(filtered_data))  # Never affects result

        return result

    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output requirement
    print(f"Target result: {final_diagnostic}")