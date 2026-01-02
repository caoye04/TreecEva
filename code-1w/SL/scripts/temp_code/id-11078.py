from collections import defaultdict

# System resource simulation for a distributed task scheduler
task_loads = [12, 15, 12, 20, 18, 25, 20, 30, 14, 16, 18]
node_mapping = ['A', 'B', 'C', 'D', 'E']
overload_buffer = 7

# Track assigned tasks per node (simulated round-robin with constraints)
assignment_tracker = defaultdict(int)
available_slots = defaultdict(lambda: 100)  # Base capacity per node
dummy_counter = 0

for i, load in enumerate(task_loads):
    selected_node = node_mapping[i % len(node_mapping)]
    assignment_tracker[selected_node] += 1
    
    # Simulate dynamic slot adjustment based on historical usage
    if load > 18:
        available_slots[selected_node] -= load * 1.2
    elif load < 15:
        available_slots[selected_node] += 5
    else:
        available_slots[selected_node] -= load * 0.8

    # Irrelevant tracking of loop iterations (distractor)
    dummy_counter += 1
    temp_shadow = dummy_counter * 0.1  # Unused variable

# Secondary adjustment pass based on assignment frequency
min_assignments = min(assignment_tracker.values())
max_assignments = max(assignment_tracker.values())
penalty_rate = 0.0

if max_assignments - min_assignments > 2:
    penalty_rate = 1.5

for node in available_slots:
    freq = assignment_tracker[node]
    if freq > min_assignments:
        available_slots[node] -= penalty_rate * 2

# Critical computation point
baseline_floor = sum(available_slots.values()) / len(available_slots)
final_capacity = max(available_slots.values()) + overload_buffer

# Extraneous post-processing (does not affect final_capacity)
cleanup_list = [x for x in available_slots.values() if x < baseline_floor]
adjusted_total = sum(cleanup_list) + overload_buffer * 0.5

print(f"Result: {final_capacity}")