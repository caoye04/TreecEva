import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 20.4, 21.9]
humidity_readings = [45, 52, 58, 47, 60, 63, 55, 50]
pressure_readings = [1013, 1015, 1010, 1008, 1017, 1020, 1014, 1012]

# Irrelevant auxiliary arrays (distractor)
altitude_zones = [120, 205, 98, 300, 150, 75, 220, 180]
rain_accumulation = [0.1, 0.0, 0.3, 0.0, 0.0, 0.0, 0.2, 0.1]
wind_speeds = [8, 12, 15, 10, 18, 20, 14, 11]

# Complex preprocessing with red herrings
def normalize_signal(data, base=100):
    normalized = []
    offset = sum(data[:3]) / len(data[:3])
    for val in data:
        adjusted = (val - offset) * 1.05
        if adjusted < 0:
            adjusted = 0
        normalized.append(round(adjusted, 2))
    return normalized

# Unused function - dead code path (distractor)
def compute_wind_chill(temp, wind):
    chill = 13.12 + 0.6215*temp - 11.37*(wind**0.16) + 0.3965*temp*(wind**0.16)
    return round(chill, 2)

# Another decoy transformation (irrelevant)
def frequency_domain_transform(seq):
    transformed = []
    for i in range(len(seq)):
        component = 0
        for j in range(len(seq)):
            angle = 2 * math.pi * i * j / len(seq)
            component += seq[j] * math.cos(angle)
        transformed.append(round(component, 2))
    return transformed

# Real processing begins here
scaled_temps = normalize_signal(temperature_readings, base=20)
scaled_humidity = normalize_signal(humidity_readings, base=50)

# Create composite index (only some components are used later)
composite_metrics = []
for i in range(len(scaled_temps)):
    metric = (
        scaled_temps[i] * 1.2 +
        scaled_humidity[i] * 0.8 +
        (pressure_readings[i] - 1000) * 0.1
    )
    composite_metrics.append(round(metric, 2))

# Destructuring and tuple unpacking (relevant)
primary_data = list(zip(temperature_readings, humidity_readings, pressure_readings))
processed_data = []

for temp, hum, pres in primary_data:
    # Non-linear transformation
    heat_index = temp + 0.36 * hum - 4.8
    if temp > 25:
        heat_index += 2.1
    elif temp < 20:
        heat_index -= 1.5
    
    # Dummy transformations with unused results (distractors)
    barometric_tendency = (pres - 1010) / 5
    dew_point_estimate = temp - ((100 - hum) / 5)
    stability_class = 'C' if barometric_tendency > 1 else 'B'
    
    # Only heat_index is actually carried forward
    processed_data.append({'index': heat_index, 'temp': temp})

# Dictionary operations: threshold configuration map (key python feature)
threshold_map = {
    'warning_low': 22.0,
    'warning_high': 28.0,
    'critical_low': 20.0,
    'critical_high': 30.0,
    'weightings': {'index': 1.0, 'temp': 0.0}  # temp weighting is ignored
}

# Linear search with early termination (relevant logic)
def find_anomalies(data, thresholds):
    anomalies = []
    weights = thresholds['weightings']
    warning_upper = thresholds['warning_high']
    warning_lower = thresholds['warning_low']
    
    for record in data:
        score = record['index'] * weights['index']  # only index matters
        if score < warning_lower or score > warning_upper:
            anomalies.append(score)
    return anomalies

# Dead-end analysis function (decoy)
def assess_air_quality(hum, temp):
    if hum > 60 and temp > 25:
        return 'Poor'
    elif hum < 30:
        return 'Dry'
    else:
        return 'Acceptable'

# Real analysis function with multiple steps
# Includes min/max/average and conditional branching
# Key execution point: final_diagnostic assignment
def analyze_readings(data, config):
    if not data:
        return -1
    
    scores = [entry['index'] for entry in data]
    total = sum(scores)
    count = len(scores)
    average_score = total / count
    
    max_score = max(scores)
    min_score = min(scores)
    range_score = max_score - min_score
    
    # Bit manipulation as red herring (irrelevant)
    magic_flag = (int(max_score) << 2) ^ int(min_score)
    magic_flag = magic_flag & 0xFF
    
    # Conditional logic chain with nested checks
    if average_score < config['warning_low']:
        base_rating = 2
    elif average_score >= config['warning_high']:
        base_rating = 4
    else:
        base_rating = 3
    
    if range_score > 6.0:
        volatility_penalty = 2
    elif range_score > 3.0:
        volatility_penalty = 1
    else:
        volatility_penalty = 0
    
    # Apply penalty only if high volatility
    adjusted_rating = base_rating
    if volatility_penalty > 0:
        adjusted_rating = max(1, base_rating - volatility_penalty)
    
    # Final computation using weighted combination
    diagnostic_value = (
        average_score * 10 + 
        adjusted_rating * 5 - 
        range_score * 2
    )
    
    # Normalize with logarithmic scale (final transformation)
    if diagnostic_value > 0:
        final_value = math.log(diagnostic_value) * 100
    else:
        final_value = -100
    
    return round(final_value, 2)

# Irrelevant sorting operation (distractor)
sorted_composite = sorted(composite_metrics, reverse=True)

# Unused list comprehension (dead code)
filtered_by_altitude = [zone for zone, temp in zip(altitude_zones, temperature_readings) if temp > 22]

# Critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")