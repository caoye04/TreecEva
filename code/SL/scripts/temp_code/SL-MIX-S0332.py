import math
from collections import defaultdict

def encode_point(x, y):
    return (x << 8) | y

def decode_point(encoded):
    x = encoded >> 8
    y = encoded & 0xFF
    return (x, y)

def calculate_centroid(vertices):
    cx = sum(v[0] for v in vertices) / len(vertices)
    cy = sum(v[1] for v in vertices) / len(vertices)
    return (cx, cy)

# Encoded vertex data for a triangle
encoded_vertices = [0x0A05, 0x1E0F, 0x1419]

# Decode vertices
vertices = [decode_point(e) for e in encoded_vertices]

# Calculate centroid
centroid = calculate_centroid(vertices)

# Spatial adjustment based on quadrant
if centroid[0] >= 0 and centroid[1] >= 0:
    adjusted_x = int(centroid[0]) + 10
    adjusted_y = int(centroid[1]) + 20
else:
    adjusted_x = int(centroid[0]) - 5
    adjusted_y = int(centroid[1]) - 5

# Encode the adjusted centroid
encoded_result = encode_point(adjusted_x, adjusted_y)

print(f"Result: {encoded_result}")