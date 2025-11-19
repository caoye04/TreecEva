from collections import defaultdict
import math

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return abs(a * b) // calculate_gcd(a, b)

class ZoneProcessor:
    def __init__(self):
        self.zones = defaultdict(int)
    
    def add_coordinate(self, x, y):
        # Encode coordinate into zone using geometric hashing
        zone_id = (x * 31 + y * 17) % 256
        self.zones[zone_id] += 1
        return zone_id

# Initialize processor
processor = ZoneProcessor()

# Delivery coordinates
coordinates = [(12, 5), (28, 15), (44, 25), (60, 35)]

# Process coordinates and collect zone IDs
zone_ids = []
for x, y in coordinates:
    zone_id = processor.add_coordinate(x, y)
    zone_ids.append(zone_id)

# Calculate spatial relationships using number theory
base_spacing = calculate_gcd(zone_ids[0], zone_ids[1])
step_size = calculate_lcm(zone_ids[2] & 0xF0, zone_ids[3] | 0x0F)

# Apply modular arithmetic to determine primary zone
primary_zone = (zone_ids[0] ^ zone_ids[2]) % 64

# Bitwise encoding for delivery permissions
permission_mask = 0b10101010
encoded_zones = (primary_zone << 2) | (base_spacing & permission_mask)

# Final delivery zone calculation
if encoded_zones > 200:
    delivery_zone_code = (encoded_zones >> 1) ^ step_size
else:
    delivery_zone_code = (encoded_zones << 1) & step_size

print(f"Result: {delivery_zone_code}")