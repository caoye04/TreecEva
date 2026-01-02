def preprocess_readings(raw_readings):
    processed = []
    scaling_factor = 1.75
    offset = -0.25
    for idx, val in enumerate(raw_readings):
        adjusted = val * scaling_factor + offset
        if adjusted < 0:
            adjusted = 0
        processed.append(round(adjusted, 3))
    return processed

# Irrelevant auxiliary function (dead code path)
def legacy_calibrate(x):
    return (x * 0.9) + 0.1

# Unused transformation matrix
decoy_matrix = [[i * j + 2 for j in range(3)] for i in range(3)]

# Simulated system sensor readings (raw)
sensor_readings = [0.45, 0.68, 0.33, 0.77, 0.52]

# Preprocess the sensor data
cleaned_readings = preprocess_readings(sensor_readings)

# Spurious intermediate calculation (distractor)
temp_aggregate = sum([x ** 0.5 for x in cleaned_readings if x > 0.5])

# Define diagnostic thresholds
thresholds = {
    'normal': (0.0, 0.6),
    'elevated': (0.6, 0.8),
    'critical': (0.8, float('inf'))
}

# System status mapping
status_codes = {'A': 'active', 'S': 'standby', 'F': 'fault'}

# Simulated system operational data
system_data = [
    {'id': 'SYS001', 'metric': cleaned_readings[0], 'mode': 'A'},
    {'id': 'SYS002', 'metric': cleaned_readings[1], 'mode': 'A'},
    {'id': 'SYS003', 'metric': cleaned_readings[2], 'mode': 'S'},
    {'id': 'SYS004', 'metric': cleaned_readings[3], 'mode': 'A'},
    {'id': 'SYS005', 'metric': cleaned_readings[4], 'mode': 'F'}
]

# Auxiliary lookup (partially used)
mode_weights = {'A': 1.0, 'S': 0.3, 'F': 0.0}

# Misleading normalization attempt (unused)
bogus_norm = [round((x - min(cleaned_readings)) / (max(cleaned_readings) - min(cleaned_readings) + 1e-8), 3) 
               for x in cleaned_readings]

# Core analysis function
def analyze_metrics(data_entries, limits):
    category_counts = {'normal': 0, 'elevated': 0, 'critical': 0}
    weighted_sum = 0.0
    valid_modes = ['A', 'S']  # Only active and standby contribute

    for index, entry in enumerate(data_entries):
        val = entry['metric']
        mode = entry['mode']
        weight = mode_weights.get(mode, 0.0)

        # Determine health category
        if val < limits['normal'][1]:
            cat = 'normal'
        elif val < limits['elevated'][1]:
            cat = 'elevated'
        else:
            cat = 'critical'
        category_counts[cat] += 1

        # Accumulate only if mode is valid
        if mode in valid_modes:
            weighted_sum += val * weight * (index + 1)  # Position-weighted

    # Compute composite score
    base_score = category_counts['elevated'] * 10 + category_counts['critical'] * 25
    adjustment = round(weighted_sum * 0.85, 3)
    
    # Hidden logic: final result depends on parity of elevated count
    if category_counts['elevated'] % 2 == 1:
        final_score = base_score - adjustment
    else:
        final_score = base_score + adjustment

    # Secondary distractor computation (never used)
    decoy_ratio = len([x for x in data_entries if x['metric'] > 0.6]) / (len(data_entries) or 1)

    return int(round(final_score))

# Execute main analysis
final_diagnostic = analyze_metrics(system_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")