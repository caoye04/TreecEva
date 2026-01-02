def calculate_efficiency(load_profile):
    base_efficiency = 98.5
    overhead = 2.3
    adjustment_factor = 0.75
    
    # Compute dynamic efficiency based on load
    adjusted_load = sum([x ** 0.5 for x in load_profile if x > 10])
    
    # Efficiency degrades logarithmically with high load
    if adjusted_load > 50:
        degradation = 10 * (adjusted_load / 50) ** 0.5
    else:
        degradation = 5 if adjusted_load > 30 else 0
    
    final_efficiency = base_efficiency - degradation - overhead
    return round(final_efficiency, 3)

# System network data
node_bandwidths = [15, 22, 8, 34, 11, 45, 19]
packet_sizes = [512, 256, 1024, 768]
latency_log = [12.3, 14.1, 11.9, 15.2]

# Simulate network load from active nodes
network_load = [bw * 2 for bw in node_bandwidths if bw >= 15]

# Irrelevant metric (distractor)
average_packet_size = sum(packet_sizes) / len(packet_sizes)

energy_threshold = 0
energy_threshold = calculate_efficiency(network_load)

print(f"Result: {energy_threshold}")