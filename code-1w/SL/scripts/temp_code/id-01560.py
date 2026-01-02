def analyze_data_stream(data_packets, config):
    # Simulate packet integrity analysis with embedded control logic
    base_offset = config['offset']
    threshold = config['threshold']
    temp_buffer = []
    checksum = 0
    overflow_count = 0
    normalization_factor = 1.0

    for i, packet in enumerate(data_packets):
        # Irrelevant normalization (dead computation)
        if len(packet) > threshold:
            normalized = [x / max(packet) for x in packet if x != 0]
            normalization_factor = sum(normalized) / len(normalized)

        # Process only packets with specific length (actual logic branch)
        if len(packet) % 2 == 1:
            shifted_sum = 0
            for val in packet:
                shifted_sum += (val & 0xFF) >> 2

            # Core processing block
            processed_value = shifted_sum ^ base_offset
            temp_buffer.append(processed_value)

            # Checksum update with bitwise mix
            for index, item in enumerate(temp_buffer):
                if item > threshold:
                    item = item % threshold
                # Key statement
                checksum = (checksum << 1) ^ index ^ processed_value

                # Fake error simulation (never triggers due to fixed data)
                if checksum < 0:
                    overflow_count += 1

        else:
            # Dead code path — never executed with current input
            dummy = [x * 2 for x in packet]
            dummy.reverse()

    # Post-processing red herring
    fake_checksum = 0
    for x in temp_buffer:
        fake_checksum += x * x
    fake_checksum = int(fake_checksum ** 0.5)

    # Final irrelevant string transformation
    metadata_str = "packet_log_0x{:04X}".format(len(data_packets))
    parts = metadata_str.split('_')
    suffix = ''.join([p[-1] for p in parts if p.startswith('x')])
    suffix_val = int(suffix, 16) if suffix.isdigit() else 0

    # Output only the real answer
    print(f"Result: {checksum}")

# Input data (fixed for determinism)
packets = [
    [12, 24, 36],
    [48, 60],
    [72, 84, 96, 108, 120],
    [132, 144, 156]
]

config_params = {
    'offset': 13,
    'threshold': 50
}

analyze_data_stream(packets, config_params)