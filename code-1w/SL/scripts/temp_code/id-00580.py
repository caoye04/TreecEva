from itertools import compress, cycle
import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.4, 19.8, 22.1, 25.6, 18.3, 20.9, 24.2, 26.7, 17.5, 21.0]
humidity_readings = [45, 60, 52, 38, 66, 58, 41, 35, 70, 55]
pressure_readings = [1013, 1020, 1015, 1008, 1022, 1017, 1010, 1005, 1025, 1018]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 45, 50, 28, 60, 40, 35, 55, 25, 48]
lux_values = [1000, 800, 1200, 600, 1400, 900, 1100, 700, 1300, 950]

# Derived metrics with partial relevance and red herrings
temperature_z_scores = [(t - 21.5) / 2.0 for t in temperature_readings]  # assumed mean=21.5, std=2.0
humidity_categories = ['low' if h < 40 else 'high' if h > 60 else 'normal' for h in humidity_readings]

# Misleading transformation chain (dead path)
transformed_pressure = []
for p in pressure_readings:
    adjusted = p * 0.98
    if adjusted > 1000:
        adjusted = math.log(adjusted) * 100
    transformed_pressure.append(round(adjusted, 2))

# Critical masking logic using bitwise and comparison ops (red herring)
mask_key = 0b1010101010
reading_flags = [hash(str(t)) % 256 for t in temperature_readings]
applied_masks = [flag & mask_key for flag in reading_flags]

# Real signal: identify anomalous temperature points using rolling window logic
window_size = 3
trend_anomalies = []
for i in range(len(temperature_readings) - window_size + 1):
    window = temperature_readings[i:i+window_size]
    trend = (window[2] - window[0])  # rate of change over 3 readings
    trend_anomalies.append(abs(trend) > 2.5)

# Extend anomalies list to match original length (padding with False)
trend_anomalies += [False] * (len(temperature_readings) - len(trend_anomalies))

# Use itertools.compress to filter valid data points
valid_indices = list(compress(range(len(temperature_readings)), [not ta for ta in trend_anomalies]))
filtered_data = list(compress(temperature_readings, [not ta for ta in trend_anomalies]))

# Distractor: complex unused data structure
diagnostic_map = {
    'ranges': {
        'temp': (min(temperature_readings), max(temperature_readings)),
        'humid': (min(humidity_readings), max(humidity_readings))
    },
    'alerts': [],
    'history': [{
        'timestamp': f"T{i}", 
        'temp': temperature_readings[i], 
        'flag': applied_masks[i]
    } for i in range(len(temperature_readings))]
}

# Unused recursive function (decoy)
def calculate_entropy(data, depth=0):
    if depth >= 3 or len(data) < 2:
        return 0.0
    mid = sum(data) / len(data)
    left = [x for x in data if x <= mid]
    right = [x for x in data if x > mid]
    return 0.1 * depth + calculate_entropy(left, depth+1) + calculate_entropy(right, depth+1)

# Real processing function (used)
def analyze_variance(readings):
    mean = sum(readings) / len(readings)
    squared_diffs = [(x - mean) ** 2 for x in readings]
    variance = sum(squared_diffs) / len(squared_diffs)
    return round(variance, 4)

# Higher-order function factory (actually used)
def make_threshold_detector(min_val, max_val):
    return lambda x: min_val <= x <= max_val

threshold_func = make_threshold_detector(18.0, 25.0)

# Secondary filtering based on threshold compliance
compliance_flags = [threshold_func(temp) for temp in filtered_data]
final_filtered = list(compress(filtered_data, compliance_flags))

# Final diagnostic computation
variance_metric = analyze_variance(final_filtered)
length_factor = len(final_filtered)

# Critical distraction: irrelevant floating-point accumulation
cumulative_phase = 0.0
phase_cycle = cycle([0.1, -0.2, 0.15])
for i in range(len(final_filtered) * 2):
    cumulative_phase += next(phase_cycle) * 0.5  # decays out

cumulative_phase = round(cumulative_phase, 4)  # misleading but unused

# Actual answer derivation
scaling_constant = 127.0
final_diagnostic = int((variance_metric * length_factor * scaling_constant) + 0.5)

# Output result as required
print(f"Result: {final_diagnostic}")