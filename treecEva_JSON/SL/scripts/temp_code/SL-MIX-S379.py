import math
from collections import defaultdict

class ElevationProfileProcessor:
    def __init__(self, data_stream):
        self.data_stream = data_stream
        self.elevations = []
        self.metrics = defaultdict(float)
    
    def __enter__(self):
        # Tokenize and decode elevation data
        tokens = self.data_stream.split(';')
        for token in tokens:
            if token.startswith('E'):
                # Decode elevation values (E followed by base36 encoded number)
                elevation_value = int(token[1:], 36)
                self.elevations.append(elevation_value)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def compute_spatial_metrics(self):
        if not self.elevations:
            return
        
        # Calculate Fibonacci-weighted elevation changes
        fib_cache = {}
        def fib(n):
            if n in fib_cache:
                return fib_cache[n]
            if n <= 1:
                return n
            fib_cache[n] = fib(n-1) + fib(n-2)
            return fib_cache[n]
        
        # Geometry calculations for spatial profiling
        peak_elevation = max(self.elevations)
        valley_elevation = min(self.elevations)
        peak_index = self.elevations.index(peak_elevation)
        valley_index = self.elevations.index(valley_elevation)
        
        # Spatial distance using Euclidean distance
        horizontal_distance = abs(peak_index - valley_index)
        vertical_distance = abs(peak_elevation - valley_elevation)
        spatial_distance = math.sqrt(horizontal_distance**2 + vertical_distance**2)
        
        # Calculate Fibonacci-weighted elevation changes
        elevation_changes = []
        for i in range(1, len(self.elevations)):
            change = self.elevations[i] - self.elevations[i-1]
            weight = fib(i % 10)  # Use Fibonacci weight cycling every 10 points
            elevation_changes.append(change * weight)
        
        # Aggregate metrics using dictionary comprehension
        self.metrics = {
            'peak': peak_elevation,
            'valley': valley_elevation,
            'spatial_distance': spatial_distance,
            'weighted_changes_sum': sum(elevation_changes),
            'average_change': sum(elevation_changes) / len(elevation_changes) if elevation_changes else 0
        }
        
        # Calculate peak elevation delta using trigonometric adjustment
        angle_factor = math.sin(math.radians(30))  # 30-degree angle factor
        peak_elevation_delta = int(peak_elevation - (valley_elevation * angle_factor))
        
        # Early return condition for special cases
        if peak_elevation > 1000:
            peak_elevation_delta = peak_elevation_delta * 2
            return peak_elevation_delta
        
        return peak_elevation_delta

data_stream = "E1a;E2t;E1k;E3c;E2v;E4f;E1z;E5j;E3h;E6g"

with ElevationProfileProcessor(data_stream) as processor:
    peak_elevation_delta = processor.compute_spatial_metrics()
    
print(f"Result: {peak_elevation_delta}")