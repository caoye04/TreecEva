def analyze_data_stream():
    # Simulate a data stream with packet sizes and types
    packets = [128, 64, 256, 32, 512, 16, 1024, 256, 64]
    packet_types = ['control', 'data', 'data', 'control', 'data', 'control', 'data', 'data', 'control']

    # Track inflow and outflow based on direction flags (simulated)
    directions = [1, -1, 1, 1, -1, -1, 1, -1, 1]  # 1 = inbound, -1 = outbound

    inflow_packets = []
    outflow_packets = []

    control_packet_sizes = []
    data_packet_sizes = []

    # Misleading: counting characters in type labels (irrelevant)
    total_chars = 0
    for ptype in packet_types:
        total_chars += len(ptype)  # Distractor: not used later

    # Classify packet sizes by type (semi-relevant, but only size matters)
    for i in range(len(packets)):
        if packet_types[i] == 'control':
            control_packet_sizes.append(packets[i])
        else:
            data_packet_sizes.append(packets[i])

    # Route packets based on direction
    for i in range(len(directions)):
        if directions[i] == 1:
            inflow_packets.append(packets[i])
        else:
            outflow_packets.append(packets[i])

    # Perform checksum (irrelevant to final result)
    checksum = 0
    for val in packets:
        checksum ^= val  # Bitwise XOR chain - red herring

    # Compute sums
    inflow_sum = sum(inflow_packets)
    outflow_sum = sum(outflow_packets)

    # Key assignment point
    net_flow = inflow_sum - outflow_sum

    # Extra state tracking (distractor)
    unique_sizes = set(packets)
    duplicate_count = len(packets) - len(unique_sizes)

    # Additional irrelevant computation
    avg_data_size = sum(data_packet_sizes) / len(data_packet_sizes) if data_packet_sizes else 0

    return net_flow

result = analyze_data_stream()
print(f"Result: {result}")