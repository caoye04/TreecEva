import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.7, 23.9]
humidity_readings = [56, 58, 61, 55, 52, 59, 60]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1011]

# Irrelevant auxiliary data (distractor)
color_spectrum = ['red', 'green', 'blue', 'infrared']
spectral_weights = {'red': 0.25, 'green': 0.35, 'blue': 0.30, 'infrared': 0.10}
weighted_avg = sum(spectral_weights[c] for c in color_spectrum if c != 'infrared')

# Signal processing pipeline
noise_floor = 0.7
smoothing_factor = 0.85

def apply_digital_filter(raw_data, factor):
    filtered = []
    accumulator = raw_data[0]
    for value in raw_data:
        accumulator = factor * accumulator + (1 - factor) * value
        filtered.append(round(accumulator, 3))
    return filtered

# Process temperature with filter
filtered_temp = apply_digital_filter(temperature_readings, smoothing_factor)

# Dead code path - never called (distractor)
def legacy_normalization(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Misleading intermediate transformation (not used in final result)
aggregated_metrics = []
for i in range(len(humidity_readings)):
    metric = humidity_readings[i] * math.cos(math.radians(temperature_readings[i]))
    aggregated_metrics.append(round(metric, 3))

# Tuple unpacking and set operations (required Python features)
signal_summary = (sum(filtered_temp), len(filtered_temp), max(filtered_temp) - min(filtered_temp))
summary_set_a = {int(signal_summary[0]), int(signal_summary[1]), int(signal_summary[2])}
summary_set_b = {1, 2, 3, int(signal_summary[0]) % 100}
disjoint_flag = len(summary_set_a.symmetric_difference(summary_set_b)) > 2

# Linear search with early exit (real logic component)
def find_anomaly_threshold(data, threshold):
    for i, val in enumerate(data):
        if val > threshold:
            return i  # returns first index above threshold
    return -1

anomaly_index = find_anomaly_threshold(filtered_temp, 24.5)

# Recursive signal classification (simple recursion)
def classify_trend(values, index=0, up_count=0, down_count=0):
    if index >= len(values):
        return 'upward' if up_count > down_count else 'downward'
    if index > 0:
        if values[index] > values[index - 1]:
            up_count += 1
        elif values[index] < values[index - 1]:
            down_count += 1
    return classify_trend(values, index + 1, up_count, down_count)

trend_classification = classify_trend(filtered_temp)

# Data fusion using lambda (required feature)
fuse_sensors = lambda t, h: round(t * (1 + h / 100), 3)
fused_readings = [fuse_sensors(filtered_temp[i], humidity_readings[i]) for i in range(len(filtered_temp))]

# Secondary derived dataset - looks important but unused in final answer
adjusted_pressure = [p * (25 / t) for t, p in zip(filtered_temp, pressure_readings)]

# Primary processing path
processed_signals = []
for val in fused_readings:
    if val > 28:
        processed_signals.append(val * 1.1)
    elif val > 26:
        processed_signals.append(val * 1.05)
    else:
        processed_signals.append(val)

# Final diagnostic analysis depends only on trend and anomaly index
# All prior steps include distractors, but only these are relevant
intermediate_score = 0
if trend_classification == 'upward':
    intermediate_score += 400
else:
    intermediate_score += 200

if anomaly_index > 2:
    intermediate_score += 50

# Bit manipulation red herring (irrelevant computation)
bit_mask = 0b110101
scrambled_score = intermediate_score ^ bit_mask & 0b111111

# Set-based validation (looks critical but not decisive)
valid_scores = {400, 450, 500, 550}
is_valid = scrambled_score in valid_scores  # always false here

# Final diagnostic uses only intermediate_score with a fixed offset
final_diagnostic = intermediate_score + 73

# Output required format
print(f"Target result: {final_diagnostic}")