import itertools
from math import sqrt

def analyze_network_traffic(packets, threshold=0.5):
    # Initialize variables for network analysis
    corrupted_packets = []
    high_priority = []
    system_health = 98.6
    
    # Process packets based on their properties
    for i, packet in enumerate(packets):
        if packet % 3 == 0 and packet % 5 == 0:
            corrupted_packets.append(packet)
            system_health -= 0.1 if system_health > 90 else 0
        elif packet % 7 == 0:
            high_priority.append(packet)
            system_health += 0.05 if system_health < 99.5 else 0
    
    # Calculate network metrics (distractions)
    packet_density = sum(packets) / len(packets) if packets else 0
    variance = sum((p - packet_density)**2 for p in packets) / len(packets) if packets else 0
    std_dev = sqrt(variance) if variance > 0 else 0
    
    # Generate potential connection combinations
    connections = []
    for combo in itertools.combinations(range(1, 6), 2):
        strength = (combo[0] * combo[1]) % 10 / 10
        connections.append(strength)
    
    # Filter valid connections based on threshold
    valid_connections = [c for c in connections if c > threshold]
    
    # Alternative calculation path (distraction)
    if system_health < 95:
        emergency_protocol = sum(high_priority) * 0.01
        recovery_factor = len(corrupted_packets) * 0.5
        potential_reliability = emergency_protocol - recovery_factor
    else:
        potential_reliability = system_health / 100
    
    # Calculate network reliability
    network_reliability = sum(valid_connections) / max(1, len(valid_connections))
    
    # Unused reliability adjustments (distractions)
    adjusted_reliability = network_reliability
    if packet_density > 50:
        adjusted_reliability *= 0.9
    elif std_dev < 10:
        adjusted_reliability *= 1.1
    
    return network_reliability

# Input data
packet_data = [15, 21, 8, 30, 7, 42]

# Process data through alternative paths (distractions)
filtered_packets = [p for p in packet_data if p % 2 == 0]
weighted_importance = sum(p * (i+1) for i, p in enumerate(packet_data))
reversed_sum = sum(packet_data[::-1]) - packet_data[0]

# Calculate final result
result = analyze_network_traffic(packet_data, 0.3)
print(f"Network reliability: {result}")