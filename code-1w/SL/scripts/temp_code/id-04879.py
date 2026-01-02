from itertools import combinations

def calculate_remaining_capacity(node_set, max_capacity):
    total_used = 0
    for r in range(1, len(node_set) + 1):
        for combo in combinations(node_set, r):
            total_used += sum(combo) % (max_capacity + 1)
    return max_capacity - (total_used % max_capacity)

# System node load values (in MB)
nodes = {3, 7, 9, 12}
max_load = 20

# Irrelevant auxiliary variable (minimal distraction)
temp_debug_log = "Phase 1 complete"

final_capacity = calculate_remaining_capacity(nodes, max_load)
print(f"Result: {final_capacity}")