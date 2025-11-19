import re
from dataclasses import dataclass
from typing import List

def transformation_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

class VertexProcessor:
    def __init__(self):
        self.state = 'INIT'
        self.score = 0
        
    @transformation_counter
    def process_vertex(self, vertex_data: str):
        # Tokenize vertex data
        tokens = re.findall(r'[A-Z]+|[-+]?\d*\.\d+|\d+', vertex_data)
        
        # Pattern matching for vertex classification
        match tokens:
            case ['PEAK', x, y] if float(y) > 10:
                self.state = 'HIGH_PEAK'
                self.score += int(float(x)) * 3
            case ['PEAK', x, y]:
                self.state = 'NORMAL_PEAK'
                self.score += int(float(x))
            case ['VALLEY', x, y] if float(y) < 0:
                self.state = 'DEEP_VALLEY'
                self.score -= int(float(x)) * 2
            case ['VALLEY', x, _]:
                self.state = 'SHALLOW_VALLEY'
                self.score -= int(float(x)) // 2
            case _:
                self.state = 'UNKNOWN'
                self.score += 1
        
        return self.score

# Fibonacci generator for spatial coefficients
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Main processing pipeline
vertices = [
    "PEAK:15.0:12.5",
    "VALLEY:8.0:-3.2",
    "PEAK:7.5:5.0",
    "UNKNOWN:3.0:1.0",
    "VALLEY:12.0:-15.7"
]

processor = VertexProcessor()
spatial_coefficients = [fibonacci(i) for i in range(1, len(vertices)+1)]
aggregate_transformation_score = 0

for i, vertex_str in enumerate(vertices):
    # Parse and format vertex
    parts = vertex_str.split(':')
    formatted_vertex = f"{parts[0]}:{parts[1]}:{parts[2]}"
    
    # Apply transformation
    base_score = processor.process_vertex(formatted_vertex)
    
    # Apply spatial coefficient from Fibonacci sequence
    aggregate_transformation_score += base_score * spatial_coefficients[i]
    
    # Early termination condition
    if processor.state == 'DEEP_VALLEY' and i >= 3:
        break

# Adjust final score with bit manipulation
aggregate_transformation_score ^= (aggregate_transformation_score >> 2) & 0x33333333
aggregate_transformation_score = ((aggregate_transformation_score & 0xAAAAAAAA) >> 1) | ((aggregate_transformation_score & 0x55555555) << 1)

print(f"Result: {aggregate_transformation_score}")