def process_temperature(temp_data):
    threshold_check = lambda x: x > 25
    filtered_data = [temp for temp in temp_data if threshold_check(temp)]
    
    if len(filtered_data) > 0:
        average_temp = sum(filtered_data) / len(filtered_data)
    else:
        average_temp = 0
    
    calibration_factor = 1.05
    final_output = round(average_temp * calibration_factor, 2)
    return final_output

readings = [22.5, 26.8, 24.3, 27.9, 23.1, 28.4]
final_output = process_temperature(readings)
print(f"Result: {final_output}")