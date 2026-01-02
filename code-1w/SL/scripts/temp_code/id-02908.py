from typing import Set

# Define sensor detection zones for two overlapping environmental sensors
temperature_zones: Set[int] = {1, 2, 3, 4, 5, 6}
humidity_zones: Set[int] = {4, 5, 6, 7, 8, 9}

deployed_nodes = [True, True, False]  # Irrelevant status tracking (minimal interference)
activation_cycle = 3  # Dummy parameter for system cycle (slight distraction)

sensor_area_a: Set[int] = temperature_zones.union({10, 11})
sensor_area_b: Set[int] = humidity_zones.difference({9})

coverage_overlap = sensor_area_a.intersection(sensor_area_b)

# Print final result as required
print(f"Result: {coverage_overlap}")

# Convert to sorted list just before print to ensure deterministic display
sorted_coverage = sorted(list(coverage_overlap))