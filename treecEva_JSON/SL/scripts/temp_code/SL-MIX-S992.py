import itertools

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def boundary_points(p1, p2):
    return gcd(abs(p1[0] - p2[0]), abs(p1[1] - p2[1])) + 1

vertices = [(0, 0), (4, 0), (0, 3)]

# Calculate bounding box
min_x = min(v[0] for v in vertices)
max_x = max(v[0] for v in vertices)
min_y = min(v[1] for v in vertices)
max_y = max(v[1] for v in vertices)

# Count boundary points
b = sum(boundary_points(vertices[i], vertices[(i + 1) % 3]) for i in range(3)) - 3

# Pick's theorem to find interior points
area = abs((vertices[0][0] * (vertices[1][1] - vertices[2][1]) +
            vertices[1][0] * (vertices[2][1] - vertices[0][1]) +
            vertices[2][0] * (vertices[0][1] - vertices[1][1])) / 2.0)
i = int(area - b / 2.0 + 1)
lattice_points = i + b

# Security score transformation
transform = lambda x: (x << 2) ^ (x >> 1) if x > 10 else (x & 0xF) | (x * 2)
final_security_score = transform(lattice_points)

print(f"Result: {final_security_score}")