def calculate_priority_score(metrics, weight_map):
    # Calculate priority based on weighted metrics
    priority = 0
    for metric, value in metrics.items():
        if metric in weight_map:
            priority += value * weight_map.get(metric, 0)
    
    # Apply normalization factor - not actually used
    normalization = sum(weight_map.values()) if weight_map else 1
    
    return priority

def optimize_network_traffic(connections):
    # This function simulates network traffic optimization
    # but doesn't affect the final answer
    optimized = {}
    for source, targets in connections.items():
        filtered_targets = {t: v for t, v in targets.items() if v > 0}
        optimized[source] = filtered_targets
    return optimized

def calculate_resource_usage(allocations, efficiency_factor=0.8):
    # Calculate theoretical resource usage
    base_usage = sum(allocations.values())
    adjusted_usage = base_usage * efficiency_factor
    
    # Apply overhead calculations
    overhead = 0
    for resource, amount in allocations.items():
        if amount > 10:
            overhead += (amount - 10) * 0.05
    
    return adjusted_usage + overhead

def calculate_optimal_allocation(load_factors, resource_availability):
    # Core algorithm to determine optimal resource allocation
    total_load = sum(load_factors.values())
    total_resources = sum(resource_availability.values())
    
    # These constants are distractions
    SCALING_FACTOR = 1.25
    EFFICIENCY_THRESHOLD = 0.75
    OVERHEAD_CONSTANT = 0.15
    
    # Calculate baseline distribution
    baseline = {}
    for server, load in load_factors.items():
        # This calculation is what matters for the answer
        proportion = load / total_load if total_load > 0 else 0
        baseline[server] = int(proportion * total_resources)
    
    # Apply adjustments based on server priorities
    priorities = {
        'server_a': 3,
        'server_b': 1,
        'server_c': 2,
        'server_d': 0  # This server doesn't exist in our data
    }
    
    # Track resources used so far
    allocated = sum(baseline.values())
    remaining = total_resources - allocated
    
    # This is a distraction - complex but ultimately unused
    potential_optimizations = {}
    for server in load_factors:
        if server in priorities:
            potential_optimizations[server] = priorities[server] * SCALING_FACTOR
    
    # Distribute remaining resources based on priority
    priority_sum = sum(priorities.get(server, 0) for server in load_factors)
    
    if priority_sum > 0 and remaining > 0:
        for server in baseline:
            if server in priorities:
                # This is the key calculation that affects the answer
                priority_share = priorities[server] / priority_sum
                baseline[server] += int(remaining * priority_share)
    
    # This network simulation doesn't affect the answer
    network_connections = {
        'server_a': {'server_b': 5, 'server_c': 3},
        'server_b': {'server_a': 2, 'server_c': 7},
        'server_c': {'server_a': 4, 'server_b': 1}
    }
    optimize_network_traffic(network_connections)
    
    return baseline

# Main execution flow
server_load = {'server_a': 50, 'server_b': 30, 'server_c': 20}

# These resource maps are distractions
historical_resources = {'server_a': 40, 'server_b': 35, 'server_c': 25}
projected_resources = {'server_a': 45, 'server_b': 25, 'server_c': 30}

# This is the actual resource map we'll use
resource_map = {'server_a': 60, 'server_b': 30, 'server_c': 30}

# Calculate metrics for each server - distraction
server_metrics = {
    'server_a': {'cpu': 0.8, 'memory': 0.7, 'network': 0.5},
    'server_b': {'cpu': 0.6, 'memory': 0.5, 'network': 0.8},
    'server_c': {'cpu': 0.5, 'memory': 0.9, 'network': 0.3}
}

weight_configuration = {'cpu': 3, 'memory': 2, 'network': 1}

# Calculate priority scores - distraction
server_priorities = {}
for server, metrics in server_metrics.items():
    server_priorities[server] = calculate_priority_score(metrics, weight_configuration)

# This is the key statement we're interested in
resource_allocation = calculate_optimal_allocation(server_load, resource_map)

# These are distraction calculations that happen after our target statement
efficiency = {}
for server, allocated in resource_allocation.items():
    load = server_load.get(server, 0)
    if load > 0:
        efficiency[server] = allocated / load

total_efficiency = sum(efficiency.values()) / len(efficiency) if efficiency else 0

print(f"Resource Allocation: {resource_allocation}")
print(f"Total Efficiency: {total_efficiency:.2f}")