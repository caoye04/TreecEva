import math

# Simulated sensor data processing with embedded logic chain
def fetch_sensor_readings():
    raw = [i * 0.7 + (i % 3) for i in range(15)]
    return raw[::2]  # slicing: every other reading

def normalize(data):
    mean = sum(data) / len(data)
    return [x - mean for x in data]

def apply_filter(sequence):
    filtered = []
    for i in range(len(sequence)):
        if i == 0:
            filtered.append(sequence[i])
        else:
            val = 0.6 * sequence[i] + 0.4 * filtered[i-1]
            filtered.append(round(val, 6))
    return filtered

def compute_entropy(arr):
    # Irrelevant distractor function – looks important but unused
    total = sum(abs(x) for x in arr)
    if total == 0:
        return 0.0
    probs = [abs(x) / total for x in arr]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def evaluate_stability(readings):
    diffs = [readings[i+1] - readings[i] for i in range(len(readings)-1)]
    variance = sum((x - sum(diffs)/len(diffs))**2 for x in diffs) / len(diffs)
    return variance < 0.15

def extract_features(signal):
    # Real feature extraction path
    amp = max(signal) - min(signal)
    peaks = [i for i in range(1, len(signal)-1) if signal[i-1] < signal[i] > signal[i+1]]
    return {'amplitude': amp, 'peak_count': len(peaks), 'energy': sum(x**2 for x in signal)}

def legacy_calibrate(buf):  # Dead code path - never called
    adjustment = 0.95
    return [x * adjustment for x in buf]

def transform_signal(data, method='advanced'):
    if method == 'basic':
        return [math.sin(x) for x in data]
    elif method == 'advanced':
        # Composite transformation with slicing and arithmetic
        shifted = [data[i] + math.cos(i * 0.5) for i in range(len(data))]
        smoothed = apply_filter(shifted)
        return smoothed[:len(smoothed)-2]  # slicing out last two elements
    else:
        return data

def analyze_pattern(dataset, params):
    # Core logic branch
    if not params['active'] or dataset is None:
        return -999

    features = extract_features(dataset)

    # Distractor block: complex-looking but unused calculation
    shadow_metric = 0
    for k in features:
        temp_val = 0
        for char in k:
            temp_val += ord(char) % 3
        shadow_metric += temp_val * features[k]
    # End of red herring

    base_score = features['amplitude'] * 100
    peak_bonus = features['peak_count'] * 25
    energy_penalty = int(features['energy'] // 5)

    # Conditional override based on config threshold
    if params['threshold'] > 0:
        if features['energy'] > params['threshold']:
            base_score *= 0.5

    result = base_score + peak_bonus - energy_penalty

    # Secondary validation gate
    if evaluate_stability(dataset):
        result += 50

    return int(result)

# Misleading initialization block (distractor variables)
diag_mode = True
system_status = "NORMAL"
buffer_cache = [0]*20
temp_log = {"start": 1, "stage": "init", "valid": False}

# Main execution flow
sensor_data = fetch_sensor_readings()  # Initial data acquisition
normalized_data = normalize(sensor_data)
filtered_data = apply_filter(normalized_data)
transformed_data = transform_signal(filtered_data, method='advanced')

# Configuration map with decoy keys
config = {
    'active': True,
    'threshold': 1.8,
    'mode': 'diagnostic',
    'debug_level': 9,
    'timeout_ms': 500,
    'retry_limit': 3
}

# Critical statement
final_diagnostic = analyze_pattern(transformed_data, config)

print(f"Result: {final_diagnostic}")