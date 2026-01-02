from itertools import accumulate

def calculate_network_load():
    # Simulate hourly data packet rates over 8 hours
    base_rate = [120, 200, 180, 240, 300, 250, 220, 280]
    
    # Apply time-based modulation (e.g., peak hour boost)
    time_factor = [1.0, 1.0, 1.2, 1.3, 1.5, 1.4, 1.2, 1.1]
    adjusted_packets = [int(base_rate[i] * time_factor[i]) for i in range(len(base_rate))]
    
    # Simulate gradual buffer accumulation per hour
    buffer_fill = list(accumulate(adjusted_packets, lambda acc, x: min(acc + x, 2000)))
    
    # Redundant calculation: theoretical throughput ceiling (not used in final result)
    max_possible_throughput = sum(base_rate) * 1.5
    efficiency_ratio = 0.85
    theoretical_limit = max_possible_throughput * efficiency_ratio  # Distractor
    
    # Compute usage levels as percentage of max capacity (2000 packets/hour)
    usage_levels = [round((buf / 2000) * 100, 2) for buf in buffer_fill]
    
    # Introduce irrelevant conditional branch (dead logic path)
    if len(usage_levels) > 10:
        correction_factor = 1.05
        usage_levels = [level * correction_factor for level in usage_levels]
    else:
        dummy_flag = True  # Dead code with no effect
        shadow_copy = usage_levels[:]  # Not used afterward
        
    # Key computation: find peak usage level
    peak_capacity = max(usage_levels)
    
    # Additional distraction: enumerate with unused index tracking
    indexed_analysis = []
    for i, level in enumerate(usage_levels):
        status = "HIGH" if level > 90 else "NORMAL"
        indexed_analysis.append((i, level, status))  # Collected but unused
    
    # Print final result as required
    print(f"Result: {peak_capacity}")
    
    return peak_capacity

# Execute function
calculate_network_load()