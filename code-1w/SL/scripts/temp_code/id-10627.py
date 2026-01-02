from collections import defaultdict, Counter
import math

# Simulated system telemetry and health monitoring with distractors
def collect_telemetry():
    raw_signals = [0.88, 0.92, 0.76, 0.94, 0.85, 0.67, 0.91, 0.83]
    noise_floor = 0.1 * sum(raw_signals) / len(raw_signals)
    adjusted = [x - noise_floor for x in raw_signals]
    return {'signals': adjusted, 'timestamp': 1678823456, 'version': '2.3.1'}

def validate_checksum(data):
    # Irrelevant validation not used in final path
    checksum = 0
    for i, val in enumerate(data['signals']):
        checksum ^= int(val * 100) + i
    return checksum % 17 == 0

def deprecated_normalization(signal_list):
    # Dead code path - never called
    return [math.tanh(x) for x in signal_list]

def compute_entropy(values):
    freqs = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freqs.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def analyze_outliers(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    threshold = mean_val - 1.5 * std_dev
    outliers = [x for x in data if x < threshold]
    return len(outliers) > 2

def derive_key_metric(signal_data):
    # Relevant but obfuscated metric calculation
    magnitude = sum(x**2 for x in signal_data) ** 0.5
    sparsity = len([x for x in signal_data if x < 0.75])
    return magnitude - sparsity * 0.1

def generate_report_metadata():
    # Distractor: generates unused metadata
    meta = defaultdict(str)
    meta['author'] = 'sysadmin'
    meta['class'] = 'diagnostic'
    meta['priority'] = 'low'
    return dict(meta)

def filter_anomalies(stream):
    # Misleading function that appears important but is bypassed
    window_size = 3
    filtered = []
    for i in range(len(stream)):
        window = stream[max(0, i - window_size):i+1]
        avg = sum(window) / len(window)
        if abs(stream[i] - avg) < 0.2:
            filtered.append(stream[i])
    return filtered

def extract_diagnostic_features(telemetry):
    signals = telemetry['signals']
    
    # Multiple layers of processing with decoys
    feature_set = {}
    
    # Real feature - used later
    feature_set['entropy'] = compute_entropy([round(x, 1) for x in signals])
    
    # Red herring features
    feature_set['peak'] = max(signals)
    feature_set['stability'] = len(signals) - len(set(round(x, 2) for x in signals))
    feature_set['decay_rate'] = (signals[0] - signals[-1]) / len(signals) if len(signals) > 1 else 0
    
    # Another distraction
    if len(signals) % 2 == 0:
        feature_set['symmetric'] = True
        temp = [signals[i] * signals[-i-1] for i in range(len(signals)//2)]
        feature_set['product_trace'] = sum(temp)
    
    return feature_set

def evaluate_health_status(features, threshold_map):
    score = 100.0
    
    # Health deductions based on features
    if features['entropy'] < threshold_map['entropy_low']:
        score -= 15.0
    elif features['entropy'] > threshold_map['entropy_high']:
        score -= 10.0
    
    if features.get('stability', 0) > 3:
        score -= 5.0  # Misleading - stability is noisy indicator
    
    if 'product_trace' in features and features['product_trace'] > 2.0:
        score += 3.0  # Distraction: symmetric boost rarely applies
    
    return score

def process_metrics(log_data, state):
    # Core function with key logic buried in noise
    features = extract_diagnostic_features(log_data)
    
    # Threshold configuration (some irrelevant)
    thresholds = {
        'entropy_low': 2.1,
        'entropy_high': 3.0,
        'outlier_count': 2,
        'magnitude_base': 1.5
    }
    
    base_diagnostic = derive_key_metric(log_data['signals'])
    health_score = evaluate_health_status(features, thresholds)
    
    # Critical transformation - depends only on base_diagnostic and entropy
    adjustment_factor = 0.8 if features['entropy'] >= 2.5 else 1.2
    intermediate = base_diagnostic * adjustment_factor
    
    # Fake branches that don't affect outcome
    if health_score > 90:
        intermediate += 0.05
    elif health_score < 70:
        intermediate -= 0.05
    
    # Final computation - only this matters
    final_diagnostic = int(intermediate * 100) / 100.0
    
    # Dead assignment
    final_diagnostic = round(final_diagnostic + 0.001, 2)  # No effect due to float precision
    
    return final_diagnostic

# Main execution flow
telemetry_log = collect_telemetry()
system_state = {'mode': 'active', 'role': 'primary', 'generation': 2}

# Unused variables - red herrings
baseline_ref = deprecated_normalization(telemetry_log['signals'])
report_header = generate_report_metadata()
anomaly_filtered = filter_anomalies(telemetry_log['signals'])
checksum_valid = validate_checksum(telemetry_log)

# Key statement
final_diagnostic = process_metrics(telemetry_log, system_state)

print(f"Result: {final_diagnostic}")