from itertools import groupby

task_priorities = [3, 1, 2, 3, 1, 2, 2, 3]
status_flags = [True, False, True, True, False, True, True, True]  # unused (minor distractor)

# Sort tasks by priority to prepare for grouping
sorted_tasks = sorted(task_priorities)

# Group consecutive tasks with same priority
unique_runs = []
for key, group in groupby(sorted_tasks):
    unique_runs.append(list(group))

total_groups = len(unique_runs)

# Additional irrelevant counter
completion_count = sum(1 for x in status_flags if x)  # not used in result

print(f"Result: {total_groups}")