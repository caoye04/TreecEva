from collections import defaultdict

# System cluster performance data
base_performance = [120, 150, 90, 200, 130]
threshold = 100

efficiency_flags = [perf > threshold for perf in base_performance]
adjusted_clusters = []

capacity_map = defaultdict(int)
for i, perf in enumerate(base_performance):
    if efficiency_flags[i]:
        adjusted_clusters.append(perf * 1.5)
    else:
        adjusted_clusters.append(perf * 0.8)

    capacity_map[f'cluster_{i}'] = adjusted_clusters[-1]

# Minor irrelevant tracking
idle_count = len([x for x in adjusted_clusters if x < 110])

# Key computation step
total_capacity = sum(capacity for capacity in adjusted_clusters)

print(f"Result: {total_capacity}")