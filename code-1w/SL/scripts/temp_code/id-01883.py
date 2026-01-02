def analyze_node_sequence(nodes):
    # Irrelevant transformation: reverses and squares indices
    reversed_indices = [len(nodes) - i for i in range(len(nodes))]
    squared_offsets = [i**2 for i in reversed_indices]
    offset_sum = sum(squared_offsets)

    # Distractor: unused function
    def decrypt_payload(data):
        return sum([ord(c) for c in data]) % 7

    # Real logic begins: filter active nodes with even IDs
    active_nodes = [node for node in nodes if node['status'] == 'ACTIVE']
    even_id_nodes = [node for node in active_nodes if node['node_id'] % 2 == 0]

    # Compute cumulative signal strength using enumerate
    signal_strengths = []
    for idx, node in enumerate(even_id_nodes):
        adjusted_power = node['power'] * (idx + 1)
        signal_strengths.append(adjusted_power)

    # Use zip to pair with dummy metadata
    timestamps = [15, 30, 45, 60]
    paired_data = list(zip(signal_strengths, timestamps))

    # Misleading intermediate: looks important but unused later
    avg_pair = sum([p[0] for p in paired_data]) / len(paired_data) if paired_data else 0

    # Core calculation: weighted depth using lambda
    weight_func = lambda x, i: x * (i * 0.1)
    weighted_values = [weight_func(val, i) for i, val in enumerate(signal_strengths)]

    # Add decoy recursive function
    def traverse_tree(depth):
        if depth <= 0:
            return 1
        return depth + traverse_tree(depth - 2)

    # Unused recursion call — red herring
    tree_result = traverse_tree(7)

    # Linear search for a threshold breach (real logic)
    threshold_breach_index = -1
    for i, val in enumerate(weighted_values):
        if val > 15.0:
            threshold_breach_index = i
            break  # early return simulation

    if threshold_breach_index == -1:
        threshold_breach_index = len(weighted_values)

    # Final diagnostic based on index and power sum
    total_power = sum(signal_strengths)
    final_score = total_power - (threshold_breach_index * 10)

    return final_score


def compute_integrity_score(node_list):
    # Dead code path: this condition never triggers due to input structure
    if any('corrupted' in node for node in node_list):
        return -999

    # Actual processing
    result = analyze_node_sequence(node_list)
    checksum = sum([node['node_id'] for node in node_list]) % 100

    # Combine with irrelevant offset
    magic_offset = 42
    adjusted_result = result + magic_offset - checksum
n
    return adjusted_result

# Simulated network node dataset
network_nodes = [
    {'node_id': 101, 'status': 'ACTIVE', 'power': 3.5},
    {'node_id': 102, 'status': 'INACTIVE', 'power': 7.2},
    {'node_id': 103, 'status': 'ACTIVE', 'power': 2.8},
    {'node_id': 104, 'status': 'ACTIVE', 'power': 6.1},
    {'node_id': 105, 'status': 'ACTIVE', 'power': 4.3},
    {'node_id': 106, 'status': 'ACTIVE', 'power': 8.7},
    {'node_id': 107, 'status': 'INACTIVE', 'power': 1.9},
    {'node_id': 108, 'status': 'ACTIVE', 'power': 5.4}
]

# Key statement
final_diagnostic = compute_integrity_score(network_nodes)
print(f"Result: {final_diagnostic}")