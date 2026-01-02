from collections import defaultdict
import math

def analyze_traffic(flow_data, thresholds):
    stats = defaultdict(int)
    for src, dst, size in flow_data:
        stats[src] += size
        stats[dst] += size  
    
    # Irrelevant aggregation
    total_pairs = len(flow_data)
    avg_flow = sum(size for _, _, size in flow_data) / total_pairs if total_pairs else 0
    
    # Distractor computation
    peak_load = max(stats.values()) if stats else 0
    normalized = {k: v / (peak_load + 1e-5) for k, v in stats.items()}
    
    # Real logic hidden among noise
    violations = 0
    for node, load in stats.items():
        if load > thresholds.get(node, 100):
            violations += 1
    return violations

def calculate_utilization(segments):
    base_map = defaultdict(list)
    temp_aggr = []
    
    for seg_id, nodes, config in segments:
        capacity = 0
        redundancy_factor = config.get('redundancy', 1)
        active_links = config.get('links', 1)
        
        # Core calculation
        for node in nodes:
            if 'router' in node:
                base_cap = len(node) * 10
                if 'core' in node:
                    base_cap *= 1.5
                capacity += base_cap
        
        # Semi-relevant adjustment
        effective_cap = math.floor(capacity * redundancy_factor)
        adjusted = effective_cap // max(active_links, 1)
        base_map[seg_id].append(adjusted)
        
        # Dead computation - doesn't impact result
        if capacity > 100:
            temp_aggr.append(math.log(capacity, 2))
    
    # Final aggregation
    result = 0
    for caps in base_map.values():
        result += sum(caps)
    
    # Additional distraction
    if result > 500:
        smoothed = round(result / 1.23, 3)
        variance_estimate = sum((x - smoothed)**2 for x in temp_aggr) if temp_aggr else 0
    
    return int(result)

# Simulated network configuration
topology_flows = [
    ('A1', 'router_edge_01', 45),
    ('B2', 'router_core_X1', 89),
    ('C3', 'router_edge_02', 34),
    ('router_core_X1', 'D4', 67),
    ('router_edge_01', 'B2', 23)
]

threshold_policy = {
    'router_edge_01': 120,
    'router_core_X1': 200,
    'router_edge_02': 120
}

# Irrelevant preprocessing
flow_names = [f"flow_{src}{dst}" for src, dst, _ in topology_flows]
distinct_nodes = set(src for src, _, _ in topology_flows) | set(dst for _, dst, _ in topology_flows)
node_class = {n: 'critical' if 'core' in n else 'standard' for n in distinct_nodes}

# Unused helper
def classify_node(n):
    return 'high-tier' if 'router_' in n and n.count('_') > 1 else 'low-tier'

# Distractor analysis call (result unused)
analyze_traffic(topology_flows, threshold_policy)

# Key data structure
network_segments = [
    ('alpha', ['router_edge_01', 'router_core_X1'], {'redundancy': 2, 'links': 2}),
    ('beta', ['router_core_X1', 'router_edge_02'], {'redundancy': 1.5, 'links': 3}),
    ('gamma', ['router_edge_01'], {'redundancy': 1, 'links': 1})
]

# Critical execution point
final_capacity = calculate_utilization(network_segments)
print(f"Result: {final_capacity}")