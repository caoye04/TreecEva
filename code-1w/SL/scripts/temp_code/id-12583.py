from collections import defaultdict
from itertools import cycle

# Simulate hourly resource usage across multiple servers over a 3-day period
def simulate_resource_usage():
    hours = list(range(24))
    days = 3
    server_names = ['alpha', 'beta', 'gamma', 'delta']
    base_loads = {'alpha': 12, 'beta': 8, 'gamma': 15, 'delta': 10}
    
    # Real tracker for actual peak calculation
    usage_tracker = defaultdict(int)
    
    # Distractor variables: tracking irrelevant metrics
    efficiency_scores = []
    outlier_count = 0
    temp_buffer = []
    historical_avgs = [0] * 24  # Unused in final logic
    snapshot_moment = None
    
    hour_cycle = cycle(hours)
    
    for day in range(days):
        for hour in range(24):
            current_hour = next(hour_cycle)
            fluctuation = (hour // 6) % 4  # Peak at noon, dip at night
            spike_factor = 1.0
            
            if 10 <= hour <= 14:
                spike_factor = 1.8  # Business hours spike
            elif 22 <= hour or hour < 6:
                spike_factor = 0.6  # Nighttime reduction
                
            daily_offset = (day * 24 + hour) % 7  # Some fake pattern
            
            # Real accumulation logic
            total_load = 0
            for server in server_names:
                base = base_loads[server]
                variability = (ord(server[-1]) % 5)  # minor variation per server
                load = base * spike_factor + variability + fluctuation
                if server == 'gamma' and hour == 12:
                    load += 3  # Special boost for gamma at noon
                usage_tracker[current_hour] += int(load)
                total_load += load
                
            # Irrelevant computations (distractors)
            avg_load = total_load / len(server_names)
            efficiency = avg_load / (sum(base_loads.values()) / len(server_names))
            efficiency_scores.append(efficiency)
            
            if avg_load > 25:
                outlier_count += 1
            
            temp_buffer.append(avg_load * 0.1)
            if len(temp_buffer) > 5:
                temp_buffer.pop(0)

    # Key computation point
    peak_capacity = max(usage_tracker.values())
    
    # More red herring operations
    smoothed_peak = peak_capacity * 0.95
    projected_next_week = (smoothed_peak + sum(efficiency_scores[:7])) // 1
    fallback_mode = False
    recovery_point = 0
    
    return peak_capacity

result = simulate_resource_usage()
print(f"Result: {result}")