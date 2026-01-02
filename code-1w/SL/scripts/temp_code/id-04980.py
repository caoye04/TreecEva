def analyze_component_health(reading, threshold_map, status_log):
    if reading < threshold_map['critical_low']:
        status_log.append('ERROR')
        return -1
    elif reading > threshold_map['critical_high']:
        status_log.append('OVERLOAD')
        return 1
    else:
        status_log.append('NORMAL')
        return 0

# Irrelevant sensor simulation data
temperature_readings = [23.4, 25.1, 22.8, 27.5, 30.0, 28.3]
humidity_readings = [45.2, 50.1, 52.3, 48.7, 55.0, 60.2]
pressure_readings = [1013, 1009, 1015, 1020, 1017, 1010]

status_log = []
threshold_map = {
    'critical_low': 20.0,
    'critical_high': 29.0
}

for temp in temperature_readings:
    analyze_component_health(temp, threshold_map, status_log)

# Decoy function - never called
def compute_thermal_gradient(seq):
    grad = 0
    for i in range(1, len(seq)):
        grad += abs(seq[i] - seq[i-1])
    return grad * 1.5

# Another red herring: unused transformation
def transform_sequence(data, factor=1.1):
    processed = []
    for x in data:
        processed.append(round(x * factor, 2))
    return processed

humidity_normalized = transform_sequence(humidity_readings, 0.9)

# Real computational path begins here
def preprocess_metrics(raw_data):
    cleaned = []
    for val in raw_data:
        str_val = f'{val:.1f}'
        if str_val.endswith('.0'):
            cleaned.append(int(val))
        else:
            cleaned.append(round(val + 0.1, 1))
    return cleaned

def calculate_weighted_sum(values, weights):
    total = 0.0
    for v, w in zip(values, weights):
        total += v * w
    return total

def extract_key_features(data_list):
    features = {}
    features['peak'] = max(data_list)
    features['baseline'] = sum(1 for x in data_list if x >= 25.0)
    features['stability'] = len([x for x in data_list if 24.0 <= x <= 26.0])
    return features

def build_benchmark_profile(features):
    profile = {}
    profile['efficiency'] = features['baseline'] * 2.5
    profile['consistency'] = features['stability'] / 6.0
    profile['headroom'] = (30.0 - features['peak']) * 1.75
    return profile

def apply_calibration_curve(value, method='sigmoid'):
    if method == 'linear':
        return value * 0.8
    elif method == 'sigmoid':
        import math
        return value / (1 + math.exp(-value/10))
    else:
        return value

def evaluate_integrity(profile):
    # Distraction: complex but unused integrity check
    checksum = 0
    for k, v in profile.items():
        checksum ^= int(v)
    return checksum % 7 == 0

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Actual relevant data
metrics_raw = [23.4, 25.1, 22.8, 27.5, 30.0, 28.3]
benchmark_weights = [0.1, 0.15, 0.1, 0.2, 0.25, 0.2]

# Processing steps with embedded distractions
processed_metrics = preprocess_metrics(metrics_raw)

# Extract only numeric components for feature engineering
digits_only = []
for m in processed_metrics:
    m_str = str(m).replace('.', '')
    for char in m_str:
        if char.isdigit():
            digits_only.append(int(char))

distinct_digits = list(set(digits_only))
distinct_digits.sort()

# Real path: feature extraction
features = extract_key_features(processed_metrics)
profile = build_benchmark_profile(features)

calibrated_efficiency = apply_calibration_curve(profile['efficiency'], 'sigmoid')
calibrated_headroom = apply_calibration_curve(profile['headroom'], 'linear')

# Final computation chain
aggregate_metric = calculate_weighted_sum(
    [calibrated_efficiency, profile['consistency'], calibrated_headroom],
    [0.4, 0.3, 0.3]
)

# Misleading alternate paths
possible_alternatives = [
    profile['efficiency'] + profile['consistency'],
    calibrated_efficiency * 2,
    aggregate_metric * 1.15
]

# Key decision point with string-based filtering
flags = []
for alt in possible_alternatives:
    flag_str = f"ALT_{int(alt)}"
    if '5' in flag_str:
        flags.append(flag_str)

# Critical assignment
final_score = int(round(aggregate_metric * 100))

# Output requirement
print(f"Result: {final_score}")