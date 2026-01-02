import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 61, 48, 55, 58, 43, 50, 53, 57]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1011, 1017, 1019, 1010]

# Irrelevant auxiliary metrics (distractors)
sound_levels = [34, 36, 33, 38, 40, 35, 32, 37, 39, 31]
luminosity = [800, 780, 810, 750, 720, 790, 820, 770, 740, 830]

# Preprocessing: Normalize readings using z-score (some are irrelevant)
def normalize_z(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [(x - mean) / std_dev for x in data]

# Misleading transformation chain
def transform_sequence(seq):
    doubled = [x * 2 for x in seq]
    shifted = [x + 1 for x in doubled]
    inverted = [1 / x if x != 0 else 0 for x in shifted]
    return inverted

# Dead function - never called but looks important
def calculate_entropy(data):
    from math import log
    total = sum(data)
    probabilities = [x / total for x in data]
    return -sum(p * log(p) for p in probabilities if p > 0)

# Another decoy: frequency analysis with no use
freq_analysis = dict(zip(range(len(temperature_readings)), 
                         [abs(t - 24) for t in temperature_readings]))

def detect_outliers(values, factor=1.5):
    sorted_vals = sorted(values)
    q1, q3 = sorted_vals[len(sorted_vals)//4], sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [v for v in values if v < lower or v > upper]

# Real processing begins here
normalized_temp = normalize_z(temperature_readings)
normalized_humid = normalize_z(humidity_readings)

# Combine relevant data using tuple pairing and filtering
temp_humid_pairs = list(zip(normalized_temp, normalized_humid))

# Filtering condition based on combined deviation
filtered_pairs = [pair for pair in temp_humid_pairs if abs(pair[0]) > 0.5 or abs(pair[1]) > 0.6]

# Extract filtered temperature components
filtered_data = [p[0] for p in filtered_pairs]

# Auxiliary computation: moving average (unused red herring)
def moving_average(data, window=3):
    return [sum(data[i:i+window]) / window for i in range(len(data) - window + 1)]

ma_result = moving_average([abs(x) for x in filtered_data])

# Threshold determined via bitwise manipulation (obfuscated but valid)
base_threshold = 73
shifted = base_threshold >> 3  # becomes 9
mask = 0b101
masked = shifted & mask  # 9 & 5 = 1
threshold = float(masked)  # threshold = 1.0

# Core diagnostic logic
status_flags = []
for val in filtered_data:
    if val > threshold:
        status_flags.append(2)
    elif val < -threshold:
        status_flags.append(-2)
    else:
        status_flags.append(1)

# Use itertools to group consecutive statuses
grouped_flags = [list(group) for k, group in itertools.groupby(status_flags)]
weighted_groups = [len(g) * g[0] for g in grouped_flags]

# Final aggregation with conditional scaling
raw_score = sum(weighted_groups)
if raw_score > 0:
    final_diagnostic = raw_score * 1.5
elif raw_score < 0:
    final_diagnostic = raw_score * 0.8
else:
    final_diagnostic = 10.5

# Additional misleading calculation (dead code path)
compression_ratio = len(filtered_data) / len(temperature_readings) if temperature_readings else 0
adjusted_entropy = compression_ratio * 100 if compression_ratio > 0.3 else 0

# Actual output
print(f"Result: {final_diagnostic}")