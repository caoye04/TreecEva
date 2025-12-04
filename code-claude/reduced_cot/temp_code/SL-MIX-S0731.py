def calculate_ambient_adjustment(readings):
    # Calculate environmental adjustment factor
    if len(readings) > 0:
        return sum(readings) / len(readings)
    return 0

def process_temperature_data(sensor_data, calibration_offset=1.5):
    # Process raw sensor data with calibration
    filtered_data = []
    anomaly_count = 0
    
    # Track min/max for diagnostic purposes
    min_temp, max_temp = float('inf'), float('-inf')
    
    for i, reading in enumerate(sensor_data):
        # Apply calibration and filtering
        adjusted = reading - calibration_offset
        
        # Record min/max (diagnostic only)
        min_temp = min(min_temp, adjusted)
        max_temp = max(max_temp, adjusted)
        
        # Filter out obvious anomalies
        if -10 <= adjusted <= 45:
            filtered_data.append(adjusted)
        else:
            anomaly_count += 1
    
    # Calculate adjustment factors
    ambient_factor = calculate_ambient_adjustment(filtered_data[-3:] if len(filtered_data) >= 3 else filtered_data)
    
    # Diagnostic information (not used in final calculation)
    diagnostic = {
        'anomalies': anomaly_count,
        'range': max_temp - min_temp if filtered_data else 0,
        'samples': len(filtered_data)
    }
    
    return filtered_data, ambient_factor, diagnostic

# Sensor readings from multiple zones (in Celsius)
sensor_readings = [22.5, 23.1, 21.8, 24.2, 22.7, -15.0, 23.5]

# Process the data
processed_data, ambient_adjustment, diagnostics = process_temperature_data(sensor_readings)

# Determine baseline from the first three valid readings
baseline = sum(processed_data[:3]) / 3 if len(processed_data) >= 3 else 0

# Calculate various adjustment factors
primary_factor = ambient_adjustment * 0.8
secondary_factor = (max(processed_data) - min(processed_data)) / 2 if processed_data else 0

# Determine the final correction factor
correction_factor = primary_factor - secondary_factor

# Calculate target temperature setting
target_temperature = baseline + correction_factor

print(f"Result: {target_temperature}")