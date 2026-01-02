from collections import defaultdict
from itertools import combinations

# Simulated network packet analysis with performance metrics
def analyze_packet_flow(packets, threshold):
    flow_stats = defaultdict(int)
    temp_buffer = []
    overflow_count = 0

    for pkt in packets:
        size = pkt['size']
        src = pkt['source']
        dest = pkt['dest']

        flow_stats[src] += size
        flow_stats[dest] += size

        if size > threshold:
            overflow_count += 1
            temp_buffer.append(size)

    # Irrelevant aggregation
    avg_overflow = sum(temp_buffer) / overflow_count if overflow_count else 0
    max_single = max(temp_buffer) if temp_buffer else 0

    return dict(flow_stats), overflow_count, avg_overflow, max_single

def calculate_efficiency_ratio(active_nodes, total_bandwidth):
    if active_nodes == 0:
        return 0.0
    # Misleading complex formula with unused components
    base = (total_bandwidth / active_nodes) ** 0.5
    penalty = 1 + (active_nodes % 3) * 0.05
    jitter_factor = sum((i * 0.01) for i in range(active_nodes)) if active_nodes < 10 else 0.05
    return round(base / penalty + jitter_factor, 4)

def evaluate_performance(metrics, base):
    score = 0
    weights = {'latency': 0.3, 'throughput': 0.5, 'errors': -0.2}
    
    # Core logic
    for key, value in metrics.items():
        if key in weights:
            score += value * weights[key]
    
    # Distractor: complex string-based validation with no impact
    status_str = "healthy" if score > base else "degraded"
    char_sum = sum(ord(c) for c in status_str)
    debug_code = ''.join([chr((char_sum % 26) + 97)] * 2)
    
    # Another red herring: unused combinatorial check
    possible_pairs = list(combinations(['a', 'b', 'c', 'd'], 2))
    pair_count = len(possible_pairs)
    
    return int(score * 10)  # Final scoring step

# Main execution
packet_data = [
    {'size': 89, 'source': 'node_a', 'dest': 'node_b'},
    {'size': 105, 'source': 'node_b', 'dest': 'node_c'},
    {'size': 76, 'source': 'node_c', 'dest': 'node_a'},
    {'size': 120, 'source': 'node_a', 'dest': 'node_d'},
    {'size': 95, 'source': 'node_d', 'dest': 'node_b'}
]

stats, overflows, _, _ = analyze_packet_flow(packet_data, threshold=100)
active_node_count = len(stats)
total_capacity = sum(stats.values())

efficiency = calculate_efficiency_ratio(active_node_count, total_capacity)

metric_data = {
    'latency': 85,
    'throughput': 92,
    'errors': 5
}
baseline = 80

final_score = evaluate_performance(metric_data, baseline)

# Print result as required
print(f"Result: {final_score}")