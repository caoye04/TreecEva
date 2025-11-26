def calculate_transmission_interval(throughput, latency):
    return (throughput * 2) + latency

def process_network_config(nodes, packets, redundancy):
    # Irrelevant intermediate calculations
    temp_throughput = nodes * packets * 3
    unused_calc = (temp_throughput >> 2) & 0xFF
    
    # Misleading variable that looks important
    network_load = temp_throughput // redundancy if redundancy else 0
    
    # Dead code path that's never executed
    if network_load > 1000:
        unused_buffer = network_load * 2
    else:
        dummy_var = network_load // 10
    
    # Core logic with multiple operations
    base_capacity = sum([packets * (i + 1) for i in range(nodes)])
    adjusted_capacity = base_capacity - (redundancy * 2)
    
    # Lambda function with conditional expression
    capacity_multiplier = lambda x: x * 3 if x % 2 == 0 else x * 2
    
    # Final calculation with slicing operation
    capacity_values = [adjusted_capacity, network_load, temp_throughput]
    final_value = capacity_multiplier(capacity_values[0:2][-1])
    
    return final_value

# Main execution with irrelevant setup
network_nodes = 4
data_packets = 7
redundancy_factor = 2

# Distractor calculations that don't affect final result
max_throughput = network_nodes * data_packets * 10
latency_estimate = max_throughput // 3
transmission_delay = calculate_transmission_interval(max_throughput, latency_estimate)

# Key execution point
final_capacity = process_network_config(network_nodes, data_packets, redundancy_factor)

# More irrelevant operations
optimization_factor = (transmission_delay & 0xF) | 0x10
network_efficiency = optimization_factor / 2.5

print(f"Target result: {final_capacity}")