from collections import defaultdict, Counter
import itertools

# Simulated sensor array data (temperature, pressure, vibration)
sensor_logs = [
    (72.3, 85.1, 12), (75.1, 86.0, 14), (70.0, 83.5, 11),
    (95.5, 90.2, 25), (68.9, 82.0, 10), (74.3, 85.8, 13),
    (105.7, 95.6, 35), (71.0, 84.3, 12), (73.8, 85.9, 15),
    (110.0, 98.1, 40), (69.5, 81.9, 9)
]

# Irrelevant mapping: model version to firmware
firmware_map = {
    'A1': 'v2.1', 'B2': 'v2.3', 'C3': 'v3.0',
    'D4': 'v3.1', 'E5': 'v3.2'
}

# Decoy function: appears useful but unused
def validate_calibration(sequence):
    return all(abs(seq - 75.0) < 15 for seq in [s[0] for s in sequence])

# Misleading intermediate calculation
rolling_avg = sum([log[1] for log in sensor_logs]) / len(sensor_logs)  # Pressure average
adjusted_offsets = [abs(log[0] - 75.0) * 0.8 for log in sensor_logs]

# Real processing begins here
operational_limits = {
    'temp_threshold': 100.0,
    'pressure_buffer': 90.0,
    'vibration_cap': 30
}

# Distractor: complex but unused data transformation
critical_flags = []
for i, entry in enumerate(sensor_logs):
    if entry[0] > operational_limits['temp_threshold'] and entry[2] > 20:
        critical_flags.append((i, 'HIGH_TEMP_VIB'))
    elif entry[1] > operational_limits['pressure_buffer']:
        critical_flags.append((i, 'HIGH_PRESSURE'))

# Unused recursive helper
def count_anomalies(logs, index=0, acc=None):
    if acc is None:
        acc = 0
    if index >= len(logs):
        return acc
    temp, press, vib = logs[index]
    if temp > 102 or vib > 32:
        return count_anomalies(logs, index + 1, acc + 1)
    return count_anomalies(logs, index + 1, acc)

# Real filtering logic
exceedance_counts = defaultdict(int)
for temp, press, vib in sensor_logs:
    if temp > operational_limits['temp_threshold']:
        exceedance_counts['temp'] += 1
    if press > operational_limits['pressure_buffer']:
        exceedance_counts['pressure'] += 1
    if vib > operational_limits['vibration_cap']:
        exceedance_counts['vibration'] += 1

# Generate threshold map using modular arithmetic and bit shifting (red herring)
base_key = 7
threshold_map = {}
for k, v in operational_limits.items():
    shifted = (int(v) >> 2) + (base_key * (base_key + 1)) // 2
    threshold_map[k] = shifted * 0.75

# Filtering relevant entries based on composite condition
filtered_data = []
decoys = []
for idx, (t, p, v) in enumerate(sensor_logs):
    # Actual filter: high vibration OR extreme temp
    if v > 20 or t > 100:
        filtered_data.append((idx, t, p, v, t * p * 0.01))
    else:
        decoys.append((idx, t))

# Another distraction: unused permutation analysis
perm_count = 0
for perm in itertools.permutations([x[2] for x in filtered_data], min(3, len(filtered_data))):
    if len(perm) == 3 and perm[0] < perm[1] < perm[2]:
        perm_count += 1

# Core processing function with multiple concepts
def process_readings(readings, thresholds):
    # Use of Counter for frequency analysis
    severity_levels = Counter()
    total_impact = 0.0
    temp_score = 0
    pressure_score = 0
    
    # Nested logic with distractors
    for item in readings:
        idx, t, p, v, impact = item
        total_impact += impact
        
        # Real scoring
        if t > thresholds['temp_threshold']:
            severity_levels['overheat'] += 1
            temp_score += int(t - 90)
        
        if p > thresholds['pressure_buffer']:
            severity_levels['overpressurized'] += 1
            pressure_score += int(p - 85)
        
        # Red herring: irrelevant bitwise check
        flag_code = v ^ 32
        if flag_code & 8:
            continue  # Meant to distract
    
    # Distractor: unused product
    combo_product = 1
    for val in severity_levels.values():
        combo_product *= (val + 1)
    
    # Real result computation
    base_diagnostic = temp_score * 2 + pressure_score
    adjustment_factor = len(readings) % 7
    
    # Final deterministic result
    final_diagnostic = base_diagnostic - adjustment_factor
    
    # Additional misleading path
    if combo_product > 100:
        final_diagnostic += 50  # Never reached due to data
    
    return int(final_diagnostic)

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")