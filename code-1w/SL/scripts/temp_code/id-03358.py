from collections import defaultdict

# Simulate environmental zone data with (zone_type, capacity)
zone_data = [
    ('residential', 320),
    ('industrial', 890),
    ('residential', 450),
    ('agricultural', 120),
    ('industrial', 760),
    ('agricultural', 95),
    ('residential', 380)
]

# Count occurrences of each zone type
zone_counter = defaultdict(int)
for zone_type, _ in zone_data:
    zone_counter[zone_type] += 1

# Filter zones with more than one occurrence and capacity above threshold
filtered_zones = []
for i, (zone_type, capacity) in enumerate(zone_data):
    if zone_counter[zone_type] > 1 and capacity > 300:
        # Apply scaling based on position in sequence
        scaled_capacity = capacity * (0.95 + 0.05 * (i % 3))
        filtered_zones.append((zone_type, int(scaled_capacity)))

# Key computation point
total_capacity = sum(capacity for _, capacity in filtered_zones)
print(f"Result: {total_capacity}")