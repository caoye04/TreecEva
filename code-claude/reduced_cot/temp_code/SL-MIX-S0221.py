from collections import Counter, defaultdict

def calculate_signal_strength(frequencies, channel_width):
    # Calculate theoretical signal strength (not used in final computation)
    strength = sum([f * 0.75 for f in frequencies])
    return strength / (channel_width * 2)

def process_network_data(packets):
    # Process network packets and extract priorities
    packet_types = Counter(packets)
    
    # Initialize variables for network analysis
    bandwidth_allocation = defaultdict(int)
    interference_levels = []
    system_load = 0
    
    # Extract frequencies for signal calculation (distractor)
    frequencies = [len(p) % 10 + 5 for p in packets[:4]]
    signal_strength = calculate_signal_strength(frequencies, 5)
    
    # Process different packet types
    for packet_type, count in packet_types.items():
        # Calculate bandwidth needs (distractor)
        bandwidth_allocation[packet_type] = count * len(packet_type)
        
        # Track interference (distractor)
        if count > 3:
            interference_levels.append(count * 0.5)
        
        # Update system load (distractor)
        system_load += count * 2
    
    # Prepare priority calculation
    priority_base = 100
    error_margin = 15
    
    # Analyze packet distribution
    if len(packets) > 10:
        distribution = packets[::2]  # Take every other packet
    else:
        distribution = packets
    
    # Calculate priority scores
    priority_scores = {}
    for i, packet in enumerate(distribution):
        if i % 3 == 0:  # Every third packet gets special priority
            priority_scores[packet] = len(packet) * 2
        else:
            priority_scores[packet] = len(packet)
    
    # These lines are important for the final calculation
    noise_factor = len(interference_levels) * 5
    actual_priority = sum(priority_scores.values()) - noise_factor
    
    # More distractor calculations
    potential_throughput = system_load * 1.5
    if signal_strength > 10:
        adjusted_priority = actual_priority + 20
    else:
        adjusted_priority = actual_priority
    
    # Final calculations (distractors)
    network_health = (priority_base - error_margin) / (system_load * 0.1)
    optimization_factor = sum(bandwidth_allocation.values()) % 10
    
    # Return multiple values (only actual_priority matters)
    return {
        'priority': actual_priority,
        'load': system_load,
        'health': network_health,
        'optimization': optimization_factor
    }

# Main execution
packet_data = ['TCP', 'UDP', 'ICMP', 'TCP', 'DNS', 'TCP', 'HTTP', 'FTP', 'SSH']
network_metrics = process_network_data(packet_data)

# Print the results
print(f"Result: {network_metrics['priority']}")