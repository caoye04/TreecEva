channels = [
    frozenset({100, 200, 300}),
    frozenset({150, 250, 350}),
    frozenset({100, 150, 200}),
    frozenset({300, 350, 400})
]
frequency_usage = {f: 0 for f in range(100, 401, 50)}
allocation_requests = [50, 75, 60, 90, 40]
threshold = 2
total_bandwidth_allocated = 0

for request in allocation_requests:
    allocated = False
    for channel in channels:
        if allocated:
            break
        overlap = {f for f in channel if frequency_usage[f] < threshold}
        if len(overlap) >= 2:
            # Greedy selection: use first available channel
            for freq in sorted(overlap):
                if frequency_usage[freq] < threshold:
                    frequency_usage[freq] += 1
                    total_bandwidth_allocated += request
                    allocated = True
                    break
    if not allocated:
        break  # Early termination if no channel available

# Merge with default allocations using dictionary comprehension
base_allocations = {f: 10 for f in range(100, 401, 100)}
final_allocations = {**frequency_usage, **{f: base_allocations.get(f, 0) + frequency_usage.get(f, 0) for f in set(frequency_usage) | set(base_allocations)}}

# Additional computation based on merged data
for f, usage in final_allocations.items():
    if usage > 3:
        total_bandwidth_allocated += f * (usage - 3)

print(f"Result: {total_bandwidth_allocated}")