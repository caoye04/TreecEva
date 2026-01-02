def analyze_sensor_coverage():
    primary_zones = {1, 2, 3, 4, 5, 6}
    backup_zones = {4, 5, 6, 7, 8, 9}
    active_filters = {2, 4, 6, 8}
    
    # Find areas covered by both primary and backup systems
    common_elements = primary_zones.intersection(backup_zones)
    
    # Simulate temporary system mode with reduced coverage
    secondary_set = {4, 5, 9, 10}
    
    # Final overlap considers both redundancy and active filters
    final_overlap = common_elements.intersection(secondary_set)
    
    # Irrelevant metric (distractor)
    system_efficiency = len(primary_zones) / 10.0
    
    return final_overlap

result_set = analyze_sensor_coverage()
final_overlap = len(result_set)
print(f"Result: {final_overlap}")