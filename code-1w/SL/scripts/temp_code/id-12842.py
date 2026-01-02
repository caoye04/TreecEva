from collections import defaultdict, Counter
import math

# Simulated sensor data ingestion (real-world context: environmental monitoring)
sensor_readings = [
    ('temp', 23.5), ('humidity', 65), ('temp', 24.1), ('pressure', 1013.2),
    ('humidity', 67), ('co2', 415), ('temp', 22.9), ('pressure', 1012.8),
    ('co2', 423), ('humidity', 63), ('temp', 24.3), ('pressure', 1014.1)
]

# Irrelevant preprocessing: dummy transformation (Distractor 1)
def transform_readings(data):
    return [round(v * 1.017, 3) for _, v in data]

dummy_transformed = transform_readings(sensor_readings)

# Group readings by type (Relevant)
readings_map = defaultdict(list)
for sensor_type, value in sensor_readings:
    readings_map[sensor_type].append(value)

# Compute averages per sensor (Partially relevant)
averages = {k: sum(v)/len(v) for k, v in readings_map.items()}

# Decoy analysis: unused statistical spread (Distractor 2)
variance_map = {}
for k, v in readings_map.items():
    mean_val = sum(v)/len(v)
    variance_map[k] = sum((x - mean_val)**2 for x in v) / len(v)

# Simulated calibration coefficients from external source (Distractor 3: misleading constants)
calibration_registry = {
    'temp': 0.92,
    'humidity': 1.05,
    'pressure': 1.003,
    'co2': 0.997
}

# Incorrect fusion method (Dead code path - Distractor 4)
if False:  # Never executed
    fused_risk_index = 0
    for typ, vals in readings_map.items():
        fused_risk_index += max(vals) - min(vals)

# Historical anomaly tracking (Unused but plausible) (Distractor 5)
anomaly_log = []
baseline_thresholds = {'temp': (20, 25), 'humidity': (40, 70), 'pressure': (1000, 1020)}
for sensor_type, values in readings_map.items():
    low, high = baseline_thresholds.get(sensor_type, (0, 100))
    for v in values:
        if v < low or v > high:
            anomaly_log.append((sensor_type, v))

# Key processing chain begins here -------------------------

# Extract co2 trend for climate impact modeling (Relevant path initiation)
co2_values = readings_map['co2']
co2_growth_rate = (co2_values[1] - co2_values[0]) / co2_values[0]

# Energy consumption model based on HVAC load (Plausible distraction but feeds into logic)
temp_fluctuation = max(readings_map['temp']) - min(readings_map['temp'])
hvac_load_estimate = temp_fluctuation * 1.8

# Primary diagnostic score: derived from CO2 growth and pressure stability (Relevant)
pressure_stability = 1 / (sum(abs(p - 1013.0) for p in readings_map['pressure']) + 1)
aggregate_score = co2_growth_rate * 1000 + pressure_stability * 50

# Red herring: unused complex bit manipulation (Distractor 6)
bit_encoded = 0
for i, val in enumerate(co2_values):
    shifted = int(val) << (i + 1)
    bit_encoded ^= shifted
bit_analysis_result = bin(bit_encoded).count('1')

# Fake fallback mechanism (Distractor 7)
def compute_alternate_diagnostic(data):
    cnt = Counter([t for t, _ in data])
    return sum(cnt.values()) % 7

# Correction system based on calibration registry (Relevant but indirect)
correction_factor = 1.0
for sensor in ['temp', 'humidity']:
    correction_factor *= calibration_registry[sensor]

correction_factor = math.log(correction_factor * 100)  # Nonlinear adjustment

# Offset determined from historical median (Relevant)
historical_median_pressure = 1013.0
offset_value = abs(historical_median_pressure - averages['pressure']) * -2

# Critical assignment — answer depends on this
final_diagnostic = aggregate_score * correction_factor + offset_value

# Final output
print(f"Result: {final_diagnostic}")