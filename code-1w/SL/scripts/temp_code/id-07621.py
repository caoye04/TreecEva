def analyze_sensor(signal_str):
    """Misleading function: appears relevant but unused in final computation."""
    if 'ERR' in signal_str:
        return -1
    parts = signal_str.split(':')
    values = [int(p) for p in parts if p.isdigit()]
    return sum(values) // len(values) if values else 0

# Irrelevant sensor simulation data
temp_log = ['T1:23', 'T2:25', 'T3:24', 'T4:ERR', 'T5:26']
humidity_codes = ['H7:45', 'H8:50', 'H9:47']

# Real processing begins here
raw_readings = [1892, 2001, 1750, 2100, 1950, 1600, 2200]
scaling_factor = 0.85
adjusted_readings = [int(x * scaling_factor) for x in raw_readings]

# Decoy transformation chain
def transform(x):
    return (x >> 2) ^ 37

obfuscated = list(map(transform, adjusted_readings))  # Dead path

# Threshold logic with red herring conditions
baseline = 1700
threshold_level = baseline * 0.9 + 50  # Evaluates to 1580 + 50 = 1630

# Filtering valid readings
valid_sensors = []
for val in adjusted_readings:
    if val > threshold_level and val % 2 == 0:
        valid_sensors.append(val)
    elif val == threshold_level:
        valid_sensors.append(val * 2)

# Linear search for calibration marker (misdirection)
search_space = list(range(100, 3000, 199))
marker_found = False
for idx, num in enumerate(search_space):
    if num == sum(valid_sensors[:2]) // 100:
        marker_found = True
        break

# Core data structure manipulation
collected_data = {
    'readings': valid_sensors,
    'meta': {
        'device_id': 'DSU-PROD-09',
        'version': 'v2.1-beta',
        'checksum': hash('v2.1-beta') % 1000
    }
}

# String-based control flag (uses string method)
status_line = 'CALIBRATION STATUS: VERIFIED AND LOCKED'
if status_line.lower().find('verified') != -1 and 'locked' in status_line.casefold():
    collected_data['calibrated'] = True

# Actual processing function used
def process_readings(data_dict, limit):
    readings = data_dict['readings']
    total = 0
    count = 0
    for r in readings:
        if r > limit * 1.05:
            total += r // 100  # Integer division and rounding effect
            count += 1
    if count == 0:
        return -999
    avg_segment = total / count  # Decimal result possible
    
    # Secondary filter based on bit properties
    binary_ones = sum(bin(r)[2:].count('1') for r in readings)
    if binary_ones > 50:
        adjustment = 2.5
    else:
        adjustment = 1.2
    
    return avg_segment * adjustment

# Critical execution point
final_diagnostic = process_readings(collected_data, threshold_level)

# Output required format
print(f"Result: {final_diagnostic}")