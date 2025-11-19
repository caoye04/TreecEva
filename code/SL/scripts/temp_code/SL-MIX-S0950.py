import math
from functools import reduce

def process_sensor_data():
    sensor_readings = {
        'temp_a': [23.5, 24.1, 22.8, 25.0],
        'temp_b': [19.2, 20.0, 18.9, 21.5],
        'temp_c': [27.3, 26.7, 28.1, 27.0]
    }
    
    # Exponential smoothing factor
    alpha = 0.3
    
    # Apply exponential smoothing and then take log of smoothed values
    smoothed_logs = {
        sensor: [math.log10(alpha * x + (1 - alpha) * sum(vals)/len(vals)) for x in vals]
        for sensor, vals in sensor_readings.items()
    }
    
    # Compute average of log values per sensor
    avg_log_values = {
        sensor: sum(log_vals)/len(log_vals)
        for sensor, log_vals in smoothed_logs.items()
    }
    
    # Hash sensor names and combine with average log values
    sensor_hashes = {sensor: hash(sensor) % 1000 for sensor in sensor_readings}
    
    # Calculate weighted combination using ternary logic for thresholding
    weighted_combinations = {
        sensor: (avg_log_values[sensor] * 100) if avg_log_values[sensor] > 1 else (avg_log_values[sensor] * 50)
        for sensor in avg_log_values
    }
    
    # Final checksum calculation using reduction
    final_checksum = reduce(
        lambda acc, sensor: acc + int(weighted_combinations[sensor]) * sensor_hashes[sensor],
        weighted_combinations,
        0
    )
    
    return final_checksum

final_checksum = process_sensor_data()
print(f"Result: {final_checksum}")