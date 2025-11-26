def analyze_network_traffic(packets, latency_threshold=100):
    # Distractor: Unused latency calculations
    max_latency = max(packets) * 2 if len(packets) > 5 else sum(packets)
    
    # Relevant: Filter packets above threshold using list comprehension
    filtered_packets = [p for p in packets if p > latency_threshold]
    
    # Distractor: Misleading intermediate result
    total_bytes = sum(packets) * 1.5
    
    # Relevant: Calculate throughput using lambda and conditional expression
    calc_throughput = lambda x, y: (x / y) * 1000 if y > 0 else 0
    throughput = calc_throughput(len(filtered_packets), len(packets))
    
    # Distractor: Dead code path that never executes
    if len(packets) < 2:
        redundant_metric = sum(p * 0.75 for p in packets)
    
    # Relevant: Apply network efficiency factor
    efficiency_factor = 0.85 if throughput > 200 else 0.92
    adjusted_throughput = throughput * efficiency_factor
    
    # Distractor: Irrelevant bit operations on packet data
    bit_analysis = packets[0] & 0xFF if packets else 0
    
    return adjusted_throughput

# Main execution with mixed data
packet_sizes = [120, 180, 90, 210, 160, 75, 195, 140]

# Distractor: Multiple irrelevant computations
network_load = sum(packet_sizes) / len(packet_sizes)
peak_utilization = max(packet_sizes) * 1.25
redundant_counter = len([p for p in packet_sizes if p < 100])

# Key execution point
result = analyze_network_traffic(packet_sizes, latency_threshold=150)

# Distractor: More misleading intermediate calculations
capacity_estimate = (network_load + peak_utilization) / 2
throughput_variance = result * 0.15

# Target variable
final_throughput = round(result, 2)

print(f"Target result: {final_throughput}")