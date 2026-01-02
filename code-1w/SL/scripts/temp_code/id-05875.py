import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.4, 19.5, 25.1, 20.0, 31.2, 18.7, 27.3, 22.9, 26.5, 24.8]
humidity_readings = [45, 53, 61, 49, 72, 58, 67, 50, 55, 60]
pressure_readings = [1013, 1009, 1015, 1020, 1005, 1011, 1018, 1014, 1007, 1010]

# Irrelevant auxiliary data (distractor)
sound_levels = [34, 41, 38, 45, 52, 39, 43, 40, 37, 44]  # Unused in logic
turbidity_index = [2.1, 1.8, 3.0, 2.4, 4.2, 1.9, 3.3, 2.2, 2.7, 2.5]  # Dead code path

# Threshold configurations for anomaly detection
threshold_map = {
    'temp': {'min': 20.0, 'max': 27.0},
    'humidity': {'min': 40, 'max': 65},
    'pressure': {'min': 1008, 'max': 1016}
}

# Data preprocessing with slicing and filtering (relevant)
recent_samples = temperature_readings[-7:]  # Last 7 readings
offset_correction = 1.2
adjusted_temps = [t + offset_correction for t in recent_samples]

# Composite data structure creation (relevant)
sensor_data = []
for i in range(len(adjusted_temps)):
    entry = {
        'idx': i,
        'temp': adjusted_temps[i],
        'humidity': humidity_readings[i+3] if i+3 < len(humidity_readings) else 50,
        'pressure': pressure_readings[(i+1)*2 % len(pressure_readings)]
    }
    sensor_data.append(entry)

# Decoy function (never called - red herring)
def compute_air_quality(sound, turbidity):
    quality_score = 0
    for s, t in zip(sound, turbidity):
        quality_score += s * (1/t)
    return round(quality_score / len(sound), 3)

# Unused set operations (distractor)
unique_pressures = set(pressure_readings)
critical_pressures = {1005, 1009, 1015}
divergent_points = unique_pressures.symmetric_difference(critical_pressures)  # Not used

# Filtering based on multi-condition criteria (relevant)
def is_stable_conditions(entry, thresholds):
    t = entry['temp']
    h = entry['humidity']
    p = entry['pressure']
    
    # Logical combination with short-circuit evaluation
    if t < thresholds['temp']['min'] or t > thresholds['temp']['max']:
        return False
    if h < thresholds['humidity']['min'] or h > thresholds['humidity']['max']:
        return False
    if p < thresholds['pressure']['min'] or p > thresholds['pressure']['max']:
        return False
    return True

filtered_data = [e for e in sensor_data if is_stable_conditions(e, threshold_map)]

# Advanced analysis with bit manipulation and aggregation (key logic)
def analyze_readings(data, config):
    if not data:
        return -1
    
    # Extract values for computation
    temps = [d['temp'] for d in data]
    pressures = [d['pressure'] for d in data]
    
    # Mean calculations
    avg_temp = sum(temps) / len(temps)
    avg_pressure = sum(pressures) / len(pressures)
    
    # Bitwise diagnostic signature (combines integer parts)
    temp_int_sum = sum(int(t) for t in temps)
    press_int_sum = sum(int(p) for p in pressures)
    
    # Key bitwise operation: XOR of aggregated integers
    diagnostic_sig = temp_int_sum ^ press_int_sum  # Core computation
    
    # Secondary validation check (affects result)
    valid_count = sum(1 for d in data if d['humidity'] > 50)
    
    # Final composite score with conditional adjustment
    base_score = int(avg_temp * 10) + int(avg_pressure / 10)
    
    # Conditional modification using logical ops
    adjustment = 5 if valid_count >= 3 and diagnostic_sig & 1 else -3
    
    # Final diagnostic combines arithmetic and bit-derived value
    final_value = base_score + adjustment + (diagnostic_sig % 97)
    
    return final_value

# Misleading intermediate analysis (distractor block)
outlier_count = 0
for reading in temperature_readings:
    if abs(reading - 25.0) > 5:
        outlier_count += 1
status_flag = 'STABLE' if outlier_count < 3 else 'VOLATILE'  # Unused

# Critical execution point
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")