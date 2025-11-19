import statistics

temperature_readings = [22.5, 24.0, 26.8, 23.1, 27.2, 25.9, 24.7]
quality_check_passed = False
stability_index = -1

with open('temp_log.txt', 'w') as f:
    f.write(str(temperature_readings))
    
    mean_temp = statistics.mean(temperature_readings)
    deviations = [abs(temp - mean_temp) for temp in temperature_readings]
    mean_deviation = statistics.mean(deviations)
    max_temp = max(temperature_readings)
    
    # Quality control check with short-circuit evaluation
    if (len(temperature_readings) > 0 and 
        mean_deviation < 10 and 
        max_temp > 25):
        quality_check_passed = True
    
    if quality_check_passed:
        variance = statistics.variance(temperature_readings)
        stability_index = round((1 / (1 + variance)) * 100, 2)
    else:
        stability_index = 0

print(f"Result: {stability_index}")