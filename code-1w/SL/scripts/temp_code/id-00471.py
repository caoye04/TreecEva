from itertools import combinations
from functools import reduce

# Simulated sensor readings with noise and calibration factors
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1]
humidity_readings = [45, 47, 50, 44, 52, 48, 55]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1018, 1017]

# Irrelevant transformations (distractors)
decoy_transform = lambda x: (x ** 2 + 3) // 7
decoy_values = [decoy_transform(int(t * 2)) for t in temperature_readings]

# Calibration lookup table (partially relevant)
calibration_map = {i: val * 0.98 for i, val in enumerate(temperature_readings)}

# Noise filter using moving average (red herring - not used in final calculation)
def apply_noise_filter(data):
    return [sum(data[max(0, i-2):i+1]) / (i+1) for i in range(len(data))]

filtered_temps = apply_noise_filter(temperature_readings)  # Dead code path

# Weight assignment based on reliability (used later)
weights = {'temp': 0.5, 'humidity': 0.3, 'pressure': 0.2}

# Outlier detection (misleading intermediate result)
def is_outlier(val, data_list):
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    std_dev = variance ** 0.5
    return abs(val - mean_val) > 2 * std_dev

outlier_flags = [is_outlier(t, temperature_readings) for t in temperature_readings]  # Not actually used

# Bit manipulation for 'data integrity check' (distractor)
def compute_integrity_key(values):
    return reduce(lambda acc, val: acc ^ int(val), map(lambda x: x * 10, values), 0)

integrity_key = compute_integrity_key(pressure_readings)  # Used nowhere critical

# Real processing begins here — subtle and buried among distractions
effective_temps = [calibration_map[i] * 1.02 for i in range(len(calibration_map))]  # Corrected temps

# Feature extraction via combinatorial analysis (relevant but indirect)
temp_pairs = list(combinations(effective_temps[:4], 2))
pair_diffs = [abs(a - b) for a, b in temp_pairs]
mean_pair_diff = sum(pair_diffs) / len(pair_diffs)

# Hidden logic: use pair difference to modulate weight
adjusted_weight_temp = weights['temp'] + (mean_pair_diff / 100)

# Normalize humidity with unused function
normalize = lambda lst: [h / max(lst) for h in lst]
scaled_humidity = normalize(humidity_readings)
mid_scaled_humid = scaled_humidity[3]  # Looks important, isn't

# Core aggregation logic disguised as auxiliary step
def compute_base_metric(temp_data, humid_data, press_data):
    avg_temp = sum(temp_data) / len(temp_data)
    avg_humid = sum(humid_data) / len(humid_data)
    avg_press = sum(press_data) / len(press_data)
    
    # Composite formula
    metric = (avg_temp * 1.1) + (avg_humid * 0.8) - (avg_press / 100)
    return metric

base_metric = compute_base_metric(effective_temps, humidity_readings, pressure_readings)

# Final score computation — depends on base_metric and adjusted_weight_temp
# All prior decoys distract from this simple dependency
final_score = int(base_metric * adjusted_weight_temp * 10)

# Unused diagnostic block (dead code)
if __debug__:
    diagnostics = {
        'raw_avg_temp': sum(temperature_readings) / len(temperature_readings),
        'calib_drift': effective_temps[0] - temperature_readings[0],
        'integrity': integrity_key
    }

print(f"Result: {final_score}")