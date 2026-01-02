def calculate_node_load(node_id, base_load=1.0):
    if node_id % 3 == 0:
        return base_load * 1.5
    elif node_id % 5 == 0:
        return base_load * 0.7
    else:
        return base_load * 1.1

# System configuration parameters
total_nodes = 12
threshold_multiplier = 0.85
maintenance_overhead = 0.1

# Simulate node health scores (irrelevant to final result but adds distraction)
node_health = [95 - (i * 3) % 15 for i in range(total_nodes)]
health_avg = sum(node_health) / len(node_health)
adjusted_health = [h * 0.01 for h in node_health if h > 80]

# Determine optimal nodes based on efficiency score
node_efficiency = []
for nid in range(1, total_nodes + 1):
    load_factor = calculate_node_load(nid)
    efficiency_score = (nid ** 0.5) / load_factor
    node_efficiency.append((nid, efficiency_score))

# Filter nodes above average efficiency
avg_efficiency = sum([score for _, score in node_efficiency]) / len(node_efficiency)
optimal_nodes = [nid for nid, score in node_efficiency if score > avg_efficiency]

# Secondary filter: only nodes with prime IDs (adds complexity but not used in final path)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_filtered = [n for n in optimal_nodes if is_prime(n)]  # distractor list

# Calculate system capacity using optimal nodes
def calculate_system_capacity(nodes_list):
    base_capacity_per_node = 25.5
    degradation = 0.02
    total_capacity = 0.0
    
    # Simulate time-based utilization cycles (nested loop - adds nesting depth)
    for cycle in range(1, 4):  # 3 time cycles
        cycle_modifier = 1 - (degradation * cycle)
        for node in nodes_list:
            # Apply conditional boost for even-numbered nodes
            boost = 1.1 if node % 2 == 0 else 1.0
            node_contribution = base_capacity_per_node * cycle_modifier * boost
            total_capacity += node_contribution
    
    # Apply threshold scaling (final adjustment)
    scaled_capacity = total_capacity * threshold_multiplier
    
    # Irrelevant post-processing (dead code path - distractor)
    if scaled_capacity > 1000:
        normalized = scaled_capacity / 10
    else:
        normalized = scaled_capacity  # unused
        
    return scaled_capacity

# Final computation step
current_utilization = sum([calculate_node_load(i) for i in range(5)])  # irrelevant metric
final_capacity = calculate_system_capacity(optimal_nodes)
print(f"Result: {final_capacity}")