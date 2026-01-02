import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 19.3, 20.1, 26.4, 27.8, 28.0, 24.7]
humidity_readings = [45, 48, 52, 58, 61, 54, 49, 53, 60, 65]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1009, 1014, 1016, 1018, 1020]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1']
version_history = {1: 'alpha', 2: 'beta', 3: 'rc'}

# Calibration factors (some are unused - red herring)
calibration = {
    'temp': 1.02,
    'humidity': 0.98,
    'pressure': 1.005,
    'light': 1.1  # Unused sensor
}

# Apply calibration to temperature (only temp used in final logic)
calibrated_temps = [t * calibration['temp'] for t in temperature_readings]

# Compute rolling average over 3 elements (with padding)
padded_temps = [calibrated_temps[0]] + calibrated_temps + [calibrated_temps[-1]]
rolling_avg = [
    (padded_temps[i] + padded_temps[i+1] + padded_temps[i+2]) / 3
    for i in range(len(calibrated_temps))
]

# Extract peak analysis (distractor computation)
peaks = []
for i in range(1, len(calibrated_temps)-1):
    if calibrated_temps[i] > calibrated_temps[i-1] and calibrated_temps[i] > calibrated_temps[i+1]:
        peaks.append((i, calibrated_temps[i]))

# Thresholds for anomaly detection (used later)
threshold_map = {
    'high_risk': 26.0,
    'moderate_risk': 24.0,
    'low_risk': 22.0
}

# Humidity-based filtering (irrelevant to final result but looks important)
normal_humidity_range = [40, 60]
filtered_by_humidity = [
    i for i in range(len(humidity_readings)) 
    if normal_humidity_range[0] <= humidity_readings[i] <= normal_humidity_range[1]
]

# Primary filtering based on calibrated temperature thresholds
risk_zones = []
for t in calibrated_temps:
    if t >= threshold_map['high_risk']:
        risk_zones.append('high')
    elif t >= threshold_map['moderate_risk']:
        risk_zones.append('moderate')
    else:
        risk_zones.append('low')

# Generate zone codes (unused distractor)
zone_codes = [r[0].upper() + str(i) for i, r in enumerate(risk_zones)]

# Actual data pipeline: filter readings above moderate threshold
critical_indices = [i for i, r in enumerate(risk_zones) if r in ['high', 'moderate']]
filtered_data = [calibrated_temps[i] for i in critical_indices]

# Secondary transformation: apply logarithmic scaling to suppress high values
log_scaled = [math.log(x) for x in filtered_data if x > 0]

# Dummy transformation chain (dead path)
squared_deltas = []
for i in range(len(log_scaled) - 1):
    delta = log_scaled[i+1] - log_scaled[i]
    squared_deltas.append(delta ** 2)

# Real processing function
def process_readings(data_list, thresholds):
    # Local mapping independent of input thresholds (misleading parameter)
    local_map = {'base': 22.5, 'scale': 1.8}
    adjusted = [local_map['scale'] * (x - local_map['base']) for x in data_list]
    
    # Nested conditional accumulation
    accumulator = 0
    for val in adjusted:
        if val < 0:
            accumulator -= val / 2
        elif val == 0:
            accumulator += 1
        else:
            if val > 5:
                accumulator += math.sqrt(val)
            else:
                accumulator += val * 0.7
    
    # Final adjustment using bit manipulation (obscure but deterministic)
    int_part = int(abs(accumulator))
    fractional = accumulator - int_part
    # XOR integer part with length of original data as noise suppression
    obfuscated = int_part ^ len(data_list)
    return obfuscated + fractional

# Execute main processing step
final_diagnostic = process_readings(filtered_data, threshold_map)

# Irrelevant formatting output (never used)
report_header = "ENV_SCAN_2023"
footer_checksum = sum([ord(c) for c in report_header]) % 100

# Print final result as required
print(f"Result: {final_diagnostic}")