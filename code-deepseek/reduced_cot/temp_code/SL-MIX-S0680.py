from collections import Counter

def validate_sensor_data(readings, calibration):
    # Distractor: unused lambda for temperature conversion
    temp_convert = lambda x: (x * 9/5) + 32
    
    # Main logic: process sensor readings with calibration
    adjusted_readings = []
    for i, reading in enumerate(readings):
        # Distractor: misleading intermediate calculation
        noise_factor = (i * 3) % 7
        temp_noise = reading + noise_factor - 2
        
        # Actual calibration adjustment
        calib_index = i % len(calibration)
        adjusted = reading * calibration[calib_index]
        adjusted_readings.append(adjusted)
        
        # Dead code path: unused validation check
        if adjusted > 1000:
            overflow_flag = True
    
    # Distractor: irrelevant statistical analysis
    reading_stats = Counter(adjusted_readings)
    most_common_val = reading_stats.most_common(1)[0][0]
    
    # Main checksum calculation
    checksum = 0
    for val in adjusted_readings:
        checksum = (checksum + int(val)) % 256
    
    # Distractor: unused bit manipulation
    bit_shifted = checksum << 2
    masked_value = bit_shifted & 0xFF
    
    # Final validation step with modular arithmetic
    validation_key = (checksum * 13) % 97
    
    return validation_key

# Sensor data simulation
sensor_readings = [45.2, 67.8, 23.1, 89.5, 12.3, 78.9, 34.6]
calibration_factors = [1.05, 0.98, 1.12, 0.95]

# Distractor: unused sensor validation
sensor_threshold = max(sensor_readings) - min(sensor_readings)

# Critical execution point
final_checksum = validate_sensor_data(sensor_readings, calibration_factors)

print(f"Result: {final_checksum}")