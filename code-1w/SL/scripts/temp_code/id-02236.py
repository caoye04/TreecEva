from itertools import dropwhile

# System monitoring simulation with preprocessing
base_loads = [15, 23, 8, 47, 16, 29, 33, 21, 9, 40, 7]
threshold = 20

def is_below_threshold(x):
    return x < threshold

# Trim beginning and end of system load readings below threshold
filtered_forward = list(dropwhile(is_below_threshold, base_loads))
reversed_remaining = base_loads[::-1]
filtered_both_sides = list(dropwhile(is_below_threshold, reversed_remaining))[::-1]

# Extract middle segment by intersecting both passes
common_start = len(base_loads) - len(filtered_both_sides)
cut_end = len(base_loads) - len(filtered_forward)
system_loads_trimmed = base_loads[common_start:cut_end]

# Key computation point
peak_capacity = max(system_loads_trimmed)

# Additional unrelated metric (minor distraction)
avg_temp = sum([22, 23, 21, 24]) / 4

print(f"Result: {peak_capacity}")