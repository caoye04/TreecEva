sensor_readings = [3, 8, 2, 7, 4, 9]
calibration_factor = 1.5
processed_data = [x * 2 if x > 5 else x + 1 for x in sensor_readings]
temp_storage = [item for item in processed_data if item > 10]
final_count = len(temp_storage)
print(f"Result: {final_count}")