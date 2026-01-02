from itertools import combinations

# Simulate performance evaluation of task pipelines in a distributed system
base_tasks = [3, 5, 7, 11, 13]
overhead_factor = 0.85
dummy_counter = 0
useless_sum = 0

# Irrelevant accumulation (distractor)
for i in range(len(base_tasks)):
    for j in range(i + 1):
        useless_sum += base_tasks[j] * (j % 3)

efficiencies = []
resource_peaks = []
temporary_buffer = []

# Evaluate all possible 3-task workflows
for combo in combinations(base_tasks, 3):
    # Real computation: pipeline throughput
    raw_throughput = combo[0] * combo[1] + combo[2]
    
    # Apply overhead and normalize by total task weight
    adjusted_load = sum(combo) * overhead_factor
    efficiency = raw_throughput / adjusted_load
    
    # Track peak resource use (semi-relevant but not used in final answer)
    peak_resource = max(combo) * 1.1
    resource_peaks.append(peak_resource)
    
    # Only efficiency matters for final result
    efficiencies.append(round(efficiency, 4))
    
    # Dummy logic to increase cognitive load
    if len(efficiencies) % 2 == 0:
        dummy_counter += 1
    else:
        temp_val = (combo[0] + combo[1]) / 2.0
        temporary_buffer.append(temp_val)

# Additional irrelevant processing (dead path)
sorted_resources = sorted(resource_peaks, reverse=True)
filtered_temps = [t for t in temporary_buffer if t > 5]

# Key statement: determine highest efficiency
peak_efficiency = max(efficiencies)

# Print final target result
print(f"Result: {peak_efficiency}")