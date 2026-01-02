from itertools import cycle

# Simulate a rotating priority queue of tasks
task_priorities = [3, 1, 4, 1, 5]
agent_load = [2, 7, 1, 8, 2]
status_flags = ['active', 'idle', 'active', 'idle', 'active']

# Irrelevant tracking variable (minor distraction)
cycle_count = 0

# Key computation variables
total_score = 0
current_index = 0

priority_cycle = cycle(task_priorities)

for status, load in zip(status_flags, agent_load):
    priority = next(priority_cycle)
    cycle_count += 1

    if status == 'idle':
        continue

    # Scoring logic: active agents with balanced load get higher score
    if load < 5:
        total_score += priority * 2
    else:
        total_score += max(priority - (load // 4), 1)
    
    # Early termination condition based on cumulative score
    if total_score >= 15:
        break

print(f"Result: {total_score}")