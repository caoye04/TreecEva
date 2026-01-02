from itertools import compress, cycle
import math

# Simulated sensor array data (temperature, pressure, humidity)
sensor_data = [
    (23.4, 101.3, 45.2), (24.1, 102.0, 43.8), (19.8, 99.7, 51.0),
    (35.6, 103.4, 33.1), (28.0, 100.1, 39.5), (22.5, 101.8, 47.3),
    (31.2, 102.9, 36.0), (18.9, 98.4, 52.7), (26.8, 100.9, 40.8),
    (33.3, 104.2, 34.9)
]

# Calibration coefficients (irrelevant for final result but looks important)
baseline_calib = { 'temp_offset': 0.8, 'pressure_gain': 1.02, 'humidity_nonlinear': 0.05 }

# Threshold configuration for anomaly detection (used in filtering)
threshold_map = {
    'temp_high': 30.0,
    'temp_low': 20.0,
    'pressure_normal': (100.0, 103.0),
    'humidity_range': 40.0
}

# Auxiliary diagnostic flags (distractor - never used again)
diag_flags = [True, False, True, True, False]
flag_cycle = cycle(diag_flags)  # Dead usage: iterator created but not consumed

# Precompute some red herring statistics
herring_stats = []
for i, entry in enumerate(sensor_data):
    temp, press, hum = entry
    # Complex-looking but irrelevant computation chain
    adjusted_temp = temp + baseline_calib['temp_offset']
    normalized_press = press * baseline_calib['pressure_gain']
    nonlinear_hum = hum + baseline_calib['humidity_nonlinear'] * (hum ** 1.5)  # Looks advanced
    score = (adjusted_temp * 0.3) + (normalized_press * 0.2) - nonlinear_hum  # Fake health score
    herring_stats.append((i, score, math.tanh(score)))  # Stored but never used

# Actual processing path begins here
valid_indices = []
critical_count = 0
entry_status = []

for idx, (t, p, h) in enumerate(sensor_data):
    temp_flag = False
    if t > threshold_map['temp_high']:
        temp_flag = True
        critical_count += 1
    elif t < threshold_map['temp_low']:
        temp_flag = True
    
    press_min, press_max = threshold_map['pressure_normal']
    pressure_flag = not (press_min <= p <= press_max)
    
    humidity_flag = h < threshold_map['humidity_range']
    
    # Only entries with temperature anomaly AND low humidity are selected
    if temp_flag and humidity_flag:
        valid_indices.append(idx)
    
    # Another distractor: complex status string not used later
    status_str = f"{'CRIT' if temp_flag else 'NORM'}-{p:.1f}-{h:.1f}"
    entry_status.append(status_str)

# Filter data using valid indices
filtered_data = [sensor_data[i] for i in valid_indices]

# Decoy function that appears relevant but is unused
def analyze_trend(data_seq):
    if len(data_seq) < 2:
        return 0.0
    diffs = [data_seq[i+1][0] - data_seq[i][0] for i in range(len(data_seq)-1)]
    return sum(diffs) / len(diffs)

# Real processing function
def process_readings(readings, config):
    if not readings:
        return -999.0
    
    # Extract temperatures from filtered readings
    temps = [r[0] for r in readings]
    pressures = [r[1] for r in readings]
    
    # Compute mean temperature
    mean_temp = sum(temps) / len(temps)
    
    # Apply artificial correction based on pressure median (unnecessary but plausible)
    sorted_press = sorted(pressures)
    n = len(sorted_press)
    mid = n // 2
    median_pressure = (sorted_press[mid] + sorted_press[-(mid+1)]) / 2
    
    # Correction factor: only applies if median pressure > 102.5
    correction = 0.0
    if median_pressure > 102.5:
        # Use itertools.compress to select high-temp readings for adjustment
        high_temp_mask = [t > mean_temp for t in temps]
        high_temps = list(compress(temps, high_temp_mask))
        if high_temps:
            correction = sum(high_temps) / len(high_temps) * 0.1
    
    # Final diagnostic is mean temperature minus correction
    result = mean_temp - correction
    
    # Distractor: create a dictionary that looks important
    summary = {
        'sample_count': len(readings),
        'raw_mean': mean_temp,
        'pressure_median': median_pressure,
        'correction_applied': correction,
        'timestamp': '2023-11-05T10:30:00Z',  # Fake metadata
        'result': result
    }
    
    return summary['result']

# Execute main logic
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")