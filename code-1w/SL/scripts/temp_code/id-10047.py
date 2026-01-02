from collections import Counter

task_loads = [15, 30, 45, 30, 60, 45, 30, 75, 60, 30]
execution_modes = ['low', 'med', 'high', 'med', 'critical', 'high', 'med', 'critical', 'high', 'med']

# Calculate frequency of each task load
task_histogram = Counter(task_loads)

# Count how many times each execution mode appears
mode_counter = Counter(execution_modes)

# Find the most common task load value
frequency_count = task_histogram
peak_frequency = max(frequency_count.values())

# Irrelevant distraction: compute average load (not used in final answer)
avg_load = sum(task_loads) / len(task_loads)

print(f"Result: {peak_frequency}")