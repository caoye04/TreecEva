import math

# Simulated sensor fusion system for environmental monitoring

def collect_sensor_data():
    raw_streams = {
        'temp': [23.5, 24.1, 22.9, 25.0, 26.3],
        'humidity': [45, 52, 58, 47, 60],
        'pressure': [1013, 1015, 1012, 1018, 1020],
        'co2': [420, 445, 460, 430, 470]
    }
    # Irrelevant transformation (distractor)
    normalized = {k: [round((v - min(vals)) / (max(vals) - min(vals) + 1e-5), 3) 
                  for v in vals] for k, vals in raw_streams.items()}
    return raw_streams

# Decoy function - looks important but unused
def legacy_calibrate(signal, factor=1.05):
    return [round(x * factor, 2) for x in signal]

# Unused helper (dead code path)
def rolling_average(data, window=3):
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result

# Real processing chain
thresholds = {
    'temp_alert': 25.0,
    'humidity_risk': 55,
    'pressure_drop': 1015,
    'co2_warning': 450
}

# Distractor dictionary with misleading keys
flags = {
    'critical': False,
    'legacy_mode': True,
    'debug_override': None,
    'version': '2.1a'
}

# Sensor-specific anomaly detection (used)
def detect_anomalies(stream, threshold):
    anomalies = []
    for idx, val in enumerate(stream):
        if val > threshold:
            anomalies.append(idx)
    return anomalies

# Complex data transformation with slicing and filtering
sensor_data = collect_sensor_data()

# Irrelevant reshaping (distractor)
temp_slice = sensor_data['temp'][1:-1]
humidity_slice = sensor_data['humidity'][::2]

# Real diagnostic logic buried among distractions
def analyze_pressure_trend(pressure_stream):
    changes = []
    for i in range(1, len(pressure_stream)):
        changes.append(pressure_stream[i] - pressure_stream[i-1])
    avg_change = sum(changes) / len(changes)
    return avg_change > 2.0

# Core processing function with multiple concepts
def process_readings(data, limits):
    # Tuple unpacking (real usage)
    temp, humidity, pressure, co2 = data['temp'], data['humidity'], data['pressure'], data['co2']
    
    # Bit manipulation red herring (irrelevant)
    magic_flag = (len(temp) << 2) ^ 0xA3
    
    # Multiple comparisons and logical combinations
    high_temp_indices = detect_anomalies(temp, limits['temp_alert'])
    high_humidity_indices = detect_anomalies(humidity, limits['humidity_risk'])
    high_co2_indices = detect_anomalies(co2, limits['co2_warning'])
    
    # Set operations with intersection (distractor)
    overlapping_risks = set(high_temp_indices) & set(high_humidity_indices)
    
    # Critical calculation buried here
    severity_score = 0
    if high_temp_indices:
        severity_score += len(high_temp_indices) * 3
    if high_co2_indices:
        severity_score += len(high_co2_indices) * 2
    if analyze_pressure_trend(pressure):
        severity_score += 5
    
    # Dictionary-based weighting (actual contribution)
    weights = {'temp': 1.2, 'co2': 0.8, 'humidity': 0.3}
    base_risk = len(high_temp_indices) * weights['temp'] + len(high_co2_indices) * weights['co2']
    
    # Final computation using slicing and arithmetic
    recent_co2_spike = max(co2[2:]) - min(co2[2:])
    
    # Actual answer derivation
    final_risk = severity_score * 10 + int(recent_co2_spike)
    
    # Red herring: unused complex expression
    decoy_result = (math.log(max(temp)) + math.sin(math.pi / 6)) / (math.sqrt(min(pressure)) or 1)
    
    return final_risk

# Key execution point
final_diagnostic = process_readings(sensor_data, thresholds)

# Print required output
print(f"Result: {final_diagnostic}")