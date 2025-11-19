import math
from itertools import combinations

class ConstellationNode:
    def __init__(self, name, sightings, next_node=None):
        self.name = name
        self.sightings = sightings
        self.next = next_node

def calculate_sector_angle(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    angle = math.degrees(math.atan2(dy, dx))
    return angle % 360

def get_optimal_sectors(sector_angles, threshold=60):
    valid_sectors = set()
    for angles in combinations(sector_angles, 2):
        diff = abs(angles[0] - angles[1])
        if diff <= threshold or (360 - diff) <= threshold:
            valid_sectors.add(frozenset(angles))
    return len(valid_sectors)

# Initialize observation data
orion_node = ConstellationNode("Orion", 42)
cassiopeia_node = ConstellationNode("Cassiopeia", 38, orion_node)
ursa_major_node = ConstellationNode("Ursa Major", 55, cassiopeia_node)
centaurus_node = ConstellationNode("Centaurus", 31, ursa_major_node)

# Process observations with hash map
constellation_sightings = {}
current = centaurus_node
while current:
    constellation_sightings[current.name] = current.sightings
    current = current.next

# Geometric analysis points
observation_points = [(0, 0), (3, 4), (5, 0), (0, 5), (4, 3)]
sector_angles = []
for i in range(len(observation_points)):
    for j in range(i+1, len(observation_points)):
        angle = calculate_sector_angle(observation_points[i], observation_points[j])
        sector_angles.append(angle)

# Apply combinatorial filtering
high_activity_constellations = {k: v for k, v in constellation_sightings.items() if v > 40}
filtered_angles = list(filter(lambda x: x <= 180, sector_angles))

# Calculate optimal sectors
optimal_sector_count = get_optimal_sectors(filtered_angles)

# Adjust based on high activity constellations
if len(high_activity_constellations) >= 2:
    optimal_sector_count *= len(high_activity_constellations)

print(f"Result: {optimal_sector_count}")