from itertools import accumulate

# Simulate daily resource allocation over a week
daily_allocations = [120, 85, 150, 60, 200, 90, 130]

def calculate_usage_profile(base_allocations):
    # Apply progressive utilization rate based on day of week
    utilization_rates = [0.8, 0.9, 0.95, 0.75, 0.99, 0.7, 0.85]
    usage_log = [int(a * r) for a, r in zip(base_allocations, utilization_rates)]
    
    # Compute cumulative system load with midweek reset
    system_loads = list(accumulate(usage_log))
    system_loads[3] = usage_log[3]  # Reset after intensive use on day 3
    system_loads[4] = system_loads[3] + usage_log[4]
    
    # Fill remaining days cumulatively
    for i in range(5, len(system_loads)):
        system_loads[i] = system_loads[i-1] + usage_log[i]
        
    peak_capacity = max(system_loads)
    return peak_capacity

result = calculate_usage_profile(daily_allocations)
print(f"Target result: {result}")