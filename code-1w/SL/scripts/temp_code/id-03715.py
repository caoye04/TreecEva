import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.9, 20.2]
humidity_readings = [45, 52, 60, 48, 55, 62, 58, 50]
pressure_readings = [1013, 1015, 1010, 1008, 1017, 1020, 1014, 1012]

# Irrelevant backup data (distractor)
backup_temperatures = [21.0, 22.5, 20.1, 23.7] * 5

# Mapping station IDs to locations (dictionary operation)
station_map = {f'ST{i+1}': loc for i, loc in enumerate(['North', 'South', 'East', 'West', 'Central', 'Northeast', 'Southeast', 'Northwest'])}

# Filter valid stations (only those with 'N' direction)
valid_stations = {k: v for k, v in station_map.items() if 'N' in v}

# Process logs: normalize and flag anomalies (relevant function)
def process_sensor_logs(temp, hum, pres):
    normalized = []
    alerts = []
    for i in range(len(temp)):
        norm_temp = (temp[i] - 20) / 5
        norm_hum = (hum[i] - 50) / 10
        composite = math.sqrt(norm_temp**2 + norm_hum**2)
        if composite > 1.0:
            alerts.append(i)
        normalized.append(composite)
    
    # Dead code path - never used (distractor)
    def deprecated_normalization(x):
        return [val / max(x) for val in x]
    
    # Unused transformation (red herring)
    pressure_ratios = [pres[i] / pres[i-1] for i in range(1, len(pres))]
    trend = sum([1 for r in pressure_ratios if r > 1.0])

    return normalized, alerts

# Apply processing
processed_logs = process_sensor_logs(temperature_readings, humidity_readings, pressure_readings)[0]

# Auxiliary diagnostic function with bit manipulation red herring
def quick_diagnostic(data):
    hash_val = 0
    for d in data:
        shifted = int(d * 100)
        hash_val ^= shifted << 2
        hash_val &= 0xFFFF  # Keep within 16 bits
    return hash_val

# Useless set operations (distractor)
potential_alert_levels = set(range(1, 10))
critical_values = {3, 5, 7, 9}
overlap_check = potential_alert_levels & critical_values
excluded = potential_alert_levels - critical_values

# Real analysis function (key logic)
def analyze_readings(readings):
    # Statistical summary
    mean_val = sum(readings) / len(readings)
    squared_deviations = [(x - mean_val)**2 for x in readings]
    variance = sum(squared_deviations) / len(squared_deviations)
    std_dev = math.sqrt(variance)
    
    # Determine stability index
    stability_score = 0
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) > std_dev:
            stability_score += 1
    
    # Transform into diagnostic metric
    diagnostic_base = int(mean_val * 1000)
    adjustment = int(std_dev * 100)
    
    # Complex but irrelevant bit twiddling (misleading intermediate)
    temp_result = diagnostic_base ^ adjustment
    temp_result = (temp_result << 3) | (temp_result >> 5)
    temp_result &= 0xFF_FF
    
    # Final computation (answer derivation)
    final_diagnostic = diagnostic_base - adjustment  # This is the real result
    
    # Decoy return path (never reached)
    if False:
        return quick_diagnostic(readings)
    
    return final_diagnostic

# Execute key statement
temp_placeholder = quick_diagnostic(processed_logs)  # Distractor call
final_diagnostic = analyze_readings(processed_logs)

# Print result as required
print(f"Result: {final_diagnostic}")