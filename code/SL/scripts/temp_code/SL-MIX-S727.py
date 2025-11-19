import math
from itertools import combinations

def calculate_triangle_properties(vertices):
    a, b, c = vertices
    side1 = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    side2 = math.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)
    side3 = math.sqrt((c[0]-a[0])**2 + (c[1]-a[1])**2)
    perimeter = side1 + side2 + side3
    s = perimeter / 2
    area_squared = s * (s - side1) * (s - side2) * (s - side3)
    area = math.sqrt(max(area_squared, 0))
    return perimeter, area

def get_intensity_modifier(triangle_type, area, perimeter):
    match triangle_type:
        case 'equilateral' if area > 50:
            return 3
        case 'isosceles' if perimeter < 20:
            return 2
        case 'scalene' if area > 30 and perimeter > 25:
            return 4
        case _:
            return 1

sensor_readings = [
    [(0, 0), (5, 0), (2.5, 4.33)],  # Equilateral-ish
    [(0, 0), (0, 6), (8, 0)],       # Right triangle
    [(1, 1), (4, 1), (1, 5)],       # Right triangle
    [(0, 0), (7, 2), (3, 6)]        # Scalene
]

adjustment_accumulator = 0
for vertices in sensor_readings:
    perimeter, area = calculate_triangle_properties(vertices)
    sides = [math.sqrt((vertices[i][0]-vertices[j][0])**2 + (vertices[i][1]-vertices[j][1])**2) 
             for i, j in combinations(range(3), 2)]
    tolerance = 0.1
    triangle_type = ('equilateral' if abs(sides[0]-sides[1]) < tolerance and abs(sides[1]-sides[2]) < tolerance
                     else 'isosceles' if abs(sides[0]-sides[1]) < tolerance or abs(sides[1]-sides[2]) < tolerance or abs(sides[0]-sides[2]) < tolerance
                     else 'scalene')
    modifier = get_intensity_modifier(triangle_type, area, perimeter)
    valid_area = area > 10
    valid_perimeter = perimeter > 15
    if valid_area and valid_perimeter and not (triangle_type == 'scalene' and area < 20):
        adjustment_accumulator += modifier * int(area) // 2
    elif valid_area or valid_perimeter:
        adjustment_accumulator += modifier

print(f"Result: {adjustment_accumulator}")