def analyze_redundancy(nodes):
    redundant_links = 0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i] & nodes[j]:  # shared frequency band
                redundant_links += 1
    return redundant_links


def track_transmission_volume(log):
    total_packets = 0
    temp_sum = 0  # distractor variable
    for entry in log:
        total_packets += entry['packets']
        temp_sum += entry['timestamp']  # irrelevant accumulation
    average_latency = sum(e['latency'] for e in log) / len(log) if log else 0  # unused metric
    return total_packets


def calculate_remaining_capacity(nodes, log):
    base_capacity = 10000
    usage_factor = 0
    
    # Real computation path
    active_nodes = set()
    for node in nodes:
        if sum(int(b) for b in format(node, '08b')) > 3:  # more than 3 frequency bands active
            active_nodes.add(node)
    
    high_load_count = 0
    for record in log:
        if record['packets'] > 500:
            high_load_count += 1
    
    # Core logic
    usage_factor += len(active_nodes) * 150
    usage_factor += high_load_count * 90
    
    # Distractor: complex but unused redundancy analysis
    redundant_connection_score = analyze_redundancy(nodes)
    stability_index = (len(nodes) * 10) - redundant_connection_score
    projected_growth = stability_index * 0.75  # not used
    
    # Another distractor loop
    phantom_usage = 0
    for _ in range(3):
        for n in nodes[:2]:
            phantom_usage += n % 7
    
    final_capacity = base_capacity - usage_factor
    
    # Critical statement
    final_capacity = calculate_remaining_capacity(network_nodes, transmission_log)
    
    return final_capacity

# Input data
network_nodes = [0b11010101, 0b11110000, 0b10101010, 0b00001111]
transmission_log = [
    {'packets': 620, 'latency': 12.5, 'timestamp': 1678884000},
    {'packets': 480, 'latency': 8.3, 'timestamp': 1678884060},
    {'packets': 710, 'latency': 14.1, 'timestamp': 1678884120},
    {'packets': 300, 'latency': 5.9, 'timestamp': 1678884180}
]

# Execution
final_capacity = 0
final_capacity = calculate_remaining_capacity(network_nodes, transmission_log)
print(f"Result: {final_capacity}")