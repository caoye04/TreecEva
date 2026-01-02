import itertools
import math

# Simulate a network health monitoring system with diagnostic metrics
def calculate_node_health(signal_strength, latency, packet_loss):
    base_score = (signal_strength * 0.6) + (100 - latency) * 0.3 - (packet_loss * 2)
    adjustment = math.sin(math.radians(latency)) * 0.5
    return max(0, min(100, base_score + adjustment))

def detect_anomaly(health_scores):
    mean_score = sum(health_scores) / len(health_scores)
    variance = sum((x - mean_score) ** 2 for x in health_scores) / len(health_scores)
    std_dev = math.sqrt(variance)
    outliers = [x for x in health_scores if abs(x - mean_score) > 2 * std_dev]
    return len(outliers) > 0, std_dev

def transform_coordinates(node_positions):
    # Irrelevant geometric transformation (distractor)
    transformed = []
    for x, y in node_positions:
        rotated_x = x * math.cos(math.pi/4) - y * math.sin(math.pi/4)
        rotated_y = x * math.sin(math.pi/4) + y * math.cos(math.pi/4)
        transformed.append((rotated_x, rotated_y))
    return transformed

def compute_bandwidth_capacity(channels, frequency_bands):
    # Red herring function - unused in final calculation
    total_capacity = 0
    for band in frequency_bands:
        for channel in channels:
            total_capacity += band * math.log2(1 + channel)
    return total_capacity

def evaluate_redundancy_paths(routing_matrix):
    # Dead code path - never invoked
    valid_paths = 0
    for path in routing_matrix:
        if all(hop != -1 for hop in path):
            segments = sum(1 for a, b in zip(path, path[1:]) if abs(a - b) == 1)
            if segments >= 3:
                valid_paths += 1
    return valid_paths

def aggregate_metrics(nodes, load_profile):
    # Core logic embedded within distractions
    health_values = []
    for node in nodes:
        raw_health = calculate_node_health(
            node['signal'], node['latency'], node['loss']
        )
        # Apply load-based degradation
        adjusted_health = raw_health * (0.9 + (0.1 * (1 - load_profile.get(node['zone'], 0))))
        health_values.append(adjusted_health)
    
    # Real anomaly detection affects final score
    has_issue, deviation_metric = detect_anomaly(health_values)
    
    # Distracting data structure manipulation
    node_ids = [node['id'] for node in nodes]
    id_pairs = list(itertools.combinations(node_ids, 2))
    pair_sums = [a + b for a, b in id_pairs if a % 2 == 0]  # Partial processing (misleading)
    dummy_sum = sum(pair_sums[:3]) if len(pair_sums) > 3 else 0  # Unused aggregation
    
    # Irrelevant string processing (distractor using required feature)
    zone_tags = [node['zone'].upper() for node in nodes]
    concatenated_zones = ''.join(zone_tags)
    checksum_char = chr(65 + (sum(ord(c) for c in concatenated_zones) % 26))
    
    # Actual determination of final diagnostic
    base_diagnostic = sum(health_values) / len(health_values)
    penalty_factor = 1.5 if has_issue else 0.0
    stability_index = 100 - (deviation_metric * 2) - penalty_factor
    
    # Final computation - only this matters
    final_diagnostic = int(base_diagnostic - (100 - stability_index) + dummy_sum * 0)  # nullify dummy influence
    
    return final_diagnostic

# Main execution context
if __name__ == '__main__':
    # Network node simulation data
    network_nodes = [
        {'id': 101, 'signal': 85.0, 'latency': 45, 'loss': 1.2, 'zone': 'alpha'},
        {'id': 102, 'signal': 76.0, 'latency': 62, 'loss': 2.1, 'zone': 'beta'},
        {'id': 103, 'signal': 90.0, 'latency': 38, 'loss': 0.8, 'zone': 'alpha'},
        {'id': 104, 'signal': 68.0, 'latency': 75, 'loss': 3.5, 'zone': 'gamma'},
        {'id': 105, 'signal': 81.0, 'latency': 52, 'loss': 1.8, 'zone': 'beta'}
    ]
    
    system_load = {'alpha': 0.3, 'beta': 0.6, 'gamma': 0.4}
    
    # Unused but plausible data structures (red herrings)
    position_grid = [(1.2, 3.5), (2.1, 6.7), (4.0, 5.3), (7.8, 2.9), (5.4, 8.1)]
    frequency_bands = [2.4, 5.0, 6.0]
    channel_list = [12, 8, 15, 7, 20]
    routing_table = [
        [1, 2, 3, -1],
        [1, 4, 5, 6],
        [-1, 4, 5, -1],
        [7, 8, 9, 10]
    ]
    
    # Transform coordinates (irrelevant operation)
    transformed_grid = transform_coordinates(position_grid)
    
    # Compute bandwidth (dead computation)
    capacity_mbps = compute_bandwidth_capacity(channel_list, frequency_bands)
    
    # The critical statement
    final_diagnostic = aggregate_metrics(network_nodes, system_load)
    
    print(f"Result: {final_diagnostic}")