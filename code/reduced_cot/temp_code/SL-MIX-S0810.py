import math
from collections import namedtuple

# Define a point in 2D space
Point = namedtuple('Point', ['x', 'y'])

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Drone positions and surveillance radii
DroneSpec = namedtuple('DroneSpec', ['position', 'radius'])
drones = [
    DroneSpec(Point(2, 3), 5),
    DroneSpec(Point(-1, 4), 3),
    DroneSpec(Point(6, 0), 4)
]

# Package drop-off locations
package_locations = [Point(x, y) for x in range(-5, 10) for y in range(-5, 10) 
                   if (x + y) % 3 == 0 and not (x == 0 and y == 0)]

# Calculate coverage using set comprehension and short-circuit evaluation
covered_points = {
    pkg for pkg in package_locations
    if any(distance(pkg, drone.position) <= drone.radius 
           and (pkg.x > 0 or pkg.y > 0)  # Only consider points in positive quadrants
           for drone in drones)
}

# Apply combinatorial filter: remove points that form equilateral triangles with any two drones
filtered_coverage = {
    point for point in covered_points
    if not any(
        abs(distance(point, d1.position) - distance(point, d2.position)) < 1e-9 and
        abs(distance(d1.position, d2.position) - distance(point, d1.position)) < 1e-9
        for i, d1 in enumerate(drones) for d2 in drones[i+1:]
    )
}

surveillance_coverage = len(filtered_coverage) + sum(1 for d in drones if d.position.x >= 0)
print(f"Result: {surveillance_coverage}")