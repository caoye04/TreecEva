def sensor_calibrate(raw_values, baseline=1.05):
    """Apply calibration to raw sensor data (irrelevant for final result)"""
    return [v * baseline for v in raw_values if v > 0]


def accumulate_deltas(values):
    """Compute sequential differences (red herring function, not used)"""
    return [values[i+1] - values[i] for i in range(len(values)-1)]


def encode_flags(status_list):
    """Convert boolean statuses to bit flags (unused path)"""
    flag = 0
    for i, active in enumerate(status_list):
        if active:
            flag |= (1 << i)
    return flag

# Simulated environmental sensor readings
raw_sensor_data = [0.88, 1.02, 0.95, 1.11, 0.76, 1.24, 0.68, 1.33]

# Irrelevant preprocessing chain
normalized = [round(x + 0.07, 2) for x in raw_sensor_data]
calibrated = sensor_calibrate(raw_sensor_data)
smoothed = [round((normalized[i] + calibrated[i]) / 2, 2) for i in range(len(normalized))]

# Decoy data structures
status_flags = [True, False, True, False, True]
flag_encoding = encode_flags(status_flags)  # Dead end

# Real processing begins here — hidden among distractions
primary_stream = [x for x in raw_sensor_data if x >= 0.9]
secondary_filter = list(filter(lambda x: abs(x - 1.0) < 0.2, primary_stream))

# Mapping sensor zones to dynamic thresholds (used later)
zone_bounds = {'A': 0.98, 'B': 1.05, 'C': 0.92}
threshold_map = {k: v + 0.03 for k, v in zone_bounds.items()}

# Simulate multi-pass validation (some steps are irrelevant)
validation_log = []
for i, val in enumerate(primary_stream):
    deviation = abs(val - 1.0)
    validation_log.append((i, deviation, deviation < 0.15))

# Critical data transformation: categorize and count
zone_data = {'A': [], 'B': [], 'C': []}
for idx, (a, b) in enumerate(zip(primary_stream, reversed(primary_stream))):
    if idx % 2 == 0:
        zone_data['A'].append(a)
    elif idx % 3 == 0:
        zone_data['B'].append(b)
    else:
        zone_data['C'].append(a + b)

# Process only non-empty zones with meaningful size
processed_data = {}
for key, readings in zone_data.items():
    if len(readings) > 0 and sum(readings) > 0:
        avg = sum(readings) / len(readings)
        processed_data[key] = round(avg, 3)

# Another decoy: recursive summation (never called in critical path)
def recursive_sum(lst, n=None):
    n = len(lst) if n is None else n
    if n <= 0:
        return 0
    return lst[n-1] + recursive_sum(lst, n-1)

# Core analysis logic — depends on processed_data and threshold_map
def analyze_readings(data_dict, thresholds):
    score = 0
    for zone, avg_val in data_dict.items():
        ref = thresholds.get(zone, 1.0)
        if avg_val > ref:
            score += int((avg_val - ref) * 1000)
        else:
            score -= int((ref - avg_val) * 500)
    # Final adjustment based on zone count
    bonus = len(data_dict) * 100
    return score + bonus

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")