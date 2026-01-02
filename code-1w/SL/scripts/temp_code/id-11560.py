def analyze_redundancy(nodes):
    redundant_links = 0
    for node in nodes:
        if len(node['connections']) > 3:
            redundant_links += 1
    return redundant_links

network_nodes = [
    {'id': 'A', 'load': 85, 'connections': [1, 2, 3], 'active': True},
    {'id': 'B', 'load': 92, 'connections': [1, 2, 3, 4], 'active': True},
    {'id': 'C', 'load': 45, 'connections': [1, 2], 'active': False},
    {'id': 'D', 'load': 76, 'connections': [1, 2, 3, 4], 'active': True}
]

baseline = 100
stress_factor = 1.3
recovery_margin = 0.85

# Irrelevant tracking variables (distractors)
current_audit_phase = 2
total_checks_run = 0
audit_log = set()
audit_log.add('phase_start')

# Misleading intermediate calculation
estimated_downtime = 0
for node in network_nodes:
    if not node['active']:
        estimated_downtime += node['load'] * 0.5

# Semi-relevant pre-processing
active_node_count = sum(1 for n in network_nodes if n['active'])
overloaded_nodes = [n for n in network_nodes if n['load'] > 90]

# Red herring: calculating redundancy but not using it directly
redundant_count = analyze_redundancy(network_nodes)
system_health_score = active_node_count * 10 - redundant_count * 2

# Core logic with conditional expressions and dictionary operations
effective_loads = {
    n['id']: n['load'] * stress_factor if n['active'] else 0
    for n in network_nodes
}

adjusted_loads = {}
for k, v in effective_loads.items():
    if v > 0:
        # Simulate load redistribution
        adjustment = v * 0.1 if v > 100 else v * 0.05
        adjusted_loads[k] = v - adjustment

# Use of set operations (union with dummy set)
dummy_set = {1, 2, 3}
active_ids = {n['id'] for n in network_nodes if n['active']}
temp_set_result = dummy_set.union(active_ids)  # unused afterward

# Final capacity calculation depends on adjusted total and recovery margin
total_adjusted_load = sum(adjusted_loads.values())
maximum_allowed_load = baseline * stress_factor * active_node_count

# Conditional expression determining final capacity
final_capacity = maximum_allowed_load - total_adjusted_load if total_adjusted_load < maximum_allowed_load else 0
final_capacity *= recovery_margin

# Print result as required
print(f"Result: {final_capacity}")