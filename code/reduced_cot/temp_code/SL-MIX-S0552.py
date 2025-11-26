def analyze_sensor_readings():
    # Initial sensor data from multiple devices
    device_a = {45, 32, 78, 12, 67}
    device_b = {32, 89, 12, 54, 91}
    device_c = {78, 91, 23, 45, 67}
    
    # Find readings common to at least two devices
    ab_common = device_a & device_b
    bc_common = device_b & device_c
    ac_common = device_a & device_c
    
    # Combine all shared readings
    shared_readings = ab_common | bc_common | ac_common
    
    # Create merged list and sort
    merged_unique = sorted(list(shared_readings))
    
    # Get the second largest value from merged unique readings
    final_result = merged_unique[-2]
    
    print(f"Target result: {final_result}")

analyze_sensor_readings()