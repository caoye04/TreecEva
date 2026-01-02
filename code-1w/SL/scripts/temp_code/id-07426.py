from itertools import cycle

def calculate_resilience(load_pattern, backup_nodes):
    base_stress = sum([x ** 2 for x in load_pattern if x > 3])
    redundancy_cycle = cycle(backup_nodes)
    adjusted_stress = 0
    for stress in load_pattern:
        if stress > 4:
            adjustment = next(redundancy_cycle)
            adjusted_stress += stress - adjustment
        else:
            adjusted_stress += stress
    return (base_stress + len(backup_nodes)) % 97

# System parameters
time_slices = [2, 5, 3, 6, 4, 7]
spare_modules = [2, 1, 3]

# Irrelevant auxiliary variable (minimal distraction)
baseline_efficiency = 85.4

resilience_score = calculate_resilience(time_slices, spare_modules)
print(f"Target result: {resilience_score}")