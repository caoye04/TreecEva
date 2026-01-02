import math

# Simulated telemetry data from satellite subsystems
telemetry_stream = [
    {'sensor': 'temp_core', 'value': 78, 'timestamp': 1623456780},
    {'sensor': 'voltage_batt', 'value': 12.4, 'timestamp': 1623456781},
    {'sensor': 'temp_core', 'value': 85, 'timestamp': 1623456782},
    {'sensor': 'pressure_hull', 'value': 14.7, 'timestamp': 1623456783},
    {'sensor': 'temp_core', 'value': 93, 'timestamp': 1623456784},
    {'sensor': 'voltage_batt', 'value': 11.8, 'timestamp': 1623456785},
    {'sensor': 'pressure_hull', 'value': 14.6, 'timestamp': 1623456786}
]

# Irrelevant baseline constants for red herring
BASELINE_TEMP = 70
CRITICAL_VOLTAGE = 10.0
WARNING_PRESSURE = 15.0

# Distractor: unused function (dead code path)
def calculate_fuel_estimate(reading):
    return (reading['value'] * 1.8 + 32) / 0.453 if reading['sensor'] == 'temp_core' else 0

# Distractor: misleading intermediate aggregation
snapshot_moment = sum([entry['timestamp'] for entry in telemetry_stream]) // len(telemetry_stream)

# Real processing begins: extract sensor readings
sensor_data = {}
for entry in telemetry_stream:
    key = entry['sensor']
    if key not in sensor_data:
        sensor_data[key] = []
    sensor_data[key].append(entry['value'])

# Compute rolling statistics (some used, some not)
avg_temp = sum(sensor_data['temp_core']) / len(sensor_data['temp_core'])
max_voltage = max(sensor_data['voltage_batt'])
min_pressure = min(sensor_data['pressure_hull'])
deviation_temp = math.sqrt(sum((x - avg_temp) ** 2 for x in sensor_data['temp_core'])) / len(sensor_data['temp_core'])

# Distractor: complex but unused bit manipulation
status_word = 0b1010
status_word ^= 0b1111
status_word <<= 2
status_word |= 0b0010
mask_applied = status_word & 0b11001100

# Distractor: irrelevant set operations (red herring)
expected_sensors = {'temp_core', 'voltage_batt', 'pressure_hull'}
redundant_sensors = {'temp_aux', 'gyro_x', 'voltage_batt'}
overlap_check = expected_sensors & redundant_sensors
priority_alerts = expected_sensors - redundant_sensors

# Conditional expression with meaningful outcome embedded
thermal_trend = 'rising' if sensor_data['temp_core'][-1] > sensor_data['temp_core'][0] else 'stable'

# Log summary construction using dictionary and conditional logic
log_summary = {
    'entries': len(telemetry_stream),
    'has_anomaly': any(v < 12.0 for v in sensor_data['voltage_batt']),
    'thermal_state': 'overheat' if avg_temp > 88 else 'nominal',
    'trend': thermal_trend,
    'deviation': round(deviation_temp, 3)
}

# System flags with bitwise-inspired but logical composition
flag_temp_high = 1 if log_summary['thermal_state'] == 'overheat' else 0
flag_voltage_low = 1 if log_summary['has_anomaly'] else 0
system_flags = (flag_temp_high << 1) | flag_voltage_low

# Unused recursive distractor function
def trace_propagation_depth(depth):
    if depth <= 1:
        return 1
    return trace_propagation_depth(depth - 1) + trace_propagation_depth(depth - 2)

# This call is never made — dead recursion path
# trace_propagation_depth(5)

# Core diagnostic processor combining multiple concepts
def process_metrics(log, flags):
    base_score = 100
    
    # Apply penalties based on log
    if log['thermal_state'] == 'overheat':
        base_score -= 35
    if log['has_anomaly']:
        base_score -= 20
    if log['trend'] == 'rising':
        base_score -= 15
    
    # Additional penalty from flag pattern
    if flags == 3:  # both temp high and voltage low
        base_score -= 25
    
    # Irrelevant floating point adjustment (distractor)
    noise_adjustment = (math.sin(math.pi / 4) * math.log(2)) / 1000
    base_score -= noise_adjustment  # negligible effect
    
    # Final clamping to valid range
    return int(max(0, min(100, base_score)))

# Key execution point
final_diagnostic = process_metrics(log_summary, system_flags)

# Output result as required
print(f"Target result: {final_diagnostic}")