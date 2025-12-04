from collections import Counter, defaultdict
import math

def analyze_packet_loss(data_stream):
    # Analyze packet integrity - not used in main calculation
    packet_counts = Counter(data_stream)
    integrity_score = sum(ord(c) % 7 for c in data_stream) / len(data_stream)
    return len(packet_counts), integrity_score

def optimize_routing(routes, congestion_map):
    # This function simulates network route optimization
    # but doesn't affect the final calculation
    optimized = {}
    for route, hops in routes.items():
        if route in congestion_map:
            optimized[route] = hops * 0.85
        else:
            optimized[route] = hops * 1.1
    return optimized

def calculate_network_efficiency():
    # Primary network data
    network_segments = ["core", "edge", "access", "backbone"]
    transmission_rates = {"core": 9800, "edge": 4500, "access": 2100, "backbone": 7600}
    packet_sizes = [64, 512, 1024, 1518]
    
    # Distractor data structures
    congestion_factors = defaultdict(lambda: 1.0)
    congestion_factors.update({"core": 0.92, "edge": 0.78, "backbone": 0.85})
    
    # Irrelevant calculations
    potential_throughput = sum(transmission_rates.values()) * 0.8
    max_packet_size = max(packet_sizes)
    min_packet_size = min(packet_sizes)
    
    # Simulated network traffic - distractor
    traffic_pattern = "AABBCCDDEEFFGGHHIIJJKK"
    unique_patterns, pattern_score = analyze_packet_loss(traffic_pattern)
    
    # More distractor calculations
    routes = {"R1": 5, "R2": 3, "R3": 8, "R4": 4}
    congestion_map = {"R1": 0.7, "R3": 0.4}
    optimized_routes = optimize_routing(routes, congestion_map)
    
    # Actual calculation begins here
    base_efficiency = 0
    for segment in network_segments:
        if segment in transmission_rates:
            # We only care about the transmission rate for each segment
            base_efficiency += transmission_rates[segment]
    
    # Apply a standard network overhead factor
    overhead_factor = 0.15
    actual_efficiency = base_efficiency * (1 - overhead_factor)
    
    # Normalize by dividing by 1000 (converting to Gbps)
    normalized_efficiency = actual_efficiency / 1000
    
    # Distractor calculation that doesn't affect result
    if pattern_score > 3:
        network_health = "Good"
        redundant_metric = normalized_efficiency * 1.1
    else:
        network_health = "Degraded"
        redundant_metric = normalized_efficiency * 0.9
    
    # Calculate a misleading value that won't be used
    misleading_result = sum(packet_sizes) / len(network_segments) * 0.01
    
    # Return the actual result
    return normalized_efficiency

# Main execution
network_efficiency = calculate_network_efficiency()

print(f"Result: {network_efficiency}")

# Distractor calculations after the main result
protocol_overhead = {"TCP": 0.12, "UDP": 0.08, "HTTP": 0.15}
if "TCP" in protocol_overhead and network_efficiency > 20:
    adjusted_efficiency = network_efficiency * (1 - protocol_overhead["TCP"])
else:
    adjusted_efficiency = network_efficiency

# This is a dead code path that will never execute
if network_efficiency < 0:
    network_efficiency = abs(network_efficiency) + 5.0

print(f"Result: {network_efficiency}")