import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def is_on_circumference(point, center_x, center_y, radius):
    distance = math.sqrt((point.x - center_x)**2 + (point.y - center_y)**2)
    return abs(distance - radius) < 1e-9

candidate_bench_positions = [
    Point(5, 0),
    Point(0, 5),
    Point(-5, 0),
    Point(0, -5),
    Point(3, 4),
    Point(4, 3),
    Point(-3, -4),
    Point(2.5, 4.33),
    Point(-2.5, -4.33),
    Point(1, 1)
]

valid_bench_count = 0
for position in candidate_bench_positions:
    if is_on_circumference(position, 0, 0, 5):
        valid_bench_count += 1

print(f"Result: {valid_bench_count}")