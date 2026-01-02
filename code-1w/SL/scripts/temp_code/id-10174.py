from itertools import combinations

# Simulate hourly network node utilization across a distributed system
node_loads = [18, 23, 15, 40, 32, 28, 35]
threshold = 25
window_size = 3

# Track rolling averages for anomaly detection (distractor computation)
rolling_averages = []
for i in range(len(node_loads) - window_size + 1):
    window_avg = sum(node_loads[i:i+window_size]) / window_size
    rolling_averages.append(round(window_avg, 2))

# Identify high-stress segments where at least two nodes exceed threshold (semi-relevant)
high_stress_periods = 0
for i, load in enumerate(node_loads):
    if load > threshold:
        if i > 0 and node_loads[i-1] > threshold:
            high_stress_periods += 1

# Generate all possible node pairs for redundancy analysis (dead code path)
redundancy_pairs = list(combinations(node_loads, 2))
valid_pairs = [pair for pair in redundancy_pairs if sum(pair) > 50]  # Not used later

# Compute usage levels based on exponential stress factor on critical nodes
usage_levels = []
for load in node_loads:
    if load > threshold:
        stress_factor = 1.5
    else:
        stress_factor = 1.1
    adjusted_usage = load * stress_factor
    if adjusted_usage.is_integer():
        usage_levels.append(int(adjusted_usage))
    else:
        usage_levels.append(int(adjusted_usage) + 1)  # Ceiling behavior

# Normalize usage levels by removing lowest two values (simulates adaptive load routing)
sorted_usages = sorted(usage_levels)
trimmed_usages = sorted_usages[2:]  # Remove two lowest simulated backup nodes

# Key computational step: determine peak capacity requirement after trimming
peak_capacity = max(usage_levels)

# Additional irrelevant tracking variables
system_efficiency = len(trimmed_usages) / len(node_loads)
anomaly_count = len([x for x in rolling_averages if x > 30])

# Final output
print(f"Result: {peak_capacity}")