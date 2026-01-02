def calculate_performance(flags):
    base_points = 100
    penalty = 0
    
    # Count how many conditions are met
    condition_count = sum([flags['latency_ok'], flags['memory_ok'], flags['throughput_ok']])
    
    # Apply bonus logic using dictionary and conditional branching
    if condition_count == 3:
        multiplier = 1.5
    elif condition_count == 2:
        multiplier = 1.2
    else:
        multiplier = 0.8
    
    # Irrelevant tracking variable (minimal distraction)
    debug_log = {'processed': True, 'stage': 'scoring'}
    
    # Compute final score
    raw_score = base_points * multiplier
    adjustment = 5 if flags['urgent_mode'] else 0
    final_score = raw_score + adjustment - penalty
    
    return final_score

# System status input
system_status = {
    'latency_ok': True,
    'memory_ok': False,
    'throughput_ok': True,
    'urgent_mode': True
}

# Additional unused flag (slight interference)
inactive_thresholds = {'cpu_max': 90, 'disk_io': 50}

final_score = calculate_performance(system_status)
print(f"Result: {final_score}")