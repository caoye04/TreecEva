import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [45, 48, 52, 58, 61, 54, 49, 56]
pressure_readings = [1013, 1015, 1012, 1009, 1007, 1010, 1014, 1016]

# Irrelevant calibration coefficients (distractor)
calib_a, calib_b, calib_c = 0.987, 1.021, 0.893
offset_matrix = [[0.1, -0.2], [0.3, 0.05]]

# Preprocess: normalize and combine readings into data windows
def preprocess_sensors(temps, humids, pressures):
    normalized = []
    for i in range(len(temps)):
        norm_temp = (temps[i] - 20) / 10
        norm_humid = humids[i] / 100
        norm_pressure = (pressures[i] - 1000) / 100
        if i % 3 == 0:
            # Artificial spike correction (dead logic path)
            norm_temp *= 0.95
        window = {
            't': round(norm_temp, 3),
            'h': round(norm_humid, 3),
            'p': round(norm_pressure, 3),
            'idx': i
        }
        normalized.append(window)
    return normalized

# Unused function - red herring
def compute_entropy(data_list):
    entropy = 0.0
    for entry in data_list:
        for key in entry:
            if isinstance(entry[key], float) and entry[key] > 0:
                entropy -= entry[key] * math.log(entry[key])
    return round(entropy, 4)

# Decoy transformation using bit manipulation (irrelevant)
bitwise_salt = 0
for reading in temperature_readings[:4]:
    intval = int(reading * 10)
    bitwise_salt ^= (intval << 2) | (intval >> 1)

# Threshold configuration map for diagnostics
threshold_map = {
    'temp_norm': {'warn': 0.3, 'crit': 0.5},
    'humid_norm': {'warn': 0.5, 'crit': 0.7},
    'pressure_norm': {'warn': 0.8, 'crit': 1.0}
}

# Secondary diagnostic flags (misleading intermediate)
diag_flags = [False] * len(temperature_readings)
flag_counter = 0
for i, t in enumerate(temperature_readings):
    if t > 25 and humidity_readings[i] < 50:
        diag_flags[i] = True
        flag_counter += 1

# Actual processing pipeline
processed_data = preprocess_sensors(temperature_readings, humidity_readings, pressure_readings)

# Accumulation of anomaly scores (core relevant logic)
anomaly_accumulator = 0
false_alarm_risk = 0.0  # Distractor variable
suppressed_warnings = []  # Dead storage

# Main analysis engine
def analyze_readings(data_windows, thresholds):
    score = 0
    temp_violations = 0
    humid_violations = 0
    pressure_violations = 0

    for window in data_windows:
        t_val = window['t']
        h_val = window['h']
        p_val = window['p']

        # Real condition checks
        if t_val > thresholds['temp_norm']['crit']:
            temp_violations += 1
        elif t_val > thresholds['temp_norm']['warn']:
            score += 2

        if h_val > thresholds['humid_norm']['crit']:
            humid_violations += 1
        elif h_val > thresholds['humid_norm']['warn']:
            score += 1

        if p_val > thresholds['pressure_norm']['crit']:
            pressure_violations += 1
        elif p_val > thresholds['pressure_norm']['warn']:
            score += 3

        # Spurious logic branch (red herring)
        if window['idx'] % 4 == 0 and t_val < 0.5:
            nonlocal false_alarm_risk
            false_alarm_risk += 0.05

    # Core computation: combinatoric penalty based on violation counts
    combo_penalty = 0
    if temp_violations > 0 and humid_violations > 0:
        combo_penalty += 5 * (temp_violations + humid_violations)
    if pressure_violations >= 2:
        combo_penalty += 8

    # Final diagnostic includes accumulation and penalty
    final_score = score + combo_penalty

    # Additional irrelevant transformation
    binary_trace = bin(final_score ^ 255).count('1')
    adjusted = final_score * (1 + 0.1 * (binary_trace % 4))

    return int(round(adjusted))

# Execute main diagnostic
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")