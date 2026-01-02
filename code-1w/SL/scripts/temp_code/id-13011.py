from itertools import accumulate

def calculate_network_load():
    base_signal = [3, -1, 4, 1, -5, 9, 2]
    filtered = [x if x > 0 else 0 for x in base_signal]
    smoothed = list(accumulate(filtered))
    
    # Simulate hourly usage growth
    usage_levels = []
    for hour in range(len(smoothed)):
        usage = smoothed[hour] + 2 * hour
        usage_levels.append(usage)
        
        if usage > 20:  # early exit if threshold exceeded
            break

    peak_capacity = max(usage_levels)
    status_flag = 'OK'
    temp_var = sum(base_signal)  # irrelevant to final result
    return peak_capacity

result = calculate_network_load()
print(f"Result: {result}")