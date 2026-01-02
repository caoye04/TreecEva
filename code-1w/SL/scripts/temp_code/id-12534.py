from collections import defaultdict, Counter
import math

# Simulated sensor data processing for autonomous drone navigation
raw_readings = [145, 176, 134, 198, 204, 123, 167, 188, 156, 177, 199, 133]

def normalize(value, min_val=100, max_val=250):
    return (value - min_val) / (max_val - min_val)

def moving_average(data, window=3):
    smoothed = []
    for i in range(len(data) - window + 1):
        smoothed.append(sum(data[i:i+window]) / window)
    return smoothed

def analyze_outliers(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [x for x in data if abs(x - mean) > 2 * std_dev]

def filter_noise(readings):
    # Irrelevant noise filtering (distractor)
    filtered = [r for r in readings if 120 < r < 210]
    return filtered

def compute_checksum(sequence):
    # Decoy function – looks important but unused in final logic
    chk = 0
    for val in sequence:
        chk ^= val
        chk = (chk * 31) % 10007
    return chk

def extract_features(data):
    features = defaultdict(float)
    features['mean'] = sum(data) / len(data)
    features['peak'] = max(data)
    features['stability'] = sum(1 for x in data if abs(x - features['mean']) < 15)
    features['trend'] = data[-1] - data[0]
    return features

def calculate_entropy(data):
    count = Counter(data)
    total = len(data)
    entropy = 0.0
    for freq in count.values():n        prob = freq / total
        entropy -= prob * math.log(prob)
    return round(entropy, 4)

def score_consistency(feature_set):
    base = feature_set['stability']
    adjustment = 0.1 if feature_set['trend'] > 0 else -0.1
    return base + adjustment

def weight_metrics(metrics_dict, config_profile='balanced'):
    profiles = {
        'aggressive': [1.2, 0.8, 1.5, 0.5],
        'conservative': [0.8, 1.2, 0.5, 1.5],
        'balanced': [1.0, 1.0, 1.0, 1.0]
    }
    weights = profiles.get(config_profile, [1.0]*4)
    weighted = {}
    keys = list(metrics_dict.keys())
    for i, key in enumerate(keys[:4]):
        weighted[key] = metrics_dict[key] * weights[i]
    return weighted

def evaluate_performance(metrics, w):
    score = 0.0
    for k in w:
        if k in metrics:
            score += metrics[k] * w[k]
    # Final nonlinear transformation
    score = math.tanh(score / 100) * 100
    return int(score)

# Irrelevant preprocessing chain (dead path)
smoothed_readings = moving_average(raw_readings, 3)
analyzed_outliers = analyze_outliers(smoothed_readings)
cleaned_signal = filter_noise(smoothed_readings)

# Core relevant data flow
normalized = [normalize(x) for x in raw_readings]
main_features = extract_features(normalized)
main_features['entropy'] = calculate_entropy([int(x*100) for x in normalized])

# Red herring: complex but unused structure
system_log = {
    'checksum': compute_checksum(raw_readings),
    'outlier_count': len(analyzed_outliers),
    'processed_length': len(cleaned_signal)
}

# Assign weights based on configuration
weights = weight_metrics(main_features, 'balanced')

# Key computation — answer depends on this
final_score = evaluate_performance(main_features, weights)

# Additional distraction: parallel irrelevant calculation
shadow_metrics = {k: v * 0.5 for k, v in main_features.items()}
final_shadow = evaluate_performance(shadow_metrics, weights)

# Output target result
print(f"Result: {final_score}")