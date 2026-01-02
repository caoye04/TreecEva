from collections import defaultdict

# Simulate a distributed system node load balancing task
def preprocess_node_data(raw_logs):
    processed = defaultdict(int)
    for log in raw_logs:
        node_id = log.split('-')[0]
        load = int(log.split('-')[1])
        processed[node_id] += load
    return processed

# Misleading auxiliary function that calculates variance but isn't used in final result
def calculate_load_variance(data):
    values = list(data.values())
    mean = sum(values) / len(values)
    squared_diffs = [(x - mean) ** 2 for x in values]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance

# Analyze communication patterns between nodes (distractor computation)
def analyze_communication(raw_logs):
    comm_pairs = set()
    for i in range(len(raw_logs) - 1):
        src = raw_logs[i].split('-')[0]
        dst = raw_logs[i+1].split('-')[0]
        if src != dst:
            comm_pairs.add((src, dst))
    return len(comm_pairs)

# Core workload balancing logic
def balance_workload(nodes, weights):
    total_weight = sum(weights)
    normalized = [w / total_weight for w in weights]
    
    # Apply exponential adjustment to prioritize heavier nodes
    adjusted = [normalized[i] * (1.5 ** i) for i in range(len(normalized))]
    
    # Introduce bitwise influence based on node index (semi-relevant)
    bit_influence = 0
    for i in range(len(nodes)):
        bit_influence ^= (i & 3)  # XOR with lower 2 bits of index
    
    # Actual key computation path
    base_load = 0
    for i, node in enumerate(nodes):
        if len(node) % 2 == 1:  # Only odd-length node IDs contribute
            base_load += adjusted[i] * 100
    
    # Secondary adjustment based on character sum (relevant filter)
    char_sum = sum(ord(c) for node in nodes for c in node)
    if char_sum > 500:
        base_load *= 1.1
    
    # Distractor: unused intermediate calculation
    dummy_aggregation = sum([len(n) * w for n, w in zip(nodes, weights)]) / (len(nodes) + 1)
    
    # Final adjustment using constant factor
    final_load = int(base_load + bit_influence * 5)
    
    return final_load

# Main execution
if __name__ == '__main__':
    # Raw system logs (simulated input data)
    raw_logs = [
        'N1-45', 'N2-30', 'N3-55', 'N1-20', 'N4-40',
        'N2-35', 'N3-25', 'N4-50', 'N1-15', 'N2-45'
    ]
    
    # Preprocess logs to get node mappings
    node_data = preprocess_node_data(raw_logs)
    nodes = sorted(node_data.keys())
    weights = [node_data[n] for n in nodes]
    
    # Analyze communication (distractor call - result not used)
    _ = analyze_communication(raw_logs)
    
    # Calculate variance (distractor call - result ignored)
    _ = calculate_load_variance(node_data)
    
    # Key statement: compute final balanced load
    final_load = balance_workload(nodes, weights)
    
    # Output target result
    print(f"Target result: {final_load}")