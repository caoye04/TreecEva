from collections import defaultdict

# Simulate network node load distribution over time
node_loads = [12, 15, 12, 18, 21, 15, 21, 24, 18, 15, 12]
threshold = 14
grace_zone = 3

# Track how often nodes exceed dynamic thresholds
event_counter = defaultdict(int)
usage_tracker = {}
baseline_shift = sum(node_loads) / len(node_loads)  # Irrelevant baseline calculation
dummy_result = [x ** 0.5 for x in node_loads if x > threshold]  # Distractor: unused computation

for idx, load in enumerate(node_loads):
    adjusted_threshold = threshold + (idx % grace_zone)

    if load > adjusted_threshold:
        event_counter['overload'] += 1
        hour_slot = idx % 12 + 1
        # Accumulate effective capacity per hour slot
        if hour_slot in usage_tracker:
            usage_tracker[hour_slot] += load * (1 + (load // 10) * 0.1)
        else:
            usage_tracker[hour_slot] = load * (1 + (load // 10) * 0.1)
    elif load == adjusted_threshold:
        event_counter['critical'] += 1  # Rare case, adds minor logic branch
    else:
        event_counter['normal'] += 1

        # Dead code path: never executed due to logic structure
        if load < 5:
            usage_tracker['low'] = 1

# Secondary distractor: complex filtering with no impact
filtered_nodes = list(filter(lambda x: x > 15, node_loads))
smoothed = [filtered_nodes[i] for i in range(len(filtered_nodes)) if i == 0 or filtered_nodes[i] != filtered_nodes[i-1]]

# Key statement where target variable is determined
peak_capacity = max(usage_tracker.values()) if usage_tracker else 0

# Additional irrelevant transformation
normalized = [round((x - min(node_loads)) / (max(node_loads) - min(node_loads)), 3) for x in node_loads]

print(f"Result: {peak_capacity}")