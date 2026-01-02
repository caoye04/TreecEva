import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9, 22.5]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 54, 50, 47]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014, 1013]

# Irrelevant backup buffer (distractor)
backup_buffer = [0] * 100
for i in range(len(backup_buffer)):
    backup_buffer[i] = (i * 7 + 13) % 101

# Signal processing pipeline
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [x - mean_val for x in signal]

def compute_magnitude(signal):
    return math.sqrt(sum([x**2 for x in signal]))

def filter_outliers(signal, threshold=2.0):
    norm_sig = normalize_signal(signal)
    filtered = [signal[i] for i in range(len(signal)) if abs(norm_sig[i]) < threshold]
    return filtered if len(filtered) > 0 else signal[:]

# Dead function - never called (decoy)
def legacy_calibration(data):
    adjusted = []
    for x in data:
        if x > 100:
            adjusted.append(x * 0.9)
        elif x < 0:
            adjusted.append(x * 1.1)
        else:
            adjusted.append(x)
    return adjusted

# Unused transformation chain (red herring)
squared_humidity = [h**2 for h in humidity_readings]
double_filtered = filter_outliers(squared_humidity, 1.5)
shifted_pressure = [p - min(pressure_readings) for p in pressure_readings][::2]  # slicing

# Core processing steps
filtered_temp = filter_outliers(temperature_readings, 1.8)
normalized_temp = normalize_signal(filtered_temp)
energy_signature = compute_magnitude(normalized_temp)

# Secondary derived metrics (some irrelevant)
mean_humidity = sum(humidity_readings) / len(humidity_readings)
rising_trend_count = sum(1 for i in range(1, len(filtered_temp)) if filtered_temp[i] > filtered_temp[i-1])

temp_variance = sum([(x - sum(filtered_temp)/len(filtered_temp))**2 for x in filtered_temp]) / len(filtered_temp)
adjusted_variance = temp_variance * (0.95 if rising_trend_count > 3 else 1.05)

# Complex conditional with misleading branches
diagnostic_flag = ''
if energy_signature > 5.0:
    diagnostic_flag = 'HIGH_ACTIVITY'
    reference_point = normalized_temp[0]
    if reference_point < 0:
        energy_signature *= 1.1
elif len(filtered_temp) < len(temperature_readings):
    diagnostic_flag = 'MODERATE_FLUCTUATION'
    energy_signature *= 0.9
    dummy_sum = sum([i for i in range(len(filtered_temp)) if i % 2 == 0])  # dead computation
else:
    diagnostic_flag = 'STABLE'
    correction_factor = 1.0
    for t in temperature_readings:
        correction_factor *= 0.995  # decoy loop

# Another red herring: unused data structure
historical_snapshot = {
    'temps': temperature_readings[:],
    'meta': {
        'source': 'Station_A1',
        'valid': True,
        'checksum': sum(temperature_readings) * 1000 % 97
    }
}

# Primary analysis function
def analyze_readings(signal_chunk):
    base_metric = compute_magnitude(signal_chunk)
    peak = max(signal_chunk)
    trough = min(signal_chunk)
    dynamic_range = peak - trough
    
    # Distractor variables
    local_cache = {}
    for idx, val in enumerate(signal_chunk):
        local_cache[f'idx_{idx}'] = val * (idx + 1)
    
    # Real logic mixed with noise
    adjustment = 1.0
    if dynamic_range > 3.0:
        adjustment = 0.85
    elif dynamic_range < 1.0:
        adjustment = 1.2
    
    # Critical calculation path
    raw_diagnostic = base_metric * adjustment * 10
    
    # Fake refinement (never affects output)
    smoothed = [signal_chunk[0]]
    for i in range(1, len(signal_chunk)):
        smoothed.append(0.7 * signal_chunk[i] + 0.3 * smoothed[-1])
    
    return int(round(raw_diagnostic))

# Data preparation step
processed_signals = normalize_signal(filter_outliers(temperature_readings, 1.8))

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

print(f"Result: {final_diagnostic}")