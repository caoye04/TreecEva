from collections import defaultdict
from itertools import combinations

# Package data: zone_id -> list of weights
shipment_manifest = {
    'Z1': [2.5, 4.0, 1.2],
    'Z2': [3.8, 2.1],
    'Z3': [5.5, 1.0, 3.3, 2.7]
}

# Zone priority mapping
zone_priority_map = {'Z1': 3, 'Z2': 2, 'Z3': 1}

# Calculate package scores
package_scores = []
for zone_id, weights in shipment_manifest.items():
    zone_priority = zone_priority_map[zone_id]
    for weight in weights:
        # String transformation to create package ID
        package_id = f"{zone_id}_{str(weight).replace('.', '_')}kg"
        # Priority score calculation
        weight_category = 'heavy' if weight > 3.0 else 'light'
        priority_score = zone_priority * (2 if weight_category == 'heavy' else 1)
        package_scores.append((package_id, priority_score))

# Group scores by priority level
priority_groups = defaultdict(list)
for pkg_id, score in package_scores:
    priority_groups[score].append(pkg_id)

# Compute routing efficiency using combinations
routing_efficiency = 0
for priority_level, packages in sorted(priority_groups.items(), reverse=True):
    # Ternary operator to determine combination size
    combo_size = 2 if len(packages) >= 2 else 1
    combo_count = len(list(combinations(packages, combo_size)))
    # Efficiency contribution: priority squared times combinations
    routing_efficiency += (priority_level ** 2) * combo_count

print(f"Result: {routing_efficiency}")