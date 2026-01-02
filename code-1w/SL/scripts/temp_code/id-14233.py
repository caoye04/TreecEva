import math

# Simulated sensor array diagnostics
sensor_ids = ['S01', 'S02', 'S03', 'S04', 'S05']
timestamps = [1623456000, 1623456060, 1623456120, 1623456180, 1623456240]

# Raw diagnostic readings (mixture of temperature, pressure, vibration)
raw_readings = [
    {'type': 'temp', 'val': 98.6, 'err': 0.1, 'active': True},
    {'type': 'pressure', 'val': 101.3, 'err': 0.5, 'active': True},
    {'type': 'vibe', 'val': 45.2, 'err': 2.3, 'active': False},
    {'type': 'temp', 'val': 97.1, 'err': 0.2, 'active': True},
    {'type': 'pressure', 'val': 102.8, 'err': 0.4, 'active': True}
]

# Irrelevant calibration lookup (distractor)
calibration_map = {sid: 1.0 + 0.01 * i for i, sid in enumerate(sensor_ids)}
calibration_sum = sum(calibration_map.values())  # unused

# Misleading transformation chain
transformed = []
for r in raw_readings:
    if r['type'] == 'temp':
        transformed.append(r['val'] * 1.8 + 32)  # to Fahrenheit (unused path)
    elif r['type'] == 'pressure':
        transformed.append(r['val'] / 10)  # kPa to bar (unused)

# Dead code path: complex filtering that's not used
redundant_filter = [x for x in raw_readings if x['err'] < 1.0 and x['active']]
dropped_count = len(raw_readings) - len(redundant_filter)  # irrelevant metric

# Real processing begins here
valid_types = {'temp', 'pressure'}
quality_offset = 0.0

# Primary filter: only active sensors with valid types
filtered_metrics = [
    r for r in raw_readings 
    if r['active'] and r['type'] in valid_types
]

# Compute aggregate baseline (only temp and pressure, active ones)
total_weighted = 0.0
weight_sum = 0.0

for reading in filtered_metrics:
    if reading['type'] == 'temp':
        weight = 0.7
    else:
        weight = 0.3
    total_weighted += reading['val'] * weight
    weight_sum += weight

baseline = total_weighted / weight_sum if weight_sum > 0 else 0

# Secondary adjustment based on error distribution
total_error = sum(r['err'] for r in filtered_metrics)
adjustment_factor = math.log(1 + total_error) if total_error > 0 else 0

# Simulate hardware degradation effect (bit manipulation red herring)
device_status = 0b1101
mask_correction = (device_status & 0b1010) >> 1  # looks important but unused

# Decoy function that's defined but not called
def compute_health_score(metrics):
    score = 100
    for m in metrics:
        score -= m['err'] * 5
    return max(score, 0)

# Real analysis function
def analyze_readings(metrics):
    if not metrics:
        return -1
    
    # Extract values and classify
    temps = [m['val'] for m in metrics if m['type'] == 'temp']
    pressures = [m['val'] for m in metrics if m['type'] == 'pressure']
    
    temp_avg = sum(temps) / len(temps) if temps else 0
    press_avg = sum(pressures) / len(pressures) if pressures else 0
    
    # Complex interaction formula
    if temp_avg > 98.0:
        if press_avg > 102.0:
            diagnostic_code = 3
        else:
            diagnostic_code = 2
    else:
        diagnostic_code = 1
    
    # Final computation with decimal precision
    base_value = temp_avg * 0.6 + press_avg * 0.4
    final_score = base_value + (diagnostic_code * adjustment_factor)
    
    # Additional distraction: unused list slicing
    history_window = timestamps[-3:]
    recent_avg = sum(history_window) / len(history_window)  # unused
    
    return round(final_score, 6)

# Key assignment
final_diagnostic = analyze_readings(filtered_metrics)

# Output result
print(f"Result: {final_diagnostic}")