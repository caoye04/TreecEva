def analyze_traffic(flow_data):
    total_packets = sum(flow_data)
    avg_packet_size = round(total_packets / len(flow_data), 2)
    spike_count = 0
    for val in flow_data:
        if val > avg_packet_size * 1.5:
            spike_count += 1
    return spike_count


def calculate_efficiency(routing_matrix):
    efficiency_scores = []
    for row in routing_matrix:
        active_nodes = [x for x in row if x > 0]
        if len(active_nodes) == 0:
            efficiency_scores.append(0.0)
        else:
            efficiency_scores.append(min(active_nodes) / max(active_nodes))
    return sum(efficiency_scores) / len(efficiency_scores)


def optimize_allocation(load_profile, threshold):
    adjusted_load = [x + 5 for x in load_profile]
    temp_buffer = [x for x in adjusted_load if x > threshold]
    scaling_factor = len(temp_buffer) / len(adjusted_load) if adjusted_load else 0
    
    # Distractor: string-based status tracking (not used in final result)
    status_log = ""
    if scaling_factor > 0.5:
        status_log += "High stress detected. "
    else:
        status_log += "Normal operation. "
    status_log = status_log.strip().replace(" ", "_").upper()
    
    # Core logic with modular arithmetic and integer division
    base_sum = sum(temp_buffer)
    mod_shift = base_sum % 7
    normalized = base_sum // 3
    
    # Additional distraction: unused sorting and sequence generation
    dummy_sequence = [i * 2 + mod_shift for i in range(10)]
    dummy_sequence.sort(reverse=True)
    
    # Final computation
    penalty = 0
    for i, val in enumerate(temp_buffer):
        if i % 2 == 0 and val % 2 == 1:
            penalty += 1
    result = normalized - penalty
    return int(result)

# Main execution
base_load = [12, 15, 8, 20, 14, 19, 11]
traffic_spikes = [9, 25, 18, 7, 33, 16]
routing_grid = [[1, 3, 2], [4, 0, 4], [2, 2, 6]]

spike_analysis = analyze_traffic(traffic_spikes)
efficiency_metric = calculate_efficiency(routing_grid)

threshold = 15
final_bandwidth = optimize_allocation(base_load, threshold)

print(f"Result: {final_bandwidth}")