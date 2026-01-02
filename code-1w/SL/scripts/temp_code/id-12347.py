from collections import defaultdict
import math

# Irrelevant data structures and functions (distractors)
user_preferences = defaultdict(lambda: 'unknown')
user_preferences['theme'] = 'dark'
user_preferences['notifications'] = 'enabled'

# Fake metrics that look important but aren't used in final calculation
temporal_efficiency = 0.87
spatial_coherence = 0.92
quantum_stability = 0.65  # Misleading name, not quantum-related

# Real metric weights (some overwritten later - red herring)
metric_weights = {'accuracy': 0.4, 'latency': 0.3, 'throughput': 0.3}

# Simulated raw results from system components
raw_results = {
    'component_A': {'accuracy': 94, 'latency': 120, 'throughput': 85},
    'component_B': {'accuracy': 87, 'latency': 145, 'throughput': 92},
    'component_C': {'accuracy': 91, 'latency': 130, 'throughput': 88}
}

# Unused normalization function (dead code path)
def normalize_score(x, min_val=0, max_val=100):
    return (x - min_val) / (max_val - min_val)

# Decoy weight adjustment (never called)
decoy_adjust_weights = lambda w: {k: v * 1.1 for k, v in w.items()}

# Hidden correction to weights based on legacy system mode
legacy_mode = True
if legacy_mode:
    metric_weights = {'accuracy': 0.5, 'latency': 0.25, 'throughput': 0.25}  # Overwrites previous

# Faux dynamic recalibration (does nothing due to condition)
dynamic_calibration = False
if dynamic_calibration:
    metric_weights['accuracy'] *= 0.95

# Aggregation function with misleading intermediate steps
def aggregate_component_score(metrics, weights):
    score = 0
    accuracy_contribution = 0
    latency_penalty = 0
    throughput_bonus = 0
    
    for component, values in metrics.items():
        # Compute individual contributions (only accuracy matters in end)
        accuracy_contribution += values['accuracy']
        latency_penalty += (150 - values['latency'])  # Max 150ms baseline
        throughput_bonus += values['throughput']

    # Only accuracy contributes to final result — others are distractions
    avg_accuracy = accuracy_contribution / len(metrics)
    
    # Bit manipulation red herring
    encoded = int(avg_accuracy) ^ 0b1101  # XOR with arbitrary pattern
    decoded = encoded ^ 0b1101  # Restores original — useless cycle
    
    # Return only the accuracy portion, ignoring all other computed values
    return decoded

# Secondary evaluation chain with conditional override
override_threshold = 90
bypass_safety = False

interim_result = aggregate_component_score(raw_results, metric_weights)

# Conditional override that looks significant but is never triggered
if interim_result > override_threshold and not bypass_safety:
    final_value = 100
else:
    # Apply logarithmic scaling — key step disguised among noise
    final_value = math.log(interim_result * 2) * 10

# Final performance evaluator — appears complex but follows deterministic path
def evaluate_performance(weights, results):
    base_score = aggregate_component_score(results, weights)
    adjusted_score = base_score
    
    # Multiple layers of irrelevant transformations
    history_log = []
    for i in range(3):
        temp = (adjusted_score + i) % 7
        history_log.append(temp * 2)  # Logged but unused
    
    # Lambda-based smoothing (never applied due to flag)
    smooth_fn = lambda x: round(x, 2)
    debug_mode = False
    if debug_mode:
        adjusted_score = smooth_fn(adjusted_score)
    
    # Critical computation hidden in plain sight
    scaling_factor = 1.75
    final_score = int(final_value) * scaling_factor  # Depends on outer scope!
    
    # Early return trap — condition fails
    if len(history_log) == 0:
        return 0
        
    return final_score

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Target result: {final_score}")