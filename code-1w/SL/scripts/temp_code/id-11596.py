import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(x):
    return sum([i * 2 for i in x if i % 3 == 0])

# Misleading metric that looks important but isn't used in final calculation
tempting_metric = lambda seq: sum([math.sin(i) for i in seq]) / len(seq) if seq else 0

# Real processing functions
def extract_signals(raw_data):
    signals = {}
    for k, v in raw_data.items():
        if 'sensor' in k:
            clean = [x for x in v if x > -1]  # filter noise
            signals[k] = [x ** 0.5 for x in clean]  # transform
    return signals

# Decoy accumulator with complex but unused logic
def accumulate_ghost(data_dict):
    ghost_sum = 0
    for key, values in data_dict.items():
        temp_val = 0
        for v in values:
            temp_val += (v % 7) * 2.3
        ghost_sum += abs(math.cos(temp_val))
    return ghost_sum  # never used

# Core metric processor
def compute_stability(signal_list):
    if not signal_list:
        return 0.0
    diffs = [abs(signal_list[i] - signal_list[i-1]) for i in range(1, len(signal_list))]
    return round(sum(diffs) / len(diffs), 6) if diffs else 0.0

# Higher-order function factory (real use of lambda)
def make_weighted_scorer(weights):
    return lambda scores: sum(w * s for w, s in zip(weights, scores))

# Main evaluation logic
def evaluate_performance(log, criteria):
    extracted = extract_signals(log)
    
    # Irrelevant intermediate structure
    debug_snapshot = {
        'timestamp': 123456789,
        'checksum': sum([len(v) for v in log.values()]) ^ 0xABCD,
        'version': '2.1-debug'
    }
    
    # Real computation begins
    stability_scores = []
    magnitude_scores = []    

    for sensor_id, readings in extracted.items():
        # Real metrics
        stability = compute_stability(readings)
        magnitude = sum([r ** 2 for r in readings]) ** 0.5
        
        stability_scores.append(stability)
        magnitude_scores.append(magnitude)
        
        # Distractor: fake normalization that does nothing
        normalized_stab = [s / (stability + 1e-9) for s in readings]
        _ = sum(normalized_stab)  # computed but unused

    # Another decoy operation
    outlier_count = 0
    for vals in log.values():
        for v in vals:
            if v > 100 or v < -50:
                outlier_count += 1

    # Real score components
    base_stability = sum(stability_scores) / len(stability_scores) if stability_scores else 0
    total_magnitude = sum(magnitude_scores)
    
    # Apply weighting via closure
    scorer = make_weighted_scorer([0.6, 0.4])
    composite = scorer([base_stability, total_magnitude / 100.0])
    
    # Final adjustment using modular arithmetic (real)
    adjustment_factor = (len(log.get('sensor_a', [])) + len(log.get('sensor_b', []))) % 13
    final_value = (composite * 100) + adjustment_factor
    
    # Critical red herring: looks like it affects result but doesn't
    temp_result = final_value
    temp_result *= 0.98
    temp_result += math.log(adjustment_factor + 1)
    
    # The real answer
    return int(round(final_value))

# Input data with realistic structure and noise
raw_log = {
    'sensor_a': [16, 25, 36, 49, 64],
    'sensor_b': [10, 18, 32, 50],
    'sensor_c': [-5, 100, 200],  # includes filtered noise
    'config_id': 999,
    'status': 'active'
}

metrics_config = ['stability', 'magnitude', 'ghost']

# Execute main logic
interim_diagnostics = accumulate_ghost(raw_log)  # distractor call
baseline = tempting_metric([1, 2, 3, 4])  # irrelevant computation

final_score = evaluate_performance(raw_log, metrics_config)
print(f"Result: {final_score}")