from itertools import combinations

# System load simulation over time slots
time_slots = [1, 2, 3, 4, 5]
base_loads = [10, 15, 12, 8, 20]
fluctuation_factors = [1.1, 0.9, 1.2]

event_loads = []
for factor in fluctuation_factors:
    adjusted = [int(load * factor) for load in base_loads]
    event_loads.append(adjusted)

# Simulate concurrent events using combinatorics
system_states = []
for combo in combinations(event_loads, 2):
    combined_state = [sum(x) for x in zip(combo[0], combo[1])]
    system_states.append(sum(combined_state))

# Critical system capacity evaluation
peak_capacity = max(system_states)

# Irrelevant diagnostic (minor interference)
diagnostic_flag = len(time_slots) > 3

print(f"Result: {peak_capacity}")