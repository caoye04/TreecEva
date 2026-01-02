def balance_workload(servers, jobs):
    # Simulate dynamic workload balancing across server nodes
    base_capacity = 100
    overhead_factor = 0.1
    efficiency_log = []
    temp_buffer = []

    for idx, (server, capacity) in enumerate(zip(servers, [base_capacity + i*5 for i in range(len(servers))])):
        load_snapshot = {}
        adjusted_jobs = []
        
        for job in jobs:
            if job['priority'] > 2:
                computed_load = (job['size'] * 1.5) % capacity
                adjusted_jobs.append(computed_load)
                load_snapshot[job['id']] = computed_load
            else:
                dummy_calc = (job['size'] ** 0.5) * overhead_factor  # Distractor: not used later
                temp_buffer.append(dummy_calc)
        
        total_load = sum(adjusted_jobs)
        if total_load > capacity * 0.8:
            total_load *= 0.9  # Apply throttling
        efficiency_log.append({'node': server, 'utilization': total_load / capacity})
        
        # Misleading state tracking (not affecting final result)
        debug_state = {
            'timestamp': idx * 10,
            'staged': len([j for j in jobs if j['priority'] == 1]),
            'skipped': 0
        }

    # Final aggregation uses only last node's processed load
    last_node_load = sum(
        (job['size'] * 1.5) % (base_capacity + (len(servers)-1)*5)
        for job in jobs if job['priority'] > 2
    )
    
    # Additional irrelevant computation
    phantom_peak = 0
    for i in range(3):
        phantom_peak += (base_capacity // (i+1)) % 7

    final_load = int(last_node_load * 0.9) if last_node_load > 80 else int(last_node_load)
    return final_load

# Input setup
nodes = ['node_alpha', 'node_beta', 'node_gamma']
tasks = [
    {'id': 't1', 'size': 20, 'priority': 3},
    {'id': 't2', 'size': 15, 'priority': 1},
    {'id': 't3', 'size': 25, 'priority': 4},
    {'id': 't4', 'size': 10, 'priority': 2},
    {'id': 't5', 'size': 30, 'priority': 3}
]

# Execute and print result
target_result = balance_workload(nodes, tasks)
print(f"Result: {target_result}")