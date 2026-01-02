import math

# Simulated sensor readings (temperature in Celsius, pressure in kPa)
sensor_readings = [
    {'temp': 23.5, 'pressure': 101.3, 'humidity': 45.2},
    {'temp': 25.1, 'pressure': 102.1, 'humidity': 43.8},
    {'temp': 22.7, 'pressure': 100.9, 'humidity': 47.1},
    {'temp': 26.3, 'pressure': 103.4, 'humidity': 42.5}
]

# Calibration data with polynomial coefficients and noise thresholds
calibration_data = {
    'poly_coefs': [0.87, -2.3, 4.1],  # f(x) = 0.87x² - 2.3x + 4.1
    'noise_floor': 0.05,
    'gain': 1.08,
    'baseline_offset': 0.93
}

# Irrelevant auxiliary data — red herring
maintenance_logs = [
    {'timestamp': '2023-05-01T10:00:00', 'action': 'clean_filter', 'status': 'OK'},
    {'timestamp': '2023-05-02T11:30:00', 'action': 'replace_sensor', 'status': 'WARNING'}
]

# Decoy function — never called but looks relevant
def analyze_maintenance(logs):
    return sum(1 for log in logs if 'WARNING' in log['status'])

# Unused transformation map — distractor
type_mapping = {
    'A': lambda x: x * 1.1,
    'B': lambda x: x * 0.95,
    'C': lambda x: x + 5
}

# Fake aggregation that looks important but unused
total_diagnostics = []
for reading in sensor_readings:
    diagnostic_value = (reading['temp'] * reading['pressure']) / (reading['humidity'] + 1)
    total_diagnostics.append(round(diagnostic_value, 3))

# Dummy sorting — irrelevant computation
total_diagnostics.sort(reverse=True)

# Real processing begins here

def apply_polynomial(x, coefs):
    return coefs[0] * x**2 + coefs[1] * x + coefs[2]


def correct_for_drift(temp, pressure, offset=0.93):
    # Simulates temperature-pressure compensation
    adjusted = (temp * 1.02) - (101.3 - pressure) * 0.15
    return adjusted + offset


def calculate_entropy(data_list):
    # Unused complex calculation — red herring
    probs = [d['humidity'] / sum(d['humidity'] for d in data_list) for d in data_list]
    return -sum(p * math.log(p) for p in probs if p > 0)

# Another decoy: bit manipulation on floats (converted via IEEE bits)
def float_to_bits(f):
    import struct
    return struct.unpack('>I', struct.pack('>f', f))[0]

def manipulate_calibration_bits(coefs):
    bits = [float_to_bits(c) for c in coefs]
    transformed = [b ^ 0xFFFF for b in bits]  # XOR with mask
    return [float_to_bits(c) & 0x7F_FF_FF_FF for c in coefs]  # Truncate sign bit

# Main calculation pipeline
def calculate_optimal_flow(readings, calib):
    cumulative = 0.0
    entropy_influence = 0.0  # Unused but calculated

    # Real logic starts
    poly = calib['poly_coefs']
    gain = calib['gain']
    baseline = calib['baseline_offset']
    floor = calib['noise_floor']

    # Step 1: Extract primary physical quantity — effective temperature
    temps = [r['temp'] for r in readings]
    pressures = [r['pressure'] for r in readings]

    # Step 2: Apply drift correction to each reading
    corrected_temps = [correct_for_drift(t, p, baseline) for t, p in zip(temps, pressures)]

    # Step 3: Apply polynomial calibration curve
    calibrated_values = [apply_polynomial(t, poly) for t in corrected_temps]

    # Step 4: Amplify signal
    amplified = [cv * gain for cv in calibrated_values]

    # Step 5: Filter out noise (simulated threshold)
    filtered = [val for val in amplified if abs(val - baseline) > floor]

    # Step 6: Compute geometric mean as stability measure
    product = 1.0
    for val in filtered:
        product *= val
    geo_mean = product ** (1.0 / len(filtered))

    # Step 7: Apply final adjustment using string-based key extraction (useless but plausible)
    config_key = 'baseline_offset'
    key_sum = sum(ord(c) for c in config_key) % 100  # Hash-like distraction
    adjustment_factor = 1 + (key_sum / 1000)  # e.g., 1.093

    # Step 8: Final flow rate calculation
    raw_flow = sum(filtered) / len(filtered)
    optimized_flow = raw_flow * adjustment_factor * math.cos(math.pi / 6)  # cos(30°) ≈ 0.866

    # Irrelevant entropy side-calculation (never used)
    entropy_influence = calculate_entropy(readings)

    # Dead code branch — looks like error handling but never triggers
    if any(r['humidity'] > 50 for r in readings):
        optimized_flow *= 0.9

    return round(optimized_flow, 6)

# Key execution point
optimized_flow_rate = calculate_optimal_flow(sensor_readings, calibration_data)

# Additional irrelevant slicing operation (on a string)
diagnostic_id = "FLOW_SENSOR_XYZ_2023"
segment = diagnostic_id[10:13]  # 'XYZ' — unused

# Print result as required
print(f"Result: {optimized_flow_rate}")