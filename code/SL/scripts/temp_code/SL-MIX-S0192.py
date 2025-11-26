import itertools

# Process scheduling simulation with priority queues
processes = ["A", "B", "C", "D", "E"]
base_priorities = [3, 1, 4, 2, 5]

# Create priority queue with process names and priorities
priority_queue = []
for idx, (process, priority) in enumerate(zip(processes, base_priorities)):
    adjusted_priority = priority * 2 + idx % 3
    priority_queue.append((process, adjusted_priority))

# Some intermediate calculations that don't affect final result
process_count = len(processes)
total_priority_sum = sum(p[1] for p in priority_queue)
avg_priority = total_priority_sum / process_count

# Sort by priority (lower number = higher priority)
priority_queue.sort(key=lambda x: x[1])

# Distractor operations - calculate some metrics but don't use them
max_priority = max(p[1] for p in priority_queue)
min_priority = min(p[1] for p in priority_queue)
priority_range = max_priority - min_priority

# Critical execution point
final_priority = priority_queue[-1][1]

# Print the result
print(f"Result: {final_priority}")