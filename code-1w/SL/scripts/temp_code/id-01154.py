def analyze_node_state(node_id, history):
    if len(history) == 0:
        return 0
    cumulative = 0
    for entry in history:
        if 'error' in entry and node_id % 2 == 0:
            cumulative -= 1
        elif 'reboot' in entry and node_id < 50:
            cumulative += 2
        else:
            cumulative += hash(entry) % 3
    return cumulative // max(1, len(history))


def build_dependency_graph(nodes):
    graph = {}
    for n in nodes:
        graph[n] = {m for m in nodes if m != n and (n * m) % 7 == 0}
    return graph

def validate_checksum(data_segment):
    if not data_segment:
        return 0
    xor_val = 0
    for b in data_segment:
        xor_val ^= b % 256
    return xor_val

def recursive_diagnostic(depth, node_list, acc):
    if depth <= 0 or not node_list:
        return acc % 100
    mid = len(node_list) // 2
    left = node_list[:mid]
    right = node_list[mid:]
    new_acc = acc + (depth * sum(node_list))
    return recursive_diagnostic(depth - 1, left, new_acc) + recursive_diagnostic(depth - 1, right, new_acc)

def compute_integrity_score(active_nodes, log_entries):
    base_score = 0
    state_map = {}
    
    # Irrelevant preprocessing block — distractor
    temp_data = [hash(str(x)) % 1000 for x in range(len(log_entries))]
    avg_temp = sum(temp_data) / len(temp_data) if temp_data else 0
    adjustment_factor = avg_temp * 0.01
    
    for node in active_nodes:
        state = analyze_node_state(node, log_entries)
        state_map[node] = state
        base_score += abs(state)
    
    # Real computation begins
    dependency_net = build_dependency_graph(active_nodes)
    edge_count = sum(len(dependents) for dependents in dependency_net.values())
    
    # Another red herring: checksum on fake data
    fake_segment = [(i * 17 + 31) % 200 for i in range(50)]
    validation_key = validate_checksum(fake_segment)
    
    # Core logic contributing to answer
    raw_diagnostic = recursive_diagnostic(3, list(state_map.values()), 7)
    
    # Decoy calculation — looks important but unused
    aggregate_risk = 0
    for k, v in state_map.items():
        if k in dependency_net and len(dependency_net[k]) > 2:
            aggregate_risk += v ** 2
    
    # Actual final computation
    scaling_factor = len(active_nodes) / (edge_count + 1)
    intermediate = (base_score * 2.5) + (raw_diagnostic * scaling_factor)
    
    # Final result
    final_diagnostic = int(intermediate - adjustment_factor) % 100000
    
    # Prints irrelevant decoy instead of target (misleading)
    print(f"System status: {aggregate_risk}")
    
    return final_diagnostic

# Critical execution point
operational_nodes = [12, 18, 21, 35, 42, 56]
system_log = ['startup', 'error_init', 'reboot', 'error_init', 'sync_complete']
final_diagnostic = compute_integrity_score(operational_nodes, system_log)
print(f"Result: {final_diagnostic}")