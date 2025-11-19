import math

def buffer_zone(radius):
    def decorator(func):
        def wrapper(*args, **kwargs):
            original_area = func(*args, **kwargs)
            buffered_area = original_area + (2 * math.pi * radius * math.sqrt(original_area/math.pi))
            return buffered_area
        return wrapper
    return decorator

elevation_points = [(10, 20), (30, 40), (50, 60)]
base_radius = 5

@buffer_zone(base_radius)
def calculate_circular_region(coords):
    x, y = coords
    return math.pi * (x/10)**2

terrain_segments = [
    {'type': 'hill', 'center': elevation_points[0], 'radius': base_radius},
    {'type': 'mountain', 'center': elevation_points[1], 'radius': base_radius*2},
    {'type': 'peak', 'center': elevation_points[2], 'radius': base_radius*1.5}
]

def get_protected_area(segment):
    area_type = segment['type']
    match area_type:
        case 'hill':
            return calculate_circular_region(segment['center'])
        case 'mountain':
            base_area = math.pi * segment['radius']**2
            return base_area * 1.5
        case 'peak':
            base_area = math.pi * segment['radius']**2
            return base_area + (base_area * 0.75)
        case _:
            return 0

conservation_area = 0
for segment in terrain_segments:
    segment_area = get_protected_area(segment)
    conservation_area += int(segment_area) if isinstance(segment_area, float) else segment_area

# Adjust for overlapping zones
overlap_deduction = 0
for i in range(len(elevation_points)):
    for j in range(i+1, len(elevation_points)):
        xi, yi = elevation_points[i]
        xj, yj = elevation_points[j]
        distance = math.sqrt((xi-xj)**2 + (yi-yj)**2)
        if distance < base_radius*2:
            overlap_deduction += (base_radius*2 - distance) * 10

conservation_area = int(conservation_area - overlap_deduction)
print(f"Result: {conservation_area}")