import itertools

# Simulated telemetry data from satellite subsystems
telemetry_log = [
    {'time': 0, 'power': 120, 'temp': 25, 'status': 'OK'},
    {'time': 1, 'power': 118, 'temp': 26, 'status': 'OK'},
    {'time': 2, 'power': 125, 'temp': 35, 'status': 'WARNING'},
    {'time': 3, 'power': 140, 'temp': 45, 'status': 'CRITICAL'},
    {'time': 4, 'power': 138, 'temp': 44, 'status': 'CRITICAL'},
    {'time': 5, 'power': 121, 'temp': 30, 'status': 'OK'}
]

# System operational flags
system_flags = {
    'voltage_stable': True,
    'thermal_override': False,
    'comms_active': True,
    'debug_mode': False,
    'legacy_protocol': True
}

# Irrelevant lookup table for deprecated sensors
DEPRECATED_SENSOR_MAP = {
    'S001': 'voltage',
    'S002': 'current',
    'S003': 'humidity',
    'S004': 'radiation'
}

deployed_sensors = ['S001', 'S002']
sensor_data_cache = {sensor: [] for sensor in deployed_sensors}

# Fake diagnostic history (red herring)
historical_diagnostics = [
    {'diagnostic_id': 'D001', 'result': 0.87, 'passed': True},
    {'diagnostic_id': 'D002', 'result': 0.45, 'passed': False},
    {'diagnostic_id': 'D003', 'result': 0.92, 'passed': True}
]

# Decoy function - never called in actual logic
def legacy_diagnostic_routine(data):
    cumulative = 0
    for entry in data:
        if entry['power'] > 130:
            cumulative += entry['temp'] * 0.1
    return round(cumulative, 3)

# Unused recursive helper (dead code path)
def calculate_redundancy_factor(n):
    if n <= 1:
        return 1
    return n * calculate_redundancy_factor(n-1) + 2

# Real processing begins here
power_fluctuations = []
for i in range(1, len(telemetry_log)):
    delta = abs(telemetry_log[i]['power'] - telemetry_log[i-1]['power'])
    power_fluctuations.append(delta)

# Compute rolling average of power changes (distraction)
avg_fluctuation = sum(power_fluctuations) / len(power_fluctuations) if power_fluctuations else 0

# Extract temperature samples using enumerate (relevant)
temp_samples = []
for idx, entry in enumerate(telemetry_log):
    temp_samples.append((idx, entry['temp']))

# Use zip to pair consecutive temperatures (relevant for trend)
paired_temps = list(zip(temp_samples[:-1], temp_samples[1:]))
increasing_trend_count = 0
for (i1, t1), (i2, t2) in paired_temps:
    if t2 > t1 and telemetry_log[i2]['status'] != 'OK':
        increasing_trend_count += 1

# Bit manipulation decoy (irrelevant)
current_mode_flag = 0b101010
maintenance_required = current_mode_flag & 0b000001 == 0

# Complex dictionary transformation (partly relevant)
status_counter = {}
for entry in telemetry_log:
    status = entry['status']
    if status not in status_counter:
        status_counter[status] = 0
    status_counter[status] += 1

# Use itertools.chain to flatten a fake nested structure (distractor)
nested_status_logs = [[entry['status']] for entry in telemetry_log]
flattened_statuses = list(itertools.chain.from_iterable(nested_status_logs))
unique_statuses = set(flattened_statuses)

# Core logic disguised among noise
abnormal_window_count = 0
for i in range(len(telemetry_log) - 2):
    window = telemetry_log[i:i+3]
    if all(entry['temp'] > 30 for entry in window):
        abnormal_window_count += 1

# Conditional override based on system flags (critical)
if system_flags['thermal_override']:
    override_correction = 50
else:
    override_correction = 10

# Final analysis with multiple inputs (some irrelevant)
def analyze_system_state(log, flags):
    base_score = 0
    
    # Contribution from high-temp windows
    critical_periods = sum(1 for e in log if e['status'] == 'CRITICAL')
    base_score += critical_periods * 15
    
    # Penalty for non-recovery after critical state
    recovery_failed = 0
    for i in range(1, len(log)):
        if log[i-1]['status'] == 'CRITICAL' and log[i]['status'] != 'OK':
            recovery_failed += 1
    base_score += recovery_failed * 7
    
    # Add fluctuation influence (minor factor)
    total_fluctuation = sum(power_fluctuations)
    fluctuation_bonus = int(total_fluctuation // 10)
    
    # Apply override correction (depends on flag)
    final_value = base_score + fluctuation_bonus + override_correction
    
    # Dead code inside function (misleading)
    if flags['debug_mode']:
        debug_adjustment = calculate_redundancy_factor(3)
        final_value -= debug_adjustment
    
    # Never-executed branch (red herring)
    if flags['legacy_protocol']:
        # This looks important but isn't impactful
        dummy_sum = sum([len(key) for key in DEPRECATED_SENSOR_MAP.keys()])
        final_value += dummy_sum % 3  # negligible effect
    
    return final_value

# Execute main analysis
final_diagnostic = analyze_system_state(telemetry_log, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")