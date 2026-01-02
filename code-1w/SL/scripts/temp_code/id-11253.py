import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.9, 20.2]
humidity_readings = [45, 50, 52, 47, 60, 65, 40, 38]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1005, 1018, 1020]

# Irrelevant constants (distractors)
CALIBRATION_FACTOR = 1.0037
REFERENCE_VOLTAGE = 3.3
MAX_BUFFER_SIZE = 256

# Preprocessing: Normalize readings using z-score (only temperature used in final logic)
def normalize(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean) / std_dev for x in data] if std_dev != 0 else [0] * len(data)

# Misleading transformation function not used in critical path
def transform_pressure(pressure):
    return [math.log(p) * CALIBRATION_FACTOR for p in pressure]

# Critical preprocessing function
processed_temperature = normalize(temperature_readings)

# Dummy processing on humidity (dead code path - not used later)
humidity_status = []
for h in humidity_readings:
    status = 'high' if h > 55 else 'normal' if h > 45 else 'low'
    humidity_status.append(status)

# String-based flag generation (uses string method - red herring)
flags = ['TEMP_' + stat.upper() + '_FLAG' for stat in humidity_status]
flag_summary = ''.join(flags).replace('FLAG', '').lower()

# Simulate data packet assembly (irrelevant)
packet_header = f"HDR:{len(processed_temperature)}:ENV"
packet_payload = [round(t, 2) for t in processed_temperature]
data_packet = packet_header + ";" + ",".join(map(str, packet_payload))

# Extract numeric payload again (unnecessary round-trip)
recovered_data = [float(x) for x in data_packet.split(';')[1].split(',')]

# Secondary transformation with conditional expression (partially relevant)
adjusted_data = [
    val * 1.05 if val > 0.5 else 
    val * 0.95 if val < -0.5 else 
    val * 1.01 for val in recovered_data
]

# Additional unused transformation (decoy)
smoothed_data = []
for i in range(len(adjusted_data)):
    window = adjusted_data[max(0, i-1):min(i+2, len(adjusted_data))]
    smoothed_data.append(sum(window) / len(window))

# Core diagnostic logic (only this affects final answer)
def count_significant_anomalies(data, threshold=0.75):
    count = 0
    for x in data:
        if abs(x) > threshold:
            count += 1
            break  # early return pattern reduces effective impact
    return count * len(data)  # amplifies count by total size

# Another irrelevant utility
def generate_timestamps(count):
    return [f"2023-01-01T12:{str(i*5).zfill(2)}:00" for i in range(count)]
timestamps = generate_timestamps(len(temperature_readings))

# Data structure mixing (cross-reference distractor)
sensor_fusion = {
    'temps': processed_temperature,
    'humid': humidity_readings,
    'press': pressure_readings,
    'anomaly_score': None
}

# Main analysis function that depends only on transformed temp anomalies
def analyze_readings(norm_temp_data):
    raw_count = count_significant_anomalies(norm_temp_data)
    scaling_factor = 1.75
    
    # Complex-looking but deterministic adjustment
    adjustment = sum(
        math.sin(x * scaling_factor) for x in norm_temp_data[:3]
    ) * 0.1
    
    # Final computation
    base_result = raw_count * 100
    final_score = int(base_result + (adjustment * 100))
    
    # Dead comparison with no side effects (misleading)
    if final_score > 200:
        compliance_status = 'breach'
    elif final_score > 100:
        compliance_status = 'warning'
    else:
        compliance_status = 'ok'
    
    return final_score

# Execute main logic
processed_data = adjusted_data  # assign to named variable as per description
critical_threshold = 0.75  # unused duplicate constant (distractor)

final_diagnostic = analyze_readings(processed_data)
print(f"Target result: {final_diagnostic}")