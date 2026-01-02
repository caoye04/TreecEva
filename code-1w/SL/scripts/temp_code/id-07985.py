from collections import defaultdict, Counter

# Simulated IoT sensor data processing with diagnostic evaluation
def process_sensor_readings(raw_readings, calibration_factor):
    calibrated = [round(x * calibration_factor, 3) for x in raw_readings]
    anomalies = [i for i, v in enumerate(calibrated) if v < -10 or v > 100]
    status_flags = ['OK' if -5 <= v <= 95 else 'OUT_OF_RANGE' for v in calibrated]
    return calibrated, anomalies, status_flags

# Misleading auxiliary function (dead code path)
def analyze_power_consumption(logs):
    peak_usage = max([log['power'] for log in logs])
    avg_load = sum([log['power'] for log in logs]) / len(logs)
    efficiency_score = (avg_load / peak_usage) * 100
    return efficiency_score  # Never used

# Core recursive transformation
def transform_series(data, depth):
    if depth == 0 or len(data) < 2:
        return data
    reduced = [data[i] + (data[i+1] - data[i]) * 0.5 for i in range(len(data)-1)]
    return transform_series(reduced, depth - 1)

# Secondary computation with red herring variables
def compute_thermal_envelope(sensor_data):
    baseline = sum(sensor_data) / len(sensor_data)
    fluctuation = sum(abs(sensor_data[i+1] - sensor_data[i]) for i in range(len(sensor_data)-1))
    stress_factor = fluctuation * 0.7 + baseline * 0.3  # Distractor metric
    normalized_stress = stress_factor / (len(sensor_data) or 1)
    return normalized_stress

# Main aggregation logic
def aggregate_metrics(log_entries, thresholds):
    severity_count = defaultdict(int)
    cumulative_risk = 0

    for entry in log_entries:
        temp = entry['temp']
        pressure = entry['pressure']
        humidity = entry['humidity']

        # Real conditionals affecting output
        if temp > thresholds['temp']:
            severity_count['overheat'] += 1
            cumulative_risk += 1.7
        if pressure < thresholds['pressure_low'] or pressure > thresholds['pressure_high']:
            severity_count['pressure_anomaly'] += 1
            cumulative_risk += 1.3
        if humidity > thresholds['humidity']:
            severity_count['moisture'] += 1
            cumulative_risk += 0.9

    # Red herring computations (irrelevant to final result)
    total_entries = len(log_entries)
    distribution_stats = Counter(severity_count.keys())
    phantom_index = sum(distribution_stats.values()) * 0.5 if distribution_stats else 0

    # Actual answer contribution
    adjustment = len(severity_count) * 100
    base_score = int(cumulative_risk * 10)
    final_score = base_score + adjustment

    return final_score

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = True
LOG_RETENTION_DAYS = 90

# Input data generation with embedded logic
raw_sensors = [23.5, 18.9, 105.2, 47.1, 36.8, -12.3, 88.4]
calibration_multiplier = 0.98

calib_vals, anomaly_indices, flags = process_sensor_readings(raw_sensors, calibration_multiplier)

transformed_series = transform_series(calib_vals, depth=3)

# Unused thermal analysis (misleading call)
thermal_metric = compute_thermal_envelope(calib_vals)

# Build structured log from processed data
health_log = []
for i, val in enumerate(transformed_series):
    record = {
        'id': f'SENSOR_{i:03d}',
        'temp': val + 20,
        'pressure': 98 + (i % 5),
        'humidity': 40 + (val % 25),
        'timestamp': f'2023-11-05T10:{10+i:02d}:00Z',
        'diagnostic_flag': flags[i] if i < len(flags) else 'OK'
    }
    health_log.append(record)

# Another decoy structure
power_logs = [
    {'cycle': i, 'power': 120 + (i * 3) % 15, 'voltage': 220} for i in range(len(health_log))
]

# Threshold map actually used in final computation
threshold_map = {
    'temp': 95.0,
    'pressure_low': 96.0,
    'pressure_high': 100.0,
    'humidity': 60.0
}

# Critical execution point
final_diagnostic = aggregate_metrics(health_log, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")