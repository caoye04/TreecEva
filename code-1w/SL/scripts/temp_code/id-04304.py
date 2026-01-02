def analyze_signal(pattern, threshold=5):
    if len(pattern) < 3:
        return 0
    count = 0
    for i in range(1, len(pattern) - 1):
        if pattern[i] > pattern[i-1] and pattern[i] > pattern[i+1]:
            count += 1
    return count * 2

# Irrelevant helper function (decoy)
def normalize_values(data):
    max_val = max(data) if data else 1
    return [x / max_val for x in data]

# Unused transformation chain
def transform_sequence(seq):
    return [x ** 0.5 for x in seq if x > 0][::-1]

# Distractor: complex but unused scoring mechanism
class ScoringEngine:
    def __init__(self):
        self.baseline = 10
    
    def compute(self, values):
        return sum(v ** 2 for v in values) / (len(values) + 1)

# Another red herring: time decay model
def apply_temporal_decay(weight, age):
    return weight * (0.9 ** age)

# Real logic begins here
def extract_features(raw_data):
    features = {}
    features['peaks'] = analyze_signal(raw_data)
    features['mean'] = sum(raw_data) / len(raw_data)
    features['trend'] = raw_data[-1] - raw_data[0]
    return features

# Conditional weighting based on data shape
def determine_weighting_strategy(data):
    n = len(data)
    if n > 6:
        return {'peaks': 3, 'mean': 2, 'trend': 1}
    elif n > 3:
        return {'peaks': 2, 'mean': 3, 'trend': 2}
    else:
        return {'peaks': 1, 'mean': 1, 'trend': 4}

# Core evaluation with slicing and conditional expression
def evaluate_performance(metrics, weights=None):
    ordered_keys = sorted(metrics.keys())
    slice_center = metrics['mean'] > 4.5
    focus_set = ordered_keys[1:] if slice_center else ordered_keys[:2]
    
    # Dictionary-based dynamic weighting
    default_weights = {'peaks': 2, 'mean': 2, 'trend': 2}
    effective_weights = weights or default_weights
    
    score = 0
    for key in focus_set:
        weight = effective_weights.get(key, 1)
        contribution = metrics[key] * weight
        # Conditional adjustment
        score += contribution if contribution > 0 else -contribution / 2
    
    # Final nonlinear adjustment
    adjustment = 1.5 if metrics['peaks'] >= 4 else 0.8
    return int(score * adjustment)

# Setup realistic dataset
signal_data = [2, 7, 4, 8, 3, 9, 1]
metric_data = extract_features(signal_data)

# Irrelevant intermediate computations
user_profile = {"id": "U9283", "access": "premium"}
dummy_calc = sum(x * x for x in range(5))  # Dead computation

# Unused alternative path
if False:
    alt_metrics = {k: v * 1.1 for k, v in metric_data.items()}
    final_score = evaluate_performance(alt_metrics)

# User-defined weights (used in real path)
user_weights = {'peaks': 3, 'mean': 1, 'trend': 4}

# Key execution point
final_score = evaluate_performance(metric_data, user_weights)

# Print result as required
print(f"Target result: {final_score}")