from itertools import combinations

# System configuration for distributed node analysis
def calculate_system_metrics(node_ids, base_load, threshold_multiplier=1.75):
    active_pairs = set()
    temp_logs = []
    usage_caps = []
    
    # Generate meaningful node pairings based on ID proximity
    for pair in combinations(node_ids, 2):
        diff = abs(pair[1] - pair[0])
        if diff < 10:
            active_pairs.add(pair)
    
    # Simulate load distribution across valid pairs
    for (a, b) in active_pairs:
        load_factor = (a + b) % 7 + 1
        computed_load = base_load * load_factor
        adjusted_load = round(computed_load * threshold_multiplier, 2)
        usage_caps.append(int(adjusted_load))

    # Irrelevant secondary calculation - distractor
    entropy_score = 0
    for i in range(len(node_ids)):
        if i % 3 == 0:
            entropy_score += node_ids[i] ^ (base_load % 5)
    
    # Dummy data structure - misleading complexity
    status_map = {}
    for idx, nid in enumerate(node_ids):
        status_map[nid] = {
            'index': idx,
            'active': nid % 2 == 0,
            'score': entropy_score - nid
        }
    
    # Key logic: determine peak capacity from usage caps
    operational_nodes = [cap for cap in usage_caps if cap > 15]
    peak_capacity = max(usage_caps) if operational_nodes else 0
    
    # Dead code path - adds interference
    if len(node_ids) > 100:
        fallback = sum([len(str(x)) for x in node_ids])
        peak_capacity = fallback // 10
    
    # Print final result as required
    print(f"Result: {peak_capacity}")
    return peak_capacity

# Execute with realistic input
node_configuration = [12, 15, 18, 23, 25, 30]
base_workload = 4.5
calculate_system_metrics(node_configuration, base_workload)