from collections import defaultdict, Counter
import math

# Simulated sensor data from industrial turbine monitoring system
def get_sensor_readings():
    return {
        'temperature': [298.15, 301.22, 299.45, 302.01, 300.67],
        'pressure': [98.2, 99.1, 97.8, 100.3, 99.9],
        'vibration': [0.12, 0.15, 0.11, 0.18, 0.14],
        'rpm': [1200, 1210, 1195, 1220, 1208]
    }

# Legacy function - unused but looks relevant
def calculate_stress_factor(temp, press):
    alpha = 0.87
    beta = 1.03
    stress = 0.0
    for i in range(50):
        stress += (temp + i) * alpha % (press + i) * beta
    return round(stress / 50, 4)

# Misleading diagnostic with decoy logic
def analyze_vibration_pattern(vib_data):
    if len(vib_data) == 0:
        return 0.0
    squared_sum = sum([x*x for x in vib_data])
    mean_square = squared_sum / len(vib_data)
    rms_vibration = math.sqrt(mean_square)
    
    # Dead code path - never reached due to logic
    if rms_vibration < 0.05:
        category = 'stable'
    elif rms_vibration < 0.15:
        category = 'moderate'
    else:
        category = 'critical'
        adjustment = 0.0
        for i in range(100):
            adjustment += math.sin(i * rms_vibration)
        rms_vibration += adjustment * 0.001  # Never actually applied
    
    return round(rms_vibration + 100, 3)  # Misleading offset

# Core data transformation pipeline
def normalize_readings(raw):
    normalized = {}
    for key, values in raw.items():
        avg = sum(values) / len(values)
        normalized[key] = [round((v - avg) / avg * 100, 2) for v in values]
    return normalized

# Bit manipulation for checksum simulation
def generate_checksum(data_list):
    checksum = 0
    for val in data_list:
        shifted = int(val * 100) << 2
        checksum ^= shifted
        checksum = (checksum & 0xFFFF) | ((checksum << 16) & 0xFFFF0000)
    return checksum & 0xFFFF

# Main analysis workflow
def compute_thermal_profile(temp_data):
    kelvin_offset = 273.15
    celsius_vals = [t - kelvin_offset for t in temp_data]
    avg_celsius = sum(celsius_vals) / len(celsius_vals)
    variance = sum([(c - avg_celsius) ** 2 for c in celsius_vals]) / len(celsius_vals)
    std_dev = math.sqrt(variance)
    return {
        'mean': round(avg_celsius, 2),
        'std_dev': round(std_dev, 3),
        'range': round(max(celsius_vals) - min(celsius_vals), 2)
    }

# Log processing with set operations and frequency counting
def parse_system_events(log_entries):
    event_types = set(['INFO', 'WARN', 'ERROR', 'DEBUG'])
    priority_events = set(['ERROR', 'CRITICAL'])
    filtered = [entry for entry in log_entries if entry['level'] in event_types]
    
    # Unused but plausible distractor structure
    context_map = defaultdict(list)
    for entry in filtered:
        timestamp = entry['time'] // 60
        context_map[timestamp].append(entry['level'])
    
    # Actual relevant computation
    level_counter = Counter([entry['level'] for entry in filtered])
    error_count = level_counter['ERROR'] + level_counter['WARN']
    return error_count

# Primary integrity assessment engine
def compute_integrity_score(thermal_load, system_log):
    # Step 1: Process thermal load
    profile = compute_thermal_profile(thermal_load)
    base_score = 100.0
    
    # Step 2: Deduct based on thermal deviation
    if profile['mean'] > 30.0:
        base_score -= (profile['mean'] - 30.0) * 1.5
    if profile['std_dev'] > 2.0:
        base_score -= (profile['std_dev'] - 2.0) * 2.0
    
    # Step 3: Process system log events
    fault_count = parse_system_events(system_log)
    base_score -= fault_count * 3.2
    
    # Step 4: Apply minimum threshold
    if base_score < 20.0:
        base_score = 20.0 + math.log(fault_count + 1)  # Prevent excessive penalization
    
    # Step 5: Final adjustment using bit-level operation (checksum derived weight)
    dummy_values = [profile['mean'], profile['std_dev'], fault_count]
    weight_checksum = generate_checksum(dummy_values)
    adjustment_factor = (weight_checksum % 100) / 1000.0
    final_score = base_score + adjustment_factor
    
    return round(final_score, 4)

# --- Execution Context ---

# Retrieve raw sensor data
raw_sensors = get_sensor_readings()

# Normalize for display (irrelevant to main calculation)
normalized_sensors = normalize_readings(raw_sensors)

# Generate fake historical comparison (dead end)
historical_mean = {
    'temperature': 299.5,
    'pressure': 99.0,
    'vibration': 0.13,
    'rpm': 1205
}

deviation_report = {}
for key in normalized_sensors:
    sample_dev = normalized_sensors[key][0]
    deviation_report[key] = sample_dev

# Prepare thermal load sequence for analysis
thermal_load = raw_sensors['temperature']  # Critical input

# Fabricate system log entries
system_log = [
    {'time': 3600, 'level': 'INFO', 'msg': 'System initialized'},
    {'time': 3650, 'level': 'WARN', 'msg': 'High vibration detected'},
    {'time': 3700, 'level': 'ERROR', 'msg': 'Sensor calibration failed'},
    {'time': 3750, 'level': 'INFO', 'msg': 'Stabilization attempt'},
    {'time': 3800, 'level': 'WARN', 'msg': 'Temperature drift observed'},
    {'time': 3850, 'level': 'DEBUG', 'msg': 'Internal state dump'}
]

# Compute vibration metric (looks important but unused)
vib_metric = analyze_vibration_pattern(raw_sensors['vibration'])

# Compute stress factor (unused legacy call)
stress_test = calculate_stress_factor(thermal_load[0], raw_sensors['pressure'][0])

# Perform core diagnostic evaluation
final_diagnostic = compute_integrity_score(thermal_load, system_log)

# Print result as required
print(f"Result: {final_diagnostic}")