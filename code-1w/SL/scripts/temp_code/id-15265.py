import math

# Simulated dataset for environmental impact analysis
temperature_readings = [23.4, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [55, 60, 58, 62, 59, 64, 57]
co2_levels = [410, 415, 408, 420, 425, 418, 412]
wind_speeds = [12, 14, 10, 15, 13, 11, 16]  # km/h, irrelevant for score

# Irrelevant transformation (distractor)
transformed_winds = [w ** 0.5 for w in wind_speeds if w > 10]

# Weight configuration for scoring model (only some are used)
weights = {
    'temp': 0.3,
    'humidity': 0.2,
    'co2': 0.5,
    'noise': 0.1,  # unused weight (red herring)
    'vibration': 0.05  # unused weight (red herring)
}

# Historical baselines (some are decoys)
baselines = {
    'temp_norm': 22.0,
    'humidity_norm': 50,
    'co2_norm': 400,
    'pressure_norm': 1013  # completely irrelevant
}

# Misleading intermediate calculations (dead paths)
baseline_deviation_sum = 0.0
for i in range(len(temperature_readings)):
    baseline_deviation_sum += abs(temperature_readings[i] - baselines['temp_norm'])

# Unused recursive function (decoy)
def compute_noise_impact(level, depth=0):
    if depth > 3:
        return level / (depth + 1)
    return compute_noise_impact((level * 0.9) + 1, depth + 1)

# Bitwise manipulation on unrelated metric (distraction)
encoded_data = 0
for val in co2_levels:
    encoded_data ^= int(val)
    encoded_data = (encoded_data << 1) & 0xFF  # cap to 8 bits

# Real processing begins: normalize and compute weighted anomalies
def calculate_anomaly_score(readings, baseline, weight):
    deviations = [(r - baseline) for r in readings]
    squared_deviations = [d ** 2 for d in deviations]
    mean_squared = sum(squared_deviations) / len(squared_deviations)
    return math.sqrt(mean_squared) * weight

def calculate_final_score(data, w):
    # Extract relevant data
    temps, humids, co2s = data
    
    # Compute individual anomaly contributions
    temp_anomaly = calculate_anomaly_score(temps, baselines['temp_norm'], w['temp'])
    humidity_anomaly = calculate_anomaly_score(humids, baselines['humidity_norm'], w['humidity'])
    co2_anomaly = calculate_anomaly_score(co2s, baselines['co2_norm'], w['co2'])
    
    # Aggregate score
    total_anomaly = temp_anomaly + humidity_anomaly + co2_anomaly
    
    # Apply non-linear compression
    normalized_score = 100 * (1 - math.exp(-0.1 * total_anomaly))
    
    # Final adjustment based on data completeness
    completeness_factor = len(temps) / 7.0  # assume 7-day window
    adjusted_score = normalized_score * completeness_factor
    
    # Secondary adjustment: penalty for high CO2 variance
    co2_variance = sum((x - sum(co2s)/len(co2s))**2 for x in co2s) / len(co2s)
    if co2_variance > 20:
        adjusted_score -= 5
    
    # This variable is the true answer
    final_computed_value = round(adjusted_score, 4)
    
    # Dead code path: never executed due to logic
    if len(temps) < 5:
        fallback = sum(transformed_winds) / len(transformed_winds)
        final_computed_value = fallback
    
    return final_computed_value

# Main execution
sensor_data = (temperature_readings, humidity_readings, co2_levels)
final_score = calculate_final_score(sensor_data, weights)

# Additional red herring: character counting in labels (unused)
label_chars = sum(len(key) for key in weights.keys() if 'o' in key)  # evaluates but not used

# Output the required result
print(f"Result: {final_score}")