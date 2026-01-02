from collections import defaultdict, Counter
import itertools

# Simulated sensor readings over time with noise and redundant channels
timestamped_readings = [
    (1001, {'temp': 23.1, 'pressure': 101.3, 'humidity': 45.2, 'aux_1': 0.0}),
    (1002, {'temp': 23.3, 'pressure': 101.4, 'humidity': 44.8, 'aux_1': 0.0}),
    (1003, {'temp': 22.9, 'pressure': 101.2, 'humidity': 46.1, 'aux_1': 0.0}),
    (1004, {'temp': 23.6, 'pressure': 101.6, 'humidity': 43.7, 'aux_1': 0.0}),
    (1005, {'temp': 24.1, 'pressure': 102.1, 'humidity': 42.9, 'aux_1': 0.0}),
    (1006, {'temp': 25.2, 'pressure': 103.3, 'humidity': 41.5, 'aux_1': 0.0}),
    (1007, {'temp': 26.8, 'pressure': 105.2, 'humidity': 39.4, 'aux_1': 0.0}),
    (1008, {'temp': 28.9, 'pressure': 107.8, 'humidity': 36.2, 'aux_1': 0.0}),
    (1009, {'temp': 31.5, 'pressure': 111.2, 'humidity': 32.1, 'aux_1': 0.0}),
    (1010, {'temp': 34.7, 'pressure': 115.3, 'humidity': 27.3, 'aux_1': 0.0})
]

# Irrelevant calibration map (distractor)
calibration_map = defaultdict(lambda: 1.0)
for i in range(5):
    for j in range(5):
        calibration_map[(i,j)] = (i * j) % 3 + 0.5

# Misleading trend analysis on auxiliary data (dead path)
def analyze_aux_trend(data):
    aux_values = [entry[1]['aux_1'] for entry in data]
    if len(aux_values) < 2:
        return 0
    diffs = [aux_values[i+1] - aux_values[i] for i in range(len(aux_values)-1)]
    return sum(diffs) / len(diffs)

# Unused recursive smoothing function (red herring)
def smooth_recursive(seq, factor=0.3, depth=0):
    if depth > 3 or len(seq) < 2:
        return seq
    smoothed = [seq[0]]
    for i in range(1, len(seq)):
        smoothed.append(factor * seq[i] + (1-factor) * smoothed[i-1])
    return smooth_recursive(smoothed, factor, depth+1)

# Decoy entropy calculation using bitwise operations (irrelevant)
def compute_entropy_signature(values):
    sig = 0
    for v in values:
        shifted = int(abs(v * 100)) & 0xFF
        sig ^= shifted
        sig = (sig << 1) | (sig >> 7)
        sig &= 0xFF
    return sig

# Real processing begins here — filter valid entries based on rising temp trend
rising_temp_periods = []
for i in range(1, len(timestamped_readings)):
    prev_temp = timestamped_readings[i-1][1]['temp']
    curr_temp = timestamped_readings[i][1]['temp']
    if curr_temp > prev_temp:
        rising_temp_periods.append(timestamped_readings[i])

# Extract only temperature and pressure (actual relevant data)
filtered_data = [(t, {'temp': r['temp'], 'pressure': r['pressure']}) for t, r in rising_temp_periods]

# Generate threshold function using lambda with closure (key concept)
thresh_base = 100.0
threshold_func = lambda x: (x['pressure'] - thresh_base) * 2.1 > x['temp']

# Secondary filter using itertools.groupby (valid usage)
groups = defaultdict(list)
for key, group in itertools.groupby(filtered_data, key=lambda x: x[0] // 100):
    groups[key].extend(list(group))

consolidated = []
for k, group in groups.items():
    for item in group:
        consolidated.append(item)

# Actual diagnostic processor
state_counter = Counter()

for ts, reading in consolidated:
    temp, press = reading['temp'], reading['pressure']
    state_counter['total_points'] += 1
    if temp > 25.0:
        state_counter['high_temp_count'] += 1
    if press > 105.0:
        state_counter['high_pressure_count'] += 1

# Critical logic: correlation between high temp and high pressure events
dependent_events = 0
independent_events = 0

for _, reading in consolidated:
    temp_flag = reading['temp'] > 25.0
    press_flag = reading['pressure'] > 105.0
    if temp_flag and press_flag:
        dependent_events += 1
    elif temp_flag or press_flag:
        independent_events += 1

# Compute joint deviation score (main signal)
avg_temp = sum(r['temp'] for _, r in consolidated) / len(consolidated)
avg_press = sum(r['pressure'] for _, r in consolidated) / len(consolidated)
baseline_deviation = (avg_temp - 23.0) * (avg_press - 101.3)

# Final diagnostic uses modular arithmetic and conditional weighting
if dependent_events >= 3:
    weight = 7
else:
    weight = 3

# Core answer computation
final_diagnostic = (dependent_events * weight + independent_events) * (baseline_deviation % 4.75)

# Print result as required
print(f"Result: {final_diagnostic}")