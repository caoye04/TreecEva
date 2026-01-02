def balance_workload(load_profile, limit):
    adjusted = {}
    overflow = 0
    for node, load in load_profile.items():
        if load > limit:
            excess = load - limit
            adjusted[node] = limit + (excess * 0.5)
            overflow += excess * 0.5
        else:
            adjusted[node] = load
    
    # Distribute overflow across underloaded nodes
    for node, load in adjusted.items():
        if load < limit and overflow > 0:
            needed = limit - load
            fill = min(needed * 0.3, overflow)
            adjusted[node] += fill
            overflow -= fill
            
    total = sum(adjusted.values())
    stability_ratio = total / len(adjusted) if adjusted else 0
    final_score = round(stability_ratio, 3)
    
    # Dummy variables for minimal interference
    dummy_flag = True
    temp_result = [x for x in range(len(adjusted))]
    
    return final_score

# System cluster load data
cluster_load = {
    'node_a': 87,
    'node_b': 95,
    'node_c': 76,
    'node_d': 102,
    'node_e': 68
}
threshold = 90

final_load = balance_workload(cluster_load, threshold)
print(f"Target result: {final_load}")