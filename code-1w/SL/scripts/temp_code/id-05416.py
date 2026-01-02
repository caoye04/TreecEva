import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 19.0, 27.3, 30.1, 18.9, 22.0, 25.7, 26.8, 20.4, 33.2, 17.6, 24.1]
humidity_readings = [45, 50, 60, 65, 40, 55, 70, 75, 52, 80, 38, 49]
pressure_readings = [1013, 1009, 1015, 1020, 1005, 1012, 1018, 1022, 1007, 1025, 1000, 1011]

# Irrelevant backup data (distractor)
backup_temps = temperature_readings[::-1]
backup_humidity = [h * 1.05 for h in humidity_readings]

# Derived metrics (some relevant, some not)
heat_index = []
for i in range(len(temperature_readings)):
    hi = temperature_readings[i] + 0.5 * (humidity_readings[i] - 50) if humidity_readings[i] > 50 else temperature_readings[i]
    heat_index.append(round(hi, 2))

# Distractor: unused wind chill calculation
wind_speed_kmh = [10, 15, 8, 20, 12, 18, 9, 25, 14, 30, 11, 16]
wind_chill = [round(13.12 + 0.6215*temperature_readings[i] - 11.37*(wind_speed_kmh[i]**0.16) + 0.3965*temperature_readings[i]*(wind_speed_kmh[i]**0.16), 2) for i in range(len(temperature_readings))]

# Thresholds for anomaly detection
threshold_map = {
    'temp_high': 28.0,
    'temp_low': 18.0,
    'humidity_critical': 75,
    'pressure_anomaly': 1020
}

# Composite risk scores - partially irrelevant
risk_scores = []
for t, h, p in zip(temperature_readings, humidity_readings, pressure_readings):
    score = 0
    if t > threshold_map['temp_high']:
        score += 3
    if h > threshold_map['humidity_critical']:
        score += 2
    if abs(p - 1013) > 10:
        score += 1
    risk_scores.append(score)

# Data preprocessing with slicing and filtering
recent_window = temperature_readings[-8:]  # Most recent 8 readings
spike_indices = [i for i, t in enumerate(recent_window) if t > threshold_map['temp_high']]

filtered_data = []
for i, temp in enumerate(temperature_readings):
    if temp < threshold_map['temp_low'] or temp > threshold_map['temp_high']:
        continue
    if humidity_readings[i] > threshold_map['humidity_critical'] + 5:
        continue
    if pressure_readings[i] > threshold_map['pressure_anomaly']:
        adjusted_temp = temp * (1 - (pressure_readings[i] - 1020) / 1000)
    else:
        adjusted_temp = temp
    
    # Apply heat index adjustment only if humidity high
    if humidity_readings[i] > 55:
        adjusted_temp = max(adjusted_temp, heat_index[i])
        
    filtered_data.append(round(adjusted_temp, 2))

# Decoy function - never called
def analyze_trend(data_slice):
    if len(data_slice) < 3:
        return 'unstable'
    diffs = [data_slice[i+1] - data_slice[i] for i in range(len(data_slice)-1)]
    avg_change = sum(diffs) / len(diffs)
    return 'rising' if avg_change > 0.5 else 'falling' if avg_change < -0.5 else 'stable'

# Auxiliary transformation (used)
def normalize_readings(raw_list, base=20.0):
    return [(x - base) / base for x in raw_list]

# Secondary processing chain
normalized_filtered = normalize_readings(filtered_data)
squared_signals = [x**2 for x in normalized_filtered if x > 0.1]

# Core diagnostic processor
# This function contains logic that combines boolean conditions and arithmetic
def process_readings(data, thresholds):
    if not data:
        return -999
    
    # Compute weighted characteristics
    base_mean = sum(data) / len(data)
    variance = sum((x - base_mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    # Boolean logic chain with short-circuiting
    is_stable = len(data) >= 5 and variance < 4.0
    has_extremes = any(x > thresholds['temp_high'] * 0.95 for x in data)
    requires_attention = is_stable or has_extremes and base_mean > 22.0
    
    # Complex conditional with nested expressions
    if requires_attention and not (base_mean < 20.0 or std_dev > 3.0):
        adjustment_factor = 1.25 if len(data) % 2 == 1 else 0.9
        penalty = 2.0 if len([x for x in data if x > thresholds['temp_high']]) >= 2 else 0.0
        
        # Final computation with multiple steps
        raw_diagnostic = base_mean * adjustment_factor - penalty
        
        # Additional correction based on pressure correlation (irrelevant here but looks important)
        high_pressure_count = sum(1 for p in pressure_readings if p > threshold_map['pressure_anomaly'])
        if high_pressure_count > 3:
            raw_diagnostic *= 0.95  # Distractor: condition never met
        
        # Slicing-based final check
        recent_filtered = data[-5:]
        if len(recent_filtered) >= 3:
            trend_boost = (recent_filtered[-1] - recent_filtered[0]) * 0.1
            raw_diagnostic += trend_boost
        
        return round(raw_diagnostic, 4)
    else:
        fallback_score = sum(data) / (len(data) + 1)
        return round(fallback_score, 4)

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")