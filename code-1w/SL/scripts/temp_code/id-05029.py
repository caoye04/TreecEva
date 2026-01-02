def calculate_sensor_network_capacity():
    locations = ['North', 'South', 'East', 'West', 'Central']
    sensor_specs = [(12, 8), (15, 6), (10, 9), (18, 5), (20, 7)]  # (range_km, capacity_units)
    operational_status = [True, False, True, True, False]
    
    total_capacity = 0
    base_threshold = 10
    
    for i, (loc, spec) in enumerate(zip(locations, sensor_specs)):
        range_km, capacity_units = spec
        coverage_multiplier = 1
        
        if range_km > base_threshold:
            coverage_multiplier = 2
        
        if operational_status[i]:
            total_capacity += sensors[i][1] * coverage_multiplier
        
    Result: {total_capacity}