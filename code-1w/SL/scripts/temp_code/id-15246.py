def analyze_sensor_overlap(active_zones, maintenance_zones, threshold_mask):
    # Simulate sensor fusion logic using set operations and bitwise analysis
    active_set = set(active_zones)
    maintenance_set = set(maintenance_zones)
    
    # Identify zones that are active but under maintenance (potential fault)
    conflict_zones = active_set & maintenance_set
    
    # Mask out zones below threshold using bitwise filtering
    filtered_conflicts = {zone for zone in conflict_zones if (zone & threshold_mask) != 0}
    
    # Track isolated zones (not adjacent to any other active zone)
    isolated_zones = {zone for zone in active_set if (zone ^ 1) not in active_set}
    
    # Combine filtered conflicts and isolated zones for final diagnosis
    final_set = filtered_conflicts | isolated_zones
    
    # Introduce a distractor variable (minimal interference)
    temp_debug_log = len(active_set) + len(maintenance_set)
    
    # Key result: extract one diagnostic code from final anomalies
    result = final_set.pop() if final_set else -1
    print(f"Result: {result}")
    return result

# Inputs based on system state
active_sensors = [5, 6, 7, 9]
maintenance_sensors = [6, 9, 10]
mask = 0b1101  # Threshold mask for valid fault reporting

result = analyze_sensor_overlap(active_sensors, maintenance_sensors, mask)