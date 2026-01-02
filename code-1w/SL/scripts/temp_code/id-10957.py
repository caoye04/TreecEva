def analyze_workload(servers, maintenance_mode=False):
    base_load = 75
    overhead_factor = 1.15
    threshold = 85

    # Simulate dynamic load adjustments across server clusters
    adjusted_loads = []
    temp_buffer = []
    for i, server in enumerate(servers):
        raw_usage = server['cpu'] + server['memory'] * 0.5
        
        # Apply time-of-day adjustment (simulated)
        if i % 3 == 0:
            raw_usage *= 1.1
        elif i % 5 == 0:
            raw_usage *= 0.95
        
        adjusted = raw_usage * overhead_factor
        adjusted_loads.append(adjusted)
        
        # Irrelevant string processing - distractor
        status_msg = f"Server {server['id']} at {raw_usage:.2f}%"
        status_msg = status_msg.upper().replace(' ', '_')
        temp_buffer.append(len(status_msg))

    # Compute rolling average for smoothing - semi-relevant but not final
    smoothed = []
    window = 3
    for i in range(len(adjusted_loads)):
        start = max(0, i - window + 1)
        smoothed.append(sum(adjusted_loads[start:i+1]) / (i - start + 1))

    # Distractor: unused data structure manipulation
    usage_stats = {i: adj for i, adj in enumerate(adjusted_loads)}
    outlier_count = sum(1 for x in adjusted_loads if x > threshold)

    # Core logic: track peak before normalization
    normalized_usages = [min(x, 100) for x in adjusted_loads]
    usage_levels = [round(x, 1) for x in normalized_usages]
    
    # Key statement
    peak_capacity = max(usage_levels)
    
    # Additional red herring computations
    avg_length = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    compression_ratio = len(servers) / (avg_length + 1e-5)
    
    # Final output
    print(f"Result: {peak_capacity}")

# Input data
server_fleet = [
    {'id': 'A1', 'cpu': 40, 'memory': 60},
    {'id': 'B2', 'cpu': 55, 'memory': 70},
    {'id': 'C3', 'cpu': 65, 'memory': 80},
    {'id': 'D4', 'cpu': 70, 'memory': 75},
    {'id': 'E5', 'cpu': 80, 'memory': 68}
]

analyze_workload(server_fleet)