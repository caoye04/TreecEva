def analyze_network_traffic(log_entries):
    packet_sizes = [entry.get('size', 0) for entry in log_entries if entry.get('protocol') == 'TCP']
    processed_data = {}
    
    # Calculate total and average packet size
    total_packets = len(packet_sizes)
    if total_packets > 0:
        total_size = sum(packet_sizes)
        average_size = total_size / total_packets
        processed_data['total'] = total_size
        processed_data['average'] = average_size
    
    # Distractor operations that don't affect final result
    connection_stats = {}
    temp_sum = sum([x * 2 for x in packet_sizes])  # Unused computation
    protocol_count = len([entry for entry in log_entries if entry.get('type') == 'incoming'])  # Red herring
    
    # Final assignment
    final_count = processed_data.get('total', 0)
    
    # Additional unused variables
    max_size = max(packet_sizes) if packet_sizes else 0
    
    print(f"Target result: {final_count}")

# Sample data
network_logs = [
    {'protocol': 'TCP', 'size': 1500, 'type': 'incoming'},
    {'protocol': 'TCP', 'size': 800, 'type': 'outgoing'},
    {'protocol': 'UDP', 'size': 512, 'type': 'incoming'},
    {'protocol': 'TCP', 'size': 1200, 'type': 'incoming'},
    {'protocol': 'TCP', 'size': 900, 'type': 'outgoing'}
]

analyze_network_traffic(network_logs)