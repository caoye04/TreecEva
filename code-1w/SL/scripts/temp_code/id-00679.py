from collections import defaultdict
import math

# Simulated sensor fusion system for autonomous drone navigation
base_signals = [0.87, 0.92, 0.65, 0.44, 0.91]
decoy_signals = [0.12, 0.34, 0.56, 0.78, 0.90]

# Irrelevant transformation (red herring)
def transform_signal(x):
    return (x ** 2 + 3.1) / 1.7

def process_calibration(data):
    calibrated = []
    for d in data:
        calibrated.append(d * 0.98 + 0.02)
    return calibrated

# Unused function - dead code path
def legacy_normalization(vec):
    mag = sum(x**2 for x in vec) ** 0.5
    return [x/mag for x in vec] if mag else vec

# Decoy metric with misleading intermediate
signal_power = sum(s**2 for s in base_signals)
noise_floor = sum(d**2 for d in decoy_signals)
effective_ratio = signal_power / (noise_floor + 1e-8)

# Real processing begins here
raw_metrics = {
    'stability': base_signals[0] * 1.05,
    'accuracy': base_signals[1] * 0.98,
    'latency': base_signals[2] * 1.12,
    'throughput': base_signals[3] * 0.88,
    'reliability': base_signals[4] * 1.01
}

# Distractor: complex but unused computation
temp_analysis = [
    (base_signals[i] - decoy_signals[i]) * math.cos(i)
    for i in range(len(base_signals))
]
sum_temp = sum(abs(x) for x in temp_analysis)

# Weight initialization with decoys
weight_pool = defaultdict(float)
weight_pool['stability'] = 0.2
weight_pool['accuracy'] = 0.25
weight_pool['latency'] = 0.15
weight_pool['throughput'] = 0.1
weight_pool['reliability'] = 0.3
weight_pool['fake_metric'] = 0.0  # red herring

# Filter out zero weights (including decoy)
metric_weights = {k: v for k, v in weight_pool.items() if v > 0}

# Simulated outcome map with irrelevant entries
outcome_registry = set(['success', 'retry', 'fail', 'timeout', 'overflow'])
raw_outcomes = {
    'stability': 0.89,
    'accuracy': 0.94,
    'latency': 0.71,
    'throughput': 0.41,
    'reliability': 0.92,
    'placeholder': 0.0,  # meaningless entry
    'backup': 0.0
}

# Core evaluation logic buried in distractions
def evaluate_performance(weights, outcomes):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Key logic intermixed with filtering
    relevant_keys = set(weights.keys()) & set(outcomes.keys())
    
    for key in sorted(relevant_keys):  # alphabetical ordering affects nothing but looks intentional
        if key == 'latency':
            # Invert latency since lower is better
            normalized = 1 - outcomes[key]
        else:
            normalized = outcomes[key]
        
        contribution = weights[key] * normalized
        weighted_sum += contribution
        total_weight += weights[key]
        
        # Side computation - looks important but unused
        rolling_avg = weighted_sum / (total_weight + 1e-8)
    
    # Final adjustment based on signal ratio (distraction)
    if effective_ratio > 1.0:
        scaling_factor = 1.05
    else:
        scaling_factor = 0.95
    
    # ACTUAL answer computation
    result = weighted_sum * scaling_factor
    
    # Dead branch - never executed due to ratio > 1
    if sum_temp < 0.5:
        result *= 0.8
        
    return result

# Trigger point of interest
eval_data = process_calibration(base_signals)
final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Target result: {final_score}")