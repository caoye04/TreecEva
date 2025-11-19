import math

def process_sensor_data(raw_readings):
    # Apply exponential weighting to emphasize strong signals
    weighted_signals = {sensor: math.exp(value/10) for sensor, value in raw_readings.items()}
    
    # Normalize using logarithmic scaling
    normalized_signals = {sensor: math.log(weight + 1) for sensor, weight in weighted_signals.items()}
    
    return normalized_signals

def calculate_aggregate_metric(processed_data, calibration_factors):
    # Combine processed data with calibration using dictionary merging
    combined_data = processed_data | calibration_factors
    
    # Apply lambda transformation for final metric calculation
    metric_transform = lambda x: round(x ** 1.5, 2)
    
    # Calculate aggregate score using set operations on sensor identifiers
    primary_sensors = frozenset(['S1', 'S2', 'S3'])
    auxiliary_sensors = frozenset(['S4', 'S5'])
    valid_sensors = primary_sensors.union(auxiliary_sensors)
    
    # Compute final metric only for valid sensors
    aggregate_components = [metric_transform(combined_data[sensor]) 
                           for sensor in valid_sensors if sensor in combined_data]
    
    # Return sum of all components as the final score
    return sum(aggregate_components)

# Initial sensor readings
sensor_readings = {'S1': 23.5, 'S2': 18.2, 'S3': 31.0, 'S4': 15.7, 'S5': 27.3}

# Calibration adjustments
calibration_data = {'S1': 1.2, 'S2': 0.8, 'S3': 1.5, 'S6': 2.0}  # Note: S6 is not used

# Process the data through the pipeline
processed_signals = process_sensor_data(sensor_readings)

# Calculate final aggregate metric
aggregate_signal_score = calculate_aggregate_metric(processed_signals, calibration_data)

print(f"Result: {aggregate_signal_score}")