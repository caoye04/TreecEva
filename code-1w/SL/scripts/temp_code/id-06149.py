from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data_stream = [
    ('temp', '23.4', 'C'), ('humidity', '45', '%'), ('temp', '25.1', 'C'),
    ('pressure', '1013.2', 'hPa'), ('temp', 'noise', 'C'), ('humidity', '50', '%'),
    ('temp', '24.8', 'C'), ('co2', '415', 'ppm'), ('humidity', 'invalid', '%'),
    ('temp', '22.9', 'C'), ('pressure', '1012.7', 'hPa'), ('temp', '26.3', 'C')
]

# Irrelevant calibration map (distractor)
calibration_offsets = {
    'temp': 0.2,
    'humidity': -1.5,
    'pressure': 0.05,
    'co2': 5
}

# Misleading intermediate transformation (dead path)
def apply_calibration(data):
    return [(t, float(v) + calibration_offsets.get(t, 0), u) for t, v, u in data if v.replace('.', '').isdigit()]

# Unused but plausible function (red herring)
def validate_readings(raw_data):
    valid_types = {'temp', 'humidity', 'pressure', 'co2'}
    errors = 0
    for typ, val, unit in raw_data:
        if typ not in valid_types or not isinstance(val, str):
            errors += 1
    return errors == 0

# Core processing pipeline
sensor_cache = defaultdict(list)
error_log = []
total_entries = 0

for sensor_type, value_str, unit in data_stream:
    total_entries += 1
    if sensor_type == 'temp' and value_str.replace('.', '').isdigit():
        try:
            temp_c = float(value_str)
            if 15 <= temp_c <= 35:
                sensor_cache['temp_raw'].append(temp_c)
            else:
                error_log.append(f'Out-of-range temperature: {temp_c}')
        except ValueError:
            error_log.append(f'Invalid temp value: {value_str}')
    elif sensor_type == 'humidity' and value_str.isdigit():
        humidity_val = int(value_str)
        if 30 <= humidity_val <= 70:
            sensor_cache['humidity_raw'].append(humidity_val)
        else:
            error_log.append(f'Extreme humidity: {humidity_val}%')

# Decoy statistical summary (irrelevant)
raw_stats = {}
if sensor_cache['temp_raw']:
    temps = sensor_cache['temp_raw']
    raw_stats['temp_avg'] = sum(temps) / len(temps)
    raw_stats['temp_peak'] = max(temps)
    raw_stats['temp_var'] = sum((x - raw_stats['temp_avg'])**2 for x in temps) / len(temps)

# String-based filtering logic (uses string methods)
diagnostic_flags = []
for entry in data_stream:
    sensor_name = entry[0]
    raw_value = entry[1]
    if 'temp' in sensor_name and raw_value.replace('.', '').isdigit():
        # Simulated fault pattern detection via string shape
        sig_digits = raw_value.split('.')[1] if '.' in raw_value else ''
        if len(sig_digits) >= 2 and sig_digits[-1] == '1':
            diagnostic_flags.append('PRECISION_ALERT')

# Real signal extraction (hidden in noise)
filtered_data = []
for val in sensor_cache['temp_raw']:
    # Apply non-linear correction (bit manipulation twist)
    binary_rep = bin(int(val * 100))
    flipped = int(binary_rep[:-2] + ('0' if binary_rep[-1] == '1' else '1'), 2)
    corrected = flipped / 100.0
    filtered_data.append(corrected)

# Threshold logic with multiple concepts
threshold_map = defaultdict(lambda: 0.0)
threshold_map.update({
    'baseline': 24.0,
    'hysteresis': 1.5,
    'decay_factor': 0.95
})

# Critical function with mixed paradigms
def process_readings(readings, config):
    if not readings:
        return -999.0
    
    # Sort and find central tendency
    sorted_vals = sorted(readings)
    median_idx = len(sorted_vals) // 2
    median_val = (sorted_vals[median_idx] + sorted_vals[~median_idx]) / 2
    
    # Weighted history simulation
    weighted_sum = 0.0
    decay = 1.0
    for i, val in enumerate(reversed(readings)):
        weighted_sum += val * decay
        decay *= config['decay_factor']
    
    historical_trend = weighted_sum / (len(readings) * 0.5 + 1)
    
    # Boolean logic chain with short-circuiting
    is_stable = len(readings) > 3 and (
        max(sorted_vals) - min(sorted_vals) < config['hysteresis'] * 2
    )
    
    # Final decision with case conversion distraction
    status_msg = "NORMAL" if is_stable else "FLUCTUATING"
    priority_code = len(status_msg.lower().replace("", ""))  # always 6 or 11 - red herring
    
    # Actual answer computation (obscured)
    baseline_delta = abs(median_val - config['baseline'])
    adjustment = math.copysign(1, median_val - config['baseline']) * math.log(
        abs(historical_trend - config['baseline']) + 1
    )
    
    final_score = (median_val + historical_trend + adjustment) / 3
    
    # Key assignment point
    final_diagnostic = round(final_score * 100) / 100
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")