def analyze_system_capacity(resources, limit):
    # Initialize tracking variables
    active_nodes = []
    temp_buffer = set()
    overflow_flags = [False] * len(resources)
    scaling_factor = 1.75
    
    for i, res in enumerate(resources):
        load = len(res['services']) * res['utilization']
        if load > limit:
            overflow_flags[i] = True
            temp_buffer.add(res['node_id'])
        else:
            active_nodes.append(res['node_id'])
    
    # Secondary analysis: filter nodes with high redundancy
    redundant_services = []
    for node in resources:
        service_set = set(node['services'])
        if 'backup' in str(node['config']).lower():
            redundant_services.extend(node['services'])
    
    # Compute effective capacity (core logic)
    base_capacity = sum(len(r['services']) for r in resources if r['node_id'] in active_nodes)
    adjusted_capacity = base_capacity * scaling_factor
    
    # Distractor: simulate historical trend analysis (not used)
    historical_loads = [base_capacity * 0.8, base_capacity * 0.9, base_capacity]
    trend_slope = (historical_loads[-1] - historical_loads[0]) / len(historical_loads)
    projected_next = historical_loads[-1] + trend_slope
    
    # Final adjustment based on security patches
    patch_count = 0
    for r in resources:
        patch_count += len([p for p in r.get('updates', []) if 'security' in p['type']])
    
    final_capacity = int(adjusted_capacity - patch_count)
    
    # Irrelevant string processing (distractor)
    status_msg = f"System has {len(active_nodes)} nodes online."
    status_clean = status_msg.replace('online', 'active').strip().upper()
    summary = status_clean[:10] + "..." if len(status_clean) > 10 else status_clean
    
    return final_capacity

# Input data setup
resource_pool = [
    {
        'node_id': 'N1',
        'services': ['auth', 'gateway', 'cache'],
        'utilization': 0.6,
        'config': {'mode': 'standard', 'redundancy': False},
        'updates': [{'type': 'security', 'id': 'sec-001'}, {'type': 'patch', 'id': 'pch-102'}]
    },
    {
        'node_id': 'N2',
        'services': ['database', 'storage'],
        'utilization': 0.9,
        'config': {'mode': 'backup', 'redundancy': True},
        'updates': [{'type': 'security', 'id': 'sec-003'}]
    },
    {
        'node_id': 'N3',
        'services': ['api', 'worker', 'logger', 'monitor'],
        'utilization': 0.4,
        'config': {'mode': 'standard', 'redundancy': False},
        'updates': [{'type': 'doc', 'id': 'doc-99'}]
    }
]

threshold = 3.0

# Execute and print result
temp_diagnostic = [len(node['services']) for node in resource_pool]  # unused tracking
baseline = sum(temp_diagnostic)  # semi-relevant but not critical
final_capacity = analyze_system_capacity(resource_pool, threshold)
print(f"Result: {final_capacity}")