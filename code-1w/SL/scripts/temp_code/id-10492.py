from collections import defaultdict

# System resource monitoring simulation
def monitor_resources():
    timestamps = [100, 101, 102, 103, 104]
    cpu_loads = [0.45, 0.67, 0.89, 0.72, 0.54]
    mem_usage = [1.2, 1.5, 2.1, 1.8, 1.4]

    # Irrelevant helper: counts timestamp digits (minimal distraction)
    digit_count = sum(len(str(ts)) for ts in timestamps)

    # Track capacity per phase using defaultdict
    capacity_map = defaultdict(float)
    for i, t in enumerate(timestamps):
        capacity_map[f'phase_{i}'] = round(cpu_loads[i] * mem_usage[i], 2)

    # Build capacity levels with zip and enumerate
    capacity_levels = []
    for idx, (phase, cap) in enumerate(zip(capacity_map.keys(), capacity_map.values())):
        adjusted_cap = cap * (0.95 + idx * 0.01)  # Slight growth factor
        capacity_levels.append((phase, round(adjusted_cap, 2)))

    # Key computation point
    peak_capacity = max(capacity_levels, key=lambda x: x[1])

    # Print result for verification
    print(f"Result: {peak_capacity[1]}")

    return peak_capacity

result = monitor_resources()