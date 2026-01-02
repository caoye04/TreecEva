from itertools import cycle

# System parameters for load distribution
capacities = [12, 8, 15, 6]
threshold = 20
scaling_factor = 1.5

# Simulate cyclic loading process
device_cycle = cycle(capacities)
current_load = 0
final_capacity = 0

for _ in range(10):
    next_boost = next(device_cycle) * scaling_factor
    current_load += next_boost
    
    # Critical intervention point: exit early if threshold exceeded
    if current_load > threshold:
        final_capacity = int(next_boost)
        break
    
    # Irrelevant tracking variable (minor distraction)
    last_load_snapshot = current_load

print(f"Result: {final_capacity}")