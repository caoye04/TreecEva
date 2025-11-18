import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def can_place(bed1, bed2):
    return distance((bed1[0], bed1[1]), (bed2[0], bed2[1])) >= bed1[2] + bed2[2]

# List of potential flower beds as (x, y, radius)
flower_beds = [
    (0, 0, 2),
    (3, 0, 1),
    (0, 4, 1),
    (5, 3, 2),
    (2, 2, 1)
]

# Sort beds by radius in descending order for greedy selection
sorted_beds = sorted(flower_beds, key=lambda x: x[2], reverse=True)

selected_beds = []
for bed in sorted_beds:
    if all(can_place(bed, selected) for selected in selected_beds):
        selected_beds.append(bed)

max_flower_beds = len(selected_beds)
print(f"Result: {max_flower_beds}")