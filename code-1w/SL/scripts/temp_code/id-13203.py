import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw = [0.88, -1.02, 3.15, 0.07, -2.21, 4.99, 1.13]
    offset = 0.5
    adjusted = [x + offset for x in raw]
    return adjusted

def apply_filter(data):
    # Irrelevant smoothing filter (not used in final path)
    smoothed = []
    for i in range(len(data)):
        if i == 0 or i == len(data) - 1:
            smoothed.append(data[i])
        else:
            smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    return smoothed

def generate_checksum(sequence):
    # Distractor: computes a checksum but not used in main logic
    chk = 0
    for val in sequence:
        chk ^= int(val * 10) & 0xFF
    return chk

def normalize_vector(vec):
    mag = math.sqrt(sum(x ** 2 for x in vec))
    return [x / mag for x in vec] if mag > 0 else vec

def evaluate_stability(index, value):
    # Complex conditional expression as red herring
    status = 'stable' if abs(value) < 1.5 else 'fluctuating'
    phase = 'peak' if value > 0 else 'trough'
    confidence = 0.9 if (index % 2 == 0) ^ (value > 0) else 0.6
    return {'status': status, 'phase': phase, 'confidence': confidence}

def compute_entropy(values):
    # Unused advanced metric
    total = sum(abs(v) for v in values)
    if total == 0:
        return 0.0
    probs = [abs(v) / total for v in values]
    return -sum(p * math.log2(p) for p in probs if p > 0)

def extract_features(data):
    # Real preprocessing step embedded among distractions
    features = {}
    features['peak_count'] = sum(1 for x in data if x > 2.0)
    features['avg_magnitude'] = sum(abs(x) for x in data) / len(data)
    features['trend'] = data[-1] - data[0]
    features['zero_crossings'] = sum(1 for i in range(1, len(data)) if data[i-1] * data[i] < 0)
    return features

def build_threshold_map(config_level=3):
    # Creates mapping used later in analysis
    base = {'critical': 3.0, 'warning': 1.8, 'info': 0.5}
    scale = 1.2 ** config_level
    return {k: v * scale for k, v in base.items()}

def analyze_signal(features, thresholds):
    score = 0
    
    # Actual logic steps
    if features['peak_count'] > 2:
        score += 15
    if features['avg_magnitude'] > thresholds['warning']:
        score += 10
    if features['trend'] > 0:
        score += 5
    if features['zero_crossings'] >= 3:
        score -= 8
    
    # Final nonlinear transformation
    adjusted_score = int((score ** 1.5) + 22.7)
    
    # Misleading secondary computation (dead end)
    auxiliary_diag = 'normal' if score < 12 else 'elevated'
    confidence_interval = (0.75, 0.92) if score % 2 == 0 else (0.68, 0.85)
    
    return adjusted_score

# Main execution flow
samples = collect_samples()

# Irrelevant transformations
filtered = apply_filter(samples)
checksum = generate_checksum(samples)
normalized = normalize_vector(samples)
entropy = compute_entropy(normalized)

# Key feature extraction (relevant)
features = extract_features(samples)

# Build actual threshold map used in analysis
threshold_map = build_threshold_map(config_level=3)

# Dead code path: simulate alternate workflow
if len(samples) % 2 == 0:
    temp_analysis = {"dummy": "placeholder"}
    backup_result = sum(f * 0.1 for f in features.values())
elif checksum > 100:
    temp_analysis = None
else:
    # This branch runs but doesn't affect final result
    temp_analysis = {'mode': 'safe', 'level': 1}
    fallback_score = math.floor(features['avg_magnitude'] * 2)

# Stability evaluation - looks important but unused
stability_reports = [evaluate_stability(i, val) for i, val in enumerate(samples)]

# String manipulation distractor
log_tag = "DIAG-" + "-".join(f'{int(f)}' for f in features.values()[:2])
diag_flag = log_tag.replace('DIAG', 'FLAG').lower() if 'info' in threshold_map else 'default'

# Set operation red herring
critical_keys = {'critical', 'warning'}
active_alerts = critical_keys & set(threshold_map.keys())
alert_count = len(active_alerts)

# Conditional expression influencing nothing
system_state = 'active' if entropy > 0.5 else 'idle'

# Core relevant assignment
processed_data = extract_features(samples)

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")