from collections import defaultdict
import math

def process_sensor_data():
    # Sensor data: (type, raw_temp, reliability_score)
    sensors = [
        ('A', 23.5, 0.9),
        ('B', 25.1, 0.85),
        ('A', 22.8, 0.92),
        ('C', 24.3, 0.78),
        ('B', 26.2, 0.88)
    ]
    
    # State machine for correction factors
    def get_correction_factor(sensor_type, temp):
        if sensor_type == 'A':
            if temp < 23.0:
                return 1.02
            elif temp > 25.0:
                return 0.98
            else:
                return 1.0
        elif sensor_type == 'B':
            if temp < 24.0:
                return 1.03
            elif temp > 26.0:
                return 0.97
            else:
                return 1.0
        else:  # type C
            return 1.01 if temp < 25.0 else 0.99
    
    # Process each sensor reading
    corrected_temps = []
    total_weight = 0
    weighted_sum = 0.0
    
    for sensor_type, raw_temp, reliability in sensors:
        correction = get_correction_factor(sensor_type, raw_temp)
        corrected_temp = raw_temp * correction
        corrected_temps.append(corrected_temp)
        
        weight = reliability ** 2  # Weight is squared reliability
        weighted_sum += corrected_temp * weight
        total_weight += weight
    
    # Calculate weighted average
    weighted_avg = weighted_sum / total_weight
    
    # Normalize against historical baseline using sigmoid function
    baseline_temp = 24.0
    deviation = weighted_avg - baseline_temp
    normalization_factor = 1 / (1 + math.exp(-deviation))
    
    # Final normalized temperature
    final_normalized_temp = baseline_temp + (deviation * normalization_factor)
    
    return final_normalized_temp

# Execute the processing pipeline
final_normalized_temp = process_sensor_data()
print(f"Result: {final_normalized_temp:.6f}")