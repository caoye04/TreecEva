def calculate_network_balance():
    # Simulate network packet flow over two channels
    channel_a_packets = [120, 150, 130, 140, 160]
    channel_b_packets = [90, 110, 105, 95, 125]

    # Combine packets using zip and sum per time interval
    total_per_interval = [a + b for a, b in zip(channel_a_packets, channel_b_packets)]

    # Incoming data: only intervals with even index contribute to incoming
    incoming = [total_per_interval[i] for i in range(0, len(total_per_interval), 2)]

    # Outgoing data: odd-indexed intervals represent outgoing traffic
    outgoing = [total_per_interval[i] for i in range(1, len(total_per_interval), 2)]

    # Key computational step
    net_flow = sum(incoming) - sum(outgoing)

    # Irrelevant auxiliary variable (minimal distraction)
    avg_flow = sum(total_per_interval) / len(total_per_interval)

    print(f"Result: {net_flow}")

calculate_network_balance()