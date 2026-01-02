import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_readings = {
        'temp': [23.5, 24.1, 22.9, 25.0, 23.8],
        'humidity': [45, 47, 50, 44, 46],
        'pressure': [1013, 1015, 1012, 1014, 1016]
    }
    return raw_readings

# Irrelevant preprocessing - distractor function
def normalize_signal(data):
    peak = max(max(d) for d in data.values())
    norm_data = {k: [v / peak for v in values] for k, values in data.items()}
    scaling_factor = 1.0 / peak
    offset_correction = 0.001 * scaling_factor
    return norm_data

# Redundant transformation - dead path
def legacy_calibrate(arr):
    adjusted = []
    for x in arr:
        if x > 100:
            adjusted.append(x * 0.98)
        else:
            adjusted.append(x + 0.2)
    return adjusted

# Unused utility - misleading intermediate
unused_checksum = lambda seq: sum((i+1)*v for i, v in enumerate(seq)) % 1000

# Real processing begins here
sensor_data = collect_sensor_data()

# Compute rolling averages (actual relevant step)
avg_temp = sum(sensor_data['temp']) / len(sensor_data['temp'])
avg_humidity = sum(sensor_data['humidity']) / len(sensor_data['humidity'])
avg_pressure = sum(sensor_data['pressure']) / len(sensor_data['pressure'])

# Distractor: complex but unused bit manipulation
status_flag = 0b101010
status_flag ^= 0b111100
status_flag &= ~0b000100
status_flag |= 0b010000
parity_check = bin(status_flag).count('1') % 2

# Decoy data structure with plausible naming
historical_snapshot = {
    'timestamp': '2023-09-15T10:30:00Z',
    'readings': sensor_data,
    'diagnostics': {
        'noise_floor': 0.0034,
        'gain_stages': [1.0, 1.8, 2.1],
        'baseline_drift': 0.07
    }
}

# Actual data processing chain
processed_data = {
    'metrics': {
        't': round(avg_temp, 2),
        'h': round(avg_humidity, 2),
        'p': round(avg_pressure, 2)
    },
    'anomalies': []
}

# Inject artificial anomaly based on logic
if avg_temp > 23.7:
    processed_data['anomalies'].append('HIGH_TEMP')
if avg_humidity < 46:
    processed_data['anomalies'].append('LOW_HUMIDITY')

# Complex conditional expression (required feature)
operational_mode = 'STABLE' if avg_pressure > 1013.5 and avg_temp < 24.5 else 'VIGILANT'

# Threshold map with decoy keys
threshold_map = {
    'critical': {'t': 25.0, 'h': 60, 'p': 1030},
    'warning': {'t': 24.0, 'h': 45, 'p': 1010},
    'info': {'t': 20.0, 'h': 30, 'p': 1000},  # unused info tier
    'reserved': {'t': 0.0, 'h': 0, 'p': 0}   # red herring
}

# Set operations - required feature (some sets are irrelevant)
active_alerts = set(processed_data['anomalies'])
critical_conditions = {'HIGH_TEMP', 'HIGH_PRESSURE', 'LOW_HUMIDITY'}
resolved_issues = {'CALIBRATION_PENDING'}
detected_severity = active_alerts & critical_conditions  # intersection matters

# Dictionary analysis with early termination
impact_scores = {}
for category in ['t', 'h', 'p']:
    score = 0
    val = processed_data['metrics'][category]
    thresholds = {lvl: cfg[category] for lvl, cfg in threshold_map.items()}
    
    # Linear search through levels (suggested paradigm)
    for level in ['critical', 'warning']:
        if val > thresholds[level]:
            score += 3 if level == 'critical' else 1
    
    impact_scores[category] = score
    
    # Early break - suggested paradigm
    if score >= 3:
        break

# Final diagnostic computation
base_risk = len(active_alerts) * 2
severity_bonus = len(detected_severity) * 4
mode_penalty = 1 if operational_mode == 'VIGILANT' else 0

# Key assignment statement
final_diagnostic = base_risk + severity_bonus + mode_penalty

# Misleading print of unrelated metric
temp_diagnostic_word = 'OK' if parity_check == 0 else 'ERROR_FLAG'

# Actual output
print(f"Result: {final_diagnostic}")