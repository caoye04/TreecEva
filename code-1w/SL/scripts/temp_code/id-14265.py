from collections import defaultdict, Counter
import math

# Simulated system log analyzer with diagnostic scoring

def preprocess_logs(raw): 
    processed = []
    for entry in raw:
        if 'ERROR' in entry['level']:
            processed.append({
                'id': entry['id'],
                'severity': len(entry['message'].split()),
                'timestamp': entry['timestamp']
            })
    return processed

# Irrelevant helper - dead code path
def deprecated_filter(data):
    return [x for x in data if x > 5]  # Unused

# Misleading normalization function (not actually used in final calculation)
def normalize_scores(scores):
    max_score = max(scores) if scores else 1
    return [s / max_score * 100 for s in scores]

# Core analysis logic
def extract_features(entries):
    feature_map = defaultdict(int)
    for e in entries:
        feature_map['total_errors'] += 1
        feature_map['cumulative_severity'] += e['severity']
        if e['severity'] > 3:
            feature_map['critical_count'] += 1
    return feature_map

def compute_entropy(values):
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total if total else 0
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 6)

# Distractor: unused statistical summary
def generate_summary(stats):
    return {
        'mean': sum(stats.values()) / len(stats),
        'min': min(stats.values()),
        'max': max(stats.values()),
        'range': max(stats.values()) - min(stats.values())
    }

# Main pattern analyzer
def analyze_pattern(logs, config):
    # Step 1: Preprocess logs
    errors = preprocess_logs(logs)
    
    # Step 2: Extract key features
    features = extract_features(errors)
    
    # Step 3: Compute derived metrics
    avg_severity = features['cumulative_severity'] / features['total_errors'] if features['total_errors'] else 0
    spike_ratio = features['critical_count'] / features['total_errors'] if features['total_errors'] else 0
    
    # Step 4: Calculate pattern entropy (based on severity distribution)
    severities = [e['severity'] for e in errors]
    entropy = compute_entropy(Counter(severities).values())
    
    # Step 5: Apply threshold rules (config-based)
    flags = 0
    if avg_severity > config['avg_thresh']:
        flags += 1
    if spike_ratio > config['spike_thresh']:
        flags += 1
    if entropy < config['entropy_floor']:
        flags += 1
    
    # Step 6: Weighted diagnostic score
    base_score = features['cumulative_severity'] * 10
    penalty = flags * 15
    bonus = int(math.ceil(avg_severity)) * 3
    
    # Step 7: Final adjustment using bitwise logic (obscure but deterministic)
    adjusted = (base_score ^ penalty) & 0xFFFF  # Mask to 16 bits
    adjusted = (adjusted + bonus) % 99997
    
    # Step 8: Final diagnostic value
    final_diagnostic = abs((adjusted * 7) // 13 + 42)
    
    # Decoy variables - irrelevant to result
    temp_debug = {'intermediate': [1,2,3], 'status': 'complete'}
    shadow_copy = features.copy()
    normalization_attempt = normalize_scores([10,20,30])
    
    return final_diagnostic

# Generate test data
raw_log_data = [
    {'id': 1, 'level': 'INFO', 'message': 'System booted', 'timestamp': 1000},
    {'id': 2, 'level': 'ERROR', 'message': 'Failed connection timeout', 'timestamp': 1005},
    {'id': 3, 'level': 'ERROR', 'message': 'Critical database failure unexpected crash', 'timestamp': 1010},
    {'id': 4, 'level': 'WARNING', 'message': 'High memory usage', 'timestamp': 1015},
    {'id': 5, 'level': 'ERROR', 'message': 'Invalid user authentication attempt', 'timestamp': 1020},
    {'id': 6, 'level': 'ERROR', 'message': 'Fatal kernel panic unrecoverable error', 'timestamp': 1025},
    {'id': 7, 'level': 'ERROR', 'message': 'Disk I/O timeout', 'timestamp': 1030}
]

thresholds = {
    'avg_thresh': 3.0,
    'spike_thresh': 0.4,
    'entropy_floor': 1.0
}

# Execute main analysis
final_diagnostic = analyze_pattern(raw_log_data, thresholds)

# Print result
print(f"Result: {final_diagnostic}")