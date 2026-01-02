from itertools import cycle

# System parameters
capacities = [12, 7, 15, 9, 20, 6]
time_phases = ['peak', 'off', 'peak', 'off', 'peak']
operation_mode = True
safety_margin = 3

# Simulate dynamic load distribution
total_load = 0
peak_capacity = 0
phase_cycle = cycle(time_phases)

for i, cap in enumerate(capacities):
    current_phase = next(phase_cycle)
    adjusted_cap = cap - safety_margin if current_phase == 'peak' else cap + safety_margin
    
    if operation_mode and adjusted_cap > 10:
        total_load += adjusted_cap
        if current_phase == 'peak':
            peak_capacity = max(peak_capacity, adjusted_cap)
            if total_load >= 30:
                break

print(f"Target result: {peak_capacity}")