import math

# Simulated sensor data and diagnostic system with red herrings
def analyze_system_metrics(raw_data):
    processed = {}
    temp_buffer = []
    checksum = 0

    for k, v in raw_data.items():
        if 'sensor' in k:
            normalized = (v - 20) / 5
            temp_buffer.append(normalized)
            if v > 30:
                processed[f'high_{k}'] = normalized
        elif 'status' in k:
            processed[k] = bool(v)
        checksum += int(v)

    processed['checksum'] = checksum % 17
    return processed

# Irrelevant auxiliary function - dead code path
def legacy_compatibility_mode(data):
    transformation = {key[::-1]: val ** 0.5 for key, val in data.items() if isinstance(val, (int, float))}
    return transformation

# Main system diagnostics
system_readings = {
    'sensor_a': 45,
    'sensor_b': 38,
    'sensor_c': 22,
    'status_power': 1,
    'status_override': 0,
    'calibration_ref': 999,  # decoy value
    'version_id': 777          # irrelevant metadata
}

# Step 1: Process raw sensor inputs
intermediate = analyze_system_metrics(system_readings)

# Step 2: Compute derived health metrics
peak_load = max(intermediate.get('high_sensor_a', 0), intermediate.get('high_sensor_b', 0))
base_stability = 100 - (peak_load * 3)

# Step 3: Initialize complex diagnostic dictionary
system_status = {
    'core': 0,
    'aux': {},
    'flags': [],
    'history': []
}

# Step 4: Conditional core value assignment
if base_stability < 80:
    system_status['core'] = 6
    if intermediate['checksum'] > 5:
        system_status['core'] += 2
    else:
        system_status['core'] += 1
else:
    system_status['core'] = 3

# Step 5: Add misleading dictionary updates
system_status['aux']['temp_debug'] = sum(abs(x) for x in [1.5, -2.3, peak_load])
system_status['aux']['legacy_mode'] = legacy_compatibility_mode({'x': 16, 'y': 25})
system_status['flags'].append('DEBUG_ACTIVE')

# Step 6: Compute health factor using bit manipulation red herring
raw_code = 0b110101
shifted = (raw_code << 2) ^ 0b1010  # result: 54
health_factor = (shifted % 7) + 0.5  # yields 5.5

# Step 7: Update history with irrelevant string transformations
log_entry = f"ERR_{''.join([chr(ord(c)+1) for c in 'XYZ'])}"
system_status['history'].append(log_entry.lower())

# Step 8: Final diagnostic computation — KEY STATEMENT
final_diagnostic = system_status.get('core') * health_factor

# Step 9: Print result as required
print(f"Result: {final_diagnostic}")