from collections import defaultdict, Counter
import math

# Simulated sensor log: (timestamp, temp_c, status_flag)
sensor_log = [
    (1001, 23.1, 'OK'), (1002, 24.5, 'OK'), (1003, -999, 'ERR'),
    (1004, 25.3, 'OK'), (1005, 26.0, 'OK'), (1006, 24.8, 'OK'),
    (1007, -999, 'ERR'), (1008, 27.1, 'OK'), (1009, 27.5, 'OK')
]

# System configuration flags
system_flags = {
    'overclock': False,
    'eco_mode': True,
    'debug_trace': True,
    'use_fahrenheit': False,
    'legacy_protocol': False
}

# Irrelevant telemetry accumulator (distractor)
cpu_telemetry = defaultdict(int)
for i in range(5):
    cpu_telemetry[f'core_{i}'] += (i ** 3) % 7

# Preprocess logs: filter errors and extract valid temps
def clean_sensor_data(logs):
    valid_temps = []
    error_count = 0
    for ts, temp, flag in logs:
        if temp != -999 and flag == 'OK':
            valid_temps.append(temp)
        else:
            error_count += 1
    # Red herring: return unused error count
    return valid_temps, error_count * 1000  

# Secondary processing: apply calibration curve
def apply_calibration(temps):
    calibrated = []
    for t in temps:
        # Real transformation
        corrected = t * 0.98 + 0.5
        calibrated.append(corrected)
    # Decoy smoothing (unused)
    smoothed = [calibrated[0]]
    for i in range(1, len(calibrated)):
        smoothed.append((smoothed[-1] + calibrated[i]) / 2)
    return calibrated  # Only calibrated used

# Analyze trend direction (distractor function)
def assess_trend(temps):
    if len(temps) < 2:
        return 'STABLE'
    changes = [temps[i] - temps[i-1] for i in range(1, len(temps))]
    avg_change = sum(changes) / len(changes)
    return 'WARMING' if avg_change > 0.1 else 'COOLING' if avg_change < -0.1 else 'STABLE'

# Main calculation with bit manipulation red herring
def calculate_thermal_response(logs, config):
    # Step 1: Clean data
    temperatures, _ = clean_sensor_data(logs)
    
    # Step 2: Apply physical calibration
    calibrated_temps = apply_calibration(temperatures)
    
    # Step 3: Compute entropy-like metric (real path)
    rounded_vals = [int(t * 10) for t in calibrated_temps]
    freq = Counter(rounded_vals)
    total = len(rounded_vals)
    shannon = sum(-(f/total) * math.log(f/total) for f in freq.values())
    
    # Distractor: Bitwise analysis of config (never affects result)
    flag_state = 0
    if config['overclock']:
        flag_state |= 1 << 3
    if config['eco_mode']:
        flag_state ^= (1 << 5)  # Toggle bit
    if config['debug_trace']:
        flag_state &= ~(1 << 1)  # Clear bit
    mask_result = flag_state & 0b11111  # Computed but unused
    
    # Step 4: Final capacity model
    base_energy = sum(calibrated_temps)
    penalty = len(calibrated_temps) if config['legacy_protocol'] else 0
    thermal_factor = base_energy / (shannon + 1e-8)
    
    # Critical statement
    thermal_capacity = int(thermal_factor) - penalty
    
    # Dead code path (never reached)
    if thermal_capacity < 0:
        thermal_capacity = abs(thermal_capacity) << 2
    
    return thermal_capacity

# Execute main logic
log_entries = sensor_log
thermal_capacity = calculate_thermal_response(log_entries, system_flags)

# Print result as required
print(f"Result: {thermal_capacity}")