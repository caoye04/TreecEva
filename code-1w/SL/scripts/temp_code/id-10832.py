from typing import Set

# Simulate coverage areas of three environmental sensors in a smart farm
sensor_coverage_1: Set[int] = {1, 2, 3, 4, 5, 6}
sensor_coverage_2: Set[int] = {4, 5, 6, 7, 8, 9}
sensor_coverage_3: Set[int] = {5, 6, 7, 8, 9, 10}

# Calculate stable monitoring zones detected by all sensors
temp_union = sensor_coverage_1 | sensor_coverage_2  # Irrelevant distractor operation
dropped_zones = {1, 10}  # Zones no longer active (not used in main computation)

final_overlap = sensor_coverage_1 & sensor_coverage_2 & sensor_coverage_3

# Output result as required
print(f"Target result: {final_overlap}")