import math

# Simulated sensor array with diagnostic flags
def analyze_sensors(raw_readings):
    processed = {}
    for key, val in raw_readings.items():
        if 'temp' in key:
            processed[key] = (val - 32) * 5 / 9  # F to C
        elif 'pressure' in key:
            processed[key] = val * 0.145038  # kPa to psi
        else:
            processed[key] = val * 1.0
    return processed

# Irrelevant auxiliary function – dead code path
def compute_orbit_decay(t, drag_coeff=0.02):
    return (t ** 2) * math.exp(-drag_coeff * t)

# Core system diagnostics
system_status = {
    'health': 0,
    'nodes_active': 0,
    'last_sync': None,
    'version': '3.7.1'
}

# Simulated hardware readings (Fahrenheit, kPa, arbitrary units)
sensor_data = {
    'temp_engine': 212.0,
    'temp_coolant': 185.0,
    'pressure_fuel': 3447.38,
    'vibration_x': 0.023,
    'vibration_y': 0.018,
    'flow_rate': 127
}

# Misleading intermediate transformation chain
normalized = analyze_sensors(sensor_data)
calibration_map = {k: abs(math.sin(v)) + 1 for k, v in normalized.items()}
aggregate_score = sum(calibration_map.values()) / len(calibration_map)

# Red herring: complex but unused calculation
entropy = 0
for x in [0.1, 0.3, 0.4, 0.2]:
    if x > 0:
        entropy -= x * math.log(x)
adjusted_entropy = entropy * 100 // 1

# Another decoy variable influenced by unrelated logic
sync_counter = 0
for i in range(50):
    sync_counter += (i * 2) % 7
    if sync_counter > 100:
        break

# Actual health computation buried in distractions
temp_celsius_avg = (normalized['temp_engine'] + normalized['temp_coolant']) / 2
deviation = abs(temp_celsius_avg - 100.0)

if deviation < 2.0:
    system_status['health'] = 85
elif deviation < 10.0:
    system_status['health'] = 60
else:
    system_status['health'] = 30

# Node activation logic with multiple branches (some irrelevant)
nodes_configured = [True, True, False, True]
system_status['nodes_active'] = len([x for x in nodes_configured if x])

# Unused dictionary update – distractor
system_status.update({'diagnostics_run': 3})

# Key statement buried late in execution
baseline_ref = math.sqrt(2 * math.pi)
calibration_factor = round(baseline_ref, 2) * 2
final_diagnostic = system_status.get('health') * calibration_factor

# Output required format
print(f"Result: {final_diagnostic}")