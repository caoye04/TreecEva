def analyze_component(reading, threshold=75):
    if reading > threshold:
        return (reading - threshold) * 1.5
    else:
        return max(0, (threshold - reading) // 5)

# Irrelevant sensor calibration data (distractor)
sensor_offsets = {'A': 2.1, 'B': -1.3, 'C': 0.7}
diagnostic_codes = [0x1A, 0x2F, 0x3C]

# Real metric data
temperature_readings = [80, 65, 90, 70]
humidity_readings = [60, 85, 75, 95]
pressure_readings = [1013, 1020, 1005, 1030]

# Misleading transformation (unused path)
def transform(x):
    return (x << 2) ^ 5

# Unused helper function (dead code)
def validate_input(data):
    return all(isinstance(x, int) for x in data)

# Process relevant metrics
raw_temp_score = sum(analyze_component(t) for t in temperature_readings)
raw_humid_score = sum(analyze_component(h, 70) for h in humidity_readings)

# Distraction: complex bit manipulation with no effect
obfuscated_key = (0b11010 ^ 0b10110) << 3
lookup_table = {i: (i * i) ^ obfuscated_key for i in range(5)}

# Unused set operations (distractor)
available_sensors = {'temp', 'humid', 'press'}
active_sensors = {'temp', 'humid'}
redundant_sensors = available_sensors - active_sensors

# Primary metric dictionary
metrics = {
    'thermal': raw_temp_score,
    'moisture': raw_humid_score,
    'vibration': 42,  # Placeholder - not processed
    'power_cycle': sum(p % 100 for p in pressure_readings)
}

# Weight mapping with decoy entries
weights = {
    'thermal': 0.35,
    'moisture': 0.45,
    'calibration': 0.05,  # Unused weight
    'redundancy': 0.0,    # Dead weight
    'vibration': 0.15     # Included but metric not properly transformed
}

# Secondary distraction: tuple unpacking with irrelevant use
calib_data = (23.5, 17.2, 41.8)
base, offset, _ = calib_data
adjustment_factor = base / (offset or 1)

# Main evaluation logic
def evaluate_performance(met, wts):
    total = 0.0
    applied_weights = 0.0
    
    # Deliberately skip 'vibration' despite its presence
    for key in ['thermal', 'moisture', 'power_cycle']:
        if key in met and key in wts:
            contribution = met[key] * wts[key]
            total += contribution
            applied_weights += wts[key]
    
    # Normalize by actual applied weights (not total defined)
    if applied_weights > 0:
        total /= applied_weights
    
    # Final adjustment based on hidden rule
    if met['thermal'] > 50:
        total += 10  # Bonus for high thermal deviation
    
    return int(total)

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")