from collections import defaultdict

# Simulate network resource allocation across nodes
def initialize_resources():
    nodes = ['N1', 'N2', 'N3', 'N4']
    base_load = [120, 85, 95, 110]
    peak_threshold = 100
    priority_map = defaultdict(lambda: 1)
    priority_map.update({'N1': 2, 'N3': 2})

    resource_pool = {}
    for i, node in enumerate(nodes):
        allocated = base_load[i] * (1.1 if base_load[i] > peak_threshold else 1.0)
        resource_pool[node] = allocated

    return resource_pool, priority_map


def calculate_efficiency_score(load):
    # Dummy efficiency curve: higher load -> diminishing returns
    if load < 90:
        return 0.9
    elif load < 110:
        return 0.75
    else:
        return 0.65


def track_historical_usage(resource_pool):
    # Irrelevant tracking function - does not affect final result
    history_log = defaultdict(list)
    for node, load in resource_pool.items():
        history_log[node].append(load * 0.95)  # Simulate decay
        history_log[node].append(load)
    return history_log  # Unused in main logic

def generate_diagnostic_report(resource_pool, priority_map):
    # Distractor: generates report but doesn't impact optimization
    diagnostics = {}
    total_load = sum(resource_pool.values())
    avg_load = total_load / len(resource_pool)
    
    for node in resource_pool:
        load = resource_pool[node]
        priority = priority_map[node]
        deviation = (load - avg_load) / avg_load
        diagnostics[node] = {
            'load': load,
            'priority': priority,
            'deviation_pct': round(deviation * 100, 2)
        }
    
    # Some meaningless transformation
    temp_adjustment = sum(d['load'] for d in diagnostics.values() if d['priority'] == 2) * 0.05
    diagnostics['summary'] = {'temp_adjustment': temp_adjustment}  # Dead-end data

    return diagnostics  # Not used later

def optimize_allocation(resource_matrix, efficiency_map):
    adjusted_matrix = {}
    scaling_factors = []  

    # Real computation begins
    for node, load in resource_matrix.items():
        base_efficiency = efficiency_map[node]
        scaled_load = load * base_efficiency
        
        # Apply conditional boost if node has high priority
        if node in ['N1', 'N3']:
            scaled_load *= 1.15  # Priority nodes get throughput boost
        
        adjusted_matrix[node] = scaled_load
        scaling_factors.append(base_efficiency)

    # Secondary adjustment based on average scaling
    avg_factor = sum(scaling_factors) / len(scaling_factors)
    global_adjustment = 1.0
    if avg_factor < 0.8:
        global_adjustment = 1.05
    else:
        global_adjustment = 0.98

    # Final bandwidth computed from adjusted loads
    final_bandwidth = sum(adjusted_matrix.values()) * global_adjustment
    
    # Red herring: irrelevant min-threshold check
    min_required = 300
    if final_bandwidth < min_required:
        fallback = min_required * 0.8
        final_bandwidth = max(final_bandwidth, fallback)

    return int(final_bandwidth)

# Main execution flow
resource_pool, priority_map = initialize_resources()

# Build efficiency map using real logic
efficiency_map = {node: calculate_efficiency_score(load) for node, load in resource_pool.items()}

# Useless historical tracking (distractor)
history = track_historical_usage(resource_pool)

# Generate unused diagnostic report (interference)
diag_report = generate_diagnostic_report(resource_pool, priority_map)

# Key statement: optimization that determines final answer
final_bandwidth = optimize_allocation(resource_pool, efficiency_map)

# Print result as required
print(f"Result: {final_bandwidth}")