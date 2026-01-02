from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant entries
temperature_readings = [23.5, 24.1, 22.8, 23.5, 24.1, 25.3, 23.5, 26.7, 24.1, 23.9]
humidity_readings = [45, 47, 46, 45, 50, 48, 45, 55, 47, 49]
pressure_readings = [1013, 1015, 1012, 1013, 1020, 1018, 1013, 1005, 1015, 1017]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 0.78
scaling_factor = 1.023
reference_checksum = 98765
redundant_flags = ['A', 'B', 'C', 'D']
metadata_log = {"version": "2.1", "calibrated": False}

# Noise injection simulation (unused path)
def apply_noise(data, factor=0.05):
    import random
    return [x + random.uniform(-factor, factor) for x in data]

# Decoy function that is never called
def deprecated_analysis(seq):
    return sum(x ** 2 for x in seq if x > 30)

# Data alignment via tuple pairing (relevant)
sensor_tuples = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Extract temperature for processing
temperatures_only = [t for t, h, p in sensor_tuples]

# Count frequency of temperature readings (useful for mode)
temp_counter = Counter(temperatures_only)
most_common_temp = temp_counter.most_common(1)[0][1]  # frequency of most common

# Compute moving average over 3 elements (with overlap)
moving_avg = [(temperatures_only[i] + temperatures_only[i+1] + temperatures_only[i+2]) / 3 
               for i in range(len(temperatures_only) - 2)]

# Identify outliers using deviation threshold
mean_temp = sum(temperatures_only) / len(temperatures_only)
outliers = [t for t in temperatures_only if abs(t - mean_temp) > 1.5]

# Flag transitions in temperature trend (increasing/decreasing)
trend_changes = 0
for i in range(1, len(temperatures_only)):
    if (temperatures_only[i] > temperatures_only[i-1] and 
        i > 1 and temperatures_only[i-1] < temperatures_only[i-2]):
        trend_changes += 1

# Destructuring assignment (tuple unpacking)
primary_mode, mode_freq = temp_counter.most_common(1)[0]

# Transform data using lambda-based normalization
normalize = lambda x: (x - mean_temp) / mean_temp
normalized_devs = [round(normalize(t), 4) for t in temperatures_only]

# Group by rounded temperature using defaultdict (irrelevant grouping)
grouped_by_rounded = defaultdict(list)
for t in temperatures_only:
    grouped_by_rounded[round(t)].append(t)

# Simulated diagnostic thresholds
threshold_breach_count = sum(1 for t in temperatures_only if t > 25.0)

# Linear search for first critical pressure drop (below 1010)
critical_pressure_index = -1
for idx, (_, _, p) in enumerate(sensor_tuples):
    if p < 1010:
        critical_pressure_index = idx
        break  # only first matters

# Unused complex derived structure (distractor)
cumulative_stats = {
    'temp_sum': sum(temperatures_only),
    'humidity_max': max(humidity_readings),
    'pressure_min': min(pressure_readings),
    'stdev_hint': (max(temperatures_only) - min(temperatures_only)) / 2
}

# Processed data construction (key step)
processed_data = {
    'base': primary_mode,
    'spread': len(outliers),
    'trends': trend_changes,
    'breaches': threshold_breach_count,
    'norm_dev': sum(abs(d) for d in normalized_devs),
    'critical_idx': critical_pressure_index if critical_pressure_index != -1 else len(sensor_tuples)
}

# Higher-order function for analysis
analyze_readings = lambda data: (
    int(data['base'] * 10) + 
    data['spread'] * 5 - 
    data['trends'] * 2 + 
    data['breaches'] * 10 + 
    int(data['norm_dev']) - 
    data['critical_idx']
)

# Execution point of interest
final_diagnostic = analyze_readings(processed_data)

# Output result as required
print(f"Target result: {final_diagnostic}")