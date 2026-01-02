import math

# Simulated sensor diagnostics with embedded logic
sensor_readings = {
    'temp': [72.5, 73.1, 71.9, 74.0, 75.2],
    'pressure': [30.1, 29.8, 30.0, 29.9, 30.2],
    'humidity': [45, 47, 46, 48, 49],
    'vibration': [0.05, 0.07, 0.06, 0.08, 0.12]
}

# Irrelevant calibration data (distractor)
calibration_offsets = {
    'temp': 0.3,
    'pressure': 0.05,
    'humidity': 2,
    'light': 12
}

# Decoy function – never called but looks important
def compute_stability_index(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance) if variance > 0.1 else 0.1

# Unused helper (dead code path)
def normalize_values(readings):
    normalized = {}
    for key, values in readings.items():
        min_val, max_val = min(values), max(values)
        normalized[key] = [(v - min_val) / (max_val - min_val) for v in values]
    return normalized

# Auxiliary transformation with partial relevance
rolling_averages = {}
for sensor, values in sensor_readings.items():
    averages = []
    for i in range(2, len(values)):
        avg = (values[i-2] + values[i-1] + values[i]) / 3
        averages.append(round(avg, 2))
    rolling_averages[sensor] = averages

# Misleading intermediate computation (partial red herring)
stability_flags = {}
for sensor, avgs in rolling_averages.items():
    if len(avgs) > 0:
        stability_flags[sensor] = max(avgs) - min(avgs) < 1.0

# Set operation to detect anomalous sensors (distractor with subtle use)
anomaly_thresholds = {"temp": 75.0, "humidity": 48, "vibration": 0.1}
critical_sensors = set()
for key, values in sensor_readings.items():
    if any(v > anomaly_thresholds.get(key, float('inf')) for v in values):
        critical_sensors.add(key)

# Bitwise diagnostic key generation – appears relevant but unused
config_key = 0b1101
for val in sensor_readings['temp']:
    config_key ^= int(val) & 0b1111

# String-based status encoding (distractor)
status_labels = []
for reading_set in sensor_readings.values():
    label = ''.join(["H" if r > sum(reading_set)/len(reading_set) else "L" for r in reading_set])
    status_labels.append(label)

# Core analysis logic (relevant)
def extract_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 1
    return trend_score

# Multi-step diagnostic processor
def generate_diagnostics(raw):
    results = {}
    for sensor, data in raw.items():
        base_metric = sum(data) / len(data)
        trend = extract_trend(data)
        # Composite score with modular weighting
        weight = len(data) % 4
        composite = (base_metric * 1.5) + (trend * 0.8) + (weight * 0.3)
        results[sensor] = round(composite, 3)
    return results

# First-level processing
diagnostics = generate_diagnostics(sensor_readings)

# Secondary transformation with filtering
filtered_diagnostics = {
    k: v for k, v in diagnostics.items() 
    if k not in ['light', 'proximity']  # Safeguard against missing keys
}

# Main analysis function with nested logic
def analyze_metrics(metrics_dict):
    aggregate = 0.0
    count = 0
    
    # Conditional branching based on sensor type
    for sensor_type, score in metrics_dict.items():
        if sensor_type == 'temp':
            adjusted = score * 1.1
        elif sensor_type == 'pressure':
            adjusted = score * 0.95
        elif sensor_type == 'humidity':
            adjusted = score * 1.05
        else:
            adjusted = score * 1.0
            
        # Nested conditional with arithmetic twist
        if adjusted > 110:
            adjusted = adjusted * 0.9
        elif adjusted < 90:
            adjusted = adjusted * 1.05
        else:
            adjusted = adjusted * 1.02
            
        # Accumulate only primary sensors
        if sensor_type in ['temp', 'pressure', 'humidity']:
            aggregate += adjusted
            count += 1
    
    # Final normalization
    if count > 0:
        final = aggregate / count
    else:
        final = 0.0
        
    # Additional interference: unused bitwise op on float (no effect)
    try:
        dummy = int(final) & 0xFF
    except:
        dummy = 0
        
    # Red herring string manipulation
    trace_id = f"DIAG-{int(final)}"
    trace_id = trace_id.replace('-', 'X')
    
    return round(final, 3)

# Execute main computation
final_diagnostic = analyze_metrics(diagnostics)

# Output result as required
print(f"Result: {final_diagnostic}")