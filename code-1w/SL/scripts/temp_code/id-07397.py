import math

# Simulated sensor data from a distributed monitoring system
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 50, 44, 60]
pressure_readings = [1013, 1015, 1012, 1010, 1008]

# Irrelevant transformation - distractor
smoothed_temps = [round((t + t*0.01), 2) for t in temperature_readings]
avg_smoothed = sum(smoothed_temps) / len(smoothed_temps)

# Data aggregation (some relevant, some not)
sensor_stats = {}
sensor_stats['temp_avg'] = sum(temperature_readings) / len(temperature_readings)
sensor_stats['humidity_max'] = max(humidity_readings)
sensor_stats['pressure_trend'] = pressure_readings[-1] - pressure_readings[0]
sensor_stats['stability_index'] = abs(sensor_stats['pressure_trend']) + 0.5 * sensor_stats['humidity_max']

# Unrelated environmental index calculation - red herring
carbon_index = 0.3 * sensor_stats['temp_avg'] + 0.7 * sensor_stats['humidity_max']
environmental_risk = 'Low' if carbon_index < 40 else 'High'

# Core system health diagnostics (partially relevant)
system_load = (85, 90, 78, 92)  # CPU usage percentages
disk_usage = {'system': 70, 'cache': 30, 'logs': 15}
active_processes = ['monitor', 'logger', 'scheduler', 'backup_agent', 'streamer']

# Decoy health check with misleading logic
def evaluate_stability(temp_data, threshold=24.0):
    above_threshold = [t for t in temp_data if t > threshold]
    return len(above_threshold) > 2

# Unused function - dead code path
def calculate_resilience_score(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val)**2 for x in data) / len(data)
    return 100 - math.sqrt(variance) * 2

# Real-time anomaly detection - partial relevance
anomalies_detected = 0
for i in range(len(temperature_readings)):
    if temperature_readings[i] > 24.0 and humidity_readings[i] < 46:
        anomalies_detected += 1

# Health state classification using tuple unpacking
status_codes = (200, 201, 503, 404)
ok_codes, warning_codes, error_codes = [], [], []
for code in status_codes:
    if code < 300:
        ok_codes.append(code)
    elif code < 500:
        warning_codes.append(code)
    else:
        error_codes.append(code)

# System status dictionary with multiple health indicators
system_status = {
    'core_health': 86,
    'subsystem_1': 77,
    'subsystem_2': 73,
    'uptime_hours': 1274,
    'anomaly_count': anomalies_detected,
    'load_balance': sum(system_load) / len(system_load)
}

# Bitwise diagnostic flag setup - mixed relevance
base_flag = 0b1010
extended_diagnostics = base_flag | 0b0101
extended_diagnostics ^= 0b1111  # Toggle bits
health_flag = extended_diagnostics & 0b0011

# Modular arithmetic for cyclic health check (relevant only in part)
cycle_position = (len(active_processes) * 3) % 7
if cycle_position in [1, 3, 5]:
    cycle_risk = 10
else:
    cycle_risk = 5

# Primary health factor computation - depends on several conditions
if system_status['core_health'] >= 80 and not error_codes:
    base_multiplier = 1.2
elif system_status['core_health'] >= 70:
    base_multiplier = 1.0
else:
    base_multiplier = 0.7

# Secondary adjustment based on decoy index
if environmental_risk == 'High':
    risk_penalty = 0.9
else:
    risk_penalty = 1.0

# Tertiary factor from bit flag
flag_boost = 1.1 if health_flag == 0b0010 else 0.95

# Final health factor with combined influences
health_factor = base_multiplier * risk_penalty * flag_boost

# Critical statement: core health multiplied by adjusted factor
final_diagnostic = system_status.get('core_health', 0) * health_factor

# Distractor print (not the target)
# print(f"System report: {sensor_stats}")

# Target result output
print(f"Result: {final_diagnostic}")