from collections import Counter

# System load simulation over time intervals
time_slots = ['morning', 'midday', 'afternoon', 'evening', 'night']
workloads = [45, 78, 63, 78, 52]

# Track capacity usage across zones
zone_a_load = [12, 25, 18, 20, 10]
zone_b_load = [15, 20, 22, 25, 18]
zone_c_load = [18, 33, 23, 33, 24]

# Irrelevant utility variable (minor distraction)
total_hours = len(time_slots)

# Aggregate per-time-slot total capacity usage
capacity_per_slot = [
    zone_a_load[i] + zone_b_load[i] + zone_c_load[i]
    for i in range(len(time_slots))
]

# Count frequency of capacity levels
capacity_counter = Counter(capacity_per_slot)

# Key computation point
peak_capacity = max(capacity_counter.values())

# Output result
print(f"Result: {peak_capacity}")