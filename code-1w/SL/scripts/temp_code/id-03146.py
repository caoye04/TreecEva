from itertools import accumulate

# System load simulation with historical data smoothing
def analyze_workload():
    base_loads = [120, 150, 135, 142, 160, 175, 168, 180]
    maintenance_overhead = 22
    scaling_factor = 0.88
    
    # Apply exponential smoothing to historical loads
    smoothed = []
    alpha = 0.3
    smoothed.append(base_loads[0])
    for i in range(1, len(base_loads)):
        smoothed.append(alpha * base_loads[i] + (1 - alpha) * smoothed[i-1])
    
    # Simulate projected usage with growth trend and noise
    trend_growth = [x * 1.05 for x in smoothed]
    noise_offset = [(-1)**i * (i % 3) for i in range(len(trend_growth))]
    noisy_projection = [trend_growth[i] + noise_offset[i] for i in range(len(trend_growth))]
    
    # Adjust for resource compression efficiency
    compressed = [int(x * scaling_factor) for x in noisy_projection]
    
    # Misleading secondary computation: average utilization
    avg_utilization = sum(compressed) / len(compressed)
    threshold_count = len([x for x in compressed if x > 150])
    
    # Redundant transformation using accumulate (not used in final result)
    cumulative_buildup = list(accumulate(compressed, lambda a, b: a + int(b * 0.1)))
    temp_analysis = [max(cumulative_buildup[:i+1]) - min(cumulative_buildup[:i+1]) 
                     for i in range(len(cumulative_buildup))]
    
    # Critical state tracking: usage projection before capacity allocation
    usage_projection = [x + maintenance_overhead for x in compressed]
    peak_capacity = max(usage_projection)
    
    # Dead code path - never executed but adds cognitive load
    if False:
        fallback_mode = sum(smoothed) // len(smoothed)
        peak_capacity = max(peak_capacity, fallback_mode + 50)
    
    return peak_capacity

result = analyze_workload()
print(f"Target result: {result}")