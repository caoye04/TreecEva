def calculate_remaining_capacity(units, threshold):
    # Simulate resource allocation across distributed nodes
    active_nodes = {i for i in range(len(units)) if units[i] > threshold / 2}
    standby_nodes = {i for i in range(len(units)) if units[i] <= threshold / 2}
    
    # Redundant health check (distractor)
    health_status = {}
    for idx in range(len(units)):
        if units[idx] < 0:
            health_status[idx] = 'ERROR'
        elif units[idx] == 0:
            health_status[idx] = 'IDLE'
        else:
            health_status[idx] = 'ACTIVE'

    # Calculate load distribution (only active_nodes matters)
    total_load = sum(units[i] for i in active_nodes)
    avg_load = total_load / len(active_nodes) if active_nodes else 0

    # Simulate capacity rebalancing
    adjusted_load = 0
    for i in active_nodes:
        if units[i] > avg_load:
            adjusted_load += units[i] * 0.9  # Overloaded node throttling
        else:
            adjusted_load += units[i] * 1.1  # Underutilized boost

    # Auxiliary calculation: node efficiency score (not used in final result)
    efficiency_score = 0
    for i in active_nodes:
        if units[i] > threshold * 0.8:
            efficiency_score += 1.5
        elif units[i] > threshold * 0.5:
            efficiency_score += 1.0
        else:
            efficiency_score += 0.5

    # Final capacity is based solely on adjusted_load and threshold scaling
    scaling_factor = 0.75 if len(active_nodes) > len(standby_nodes) else 0.6
    projected_capacity = adjusted_load * scaling_factor
    reserved_buffer = threshold * 0.1
    final_capacity = projected_capacity - reserved_buffer

    # Irrelevant debug print (dead code path)
    debug_trace = []
    for i in sorted(active_nodes.union(standby_nodes)):
        debug_trace.append(f"Node {i}: {units[i]}")

    return int(final_capacity)

# System configuration
processing_units = [12, 18, 5, 23, 7, 14, 9]
max_threshold = 20

# Key execution point
final_capacity = calculate_remaining_capacity(processing_units, max_threshold)
print(f"Result: {final_capacity}")