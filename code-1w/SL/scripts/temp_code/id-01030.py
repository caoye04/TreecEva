def analyze_data_stream(data_packets, thresholds):
    # Irrelevant preprocessing: base conversion noise
    hex_mapping = {i: hex(i)[2:] for i in range(16)}
    decoy_counter = 0
    for i in range(len(data_packets)):
        if data_packets[i] > 10:
            decoy_counter += int(hex_mapping.get(data_packets[i] % 10, '0'), 16)

    # Distractor: fake checksum with unused result
    fake_checksum = 0
    for byte in b'ignored_payload':
        fake_checksum = (fake_checksum * 31 + byte) % 10007

    # Real logic begins: filter packets by dynamic threshold
    dynamic_threshold = sum(thresholds) / len(thresholds)
    size_map = {}
    for packet in data_packets:
        size_key = packet // 10 * 10
        size_map[size_key] = size_map.get(size_key, 0) + 1

    # Secondary distractor: sorting unrelated metadata
    metadata = [(v, k) for k, v in size_map.items()]
    metadata.sort(reverse=True)  # Unused sort result

    # Core logic masked by enumeration and zip red herrings
    processed = []
    indices = list(range(len(data_packets)))
    for idx, (packet, _) in enumerate(zip(data_packets, indices)):
        if packet < dynamic_threshold:
            processed.append(packet * 2)
        elif packet == dynamic_threshold:
            processed.append(packet)
        else:
            processed.append(packet // 2)

    # Another decoy: bit manipulation with no effect
    bit_cascade = 0
    for i in range(8):
        bit_cascade ^= (bit_cascade << 1) | 1
        bit_cascade &= 0xFF

    # Actual filtering based on frequency and parity (hidden requirement)
    frequency_filtered = []    
    for val in processed:
        freq = size_map.get(val // 10 * 10, 0)
        if freq >= 2 and val % 2 == 0:
            frequency_filtered.append(val)

    # Critical line: answer depends on this sum
    valid_entries = [x for x in frequency_filtered if x > 15]
    filtered_sum = sum(valid_entries)

    # Final red herring: complex string transformation
    log_entry = ""
    for i, char in enumerate('diagnostic_trace'):
        shift = i % 3
        log_entry += char.upper() if shift == 1 else char.lower()
    
    # Output the target result
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Inputs
packets = [12, 15, 12, 25, 15, 30, 12, 8, 25, 15]
thresh = [10, 20, 15]

result = analyze_data_stream(packets, thresh)