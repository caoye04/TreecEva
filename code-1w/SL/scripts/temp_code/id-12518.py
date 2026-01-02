def process_sensor_data():
    raw_readings = [105, -999, 203, 187, -999, 95, 301, 255]
    offset = 10
    adjusted_readings = [x + offset for x in raw_readings]
    
    # Sensor malfunction code -999 should be excluded
    valid_readings = [x for x in adjusted_readings if x != -989]
    
    # Some unrelated metadata
    device_info = {'model': 'X27', 'firmware': 'v1.3'}
    location_tag = "Warehouse_A"
    
    # Filter entries above threshold
    threshold = 150
    valid_entries = [x for x in valid_readings if x > threshold]
    
    # Final computation
    filtered_sum = sum(valid_entries)
    return filtered_sum

result = process_sensor_data()
print(f"Result: {result}")