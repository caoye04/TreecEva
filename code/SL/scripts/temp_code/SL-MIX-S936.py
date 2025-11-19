import math

class PrecisionManager:
    def __enter__(self):
        self.old_precision = math.pow(10, -9)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Circle 1: center (x1, y1) and radius r1
circle1_x, circle1_y, r1 = 0, 0, 5

# Circle 2: center (x2, y2) and radius r2
circle2_x, circle2_y, r2 = 8, 0, 4

distance_func = lambda x1, y1, x2, y2: math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

with PrecisionManager() as pm:
    center_distance = distance_func(circle1_x, circle1_y, circle2_x, circle2_y)
    collision_threshold = r1 + r2
    collision_detected = 1 if center_distance <= collision_threshold else 0

print(f'Result: {collision_detected}')