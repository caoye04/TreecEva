import itertools

def calculate_area(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0

sensor_locations = [(0, 0), (1, 2), (3, 1), (4, 3), (5, 0), (6, 2), (7, 4)]
area_threshold = 1.5
valid_triangle_count = 0

for combo in itertools.combinations(sensor_locations, 3):
    p1, p2, p3 = combo
    if (p1[0] + p2[0] + p3[0]) % 3 != 0:
        continue
    area = calculate_area(p1, p2, p3)
    if area > area_threshold:
        valid_triangle_count += 1

print(f"Result: {valid_triangle_count}")