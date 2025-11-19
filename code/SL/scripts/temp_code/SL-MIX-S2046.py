import math

def process_sensor_data():
    raw_readings = {
        'sensor_alpha': [25.3, 26.1, 24.8, 27.2],
        'sensor_beta': [23.9, 24.5, 25.0, 24.1],
    }
    
    # Simulate additional readings
    for i in range(3):
        raw_readings[f'sensor_gamma_{i}'] = [20 + i * 1.5 + j * 0.2 for j in range(4)]
    
    reliability_flags = {
        'sensor_alpha': True,
        'sensor_beta': False, # Unreliable
    }
    
    # Default all gamma sensors as reliable
    for k in raw_readings:
        if k not in reliability_flags:
            reliability_flags[k] = True
    
    weights = {name: 1.0 for name in raw_readings}
    weights['sensor_alpha'] = 1.5
    
    normalized_data = {}
    for sensor, values in raw_readings.items():
        if reliability_flags[sensor]:
            # Normalize using log scaling
            norm_vals = [math.log(v + 1) for v in values]
            normalized_data[sensor] = norm_vals
    
    # Weighted aggregation
    aggregate_per_sensor = {
        sensor: sum(vals) * weights[sensor]
        for sensor, vals in normalized_data.items()
    }
    
    # Apply exponential smoothing factor
    smoothing_factors = {s: math.exp(-0.1 * i) for i, s in enumerate(aggregate_per_sensor)}
    
    final_components = {
        s: aggregate_per_sensor[s] * smoothing_factors[s]
        for s in aggregate_per_sensor
    }
    
    final_aggregate = sum(final_components.values())
    return final_aggregate

final_aggregate = process_sensor_data()
print(f"Result: {final_aggregate}")