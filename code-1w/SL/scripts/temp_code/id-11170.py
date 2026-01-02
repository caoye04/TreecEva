def calculate_remaining_capacity(nodes, threshold):
    total_load = sum(node['load'] for node in nodes)
    max_capacity = len(nodes) * 100
    overload_count = sum(1 for node in nodes if node['load'] > threshold)
    
    # Irrelevant computation: historical average (not used in final result)
    historical_avg = sum(node.get('prev_load', 75) for node in nodes) / len(nodes) if nodes else 0
    
    # Semi-relevant transformation: normalize loads
    normalized = [node['load'] / 100.0 for node in nodes]
    efficiency_ratio = sum(normalized) / len(normalized) if normalized else 0
    
    # Distractor: complex conditional expression with unused outcome
    status_flags = [
        'over' if n['load'] > threshold else 'optimal' if n['load'] > 50 else 'under'
        for n in nodes
    ]
    critical_nodes = status_flags.count('over')
    
    # Dead code path: never accessed in this execution
    debug_mode = False
    if debug_mode:
        print(f'Debug: {historical_avg=}, {efficiency_ratio=}')

    # Core logic with modular arithmetic and conditional expression
    adjusted_capacity = max_capacity - total_load
    penalty = overload_count * 10 if overload_count > 0 else 0
    resilience_bonus = 5 if all(node['load'] < 90 for node in nodes) else 0
    
    # Key statement
    final_capacity = adjusted_capacity - penalty + resilience_bonus
    
    return final_capacity

# Setup data
nodes = [
    {'load': 85, 'prev_load': 78},
    {'load': 92, 'prev_load': 88},
    {'load': 45, 'prev_load': 50},
    {'load': 67, 'prev_load': 60},
    {'load': 88, 'prev_load': 82}
]
threshold = 90

# Execute
final_capacity = calculate_remaining_capacity(nodes, threshold)
print(f"Result: {final_capacity}")