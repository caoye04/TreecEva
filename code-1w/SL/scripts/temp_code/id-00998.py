import itertools

# Simulated sensor data with noise and redundant fields
data_packet = [
    {'id': 1, 'temp_raw': 23.5, 'status': 'OK', 'timestamp': '2023-05-01 10:00'},
    {'id': 2, 'temp_raw': -999, 'status': 'ERR', 'timestamp': '2023-05-01 10:01'},
    {'id': 3, 'temp_raw': 24.1, 'status': 'OK', 'timestamp': '2023-05-01 10:02'},
    {'id': 4, 'temp_raw': 23.8, 'status': 'OK', 'timestamp': '2023-05-01 10:03'},
    {'id': 5, 'temp_raw': -999, 'status': 'ERR', 'timestamp': '2023-05-01 10:04'},
    {'id': 6, 'temp_raw': 24.0, 'status': 'OK', 'timestamp': '2023-05-01 10:05'}
]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 1.002
CALIBRATION_FACTOR_B = 0.998
REFERENCE_OFFSET = 0.5
MAX_THEORETICAL_VALUE = 99.9

# Noise threshold flags (partially relevant but not used in final logic)
NOISE_FLOOR = -100
SATURATION_LIMIT = 100

# Data transformation pipeline
filtered_data = [entry for entry in data_packet if entry['status'] == 'OK']

# Extract raw temperatures
raw_temps = [entry['temp_raw'] for entry in filtered_data]

# Apply smoothing filter (moving average of window size 2)
smoothed_temps = []
for i in range(len(raw_temps)):
    if i == 0:
        smoothed_temps.append(raw_temps[i])
    else:
        smoothed_temps.append((raw_temps[i-1] + raw_temps[i]) / 2)

# Normalize temperatures relative to baseline (first valid reading)
baseline = raw_temps[0]
normalized_deviation = [(t - baseline) for t in raw_temps]

# Compute rolling variance (unused - red herring)
variance_window = []
for i in range(1, len(normalized_deviation)):
    mean_so_far = sum(normalized_deviation[:i+1]) / (i+1)
    var = sum((x - mean_so_far)**2 for x in normalized_deviation[:i+1]) / (i+1)
    variance_window.append(var)

# Simulate checksum validation (dead code path)
def validate_checksum(data):
    total = 0
    for d in data:
        total += int(d * 10) % 7
    return total % 13 == 0

# Unused helper function (decoy)
def transform_coordinates(x, y):
    return (x * 0.9 + 1.1, y * 1.1 - 0.9)

# Bit manipulation mask for hypothetical error detection (not actually used)
ERROR_DETECTION_MASK = 0b110101
ACTIVE_SENSOR_BIT = 0b001000

# Complex data restructuring using itertools (some parts irrelevant)
grouped_by_temp_class = {k: list(g) for k, g in itertools.groupby(
    sorted(filtered_data, key=lambda x: x['temp_raw'] > 23.9),
    key=lambda x: 'high' if x['temp_raw'] > 23.9 else 'low'
)}

high_temp_entries = grouped_by_temp_class.get('high', [])
low_temp_entries = grouped_by_temp_class.get('low', [])

# Augment entries with dummy features (distraction)
for entry in high_temp_entries:
    entry['flag'] = True
    entry['aux_value'] = entry['temp_raw'] * 0.1

# Linear search for first high-temp entry (used in critical path)
first_high_temp_index = -1
for idx, entry in enumerate(filtered_data):
    if entry['temp_raw'] > 23.9:
        first_high_temp_index = idx
        break

# Critical processing chain
offset_correction = 0.25
if first_high_temp_index > 0:
    offset_correction *= 2.0  # Double correction if delayed response

adjusted_temps = [t + offset_correction for t in raw_temps]

# Compute weighted score based on position and value
weights = [1.0, 1.2, 1.4, 1.6]  # Increasing importance over time
weighted_sum = 0.0
for i, temp in enumerate(adjusted_temps):
    weight = weights[min(i, len(weights)-1)]
    weighted_sum += temp * weight

# Secondary adjustment based on count of high-temp entries
bonus_factor = len(high_temp_entries) * 1.5

# Final aggregation function
def compute_final_score(data):
    base = weighted_sum
    bonus = bonus_factor ** 2
    penalty = len([e for e in data_packet if e['status'] == 'ERR']) * 10
    result = (base + bonus) - penalty
    # Additional non-linear term
    result = result * (1 + 0.01 * first_high_temp_index)
    return round(result, 4)

# Processed data (dummy container - distractor)
processed_data = {
    'entries': filtered_data,
    'stats': {
        'count': len(filtered_data),
        'bonus_applied': bonus_factor,
        'first_high_idx': first_high_temp_index
    }
}

# Key execution point
final_score = compute_final_score(processed_data)
print(f"Target result: {final_score}")