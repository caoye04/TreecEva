def calculate_throughput(nodes, packets):
    throughput = (packets * 8) // nodes
    redundancy_factor = nodes % 3
    return throughput - redundancy_factor

def analyze_connectivity(active_nodes, error_count):
    connectivity_score = active_nodes * 10
    if error_count > 0:
        penalty = error_count * 15
        connectivity_score -= penalty
    else:
        connectivity_score += 5
    return connectivity_score

def final_computation(nodes, packets, errors):
    throughput_result = calculate_throughput(nodes, packets)
    connectivity_result = analyze_connectivity(nodes, errors)
    
    # Distractor calculations
    packet_loss = (errors * 100) // packets if packets > 0 else 0
    node_utilization = (packets * 10) // nodes if nodes > 0 else 0
    
    # Main computation path
    if errors == 0:
        efficiency = (throughput_result * connectivity_result) // 100
    else:
        error_penalty = errors * 8
        efficiency = (throughput_result * connectivity_result) // 100 - error_penalty
    
    # More distractors (dead code)
    theoretical_max = nodes * 100
    optimization_factor = theoretical_max // 4
    
    return efficiency

# Main execution
active_nodes = 12
processed_packets = 96
error_flags = 2

# Distractor variables
network_latency = active_nodes * 3
packet_overflow = processed_packets % 7
protocol_overhead = network_latency + packet_overflow

# Dead code path (unused)
if protocol_overhead > 20:
    optimization_factor = protocol_overhead // 2
else:
    optimization_factor = protocol_overhead * 2

network_efficiency = final_computation(active_nodes, processed_packets, error_flags)

# More irrelevant computations
bandwidth_utilization = (processed_packets * 10) // active_nodes
quality_score = bandwidth_utilization - error_flags

print(f"Result: {network_efficiency}")