from collections import defaultdict

# Simulate distributed task scheduling across compute nodes
def calculate_node_efficiency(base_load, overhead_factor):
    efficiency = base_load * (1.0 - 0.05 * overhead_factor)
    penalty = 0.0
    if base_load > 70:
        penalty = (base_load - 70) * 0.3
    return max(efficiency - penalty, base_load * 0.4)

def generate_cluster_map(nodes_config):
    cluster_map = defaultdict(list)
    temp_store = []
    for idx, (zone, count) in enumerate(zip(['alpha', 'beta', 'gamma'], [3, 2, 4])):
        for i in range(count):
            node_id = f'{zone}-{i}'
            temp_store.append(node_id)
            cluster_map[zone].append({
                'id': node_id,
                'base_index': idx + i,
                'active': True
            })
    # Irrelevant aggregation
    stats = {k: len(v) for k, v in cluster_map.items()}
    return cluster_map

def balance_workload(weights, capacity):
    adjusted = [w * 1.1 for w in weights]
    overflow = sum(adjusted) - capacity
    reduction_factor = 0.9
    if overflow > 0:
        reduction_factor = (capacity / sum(adjusted))
    
    final_loads = []
    for a in adjusted:
        load = a * reduction_factor
        if load < 5:
            load = 5  # minimum threshold
        final_loads.append(load)
    
    # Dead computation - doesn't affect output
    temp_analysis = {}
    for i, load in enumerate(final_loads):
        temp_analysis[f'step_{i}'] = {
            'raw': adjusted[i],
            'reduced': load,
            'delta': adjusted[i] - load
        }
    
    total_final = sum(final_loads)
    return int(round(total_final))

# Main execution
node_capacity = 250
cluster_weights = [68, 72, 55, 81, 44, 63, 77]

# Spurious data processing
shadow_buffer = [x ^ 25 for x in cluster_weights if x % 2 == 0]
dummy_pairs = list(zip(cluster_weights, [x * 0.95 for x in cluster_weights]))
index_tracker = {i: val for i, val in enumerate(dummy_pairs)}

# Unused helper function (dead code path)
def debug_trace_path(seq):
    log_entries = []
    for i, s in enumerate(seq):
        log_entries.append(f"{i}: {s} -> {s % 17}")
    return '\n'.join(log_entries)

# Real computation begins
cluster_map = generate_cluster_map({'zones': 3, 'nodes': 9})
efficiencies = [calculate_node_efficiency(w, 2) for w in cluster_weights]

# Key assignment
final_load = balance_workload(cluster_weights, node_capacity)

print(f"Result: {final_load}")