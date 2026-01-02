import math

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'temp': 23.5, 'hum': 65, 'press': 1013, 'err': 0, 'ts': 1680000000},
    {'temp': 24.1, 'hum': 63, 'press': 1012, 'err': 0, 'ts': 1680000060},
    {'temp': 22.8, 'hum': 67, 'press': 1014, 'err': 1, 'ts': 1680000120},  # corrupted
    {'temp': 25.3, 'hum': 59, 'press': 1011, 'err': 0, 'ts': 1680000180},
    {'temp': 26.0, 'hum': 57, 'press': 1010, 'err': 0, 'ts': 1680000240},
    {'temp': 24.8, 'hum': 60, 'press': 1013, 'err': 0, 'ts': 1680000300},
    {'temp': 23.9, 'hum': 64, 'press': 1015, 'err': 0, 'ts': 1680000360},
    {'temp': 22.1, 'hum': 70, 'press': 1016, 'err': 0, 'ts': 1680000420}
]

# Irrelevant calibration constants (distractors)
CALIBRATION_A = 0.987
CALIBRATION_B = 1.012
REFERENCE_PRESSURE = 1013.25
OFFSET_MATRIX = [[1.0, 0.1], [0.05, 1.1]]

# Decoy function that looks important but is never used
def apply_calibration(data, a, b):
    return [d * a + b for d in data]

# Another decoy - unused transformation
transformation_log = []
def log_transform(x):
    if x > 0:
        result = math.log(x)
        transformation_log.append(result)
        return result
    return 0

# Data preprocessing pipeline
valid_data = [entry for entry in data_stream if entry['err'] == 0]  # filter errors

# Extract time series sequences
temp_series = [entry['temp'] for entry in valid_data]
hum_series = [entry['hum'] for entry in valid_data]
pres_series = [entry['press'] for entry in valid_data]

time_stamps = [entry['ts'] for entry in valid_data]

delta_t = [time_stamps[i+1] - time_stamps[i] for i in range(len(time_stamps)-1)]

# Compute rolling metrics (some irrelevant)
avg_temp = sum(temp_series) / len(temp_series)
avg_hum = sum(hum_series) / len(hum_series)
avg_press = sum(pres_series) / len(pres_series)

temp_std = (sum((t - avg_temp)**2 for t in temp_series) / len(temp_series))**0.5
hum_change_rate = (hum_series[-1] - hum_series[0]) / len(hum_series)

# String-based status encoding (distraction)
current_status = "stable" if temp_std < 1.5 else "fluctuating"
status_code = ''.join([c.upper() + str(ord(c)) for c in current_status])

# Redundant bit manipulation (misleading)
status_hash = 0
for c in status_code:
    status_hash ^= ord(c) << 2
    status_hash &= 0xFFFF  # limit to 16 bits

# Slice relevant portion: last 5 clean readings
data_slice = valid_data[-5:]

# Additional distraction: sorting by irrelevant field
sorted_by_pressure = sorted(data_slice, key=lambda x: x['press'], reverse=True)
sorted_by_time = sorted(data_slice, key=lambda x: x['ts'])

# Weight configuration for scoring (critical)
weights = {
    'temperature_weight': 0.4,
    'humidity_weight': 0.3,
    'pressure_trend_weight': 0.3
}

# Auxiliary functions
def extract_trend(values):
    if len(values) < 2:
        return 0
    return values[-1] - values[0]  # net change

def normalize(value, base):
    return abs(value - base) / base

def safe_average(lst):
    return sum(lst) / len(lst) if lst else 0

# Main processing function
def process_metrics(entries, w):
    temps = [e['temp'] for e in entries]
    hums = [e['hum'] for e in entries]
    press_vals = [e['press'] for e in entries]

    # Real metric calculations
    temp_trend = extract_trend(temps)
    hum_avg = safe_average(hums)
    press_trend = extract_trend(press_vals)

    # Normalize against reference
    temp_deviation = abs(temp_trend)  # more impact
    hum_normalized = normalize(hum_avg, 60)
    press_normalized = abs(press_trend) / 1013

    # Apply weights
    temp_score = temp_deviation * w['temperature_weight']
    hum_score = (1 - hum_normalized) * w['humidity_weight']  # inverted
    press_score = (1 - press_normalized) * w['pressure_trend_weight']

    # Final aggregation
    raw_score = temp_score + hum_score + press_score

    # Distraction: unused intermediate
    ceilinged = math.ceil(raw_score * 100)
    floored = math.floor(raw_score * 100)

    # Actual final adjustment using string slicing on status_code (subtle but valid)
    slice_key = int(status_code[3:5]) % 100  # uses earlier string, adds dependency
    adjusted_score = raw_score * (1 + slice_key / 1000)

    return round(adjusted_score, 6)

# Execute critical statement
final_score = process_metrics(data_slice, weights)

# Print result as required
print(f"Target result: {final_score}")