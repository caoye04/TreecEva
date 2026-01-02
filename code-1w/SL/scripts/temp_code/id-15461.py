from itertools import cycle

# System parameters
capacities = [120, 150, 130, 170, 160]
tolerance_threshold = 145
stability_margin = 8
event_sequence = cycle([1, 0, -1])

# Simulate load adjustment under fluctuating conditions
current_load = 100
peak_capacity = 0

for capacity in capacities:
    current_load += next(event_sequence) * 5
    adjusted_capacity = capacity - stability_margin
    
    if current_load > adjusted_capacity:
        peak_capacity = adjusted_capacity
        break
    
    if capacity > peak_capacity:
        peak_capacity = capacity

print(f"Result: {peak_capacity}")