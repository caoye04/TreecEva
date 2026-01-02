import math

# Simulated sensor array diagnostics with redacted calibration logic
def calibrate_sensors(raw_readings):
    calibrated = {}
    for key, val in raw_readings.items():
        if 'temp' in key:
            calibrated[key] = val * 1.02 + 3.5
        elif 'pressure' in key:
            calibrated[key] = val * 0.987 - 1.2
        else:
            calibrated[key] = val * 1.05  # placeholder scaling
    return calibrated

# Irrelevant preprocessing: spectral normalization (unused)
def normalize_spectrum(data):
    max_val = max(data.values())
    return {k: v / max_val * 100 for k, v in data.items()}

# Legacy function for deprecated hardware (dead code path)
def legacy_compatibility_layer(inputs):
    transformed = {}
    for k, v in inputs.items():
        transformed[f'legacy_{k}'] = v * 0.5 + 10
    return transformed

# Core transformation pipeline
transform_data = lambda x: {k: math.sqrt(v) if v > 0 else 0 for k, v in x.items()}

# Misleading intermediate diagnostic (decoy)
def compute_health_index(values):
    total = sum(v for v in values if v > 5)
    count = len([v for v in values if v < 20])
    return total * count // 2 if count else 0

# Actual metric processor (used in final step)
def process_metrics(metrics, cfg):
    base_score = 0
    penalty = 0

    for key, value in metrics.items():
        if 'sensor_3_temp' in key and value > 25:
            base_score += int(value)
        elif 'sensor_5_pressure' in key:
            base_score += int(value // 2)
        else:
            penalty += 1

    adjustment = cfg.get('sensitivity', 1) * (base_score - penalty)
    return adjustment ** 2

# Configuration with misleading fields
config = {
    'version': '2.1.0',
    'calibration_required': True,
    'sensitivity': 3,
    'timeout_ms': 5000,
    'debug_mode': False,
    'threshold': 42.5
}

# Raw input data from IoT device cluster
dataset = {
    'sensor_1_temp': 18.4,
    'sensor_2_temp': 21.0,
    'sensor_3_temp': 27.6,
    'sensor_4_humidity': 45.2,
    'sensor_5_pressure': 68.0,
    'sensor_6_light': 120.5,
    'aux_power_draw': 7.3
}

# Step 1: Calibrate relevant sensors
adjusted_readings = calibrate_sensors(dataset)

# Step 2: Apply core transformation (square root scaling)
transformed_data = transform_data(adjusted_readings)

# Step 3: Compute decoy health index (never used later)
decoy_index = compute_health_index(list(transformed_data.values()))

# Step 4: Normalize spectrum (completely irrelevant)
spectral_norm = normalize_spectrum(adjusted_readings)

# Step 5: Process final diagnostic metric
final_diagnostic = process_metrics(transformed_data, config)

print(f"Result: {final_diagnostic}")