def compute_network_efficiency(nodes, sizes, rates):
    # Distractor: unused calculation for network latency
    latency_estimate = sum(sizes) / len(rates) * 3.14
    
    # Distractor: misleading variable for bandwidth allocation
    bandwidth_factor = (max(rates) - min(rates)) * len(nodes)
    
    # Relevant: process active transmission metrics
    transmission_pairs = list(zip(sizes, rates))
    successful_transmissions = []
    
    for i, (size, rate) in enumerate(transmission_pairs):
        # Distractor: dead code path for packet loss simulation
        if size > 1500:
            packet_loss = size * 0.1
        
        # Relevant: calculate throughput for each transmission
        if rate > 50:
            throughput = (size * rate) / 1024
            successful_transmissions.append(throughput)
        else:
            # Distractor: misleading low-rate calculation
            degraded_throughput = size * 0.5
    
    # Distractor: unused network capacity calculation
    network_capacity = sum(rates) * 2.5
    
    # Relevant: compute final throughput with quality adjustment
    if successful_transmissions:
        avg_throughput = sum(successful_transmissions) / len(successful_transmissions)
        quality_factor = len([n for n in nodes if n % 2 == 0]) / len(nodes)
        final_result = avg_throughput * quality_factor
    else:
        # Distractor: misleading fallback calculation
        final_result = bandwidth_factor * 0.1
    
    return round(final_result, 2)

# Main execution
active_nodes = [1, 2, 3, 4, 5, 6]
packet_sizes = [512, 1024, 768, 1536, 896, 1280]
transmission_rates = [75, 45, 90, 60, 85, 55]

# Distractor: unused network topology calculation
topology_complexity = len(active_nodes) ** 2 / 3

# Target calculation
final_throughput = compute_network_efficiency(active_nodes, packet_sizes, transmission_rates)

# Distractor: misleading alternative calculation
alternative_throughput = (sum(packet_sizes) * sum(transmission_rates)) / 10000

print(f"Result: {final_throughput}")