def calculate_remaining_capacity(nodes, threshold):
    active_loads = set()
    temp_buffer = []
    overflow_flags = [False] * len(nodes)
    balance_factor = 0
    
    for i, node in enumerate(nodes):
        raw_load = node['load']
        capacity = node['capacity']
        
        # Irrelevant transformation (distractor)
        normalized = raw_load / (capacity + 1e-5)
        temp_buffer.append(normalized)
        
        if raw_load > threshold:
            overflow_flags[i] = True
            balance_factor += 1
        
        # Real logic: track only nodes below threshold
        if raw_load < capacity * 0.8:
            active_loads.add(raw_load)

    # Secondary loop: simulate rebalancing (some steps are irrelevant)
    rebalanced_loads = []
    dummy_shift = 0
    for load in sorted(active_loads):
        shifted = load * 0.95 + dummy_shift
        dummy_shift = (dummy_shift + 1) % 3
        rebalanced_loads.append(shifted)

    # Additional distraction: unused sorting attempt
    try:
        temp_buffer.sort(reverse=True)
        median = temp_buffer[len(temp_buffer)//2]
    except:
        median = 0

    # Core calculation: sum of adjusted loads above a derived floor
    base_floor = threshold * 0.6
    adjusted_sum = 0
    for val in rebalanced_loads:
        if val > base_floor:
            adjusted_sum += val

    # Final computation using set size and filtered sum
    stability_bonus = len(active_loads) * 0.5
    final_capacity = int(adjusted_sum + stability_bonus)

    # Print required at end
    return final_capacity

# Input data
processing_nodes = [
    {'load': 45, 'capacity': 100},
    {'load': 70, 'capacity': 120},
    {'load': 30, 'capacity': 80},
    {'load': 90, 'capacity': 150},
    {'load': 25, 'capacity': 60}
]
load_threshold = 65

# Execution
final_capacity = calculate_remaining_capacity(processing_nodes, load_threshold)
print(f"Result: {final_capacity}")