def analyze_sensor_data(raw_readings):
    threshold = 50
    adjusted_readings = [x - 10 for x in raw_readings if x > 30]
    
    # Irrelevant metadata (minimal distraction)
    device_info = {'model': 'SensX20', 'calibrated': True}
    normalized = [round(x * 0.98, 2) for x in adjusted_readings]
    
    # Key computation path
    outlier_set = {99, 100, 101}  # possible corrupted values
    filtered_data = [x for x in normalized if int(x) not in outlier_set]
    filtered_sum = sum(filtered_data)
    
    # Additional irrelevant variable
    report_timestamp = "2023-11-05"
    return filtered_sum

# Main execution
data_stream = [35, 45, 60, 99, 70, 25, 80]
result = analyze_sensor_data(data_stream)
filtered_sum = result
print(f"Target result: {filtered_sum}")