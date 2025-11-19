import statistics

def calculate_quality_score(readings):
    if len(readings) < 3:
        return -1
    
    # Check for duplicates using set
    if len(set(readings)) != len(readings):
        return 0
    
    # Calculate variance and scale
    variance = statistics.variance(readings)
    return round(variance * 100)

# Sensor data from device
sensor_data = [12, 15, 14, 18, 16, 17, 19, 20]

# Process the data
quality_check_passed = len(sensor_data) >= 3 and len(set(sensor_data)) == len(sensor_data)
final_score = calculate_quality_score(sensor_data) if quality_check_passed else (-1 if len(sensor_data) < 3 else 0)

# Ternary operator for special case adjustment
final_score = final_score if final_score != 0 else (0 if len(set(sensor_data)) != len(sensor_data) else 1)

print(f"Result: {final_score}")