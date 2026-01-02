def calculate_utilization(segments):
    total_bandwidth = 0
    active_links = 0
    redundancy_factor = 1.75
    overhead_estimate = 0
    
    for segment in segments:
        nodes = segment['nodes']
        links = segment['links']
        
        # Irrelevant computation: estimating latency (not used)
        avg_latency = sum([len(n) for n in nodes]) / len(nodes) if nodes else 0
        overhead_estimate += avg_latency * 0.3
        
        # Relevant logic: count active links and bandwidth
        link_count = len(links)
        if link_count > 2:
            active_links += link_count
            
        # Bandwidth modeled as product of node length combinations
        combinatoric_bandwidth = 0
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                combinatoric_bandwidth += len(nodes[i]) + len(nodes[j])
        
        total_bandwidth += combinatoric_bandwidth

    # Distractor: unused security check
    security_audit_log = set()
    for segment in segments:
        flagged = {n for n in segment['nodes'] if 'admin' in n}
        security_audit_log.update(flagged)
    
    # Conditional expression for efficiency tier
    efficiency_tier = 'high' if total_bandwidth > 50 else 'medium' if total_bandwidth > 20 else 'low'
    
    # Final utilization includes only active links and bandwidth
    base_utilization = total_bandwidth * (active_links / len(segments) if segments else 1)
    final_capacity = int(base_utilization * 0.85)  # 15% protocol overhead
    
    return final_capacity

# Network configuration data
topology = [
    {
        'nodes': ['client_a', 'server_z', 'relay_m'],
        'links': ['lz1', 'lz2', 'lz3', 'lz4']
    },
    {
        'nodes': ['edge_1', 'edge_2'],
        'links': ['le1', 'le2']
    },
    {
        'nodes': ['hub_x', 'hub_y', 'hub_z', 'backup_n'],
        'links': ['lh1', 'lh2', 'lh3']
    }
]

# Misleading pre-computation (dead-end analysis)
redundant_analysis = [len(seg['nodes']) ** 2 for seg in topology]
avg_redundancy = sum(redundant_analysis) / len(redundant_analysis)

# Key execution point
final_capacity = calculate_utilization(topology)
print(f"Result: {final_capacity}")