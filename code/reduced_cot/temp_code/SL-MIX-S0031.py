from collections import defaultdict
import numpy as np

def validate_coordinates(func):
    def wrapper(*args, **kwargs):
        coords = args[1]
        if not all(isinstance(c, (int, float)) and -90 <= c <= 90 for c in coords[:2]):
            raise ValueError("Invalid coordinates")
        return func(*args, **kwargs)
    return wrapper

class GeoSpaceMeta(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                dct[attr_name] = validate_coordinates(attr_value)
        return super().__new__(cls, name, bases, dct)

class GeospatialProcessor(metaclass=GeoSpaceMeta):
    def __init__(self):
        self.coord_cache = defaultdict(list)
    
    def transform(self, point):
        x, y = point
        # Rotation matrix for 90 degrees
        rotation_matrix = np.array([[0, -1], [1, 0]])
        transformed = np.dot(rotation_matrix, np.array([x, y]))
        return transformed.tolist()

# Initialize processor
processor = GeospatialProcessor()

# Encoded input coordinates as frozensets
raw_points = [
    frozenset({(10, 20)}),
    frozenset({(30, 40)}),
    frozenset({(-10, -30)})
]

# Transformation pipeline
encoded_areas = []
for fp in raw_points:
    point = list(fp)[0]
    transformed_point = processor.transform(point)
    encoded_areas.append(frozenset({tuple(transformed_point)}))

# Area calculation from transformed points
areas = []
for ea in encoded_areas:
    x, y = list(ea)[0]
    area = abs(x * y)
    areas.append(area)

transformed_area = sum(areas)
print(f"Result: {transformed_area}")