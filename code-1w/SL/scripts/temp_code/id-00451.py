from itertools import groupby

classroom_specs = [
    ('A', 25), ('B', 30), ('C', 25), ('D', 40), ('E', 30)
]

# Extract capacity values sorted by room type
sorted_caps = sorted(classroom_specs, key=lambda x: x[0])

capacity_trends = []
running_total = 0

for room, cap in sorted_caps:
    running_total += cap
    capacity_trends.append((room, running_total))

# Key computation point
peak_capacity = max(capacity_trends, key=lambda x: x[1])

# Additional minor operation to slightly increase intervention
idle_rooms = [r for r, c in classroom_specs if c < 30]

print(f"Result: {peak_capacity[1]}")