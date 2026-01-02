import math

# Irrelevant sensor simulation data
def generate_noise(length):
    return [math.sin(i * 0.1) + math.cos(i * 0.3) for i in range(length)]

sensor_noise = generate_noise(100)
offset_correction = sum([abs(x) for x in sensor_noise[:10]]) * 0.05

# Data preprocessing pipeline
raw_readings = [18, 22, 19, 25, 30, 28, 20]
filter_threshold = 24
filtered_data = [x for x in raw_readings if x < filter_threshold]

# Decoy calibration function (never used)
def legacy_calibrate(x):
    return x * 1.8 + 32

# Signal mapping using dictionary and string operations
device_map = {
    'A1': 'sensor_thermal',
    'B2': 'sensor_pressure',
    'C3': 'sensor_humidity'
}

labels = ['A1', 'B2', 'C3']
label_codes = [code.lower().replace('_', '') for code in device_map.values()]

# Real processing begins here
scaling_factor = 3.7
adjusted_readings = [x * scaling_factor for x in filtered_data]

# String-based mode selection
operation_mode = 'CALIBRATE_HIGH_RES'
if operation_mode.startswith('CALIBRATE'):
    mode_value = len(operation_mode) - 8
else:
    mode_value = 1

# Intermediate transformation with distractor variables
buffer_cache = {}
duplicate_flag = False
for i, val in enumerate(adjusted_readings):
    key_str = f"entry_{i}"
    buffer_cache[key_str] = round(val ** 0.5, 4)
    if buffer_cache[key_str] in adjusted_readings:
        duplicate_flag = True

interim_list = list(buffer_cache.values())
smoothed_data = [x for x in interim_list if x > 4.0]

# Aggregation with misleading sum components
total_power = sum([x * 2 for x in sensor_noise[:len(raw_readings)]])  # red herring
baseline_reference = offset_correction * 12.4  # irrelevant

processed_data = sum(smoothed_data) + mode_value

# Finalization logic with dictionary lookup distraction
diagnostic_codes = {k: v.upper() for k, v in device_map.items()}
active_diagnostics = [diagnostic_codes[k] for k in diagnostic_codes.keys() if 'A' in k or 'C' in k]

def finalize_calibration(value):
    # Complex final adjustment with case conversion distraction
    temp_code = "ThErMaL_UnIt".swapcase()
    checksum = 0
    for char in temp_code:
        if char.islower():
            checksum += ord(char) % 10
    
    # Actual computation buried in noise
    base = value * 2.3
    adjustment = math.log(checksum + 1)  # small but non-zero
    return int(base + adjustment)

# Key execution point
thermal_capacity = finalize_calibration(processed_data)

# Dead code path - looks important but unused
if duplicate_flag:
    fallback_result = baseline_reference / (total_power + 1)
    thermal_capacity -= int(fallback_result)

print(f"Result: {thermal_capacity}")