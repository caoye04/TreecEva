def preprocess_data(values, threshold=500):
    # Preprocess data to remove outliers
    processed = [v for v in values if v < threshold]
    return processed if processed else [0]

def apply_atmospheric_correction(value, correction_factors):
    # Apply various atmospheric corrections to sensor readings
    base = value
    for factor in correction_factors:
        if factor > 0:
            base = base * (1 + factor/100)
        else:
            # Negative factors are subtracted differently
            base = base * (1 - abs(factor)/50)
    return base

def calculate_drift_compensation(sensor_health):
    # Calculate sensor drift compensation based on health indicators
    drift = 0
    if sensor_health['calibration_age'] > 30:
        drift -= sensor_health['calibration_age'] // 10
    
    if sensor_health['error_count'] > 0:
        drift -= sensor_health['error_count'] * 2
        
    if sensor_health['temperature'] > 85:
        drift -= (sensor_health['temperature'] - 85) * 1.5
    elif sensor_health['temperature'] < 10:
        drift -= (10 - sensor_health['temperature']) * 0.8
        
    return max(-25, drift)  # Cap at -25% drift

def calculate_effective_altitude(readings, sensor_status):
    # Main function to calculate effective altitude from sensor readings
    
    # Sensor configuration and environmental factors
    air_density = 1.225  # kg/m³ at sea level
    temperature_readings = [22, 21, 20, 19, 18]  # Celsius
    pressure_variance = 0.05  # 5% variance in pressure readings
    magnetic_interference = sensor_status['magnetic_interference']
    
    # Filtering extreme values
    filtered_readings = preprocess_data(readings, 9500)
    
    # Calculate average reading
    avg_reading = sum(filtered_readings) / len(filtered_readings)
    
    # Calculate barometric altitude adjustment
    barometric_factor = 0
    if sensor_status['barometer_active']:
        # Simulate barometer calculation with pressure variance
        pressure_ratio = (1 - pressure_variance) if avg_reading > 5000 else (1 + pressure_variance)
        barometric_factor = avg_reading * 0.12 * pressure_ratio
    
    # Temperature compensation is calculated but not used in final calculation (distractor)
    temp_compensation = sum(temperature_readings) / len(temperature_readings) - 20
    temp_factor = 1 + (temp_compensation / 100)
    
    # Magnetic interference adjustment
    mag_adjustment = 0
    if magnetic_interference > 0:
        mag_adjustment = -15 if magnetic_interference > 2 else -7
    
    # Calculate sensor drift based on health
    drift_percent = calculate_drift_compensation(sensor_status['health'])
    
    # Apply corrections
    correction_factors = [drift_percent, mag_adjustment / 100]
    
    # These atmospheric density calculations are distractors
    density_altitude = avg_reading * (288.15 / (273.15 + sum(temperature_readings) / len(temperature_readings)))
    density_correction = (1.225 / air_density) - 1
    
    # Calculate adjusted reading
    if sensor_status['use_legacy_algorithm']:
        # Legacy algorithm path (distractor)
        intermediate = avg_reading * (1 + (drift_percent / 100))
        adjusted_reading = intermediate + mag_adjustment
    else:
        # Current algorithm path (actual calculation path)
        adjusted_reading = apply_atmospheric_correction(avg_reading, correction_factors)
    
    # Final calculation with barometric adjustment
    if sensor_status['barometer_active'] and barometric_factor > 0:
        return int(adjusted_reading + barometric_factor)
    else:
        return int(adjusted_reading)

# Sensor readings and status
altitude_readings = [4267, 4256, 4289, 4302, 9876, 4275]
sensor_status = {
    'barometer_active': False,
    'magnetic_interference': 3,
    'use_legacy_algorithm': False,
    'health': {
        'calibration_age': 45,
        'error_count': 2,
        'temperature': 90
    }
}

# Calculate the final altitude
final_altitude = calculate_effective_altitude(altitude_readings, sensor_status)
print(f"Target result: {final_altitude}")