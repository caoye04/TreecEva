from collections import defaultdict, Counter

# Network node simulation with resource allocation
node_loads = [12, 15, 8, 23, 16, 9, 14, 19, 21, 11]
threshold = 15
critical_nodes = []
overflow_count = 0
load_snapshot = {}

# Misleading pre-processing: counts even/odd (not used in final logic)
even_odd_stats = {'even': 0, 'odd': 0}
for load in node_loads:
    if load % 2 == 0:
        even_odd_stats['even'] += 1
    else:
        even_odd_stats['odd'] += 1

# Simulate dynamic threshold adjustment (distraction)
dynamic_adjustment = sum(load for load in node_loads if load > threshold) // len(node_loads)
adjusted_threshold = threshold + dynamic_adjustment // 3

# Real logic: identify critical nodes above threshold
for i, load in enumerate(node_loads):
    if load > threshold:
        critical_nodes.append(i)
    if load > 20:
        overflow_count += 1

# Take snapshot of high-load nodes (semi-relevant)
for idx in critical_nodes:
    load_snapshot[idx] = node_loads[idx]

# Simulated historical data (dead code path - not used)
historical_peaks = defaultdict(int)
historical_peaks['max_recent'] = max(node_loads)
historical_peaks['avg_peak'] = sum(node_loads) / len(node_loads)

# Auxiliary function with distraction
def calculate_efficiency_score(nodes, loads):
    total = sum(loads[i] for i in nodes)
    penalty = len([i for i in nodes if loads[i] > 20]) * 1.5
    return round(total - penalty, 2) if nodes else 0.0

# Unused helper: suggests importance but doesn't affect outcome
def predict_future_load():
    trend = sum(node_loads[i] - node_loads[i-1] for i in range(1, len(node_loads)))
    return max(0, node_loads[-1] + trend // len(node_loads))

# Core optimization logic
base_allocation = sum(node_loads) * 0.8
contingency_reserve = len(critical_nodes) * 12

# Use list comprehension and conditional expression
allocation_boost = sum([load // 2 for load in node_loads if load > threshold])
allocation_boost += 5 if overflow_count > 0 else 0

# Final bandwidth calculation - key result
def optimize_allocation():
    efficiency = calculate_efficiency_score(critical_nodes, node_loads)
    base = base_allocation + contingency_reserve
    # Apply efficiency multiplier only if more than one critical node
    adjusted = base * (efficiency / 100) if len(critical_nodes) > 1 else base
    return int(adjusted + allocation_boost)

final_bandwidth = optimize_allocation()

# Output result
print(f"Result: {final_bandwidth}")