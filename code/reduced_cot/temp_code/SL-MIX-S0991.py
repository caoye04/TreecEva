import math

def calculate_angle_degrees(A, B, C):
    # Calculate angle at vertex B
    BA = (A[0] - B[0], A[1] - B[1])
    BC = (C[0] - B[0], C[1] - B[1])
    dot_product = BA[0] * BC[0] + BA[1] * BC[1]
    magnitude_BA = math.sqrt(BA[0]**2 + BA[1]**2)
    magnitude_BC = math.sqrt(BC[0]**2 + BC[1]**2)
    if magnitude_BA == 0 or magnitude_BC == 0:
        return 0
    cos_angle = dot_product / (magnitude_BA * magnitude_BC)
    # Clamp to avoid numerical errors
    cos_angle = max(-1, min(1, cos_angle))
    angle_rad = math.acos(cos_angle)
    return math.degrees(angle_rad)

# Triangle vertices: list of tuples (x, y)
triangles = [
    [(0, 0), (4, 0), (2, 3)],      # Triangle 1
    [(1, 1), (5, 1), (3, 4)],      # Triangle 2
    [(0, 0), (3, 0), (0, 3)],      # Triangle 3
    [(2, 2), (6, 2), (4, 5)],      # Triangle 4
    [(1, 0), (4, 0), (2.5, 0.5)]   # Triangle 5
]

smallest_angles = []
for tri in triangles:
    angles = []
    # Calculate all three angles of the triangle
    for i in range(3):
        A = tri[i]
        B = tri[(i + 1) % 3]
        C = tri[(i + 2) % 3]
        angle = calculate_angle_degrees(A, B, C)
        angles.append(angle)
    smallest_angle = min(angles)
    smallest_angles.append(smallest_angle)

# Calculate average of smallest angles
average_min_angle = sum(smallest_angles) / len(smallest_angles)

# Count triangles with smallest angle below average
below_average_flags = [angle < average_min_angle for angle in smallest_angles]
degenerate_count = sum(below_average_flags)

print(f"Result: {degenerate_count}")