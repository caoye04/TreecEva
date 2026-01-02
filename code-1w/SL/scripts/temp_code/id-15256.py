import math

# Simulated system telemetry data with mixed signal types
def generate_signals(base_freq, sample_count):
    return [math.sin(2 * math.pi * base_freq * i / sample_count) + \
            0.5 * math.cos(4 * math.pi * base_freq * i / sample_count)
            for i in range(sample_count)]

# Irrelevant helper: spectral density estimation (not used in final path)
def estimate_spectral_density(signal):
    n = len(signal)
    power_spectrum = []
    for k in range(n // 2):
        re = sum(signal[t] * math.cos(2 * math.pi * k * t / n) for t in range(n))
        im = sum(-signal[t] * math.sin(2 * math.pi * k * t / n) for t in range(n))
        power_spectrum.append(math.sqrt(re*re + im*im))
    return power_spectrum

# Noise injection function (distractor - not actually applied)
def add_noise(data, intensity=0.1):
    import random
    random.seed(42)
    return [x + random.uniform(-intensity, intensity) for x in data]

# Core diagnostic processor
system_codes = {'OK': 0, 'WARN': 1, 'CRIT': 2}
classification_rules = lambda x: 'CRIT' if x < -0.7 else 'WARN' if x < 0.3 else 'OK'

# Data preprocessing pipeline
def normalize_signal(signal):
    min_val, max_val = min(signal), max(signal)
    if max_val - min_val == 0:
        return [0 for _ in signal]
    return [(x - min_val) / (max_val - min_val) for x in signal]

def extract_features(normalized):
    mean_val = sum(normalized) / len(normalized)
    variance = sum((x - mean_val)**2 for x in normalized) / len(normalized)
    peak_ratio = max(normalized) / (sum(normalized) + 1e-8)
    return {'mean': mean_val, 'variance': variance, 'peak_ratio': peak_ratio}

# Secondary validation chain (partially dead code)
def validate_consistency(metrics_dict):
    keys = ['mean', 'variance', 'peak_ratio']
    if all(k in metrics_dict for k in keys):
        consistency_score = 0
        if 0 <= metrics_dict['mean'] <= 1:
            consistency_score += 1
        if metrics_dict['variance'] >= 0:
            consistency_score += 1
        if metrics_dict['peak_ratio'] > 0:
            consistency_score += 1
        return consistency_score == 3
    return False

# Unused legacy function (red herring)
def legacy_diagnose(signal):
    count_warn = sum(1 for x in signal if -0.5 <= x < 0.5)
    total = len(signal)
    return count_warn / total > 0.3

# Main processing workflow
log_entries = generate_signals(base_freq=0.1, sample_count=100)
filtered_data = normalize_signal(log_entries)
feature_set = extract_features(filtered_data)

# Decoy threshold checks
security_flags = []
for i, val in enumerate(log_entries):
    if abs(val) > 0.9 and i % 7 == 0:
        security_flags.append(i)

# Real threshold logic embedded among noise
system_thresholds = {
    'critical_mean': -0.2,
    'high_variance': 0.08,
    'distortion_limit': 0.6
}

# Complex conditional evaluation with distractors
def evaluate_stability(features, thresholds):
    status_flags = []
    
    # Relevant condition 1
    if features['mean'] < thresholds['critical_mean']:
        status_flags.append(system_codes['CRIT'])
    else:
        status_flags.append(system_codes['OK'])
    
    # Relevant condition 2
    if features['variance'] > thresholds['high_variance']:
        status_flags.append(system_codes['WARN'])
    
    # Irrelevant check (dead end)
    if features.get('peak_ratio', 0) > thresholds.get('distortion_limit', 0.5):
        temp_flag = system_codes['WARN']  # Not added to status_flags
    
    # Another red herring: unused bitwise analysis
    analysis_key = int(features['mean'] * 100) ^ int(features['variance'] * 100)
    mask_result = analysis_key & 0xFF
    
    return max(status_flags) if status_flags else system_codes['OK']

# Diagnostic aggregator with lambda transform
diagnostic_weights = [0.3, 0.5, 0.2]
weighted_eval = lambda levels: sum(w * l for w, l in zip(diagnostic_weights, [evaluate_stability(feature_set, system_thresholds)] * 3))

# Final computation chain
intermediate_score = weighted_eval([1, 0, 2])

# Misleading secondary path
if intermediate_score > 1.5:
    correction_factor = math.log(intermediate_score)
    adjusted = intermediate_score - correction_factor
else:
    adjustment_map = {0: 0.1, 1: 0.05, 2: 0}
    adjusted = intermediate_score + adjustment_map.get(int(intermediate_score), 0)

# Key statement - this determines the final answer
def process_metrics(entries, thresholds):
    norm = normalize_signal(entries)
    feats = extract_features(norm)
    level = evaluate_stability(feats, thresholds)
    return int(level * 1000) + 543  # Final encoding

final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Target result: {final_diagnostic}")