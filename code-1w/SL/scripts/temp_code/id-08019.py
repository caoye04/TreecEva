import math

# Simulated sensor array data with calibration offsets
def collect_sensor_data():
    raw_readings = {
        'temp': [23.5, 24.1, 22.9, 25.0, 23.8],
        'pressure': [101.3, 102.1, 100.7, 103.5, 101.9],
        'humidity': [45, 47, 44, 50, 46]
    }
    calibration_factor = 1.02
    adjusted = {k: [round(v_i * calibration_factor, 2) for v_i in v] for k, v in raw_readings.items()}
    return adjusted

# Misleading auxiliary function (dead code path)
def legacy_normalization(data):
    norm_data = {}
    for k, values in data.items():
        mean_val = sum(values) / len(values)
        norm_data[k] = [v / mean_val for v in values]
    return norm_data  # Never actually used

# Real preprocessing pipeline
def filter_outliers(readings, threshold=1.5):
    filtered = {}
    for sensor, vals in readings.items():
        q1 = sorted(vals)[1]
        q3 = sorted(vals)[-2]
        iqr = q3 - q1
        low_lim = q1 - threshold * iqr
        high_lim = q3 + threshold * iqr
        filtered[sensor] = [v for v in vals if low_lim <= v <= high_lim]
    return filtered

def smooth_data(sequence, factor=0.3):
    if len(sequence) == 0:
        return []
    smoothed = [sequence[0]]
    for i in range(1, len(sequence)):
        smoothed.append(round(smoothed[-1] * (1 - factor) + sequence[i] * factor, 2))
    return smoothed

# Auxiliary statistic (distractor)
def compute_range_extremes(dataset):
    extremes = {}
    for key, vals in dataset.items():
        extremes[key] = {'min': min(vals), 'max': max(vals)}
    temp_min = extremes['temp']['min']
    pressure_max = extremes['pressure']['max']
    dummy_calc = (pressure_max * 1000) % 7  # Red herring computation
    return extremes

# Core analysis logic
def integrate_signals(temp_vals, press_vals, humid_vals):
    # Weighted composite index based on environmental stability
    temp_stable = all(abs(temp_vals[i] - temp_vals[i-1]) < 0.8 for i in range(1, len(temp_vals)))
    press_trend = sum(press_vals[i] - press_vals[i-1] for i in range(1, len(press_vals)))
    humidity_avg = sum(humid_vals) / len(humid_vals)
    
    # Complex interaction formula
    base_index = 0
    if temp_stable:
        base_index += 15
    if abs(press_trend) < 1.5:
        base_index += 12
    if 44 <= humidity_avg <= 48:
        base_index += 8
    
    adjustment = (press_trend * 3) + (humidity_avg / 10)
    final_score = base_index + adjustment
    return round(final_score, 2)

# Main diagnostic engine
def analyze_readings(data_dict):
    temp_series = data_dict.get('temp', [])
    press_series = data_dict.get('pressure', [])
    humid_series = data_dict.get('humidity', [])
    
    # Secondary validation check (distractor)
    valid_sensors = 0
    for k in ['temp', 'pressure', 'humidity']:
        if k in data_dict and len(data_dict[k]) > 0:
            valid_sensors += 1
    reliability_factor = valid_sensors / 3
    
    # Actual signal integration
    integrated_value = integrate_signals(temp_series, press_series, humid_series)
    
    # Dummy entropy calculation (irrelevant)
    entropy_proxy = 0
    for val in temp_series + press_series + humid_series:
        if val > 0:
            entropy_proxy += math.log(val) * (-val / 100)
    
    # Final diagnostic decision logic
    if integrated_value > 25:
        diagnosis_code = 1
    elif integrated_value > 15:
        diagnosis_code = 2
    else:
        diagnosis_code = 3
    
    # Key computational step - combines multiple factors
    final_diagnostic = int((integrated_value * 100) // (diagnosis_code + 1))
    
    # Dead-end debugging block (never reached)
    debug_snapshot = {}
    if False:
        debug_snapshot['raw_integrated'] = integrated_value
        debug_snapshot['coded'] = diagnosis_code
        for k in data_dict:
            debug_snapshot[f'{k}_len'] = len(data_dict[k])
    
    return final_diagnostic

# Execution flow
sensor_data = collect_sensor_data()
extremes_log = compute_range_extremes(sensor_data)  # Uses but doesn't alter main flow

filtered_data = filter_outliers(sensor_data)
processed_data = {}
for k, v in filtered_data.items():
    processed_data[k] = smooth_data(v)

# Irrelevant transformation chain
buffer_copy = {key: [x + 0.1 for x in val] for key, val in processed_data.items()}
del buffer_copy  # Resource cleanup (distractor)

# Critical execution point
temp_snapshot = {k: v[:] for k, v in processed_data.items()}  # Backup
final_diagnostic = analyze_readings(processed_data)
print(f"Result: {final_diagnostic}")