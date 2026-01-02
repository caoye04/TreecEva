def optimize_allocation(resources, limit):
    temp_snapshot = resources[:]
    adjusted = [r * 1.5 for r in resources if r < limit]
    surplus = sum([r for r in resources if r > 2 * limit])
    deficit = sum([limit - r for r in resources if r < limit])
    scaling_factor = 0.9 if surplus > deficit else 1.1

    # Misleading transformation on copy
    dummy_normalized = [(r - min(temp_snapshot)) / (max(temp_snapshot) - min(temp_snapshot) + 1) for r in temp_snapshot]
    bucketed = [int(n * 10) for n in dummy_normalized]

    # Core logic hidden among distractions
    valid_indices = [i for i, r in enumerate(resources) if r >= limit]
    maintained = [resources[i] for i in valid_indices]
    enhanced = [val * scaling_factor for val in adjusted]

    aggregated = maintained + enhanced
    if len(aggregated) == 0:
        return 0
    
    final_bandwidth = sum(aggregated) / len(aggregated)
    return final_bandwidth

# Simulate system resource units across nodes
resource_pool = [12, 7, 3, 25, 8, 1, 18, 5]
threshold = 6
monitoring_log = set()
for val in resource_pool:
    if val < threshold:
        monitoring_log.add(f"low_resource_{val}")

baseline_avg = sum(resource_pool) / len(resource_pool)
dummy_slices = resource_pool[2:6:2]

# Key execution point
final_bandwidth = optimize_allocation(resource_pool, threshold)
print(f"Target result: {final_bandwidth}")