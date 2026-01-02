import math

# Simulated sensor fusion system for environmental monitoring
def analyze_readings(data_stream):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in data_stream if x > 0]
    filtered = list(filter(lambda x: x < 100, normalized))
    
    # Core computation buried among distractions
    base_sum = sum(filtered)
    outlier_count = len([x for x in data_stream if x < 0])  # unused red herring
    adjustment_factor = 0.9 if base_sum > 500 else 1.1
    
    processed = []
    for val in data_stream:
        if val == 0:
            continue
        processed.append(abs(val) ** 0.5 * adjustment_factor)
    
    # Distractor: complex but unused transformation
    transformed = [math.sin(x / 10) for x in processed if x % 2 != 0]
    dummy_aggregate = sum(transformed) / len(transformed) if transformed else 0
    
    # Critical path disguised as side calculation
    temp_result = 0
    for i, v in enumerate(processed):
        if i % 3 == 0:
            temp_result += v * 1.5
    
    return temp_result

# Decoy function - looks important but never called
def validate_calibration(reference, readings):
    diff = [abs(a - b) for a, b in zip(reference, readings)]
    threshold = sum(diff) / len(diff) if diff else 0
    return threshold < 5

# Another decoy - recursive but irrelevant
def compute_entropy(values, depth=0):
    if depth >= 3 or not values:
        return 0
    p = [v / sum(values) for v in values if v > 0]
    return -sum(pi * math.log(pi) for pi in p if pi > 0) + compute_entropy(p, depth + 1)

# Main evaluation logic with multiple concepts
metric_weights = {
    'sensitivity': 0.3,
    'stability': 0.25,
    'consistency': 0.35,
    'reliability': 0.1
}

raw_results = [
    42, 67, 0, 89, -5, 34, 91, 12, 77, 56,
    23, 68, 0, 45, 73, 88, 19, 64, 37, 51
]

auxiliary_data = [x * 2 for x in raw_results if x > 0]  # distractor list

# Unused statistical measures (red herrings)
mean_value = sum(raw_results) / len(raw_results)
deviation = [abs(x - mean_value) for x in raw_results]
population_variance = sum(d ** 2 for d in deviation) / len(deviation)

# Critical intermediate step disguised as utility
def extract_key_metrics(data):
    positive_only = [x for x in data if x > 0]
    count_by_category = {
        'high': len([x for x in positive_only if x >= 70]),
        'medium': len([x for x in positive_only if 40 <= x < 70]),
        'low': len([x for x in positive_only if x < 40])
    }
    
    # Real signal in noise
    raw_magnitude = sum(positive_only) / 100.0
    fluctuation_index = count_by_category['high'] * count_by_category['low']
    
    return raw_magnitude, fluctuation_index

# Secondary processing chain with early termination
prev_results = []
def track_history(new_entry):
    if len(prev_results) > 5:
        prev_results.pop(0)
    prev_results.append(new_entry)
    if new_entry < 10:
        return False  # short-circuit
    return True

# Core evaluation with mixed paradigms
def evaluate_performance(weights, results):
    # First dependency
    analysis_a = analyze_readings(results)
    
    # Second dependency
    magnitude, index = extract_key_metrics(results)
    
    # Multiple assignments - distractor
    w_sens, w_stab, w_cons, w_rel = weights.values()
    
    # Real computation hidden among decoys
    score_component_1 = analysis_a * w_sens
    score_component_2 = magnitude * w_stab
    
    # Critical formula
    base_score = score_component_1 + score_component_2
    penalty = index * 0.15
    final_raw = base_score - penalty
    
    # Dead code path (never reached due to logic)
    if final_raw < 0 and False:  
        fallback = compute_entropy(results)
        final_raw = fallback
    
    # Tuple unpacking distraction
    config_settings = ('mode_A', 'threshold_X', 'active')
    mode, thresh, status = config_settings
    
    # Actual answer computation
    scaling_constant = 2.71828  # e approx
    final_score = int(final_raw * scaling_constant)  # key result
    
    # Last-minute override guard (untriggered)
    if status == 'inactive' and mode == 'debug':
        final_score = -999
    
    return final_score

# Execute main logic
temp_var = evaluate_performance(metric_weights, raw_results)
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Target result: {final_score}")