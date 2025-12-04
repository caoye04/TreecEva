from collections import Counter, defaultdict

def analyze_packet_headers(headers):
    # Analyze packet headers for protocol distribution
    protocol_counts = Counter(headers)
    most_common = protocol_counts.most_common(3)
    
    # Calculate weighted score based on protocol distribution
    weights = {'TCP': 1.5, 'UDP': 0.8, 'ICMP': 2.0, 'HTTP': 1.2}
    weighted_sum = sum(weights.get(protocol, 1.0) * count for protocol, count in most_common)
    
    return weighted_sum / len(headers) if headers else 0

def optimize_routing_path(network_map):
    # Simulate network path optimization
    nodes = len(network_map)
    optimal_path = []
    
    for i in range(nodes):
        if i % 3 == 0:
            optimal_path.append(i * 2)
        elif i % 3 == 1:
            optimal_path.append(i + 1)
        else:
            optimal_path.append(i // 2)
    
    return sum(optimal_path) % 17

def calculate_effective_bandwidth(packet_sizes, errors):
    # Calculate effective network throughput considering errors
    base_throughput = 100.0
    error_factor = 0.0
    
    # Extract relevant packet sizes (only those divisible by 8)
    relevant_sizes = [size for size in packet_sizes if size % 8 == 0]
    
    # Process errors dictionary
    for error_type, count in errors.items():
        if error_type == 'collision':
            error_factor += count * 0.05
        elif error_type == 'corruption':
            error_factor += count * 0.08
        elif error_type == 'timeout':
            error_factor += count * 0.03
    
    # Apply packet size adjustments
    size_factor = sum(relevant_sizes) / 1024 if relevant_sizes else 1
    
    # Calculate network efficiency using bit operations
    efficiency_bits = 0
    for i, size in enumerate(relevant_sizes):
        if i < 5:  # Only process first 5 elements
            efficiency_bits |= (1 << (size % 6))  # Set bits based on packet size
    
    efficiency = bin(efficiency_bits).count('1') / 6  # Count set bits, normalize
    
    # Apply all factors to calculate throughput
    return base_throughput * (1 - error_factor) * size_factor * efficiency

# Network simulation parameters
network_map = [3, 7, 2, 9, 5, 1, 8]
routing_efficiency = optimize_routing_path(network_map)

# These packet sizes represent different protocols (in bytes)
packet_sizes = [64, 128, 512, 256, 1024, 768, 32, 96]

# Transmission stats and error tracking
protocol_headers = ['TCP', 'UDP', 'TCP', 'ICMP', 'TCP', 'UDP', 'HTTP']
header_score = analyze_packet_headers(protocol_headers)

# Build error dictionary with various network problems
transmission_errors = defaultdict(int)
transmission_errors['collision'] = 3
transmission_errors['corruption'] = 2
transmission_errors['timeout'] = 4
transmission_errors['fragmentation'] = 1  # Not used in calculations

# Calculate network congestion index (not directly used)
congestion_index = sum(packet_sizes) / (len(packet_sizes) * header_score)

# Process packet queue - slicing operations
packet_queue = packet_sizes[:]
processed_packets = packet_queue[2:6]  # Extract middle section
reversed_packets = packet_queue[::-2]  # Every other packet in reverse

# This is used for visualization only
network_visualization = {
    'nodes': len(network_map),
    'links': len(network_map) - 1,
    'throughput_history': [92.5, 88.7, 95.2, 91.3]
}

# Calculate effective network throughput
network_throughput = calculate_effective_bandwidth(packet_sizes, transmission_errors)

# Additional network metrics (not used for final result)
latency = sum(reversed_packets) / len(reversed_packets) * 0.01
jitter = max(processed_packets) - min(processed_packets) / 1000

print(f"Network analysis complete")
print(f"Routing efficiency: {routing_efficiency}")
print(f"Protocol distribution: {header_score:.2f}")
print(f"Network congestion: {congestion_index:.2f}")
print(f"Result: {network_throughput}")