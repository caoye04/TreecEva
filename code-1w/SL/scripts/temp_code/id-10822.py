from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return entropy

# Misleading performance metric (not actually used in final logic)
def legacy_metric(values):
    weighted_sum = 0
    for i, v in enumerate(values):
        weighted_sum += v * (0.9 ** i)
    return weighted_sum / len(values) if values else 0

# Core transformation pipeline (some stages are red herrings)
def preprocess_signal(raw_signal):
    filtered = [x for x in raw_signal if x >= 0]
    normalized = [x / max(filtered) for x in filtered] if filtered else []
    smoothed = []
    for i in range(len(normalized)):
        window = normalized[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))
    return smoothed

def extract_features(signal):
    features = defaultdict(float)
    features['peak'] = max(signal) if signal else 0
    features['variance'] = sum((x - sum(signal)/len(signal))**2 for x in signal)/len(signal) if signal else 0
    features['trend'] = sum(signal[i+1] - signal[i] for i in range(len(signal)-1)) if len(signal) > 1 else 0
    features['complexity'] = len([x for x in signal if x > 0.5])
    return features

# Distractor: unused feature engineering
def generate_synthetic_metrics(base):
    synthetic = {}
    for key in base:
        synthetic[f'{key}_adj'] = base[key] * 1.23
        synthetic[f'{key}_norm'] = abs(base[key] - 0.5) * 2
    return synthetic

# Real evaluation logic buried among distractions
def assess_stability(feature_set):
    score = 0
    if feature_set['peak'] > 0.7:
        score += 20
    if feature_set['variance'] < 0.1:
        score += 30
    if feature_set['trend'] > 0:
        score += 25
    # This condition is critical but obscured
    if feature_set['complexity'] >= 3 and feature_set['peak'] > 0.6:
        score += 45
    return score

def adjust_for_baseline(stability_score, baseline):
    adjustment = 0
    if baseline > 75:
        adjustment = -15
    elif baseline < 50:
        adjustment = 10
    else:
        adjustment = 5
    return stability_score + adjustment

# Main evaluation (only this path matters)
def evaluate_performance(metrics, base_ref):
    # This slicing masks relevance — only first 6 elements matter
    truncated = metrics['signal'][:6]
    processed = preprocess_signal(truncated)
    feats = extract_features(processed)
    
    # Dead code path — looks important but unused
    aux_metrics = generate_synthetic_metrics(feats)
    aux_metrics['diagnostic'] = calculate_entropy([int(f*10) for f in processed])
    
    # Actual scoring chain
    raw_stability = assess_stability(feats)
    adjusted = adjust_for_baseline(raw_stability, base_ref)
    return int(adjusted)

# Decoy data structures
dummy_logs = [
    {'event': 'init', 'ts': 1001, 'value': 23.1},
    {'event': 'poll', 'ts': 1005, 'value': 25.3},
    {'event': 'poll', 'ts': 1010, 'value': 24.9}
]

historical_baselines = {
    'Q1': 67, 'Q2': 72, 'Q3': 58, 'Q4': 81,
    'thresholds': [0.5, 0.75, 0.9],
    'weights': (0.1, 0.3, 0.6)
}

# Critical input data — subtle manipulation via slicing and filtering
raw_input_stream = [12, -5, 18, 23, -8, 15, 16, 20, -3]  # Only first 6 non-negative: [12,18,23,15,16,20]
baseline_reference = 48

metric_data = {
    'source': 'sensor_array_7',
    'version': '3.2.1',
    'signal': raw_input_stream,
    'timestamp': 1625097600
}

# Execution with irrelevant intermediate prints (distractors)
print(f"Processing signal of length {len(metric_data['signal'])}")
print(f"Baseline context: {baseline_reference}")

# Key statement
final_score = evaluate_performance(metric_data, baseline_reference)

# Output required format
Target result: {final_score}