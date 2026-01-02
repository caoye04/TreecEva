from collections import defaultdict

# System load simulation over time slots
cpu_loads = [12, 15, 23, 7, 19, 31, 8]
memory_pressure = [4, 6, 5, 3, 10, 12, 2]
time_slots = ['t0', 't1', 't2', 't3', 't4', 't5', 't6']

# Irrelevant distractor variables (minimal interference)
dummy_flag = False
placeholder_data = [0] * len(cpu_loads)

# Aggregation structure using defaultdict
load_summary = defaultdict(int)
total_load = 0
threshold_met = False

for idx, (cpu, mem) in enumerate(zip(cpu_loads, memory_pressure)):
    # Compute combined load score
    load_score = cpu + mem * 2
    load_summary[time_slots[idx]] = load_score
    total_load += load_score
    
    # Critical condition with early break
    if load_score > 40 and not threshold_met:
        threshold_met = True
        break

print(f"Result: {total_load}")