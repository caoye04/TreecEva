from functools import wraps
from collections import namedtuple
import math

def precision_control(decimal_places):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return round(result, decimal_places)
        return wrapper
    return decorator

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

Coordinate = namedtuple('Coordinate', ['x', 'y'])

@precision_control(3)
def scale_coordinate(value, factor):
    return value * factor

def process_geospatial_data(raw_coord):
    # Convert to named tuple
    coord = Coordinate(*raw_coord)
    
    # Calculate Fibonacci scaling factor (using x-coordinate's integer part)
    fib_index = int(abs(coord.x)) % 10 + 5
    scaling_factor = fibonacci(fib_index) / 1000.0
    
    # Apply scaling with precision control
    scaled_x = scale_coordinate(coord.x, scaling_factor)
    scaled_y = scale_coordinate(coord.y, scaling_factor)
    
    # Perform bitwise operations on scaled values
    x_bits = int(scaled_x * 1000) & 0xFF
    y_bits = int(scaled_y * 1000) | 0x10
    
    # Apply XOR mask based on geometric properties
    magnitude = math.sqrt(x_bits**2 + y_bits**2)
    mask = int(magnitude) ^ 0xAA
    
    # Final transformation
    transformed_x = (x_bits ^ mask) >> 2
    transformed_y = (y_bits ^ mask) << 1
    
    return transformed_x, transformed_y

# Process the coordinate
target_coord = (23.7, -45.2)
transformed_x, transformed_y = process_geospatial_data(target_coord)
print(f"Result: {transformed_y}")