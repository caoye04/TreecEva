def analyze_set_relationships():
    # Initial data from two sensors
    sensor_a_readings = {12, 34, 56, 78, 91, 102, 113}
    sensor_b_readings = {34, 56, 78, 131, 142, 113}

    # Filter valid readings (even numbers only)
    valid_sensor_a = {x for x in sensor_a_readings if x % 2 == 0}
    valid_sensor_b = {x for x in sensor_b_readings if x % 2 == 0}

    # Compute unique elements present in both sets
    unique_elements_in_both = valid_sensor_a & valid_sensor_b

    # Final count of overlapping valid readings
    final_overlap_count = len(unique_elements_in_both)
    
    # Irrelevant distraction: unused variable (minimal interference)
    total_unique_readings = len(sensor_a_readings | sensor_b_readings)
    
    print(f"Result: {final_overlap_count}")

analyze_set_relationships()