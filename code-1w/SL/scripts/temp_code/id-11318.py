primary_zones = {1, 2, 3, 4, 5}
backup_zones = {4, 5, 6, 7}
active_sensors = {1, 2, 3, 4}
secondary_sensors = {3, 4, 5, 6}

deployed = len(primary_zones.union(backup_zones))
coverage_overlap = active_sensors.intersection(secondary_sensors)
final_count = len(coverage_overlap) + (deployed % 4)

Result: final_count