def evaluate_system_redundancy():
    primary_sensors = {1, 2, 3, 4, 5, 6}
    backup_sensors = {5, 6, 7, 8, 9}
    
    # Calculate redundant sensor coverage
    active_zones = primary_sensors.union({10, 11})
    backup_zones = backup_sensors.difference({8})
    coverage_overlap = len(active_zones.intersection(backup_zones))
    
    # Auxiliary calculation (not affecting main result)
    total_active = len(active_zones)
    system_efficiency = total_active * 0.95
    
    return coverage_overlap

result = evaluate_system_redundancy()
print(f"Result: {result}")