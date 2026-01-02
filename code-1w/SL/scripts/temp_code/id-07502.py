from itertools import combinations

# System load simulation over time with redundancy calculations
def simulate_load_sequence(base_load, fluctuation_rate, duration):
    return [int(base_load + (i % 4 - 1.5) * fluctuation_rate) for i in range(duration)]

# Redundant helper to calculate moving average (not used in final result)
def moving_average(data, window=3):
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]

# Simulate network traffic pattern across 8 hours
traffic_loads = simulate_load_sequence(base_load=120, fluctuation_rate=38, duration=8)

# Misleading intermediate: transform into frequency buckets (unused)
frequency_map = {x: traffic_loads.count(x) for x in set(traffic_loads)}
unique_counts = sorted(frequency_map.values())

# Generate all possible two-hour high-usage windows using combinations
window_combinations = list(combinations(traffic_loads, 2))
two_hour_peaks = [max(pair) for pair in window_combinations]

# Calculate decay-adjusted utilization (semi-relevant but not critical)
decay_factor = 0.9
adjusted_utilization = [val * (decay_factor ** i) for i, val in enumerate(traffic_loads)]

# Core metric: track cumulative usage pattern across overlapping segments
usage_trajectory = []
for shift in range(3):
    segment = traffic_loads[shift:shift+5]  # sliding 5-hour view
    hourly_delta = sum(segment) // len(segment)
    usage_trajectory.append(hourly_delta)

# Introduce distractor: analyze pairwise ratios (never used)
ratio_analysis = list(map(lambda x: round(x[0]/x[1], 2) if x[1] != 0 else 0, combinations(traffic_loads[:4], 2)))

# Key computational step
peak_capacity = max(usage_trajectory)

# Distractor: unpack tuple into unused variables
total_volume, _, *surplus = (sum(traffic_loads), sum(adjusted_utilization), ratio_analysis)

# Final output
print(f"Result: {peak_capacity}")