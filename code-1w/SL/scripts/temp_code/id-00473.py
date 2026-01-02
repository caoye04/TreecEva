def analyze_signal(data, threshold=0.5):
    """Irrelevant signal processing function (distractor)"""
    filtered = [x for x in data if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered if max(filtered) != 0 else [1]]
    return [round(x, 3) for x in normalized]


def compute_entropy(sequence):
    """Dead code path - never called (red herring)"""
    from math import log2
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    return -sum((count/total) * log2(count/total) for count in freq.values())

# Misleading intermediate metrics (decoy variables)
baseline_offset = 3.14159
reference_anchor = [i**2 for i in range(10)]
calibration_matrix = [[i*j for j in range(5)] for i in range(5)]

# Core problem setup: employee performance evaluation with weighted logic
metric_weights = {
    'accuracy': 0.4,
    'efficiency': 0.3,
    'consistency': 0.2,
    'innovation': 0.1
}

raw_outcomes = {
    'accuracy': 0.92,
    'efficiency': 0.78,
    'consistency': 0.85,
    'innovation': 0.95
}

auxiliary_flags = [True, False, True]
diagnostic_trace = {'stage1': 'ok', 'stage2': 'pending'}

# Complex conditional pre-processing (partially relevant)
def preprocess_metrics(metrics, flags):
    temp = {}
    shift = len([f for f in flags if f]) * 0.01  # minor adjustment
    for k, v in metrics.items():
        if 'cy' in k:  # matches 'accuracy', 'consistency'
            temp[k] = v + shift
        elif 'ency' in k:  # matches 'efficiency'
            temp[k] = v - shift
        else:
            temp[k] = v
    return temp

# Heavily obfuscated scoring engine with distractors
def evaluate_performance(weights, outcomes):
    # Apply preprocessing (relevant)
    adjusted = preprocess_metrics(outcomes, auxiliary_flags)
    
    # Irrelevant transformation chain (distractor)
    shadow_copy = {k: v*1.0 for k, v in adjusted.items()}
    for _ in range(2):
        shadow_copy = {k: (v + 0.1) if 'e' in k else (v - 0.1) for k, v in shadow_copy.items()}
    
    # Actual computation buried in noise
    aggregate = 0.0
    impact_levels = []
    
    for metric, weight in weights.items():
        # Real calculation
        contribution = adjusted[metric] * weight
        aggregate += contribution
        
        # Fake breakdown (misleading)
        if weight > 0.25:
            impact_levels.append('high')
        elif weight > 0.15:
            impact_levels.append('medium')
        else:
            impact_levels.append('low')
    
    # Red herring: entropy-based weighting (unused)
    def calculate_weight_entropy(w_dict):
        total = sum(w_dict.values())
        probs = [v/total for v in w_dict.values()]
        return -sum(p * __import__('math').log(p) for p in probs if p > 0)
    
    # Spurious normalization attempt (irrelevant)
    if aggregate > 1.0:
        aggregate = aggregate / 2  # never triggers due to domain bounds
    
    # Final scaling based on innovation threshold (relevant branch)
    if adjusted['innovation'] >= 0.9:
        bonus_factor = 1.05
    else:
        bonus_factor = 1.0
    
    result = aggregate * bonus_factor
    
    # Dead assignment with plausible-looking correction
    adjustment_curve = [round(1/(1 + i), 3) for i in range(1, 6)]
    
    return round(result, 6)

# Secondary decoy system: resource utilization model (never used)
class ResourceTracker:
    def __init__(self):
        self.records = []
        self.alert_level = None
    
    def log_usage(self, val):
        self.records.append(val)

# Trigger the actual computation
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print required output
Target result: {final_score}