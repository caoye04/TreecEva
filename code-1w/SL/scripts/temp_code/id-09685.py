def analyze_signal_packet(raw_stream):
    # Irrelevant signal preprocessing (dead path)
    filtered_noise = [x for x in raw_stream if x > -50 and x < 50]
    normalized = [round(x / 2.3, 2) for x in filtered_noise]
    spike_count = len([x for x in normalized if x > 40])

    # Distractor: Fake checksum using string slicing
    stream_label = 'SIG-PRIME-9'
    segment_code = stream_label[4:8]
    fallback_key = len(segment_code) * 113

    # Real data path begins
    payload = raw_stream[::2]  # Every other sample
    data_sum = sum(payload)

    # Metadata extraction with bit manipulation red herring
    flags = 0b110101
    mode_flag = flags & 0b1111
    debug_mask = flags >> 4
    metadata_key = mode_flag ^ 256  # Key is 261

    # Decoy dictionary with misleading entries
    diagnostics = {
        'status': 'nominal',
        'phase': 3,
        'reading': spike_count,
        'fallback': fallback_key,  # 452, irrelevant
        'history': [120, fallback_key, spike_count]
    }

    # Set operations - actual use
    readings_set = set(payload)
    outlier_check = set(range(0, 100, 7))  # multiples of 7 under 100
    overlaps = readings_set.intersection(outlier_check)
    adjustment = len(overlaps) * 17

    # Real calculation chain
    data_sum += adjustment  # Modify based on overlap count

    # Critical statement
    checksum = (data_sum ^ metadata_key) % 9791

    # Dead-end conditional (never reached in normal execution)
    if diagnostics['phase'] > 5:
        checksum = fallback_key % 1009
        temp = [x for x in raw_stream if x in readings_set and x % 2 == 0]
        checksum += len(temp)

    # Unused recursive helper (distractor)
    def integrate_series(n):
        if n <= 1:
            return n
        return integrate_series(n-1) + integrate_series(n-2)

    return checksum

# Input data
transmission = [123, -45, 89, 102, 77, 156, 211, -67, 94, 113]

# Execution
result = analyze_signal_packet(transmission)
print(f"Result: {result}")