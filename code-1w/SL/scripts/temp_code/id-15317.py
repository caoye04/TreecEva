import itertools

def analyze_sequence(seq):
    return sum(a * b for a, b in itertools.pairwise(seq)) if len(seq) > 1 else 0

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    from math import log2
    return -sum(p * log2(p) for p in probs)

def filter_outliers(data, factor=1.5):
    if len(data) < 3:
        return data
    sorted_data = sorted(data)
    q1, q3 = sorted_data[len(sorted_data)//4], sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

def dummy_transform(x):
    # Irrelevant transformation used as red herring
    return (x ** 2 + 3*x + 1) % 100

def accumulate_diagnostics(logs):
    # Dead code path — never actually used in main logic
    result = {}
    for tag, val in logs.items():
        if 'error' in tag:
            result[tag] = dummy_transform(val)
    return result

def evaluate_stability(readings):
    # Computes variance-like metric but not directly used
    mean_val = sum(readings) / len(readings)
    deviation_sq = sum((x - mean_val) ** 2 for x in readings)
    return deviation_sq / len(readings) if readings else 0

def process_metrics(data, config):
    # Core function — computes final answer
    signal_chain = data['signals']
    base_score = analyze_sequence(signal_chain)
    
    # Distractor: unused entropy computation on irrelevant field
    _ = compute_entropy(data.get('noise_levels', [1]))
    
    # Extract relevant diagnostics
    diagnostics = data['diagnostics']
    filtered_vals = filter_outliers(diagnostics)
    
    # Key intermediate step
    adjustment_factor = len(filtered_vals) if filtered_vals else 1
    
    # Another red herring: stability check that doesn't affect outcome
    stability_metric = evaluate_stability(diagnostics)
    offset_tweak = stability_metric * 0.0  # Neutralized deliberately
    
    # Real computation path
    reference_key = 'baseline_ref'
    if reference_key in config:
        base_score += config[reference_key]
    
    # Multiple assignments and distractors
    temp_results = {}
    temp_results['raw'] = base_score
    temp_results['adjusted'] = base_score * adjustment_factor
    temp_results['offset'] = offset_tweak
    
    # Use dictionary operations meaningfully
    keys_of_interest = ['mode_a', 'mode_b', 'mode_c']
    mode_scores = {k: data['modes'][k] for k in keys_of_interest if k in data['modes']}
    mode_bonus = sum(mode_scores.values()) * 0.5  # Only partial use
    
    # Final logic
    final_value = temp_results['adjusted'] + mode_bonus
    
    # Decoy assignment to mislead
    final_value = final_value if final_value > 0 else abs(final_value)
    
    return int(final_value)

# Simulated dataset with meaningful structure
health_data = {
    'signals': [3, 1, 4, 1, 5, 9, 2],           # Used in pairwise product sum
    'diagnostics': [10, 12, 15, 10, 11, 10, 100], # Outlier present (100)
    'noise_levels': [5, 3, 8, 2],                # Unused
    'modes': {
        'mode_a': 6,
        'mode_b': 4,
        'mode_c': 2,
        'mode_x': 99                            # Irrelevant key
    }
}

thresholds = {
    'baseline_ref': 7,
    'alert_level': 95,                           # Unused
    'recovery_window': 3                       # Unused
}

# Dead code call (no effect)
dummy_logs = {'error_1': 42, 'error_2': 67}
_ = accumulate_diagnostics(dummy_logs)

# Main execution
interim_signal = analyze_sequence(health_data['signals'])
_ = compute_entropy([2, 3, 5, 7])  # Red herring call

final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")