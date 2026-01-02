import math

# Simulated sensor array data from environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.3, 24.9, 23.7, 22.4]
humidity_readings = [45, 48, 52, 44, 60, 58, 50, 55]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016, 1011]

# Irrelevant auxiliary variables (distractors)
baseline_offset = 0.97
scaling_factor = 1.03
auxiliary_cache = {}
transient_state = True
sync_interval = 7

# Signal processing functions
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [(x - mean_val) * scaling_factor for x in signal]

def detect_anomalies(data):
    threshold = sum([abs(x) for x in data]) / len(data)
    anomalies = []
    for i, val in enumerate(data):
        if abs(val) > threshold * 1.3:
            anomalies.append((i, val))
    return anomalies

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probabilities)

def shift_window(data, window_size=3):
    """Sliding window transformation - irrelevant to final result"""
    result = []
    for i in range(len(data) - window_size + 1):
        result.append(sum(data[i:i+window_size]))
    return result

def filter_outliers(data, factor=1.5):
    """Dead code path - never called"""
    median = sorted(data)[len(data)//2]
    mad = sorted([abs(x - median) for x in data])[len(data)//2]
    return [x for x in data if abs(x - median) <= factor * mad]

def transform_coordinates(x, y):
    """Decoy function with no usage"""
    return (x * math.cos(y), y * math.sin(x))

# Data preprocessing pipeline
normalized_temp = normalize_signal(temperature_readings)
normalized_humid = normalize_signal(humidity_readings)

# Composite feature engineering
composite_index = [
    temp * 0.6 + humid * 0.01 + (press - 1000) * 0.05
    for temp, humid, press in zip(temperature_readings, humidity_readings, pressure_readings)
]

# Misleading intermediate analysis
entropy_value = compute_entropy(composite_index)
anomaly_list = detect_anomalies(normalized_temp)
windowed_data = shift_window(composite_index, 4)  # Unused result

# Tuple unpacking and conditional logic red herring
status_flags = []
for idx, val in enumerate(composite_index):
    if val > 25.0:
        status_flags.append((idx, 'HIGH'))
    elif val < 15.0:
        status_flags.append((idx, 'LOW'))
    else:
        status_flags.append((idx, 'NORMAL'))

# Real processing begins here — hidden among noise
processed_signals = [
    round(x, 2) for x in normalized_temp
    if abs(x) > 0.5  # Only significant deviations kept
]

# Hidden rule: count how many processed signals are above 1.0 after rounding
high_deviation_count = len([x for x in processed_signals if x > 1.0])

# Bit manipulation decoy — looks important but unused
bit_signature = 0
for i in range(len(processed_signals)):
    bit_signature ^= int(abs(processed_signals[i]) * 100) << (i % 5)

# Actual diagnostic logic buried in abstraction
def analyze_readings(signals):
    base_score = len(signals) * 10
    adjustment = 0
    for s in signals:
        if s > 0:
            adjustment += int(s * 2)
        else:
            adjustment -= int(abs(s) * 1.5)
    # Final computation depends only on high_deviation_count from outer scope
    global high_deviation_count
    return base_score + adjustment + (high_deviation_count ** 3)

# Key execution point
final_diagnostic = analyze_readings(processed_signals)

# Print required output
print(f"Result: {final_diagnostic}")