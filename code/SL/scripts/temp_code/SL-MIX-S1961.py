import math
from functools import reduce

def process_geospatial_data():
    coordinates = [(3, 4), (5, 12), (8, 15), (7, 24)]
    transformation_rules = ['scale', 'rotate', 'translate']
    scale_factor = 2
    
    # Step 1: Apply transformations using switch-like dictionary
    transformed_coords = []
    for coord in coordinates:
        x, y = coord
        for rule in transformation_rules:
            transform_map = {
                'scale': lambda p: (p[0] * scale_factor, p[1] * scale_factor),
                'rotate': lambda p: (p[0] * math.cos(math.pi/4) - p[1] * math.sin(math.pi/4), 
                                   p[0] * math.sin(math.pi/4) + p[1] * math.cos(math.pi/4)),
                'translate': lambda p: (p[0] + 10, p[1] + 10)
            }
            # Short-circuit evaluation in condition
            if rule in transform_map and len(transformed_coords) < 20:
                coord = transform_map[rule](coord)
        transformed_coords.append(coord)
    
    # Step 2: Calculate distances using list comprehension
    distances = [math.sqrt(x**2 + y**2) for x, y in transformed_coords]
    
    # Step 3: Apply ternary operator filtering
    filtered_distances = [d if d > 15 else 0 for d in distances]
    
    # Step 4: Use functional programming to aggregate
    product_of_distances = reduce(lambda a, b: a * b if a != 0 and b != 0 else max(a, b), filtered_distances, 1)
    
    # Step 5: Parse metadata string
    metadata = "type:geospatial;unit:meters;precision:float"
    tokens = metadata.split(';')
    unit_token = next((token for token in tokens if token.startswith('unit:')), None)
    unit_value = unit_token.split(':')[1] if unit_token else 'unknown'
    
    # Final calculation
    final_metric = int(product_of_distances) % 1000 if unit_value == 'meters' else -1
    
    return final_metric

final_metric = process_geospatial_data()
print(f"Result: {final_metric}")