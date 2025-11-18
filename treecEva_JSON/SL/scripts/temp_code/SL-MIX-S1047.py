import itertools
from collections import defaultdict

def encode_waypoint(location_id, time_slot):
    return (location_id * 17 + time_slot * 23) % 100

def calculate_checksum(route):
    checksum = 0
    for i, waypoint in enumerate(route):
        checksum = (checksum + waypoint * (i + 1)) % 97
    return checksum

# Encoded delivery locations
locations = [12, 28, 35, 44]
time_slots = [5, 13, 22]

# Generate all possible route combinations using cartesian product
encoded_routes = [
    tuple(encode_waypoint(loc, ts) for loc, ts in zip(route, time_slots))
    for route in itertools.product(locations, repeat=len(time_slots))
]

# Dictionary to store frequency of checksums
checksum_frequency = defaultdict(int)

# Calculate checksum for each route and track frequencies
for route in encoded_routes:
    checksum = calculate_checksum(route)
    checksum_frequency[checksum] += 1

# Find the most frequent checksum
most_frequent_checksum = max(checksum_frequency.items(), key=lambda x: x[1])[0]

# Apply modular exponentiation as final verification step
final_route_checksum = pow(most_frequent_checksum, 3, 101)

print(f"Result: {final_route_checksum}")