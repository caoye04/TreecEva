import math
from functools import lru_cache
from collections import defaultdict

def triangle_area(a, b, c):
    # Using Heron's formula
    s = (a + b + c) / 2.0
    try:
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    except ValueError:
        return 0.0

def quality_metric(area, perimeter):
    if perimeter <= 0:
        return 0.0
    log_scale = math.log(perimeter + 1)
    return area / (log_scale if log_scale > 0 else 1)

@lru_cache(maxsize=None)
def compute_triangle_quality(edge1, edge2, edge3):
    area = triangle_area(edge1, edge2, edge3)
    perimeter = edge1 + edge2 + edge3
    return quality_metric(area, perimeter)

# Triangle mesh definitions
triangles = [
    (3.0, 4.0, 5.0),
    (5.0, 5.0, 5.0),
    (6.0, 8.0, 10.0),
    (7.0, 10.0, 12.0),
    (9.0, 12.0, 15.0)
]

# Dynamic programming cache for aggregated metrics
quality_cache = defaultdict(float)

# Process each triangle
for idx, (e1, e2, e3) in enumerate(triangles):
    base_quality = compute_triangle_quality(e1, e2, e3)
    # Apply recursive refinement factor
    refinement = 0
    temp_e1, temp_e2, temp_e3 = e1, e2, e3
    while temp_e1 > 1.0 and temp_e2 > 1.0 and temp_e3 > 1.0:
        temp_e1 /= 2.0
        temp_e2 /= 2.0
        temp_e3 /= 2.0
        refinement += compute_triangle_quality(temp_e1, temp_e2, temp_e3)
    
    # Combine base quality with refinement using exponent
    combined = base_quality + (refinement / math.exp(0.1 * idx))
    quality_cache[idx] = combined

# Calculate final metric as weighted sum
final_metric = 0.0
weights = [0.1, 0.2, 0.3, 0.25, 0.15]
for i in range(len(triangles)):
    final_metric += quality_cache[i] * weights[i]

# Apply global normalization
final_metric = math.pow(final_metric, 1/3) * math.log(final_metric + math.e)

print(f"Result: {round(final_metric, 6)}")