import math

# Simulated sensor readings and system diagnostics
sensor_data = {
    'temp': [23.5, 24.1, 22.8, 25.0, 23.9],
    'pressure': [101.3, 102.1, 100.7, 103.4, 101.8],
    'vibration': [0.45, 0.67, 0.52, 0.89, 0.76],
    'humidity': [45, 47, 44, 48, 50]
}

# Irrelevant calibration constants (distractors)
calibration_offsets = {'alpha': 0.98, 'beta': 1.02, 'gamma': 0.99}
baseline_readings = {'temp': 20.0, 'pressure': 100.0}

# System thresholds (some are decoys)
thresh = {
    'temp_high': 30.0,
    'temp_low': 15.0,
    'vibration_alert': 0.8,
    'pressure_critical': 110.0,
    'humidity_warning': 60
}

# Unused diagnostic map (red herring)
diag_map = {
    1: 'normal',
    2: 'caution',
    3: 'alert',
    4: 'critical',
    5: 'unknown'
}

# Phantom subsystem statuses (dead code path)
subsystem_status = {
    'power': 'stable',
    'comms': 'active',
    'storage': 'full',  # irrelevant
    'cache': 'cleared'   # never used
}

# Auxiliary function that looks important but isn't called
def normalize_reading(val, base):
    return (val - base) / base

# Decoy transformation matrix (never used)
transform_matrix = [
    [1.0, -0.1],
    [0.05, 1.1]
]

# Real processing begins here
averages = {}
for key in sensor_data:
    averages[key] = sum(sensor_data[key]) / len(sensor_data[key])

# Compute derived metrics
thermal_index = (averages['temp'] - 20) * 1.5
pressure_delta = averages['pressure'] - baseline_readings['pressure']
vibration_risk = averages['vibration'] > thresh['vibration_alert']

# Hidden logic: count how many sensors exceed their baseline ratio
excess_count = 0
for key in ['temp', 'pressure', 'humidity']:
    if key in baseline_readings:
        if averages[key] / baseline_readings[key] > 1.03:
            excess_count += 1
    else:
        # This block runs for 'humidity' but does nothing
        continue

# Bit manipulation for checksum (looks complex but deterministic)
data_keys = sorted(sensor_data.keys())
checksum = 0
for i, k in enumerate(data_keys):
    checksum ^= (len(sensor_data[k]) << 2)
    checksum += int(averages[k]) if isinstance(averages[k], float) else 0

# Recursive depth counter (simple recursion with bounded depth)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n - 2)

recursion_trace = calculate_depth(5)  # Returns 5 + 3 + 1 = 9

# Set operations to filter anomalies (some elements are distractions)
anomaly_set = set()
for val in sensor_data['vibration']:
    if val > 0.7:
        anomaly_set.add(round(val, 2))

# Dummy aggregation (unused)
summary_stats = {
    'max_vibration': max(sensor_data['vibration']),
    'min_temp': min(sensor_data['temp']),
    'range_humidity': max(sensor_data['humidity']) - min(sensor_data['humidity'])
}

# Core decision logic buried among distractors
system_state = {
    'risk_factor': 0,
    'stability': '',
    'flags': [],
    'checksum': checksum,
    'trace': recursion_trace
}

if thermal_index > 5.0:
    system_state['risk_factor'] += 2
if vibration_risk:
    system_state['risk_factor'] += 3
if excess_count >= 2:
    system_state['risk_factor'] += 1

# Multiple assignments that look significant
level_x, level_y = system_state['risk_factor'], thermal_index
level_z = level_x * 0.5 + level_y * 0.1

# Final assignment buried in function call
def analyze_metrics(state):
    risk = state['risk_factor']
    trace = state['trace']
    chk = state['checksum']
    
    # Complex-looking but deterministic formula
    intermediate = (risk * 100) + trace
    if chk > 50:
        intermediate -= 10
    
    # Red herring: unused dict update
    state['diagnostic_code'] = 'DX' + str(intermediate)
    
    # Actual answer computation
    final_score = intermediate + (chk % 7)
    
    # Dead branch with misleading comment
    if False:  # This was used in debug mode
        final_score = 999  
    
    return final_score

# Critical execution point
final_diagnostic = analyze_metrics(system_state)

# Output result as required
print(f"Target result: {final_diagnostic}")