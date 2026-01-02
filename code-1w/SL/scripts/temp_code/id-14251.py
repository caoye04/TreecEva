from collections import Counter

# System performance monitoring simulation
cpu_usage = [78, 85, 90, 75, 88]
memory_usage = [80, 82, 89, 74, 85]
disk_io = [70, 88, 84, 78, 80]

# Calculate composite system loads per node
system_loads = []
for i in range(len(cpu_usage)):
    avg_load = (cpu_usage[i] + memory_usage[i] + disk_io[i]) / 3
    system_loads.append(round(avg_load))

# Identify dominant load pattern using Counter
counter = Counter(system_loads)
dominant_load = counter.most_common(1)[0][0]

# Secondary metric: number of nodes above threshold
overloaded_nodes = sum(1 for load in system_loads if load > 85)

# Final decision based on maximum observed load
final_load = max(system_loads)