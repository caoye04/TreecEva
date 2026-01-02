from collections import defaultdict, Counter
import itertools

# Simulated sensor array data (temperature, pressure, humidity)
sensor_logs = [
    (23.4, 101.3, 45.0), (22.9, 102.1, 47.3), (24.1, 100.8, 44.1),
    (35.6, 99.4, 61.2), (23.8, 101.0, 46.0), (24.0, 100.9, 45.8),
    (22.1, 103.2, 39.9), (36.2, 98.7, 63.4), (23.5, 101.5, 45.2)
]

# Irrelevant baseline calibration map (distractor)
calibration_map = {i: round(273.15 + i*0.3, 2) for i in range(50)}

# Real processing parameters
def initialize_thresholds():
    default_thresh = defaultdict(lambda: (0.0, 100.0))
    default_thresh['temp'] = (22.5, 24.5)
    default_thresh['pressure'] = (100.5, 102.5)
    default_thresh['humidity'] = (44.0, 48.0)
    return default_thresh

threshold_map = initialize_thresholds()

# Decoy function - looks important but unused
def validate_calibration(data, ref):
    return sum(abs(d - ref[i]) for i, d in enumerate(data) if i < len(ref)) < 15.0

# Auxiliary transformation (partially relevant)
def classify_environment(temp, press, humid):
    categories = []
    if temp < 23.0:
        categories.append('cool')
    elif temp > 24.0:
        categories.append('warm')
    else:
        categories.append('normal_temp')
    
    if press < 101.0:
        categories.append('low_pressure')
    elif press > 102.0:
        categories.append('high_pressure')
    
    if humid < 44.0:
        categories.append('dry')
    elif humid > 48.0:
        categories.append('humid_env')
    
    return tuple(categories)

# Generate environment labels (used later)
environment_classes = [classify_environment(t, p, h) for t, p, h in sensor_logs]

class_counter = Counter(itertools.chain.from_iterable(environment_classes))

# Misleading anomaly detection (dead path)
def detect_anomaly_sequence(logs):
    anomalies = 0
    for i in range(len(logs) - 2):
        window = logs[i:i+3]
        temps = [w[0] for w in window]
        if max(temps) - min(temps) > 10.0:  # Impossible in this dataset
            anomalies += 1
    return anomalies

# Unused call (red herring)
anomaly_count = detect_anomaly_sequence(sensor_logs)

# Actual filtering logic
valid_indices = []
for idx, (t, p, h) in enumerate(sensor_logs):
    temp_ok = threshold_map['temp'][0] <= t <= threshold_map['temp'][1]
    press_ok = threshold_map['pressure'][0] <= p <= threshold_map['pressure'][1]
    humid_ok = threshold_map['humidity'][0] <= h <= threshold_map['humidity'][1]
    if temp_ok and press_ok and humid_ok:
        valid_indices.append(idx)

filtered_data = [sensor_logs[i] for i in valid_indices]

# Bit manipulation decoy (irrelevant computation)
bit_flags = 0
for entry in filtered_data:
    t_int = int(entry[0] * 10)
    p_int = int(entry[1])
    bit_flags ^= (t_int & 0xFF) | ((p_int << 2) & 0x3FC)

# Core diagnostic processor
def process_readings(readings, thresholds):
    if not readings:
        return -1
    
    # Extract values for statistical analysis
    temps = [r[0] for r in readings]
    pressures = [r[1] for r in readings]
    humidities = [r[2] for r in readings]
    
    avg_temp = sum(temps) / len(temps)
    avg_press = sum(pressures) / len(pressures)
    
    # Weighted stability index
    temp_dev = sum((t - avg_temp)**2 for t in temps)
    press_dev = sum((p - avg_press)**2 for p in pressures)
    
    # Apply correction factors (hidden logic)
    correction_factor = 1.0
    if class_counter.get('warm', 0) > 2:
        correction_factor *= 0.9
    if any('humid_env' in ec for ec in environment_classes):
        correction_factor *= 1.05
    
    # Final diagnostic score
    stability_score = (1000 - (temp_dev * 50 + press_dev * 10)) * correction_factor
    
    # Secondary adjustment based on count
    reading_count_score = len(readings) * 15
    
    # Combine scores with integer truncation
    final_score = int(stability_score + reading_count_score)
    
    # Tertiary adjustment via bitwise quirk
    final_score = (final_score ^ 0x5F) & 0x7FFF  # Mask to positive 15-bit
    
    return final_score

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")