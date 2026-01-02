def analyze_network_flow(traffic_matrix, node_weights):
    flow_scores = {}
    for idx, row in enumerate(traffic_matrix):
        base_score = 0
        for j, val in enumerate(row):
            if val > 0:
                base_score += val ^ node_weights[idx] & (j + 1)
        flow_scores[f'node_{idx}'] = base_score % 13
    return flow_scores


def validate_checksum(entries):
    total = 0
    for i, entry in enumerate(entries):
        if i % 3 == 0:
            total += sum([entry.count(str(x)) for x in range(3)]) * i
    return total - len(entries)


def transform_data_sequence(seq):
    transformed = []
    for i, item in enumerate(seq):
        shifted = (item << 2) ^ 5
        if i % 2 == 0:
            shifted = (shifted >> 1) + i
        transformed.append(shifted)
    # Dead code path - irrelevant to final result
    if len(transformed) > 10:
        return [x * 2 for x in transformed]
    return transformed


def build_index_map(keys, values):
    # Uses zip and dictionary operation but is not critical
    temp_map = dict(zip(keys, values))
    enhanced = {k: v * 3 for k, v in temp_map.items() if v < 100}
    return enhanced  # Unused in main logic


def compute_integrity_score(nodes, logs):
    score = 0
    state_log = []
    
    # Core logic begins
    for i, (node, weight) in enumerate(nodes.items()):
        if i % 2 == 0:
            temp_val = weight ** 2 - (i * 7)
            if temp_val < 0:
                temp_val = abs(temp_val) ^ 15
            state_log.append(temp_val)
    
    # Secondary processing with filtering
    filtered_states = [x for x in state_log if x % 4 == 2]
    
    # Tertiary transformation using bitwise mix
    for j, val in enumerate(filtered_states):
        mod = (val >> j % 3) ^ (j + 5)
        if mod > 20:
            mod = mod // 2
        score += mod
    
    # Final adjustment based on log length parity
    if len(logs) % 2 == 1:
        score = score * 2 + 7
    else:
        score = score + 13
    
    # Irrelevant side calculation (distractor)
    fake_entropy = 0
    for log in logs:
        for char in log:
            fake_entropy += ord(char) % 11
    fake_entropy = fake_entropy / (len(logs) or 1)
    
    # Decoy assignment (misleading)
    baseline = validate_checksum(logs)
    
    # Key assignment
    final_diagnostic = score  # This is the target variable
    
    # Red herring: complex unpacking that does nothing
    if len(state_log) >= 3:
        first, *rest, last = state_log
        mid_vals = [x for x in rest if x > 5]
        _ = (first + last) * len(mid_vals)  # unused

    return final_diagnostic

# Main execution
network_nodes = {'alpha': 12, 'beta': 18, 'gamma': 24, 'delta': 30, 'epsilon': 14}
firewall_logs = [
    'LOG:ERR:001', 'DROP:SRC=10.0.0.5', 'ALLOW:PORT=80',
    'ALERT:SCAN:2024', 'LOG:INFO:OK'
]

auxiliary_sequence = [3, 7, 2, 8, 5, 12, 9]
key_list = ['a', 'b', 'c', 'd']
value_list = [10, 25, 150, 80]

# Distractor calls
_ = analyze_network_flow([[1, 2], [3, 4]], [2, 3])
_ = transform_data_sequence(auxiliary_sequence)
_ = build_index_map(key_list, value_list)

# Critical execution point
final_diagnostic = compute_integrity_score(network_nodes, firewall_logs)
print(f"Result: {final_diagnostic}")