import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.4, 25.1, 22.8, 26.5, 24.3, 27.0, 23.9, 25.6]
humidity_readings = [56, 61, 58, 63, 59, 65, 57, 62]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1018, 1011, 1017]

# Irrelevant auxiliary arrays (distractors)
luminosity_readings = [890, 910, 870, 930, 880, 950, 860, 920]  # Not used in final calculation
wind_speed_readings = [4.2, 3.8, 5.1, 4.6, 3.9, 5.3, 4.0, 4.8]  # Dead-end processing

# Misleading preprocessing: looks important but unused in critical path
def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

filtered_temp = filter_outliers(temperature_readings)  # Computed but not used later
correlation_index = 0
for i in range(len(humidity_readings)):
    correlation_index += humidity_readings[i] * (i + 1)  # Artificial index with no real impact
correlation_index = correlation_index % 100  # Further obfuscation

# Real processing begins here — subtle because surrounded by noise
def normalize(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

norm_temp = normalize(temperature_readings)
norm_humidity = normalize(humidity_readings)
norm_pressure = normalize(pressure_readings)

# Composite health index using weighted fusion (key logic buried in middle)
def compute_stability_index(temp, hum, pres):
    temp_variability = sum(abs(a - b) for a, b in zip(temp, temp[1:]))
    hum_trend = sum(1 for a, b in zip(hum, hum[1:]) if b > a) - sum(1 for a, b in zip(hum, hum[1:]) if b < a)
    pres_stability = len(pres) / (sum((1 / (abs(p - 1) + 0.1)) for p in normalize([abs(p - 1013) for p in pressure_readings])))
    return (temp_variability * 1.5 + hum_trend * 0.8 + pres_stability * 2.0)

stability_score = compute_stability_index(norm_temp, norm_humidity, norm_pressure)

# Unused decoy function to mislead control flow analysis
def predict_failure_risk(score):
    if score < 5:
        return "LOW"
    elif score < 10:
        return "MODERATE"
    else:
        return "HIGH"
    return "UNKNOWN"  # Dead code

# Data transformation pipeline with list comprehension (required Python feature)
processed_data = [
    {
        'idx': i,
        'thermal': round(norm_temp[i], 3),
        'moisture': round(norm_humidity[i], 3),
        'barometric': round(norm_pressure[i], 3),
        'composite': (norm_temp[i]*0.4 + norm_humidity[i]*0.3 + norm_pressure[i]*0.3)
    }
    for i in range(len(norm_temp))
]

# Secondary irrelevant computation on processed data
average_composite = sum(entry['composite'] for entry in processed_data) / len(processed_data)
deviation_penalty = sum((entry['composite'] - average_composite) ** 2 for entry in processed_data)

# Core analysis function — answer depends on this
valid_thresholds = [e['thermal'] > 0.5 for e in processed_data]
trigger_count = sum(valid_thresholds)

# Another red herring: complex-looking but unused bit manipulation
checksum = 0
for entry in processed_data:
    checksum ^= int(entry['moisture'] * 100) & 0xFF
crc_flag = checksum & 0x0F

# Critical function that computes the final result
def analyze_readings(data):
    high_thermal_count = len([e for e in data if e['thermal'] > 0.6])
    avg_barometric = sum(e['barometric'] for e in data) / len(data)
    
    # Hidden conditional logic with multiple dependencies
    if high_thermal_count >= 3:
        adjustment = 1.25
    else:
        adjustment = 0.85
    
    # Key formula: combines arithmetic, list operations, and stability score
    base_value = stability_score * adjustment
    penalty = 0
    for i in range(1, len(data)):
        if data[i]['moisture'] < data[i-1]['moisture']:
            penalty += 0.15
    
    # Final deterministic computation
    result = base_value - penalty + avg_barometric * 10
    return round(result, 4)

# Execution point of interest
final_diagnostic = analyze_readings(processed_data)

# Output the target result
print(f"Result: {final_diagnostic}")