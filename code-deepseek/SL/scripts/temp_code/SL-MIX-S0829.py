def analyze_network_throughput(packets, capacity):
    # Distractor: misleading calculation that looks important
    total_bytes = sum(packet['size'] for packet in packets)
    theoretical_max = capacity * 1000  # Misleading conversion
    
    # Distractor: unused sorting operation
    sorted_packets = sorted(packets, key=lambda x: x['timestamp'])
    
    # Relevant: actual throughput calculation
    successful_packets = [p for p in packets if p['status'] == 'delivered']
    total_delivered = sum(p['size'] for p in successful_packets)
    
    # Distractor: dead code path with bitwise operations
    if theoretical_max & 0xFF == 0:
        unused_result = (theoretical_max >> 4) ^ 0xAB
    
    # Relevant: final throughput calculation
    time_window = 60  # seconds
    actual_throughput = total_delivered / time_window
    
    # Distractor: misleading intermediate result
    efficiency_ratio = actual_throughput / capacity if capacity > 0 else 0
    
    return actual_throughput

# Mock network data with distractors
data_packets = [
    {'size': 1500, 'status': 'delivered', 'timestamp': 100},
    {'size': 800, 'status': 'dropped', 'timestamp': 200},
    {'size': 1200, 'status': 'delivered', 'timestamp': 50},
    {'size': 950, 'status': 'delivered', 'timestamp': 300},
    {'size': 1800, 'status': 'queued', 'timestamp': 150}
]

bandwidth_capacity = 100  # Mbps
redundant_capacity = bandwidth_capacity * 2  # Unused distractor

# Main execution
throughput_analysis = analyze_network_throughput(data_packets, bandwidth_capacity)

# Distractor: misleading transformation
scaled_throughput = throughput_analysis * 1.5

# Target variable calculation
final_throughput = int(throughput_analysis)

# More distractors
optimization_factor = 0.85
potential_improvement = final_throughput * optimization_factor

print(f"Result: {final_throughput}")