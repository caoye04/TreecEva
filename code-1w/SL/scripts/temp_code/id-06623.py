from collections import defaultdict

# Simulate a system processing tasks with varying cycle counts
task_list = ['parse', 'encode', 'decode', 'parse', 'encode', 'validate', 'parse']
cycle_costs = {'parse': 12, 'encode': 18, 'decode': 15, 'validate': 22}

# Count frequency of each task
task_freq = defaultdict(int)
for task in task_list:
    task_freq[task] += 1

# Map each unique task to total cycles consumed
cycle_map = {}
for task, count in task_freq.items():
    cycle_map[task] = count * cycle_costs[task]

# Compute total system cycles
total_cycles = sum(cycle_map.values())

# Irrelevant auxiliary counter for minor distraction
dummy_counter = 0
for i in range(3):
    dummy_counter += i ** 2

print(f"Result: {total_cycles}")