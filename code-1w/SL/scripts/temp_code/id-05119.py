def calculate_sensor_redundancy():
    primary_zones = {1, 2, 3, 4, 5}
    secondary_zones = {4, 5, 6, 7}
    
    active_sensors = {2, 3, 4, 5, 8}
    backup_sensors = {1, 4, 5, 6}
    
    # Irrelevant calculation: total zone count (minor distraction)
    total_unique_zones = len(primary_zones.union(secondary_zones))
    
    coverage_overlap = active_sensors.intersection(backup_sensors)
    
    # Additional unrelated sensor stat
    redundant_count = len(backup_sensors.difference(active_sensors))
    
    return coverage_overlap

result = calculate_sensor_redundancy()
print(f'Result: {result}')