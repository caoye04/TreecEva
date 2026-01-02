from itertools import compress

# System resource monitoring simulation
cpu_loads = [78, 85, 90, 88, 76]
memory_usage = [64, 72, 80, 85, 70]
total_capacity = 100

# Calculate normalized usage ratios
efficiency_scores = []
for i in range(len(cpu_loads)):
    avg_usage = (cpu_loads[i] + memory_usage[i]) / 2
    normalized_ratio = avg_usage / total_capacity
    efficiency_scores.append(round(normalized_ratio, 3))

# Determine if high-usage threshold is consistently exceeded
dominant_usage = list(compress(cpu_loads, (usage > 80 for usage in cpu_loads)))
usage_count = len(dominant_usage)

# Key evaluation: is threshold met across all periods?
threshold_met = all(usage_ratio > 0.75 for usage_ratio in efficiency_scores)

# Print result
print(f"Result: {threshold_met}")