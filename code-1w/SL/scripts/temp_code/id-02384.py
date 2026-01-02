from collections import defaultdict
import math

# Simulated sensor data processing for a spacecraft subsystem
sensor_readings = [
    ("temp_core", [23.5, 24.1, 23.9, 25.0, 26.2]),
    ("temp_battery", [19.2, 18.9, 19.5, 20.1, 21.3]),
    ("voltage_main", [119.8, 120.1, 119.7, 118.9, 117.5]),
    ("voltage_aux", [5.01, 5.03, 4.98, 4.95, 5.05])
]

# Irrelevant auxiliary data — red herring
maintenance_schedule = {
    "last_calibration": "2023-07-15",
    "next_checkup": "2024-01-15",
    "engineer_id": "ENG-8842"
}

# Decoy function — never used in actual computation path
def analyze_stability_legacy(data):
    return sum(x ** 2 for x in data) / len(data)

# Real processing pipeline
system_health_map = defaultdict(lambda: {"mean": 0, "variance": 0, "anomalies": 0})

for sensor_name, readings in sensor_readings:
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    anomalies = sum(1 for x in readings if abs(x - mean_val) > 1.5)
    
    system_health_map[sensor_name]["mean"] = mean_val
    system_health_map[sensor_name]["variance"] = variance
    system_health_map[sensor_name]["anomalies"] = anomalies

# Bit manipulation decoy — looks important but unused
checksum_key = 0
for i in range(len(maintenance_schedule)):
    checksum_key ^= (i + 5) << 2
    checksum_key += len(maintenance_schedule.keys())

# Unused intermediate transformation
transformed_readings = list(map(lambda x: (x[0], [round(val * 1.01, 2) for val in x[1]]), sensor_readings))

# Threshold definitions (some irrelevant entries included)
system_thresholds = {
    "temp_core": {"warn_high": 25.0, "fail_high": 30.0},
    "temp_battery": {"warn_high": 22.0, "fail_high": 25.0},
    "voltage_main": {"warn_low": 118.0, "fail_low": 115.0},
    "voltage_aux": {"warn_low": 4.9, "fail_low": 4.5},
    "pressure_cabin": {"warn_low": 90.0, "fail_low": 80.0}  # Not present in data
}

# Diagnostic scoring logic
def evaluate_sensor_status(sensor_name, health_data, thresholds):
    if sensor_name not in thresholds:
        return 0  # No threshold → no impact
    
    status_score = 10
    specs = thresholds[sensor_name]
    
    if sensor_name.startswith("temp"):
        if health_data["mean"] > specs["warn_high"]:
            status_score -= 3
        if health_data["anomalies"] > 1:
            status_score -= 2
    elif sensor_name.startswith("voltage"):
        if health_data["mean"] < specs["warn_low"]:
            status_score -= 4
        if health_data["variance"] > 1.0:
            status_score -= 3
    
    return max(status_score, 0)

# Aggregation with distractor logic
def aggregate_diagnostics(health_map, thresholds):
    raw_scores = []
    weight_map = {"temp_core": 1.2, "temp_battery": 1.0, "voltage_main": 1.5, "voltage_aux": 0.8}
    
    # Distractor loop — calculates but doesn't affect final score
    temp_debug = []
    for name, data in health_map.items():
        if "temp" in name:
            normalized_variance = data["variance"] / (data["mean"] + 1e-5)
            temp_debug.append(normalized_variance)
    
    # Actual scoring path
    for name, data in health_map.items():
        score = evaluate_sensor_status(name, data, thresholds)
        weighted_score = score * weight_map.get(name, 1.0)
        raw_scores.append(weighted_score)
    
    # Final diagnostic calculation
    base_diagnostic = sum(raw_scores)
    adjustment_factor = math.log(1 + len([s for s in raw_scores if s < 5]))
    final_value = base_diagnostic - adjustment_factor
    
    # Dead code branch — never executed due to logic
    if len(temp_debug) > 10:
        final_value += sum(temp_debug) // len(temp_debug)
    
    return round(final_value, 4)

# Key execution point
diagnostics_log = dict(system_health_map)
final_diagnostic = aggregate_diagnostics(diagnostics_log, system_thresholds)

# Output result
print(f"Result: {final_diagnostic}")