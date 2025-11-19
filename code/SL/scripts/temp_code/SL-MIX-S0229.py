import re

# Package data: (package_id, weight, priority, destination_zone)
packages = [
    ('PKG001', 15, 40, 'ZONE_A'),
    ('PKG002', 10, 25, 'ZONE_B'),
    ('PKG003', 20, 45, 'ZONE_A'),
    ('PKG004', 8, 20, 'ZONE_C'),
    ('PKG005', 12, 30, 'ZONE_A'),
    ('PKG006', 25, 50, 'ZONE_B'),
    ('PKG007', 5, 15, 'ZONE_C'),
    ('PKG008', 18, 35, 'ZONE_A')
]

truck_capacity = 50
zone_filter_pattern = r'ZONE_[AB]'

# Step 1: Filter packages matching zone pattern
filtered_packages = [pkg for pkg in packages if re.match(zone_filter_pattern, pkg[3])]

# Step 2: Calculate priority-to-weight ratio and sort descending (greedy approach)
ranked_packages = sorted(filtered_packages, key=lambda p: p[2]/p[1], reverse=True)

# Step 3: Greedily select packages within capacity
loaded_packages = []
current_weight = 0
for pkg in ranked_packages:
    if current_weight + pkg[1] <= truck_capacity:
        loaded_packages.append(pkg)
        current_weight += pkg[1]

# Step 4: Create loading sequence mapping using dictionary comprehension
loading_sequence = {pkg[0]: idx+1 for idx, pkg in enumerate(loaded_packages)}

# Step 5: Compute total priority score of loaded packages
total_priority_score = sum(pkg[2] for pkg in loaded_packages)

print(f"Result: {total_priority_score}")