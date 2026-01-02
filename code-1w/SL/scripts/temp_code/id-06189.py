def analyze_metrics(data, threshold=0.5):
    normalized = [round(x / sum(data), 3) for x in data]
    high_vals = [v for v in normalized if v > threshold]
    low_vals = [v for v in normalized if v <= threshold]
    return high_vals, low_vals


def transform_key(indicator):
    shift = len(indicator) % 4
    shifted = [(x << shift) & 15 for x in indicator]
    return [x ^ 3 for x in shifted]


def filter_signals(inputs):
    valid = []
    for val in inputs:
        if val & 1:
            valid.append(val * 2)
        else:
            valid.append(val + 1)
    sorted_valid = sorted(valid, reverse=True)
    return sorted_valid[:len(sorted_valid)//2 + 1]


def compute_baseline(reference):
    base = 0
    for r in reference:
        base += r % 7
    return base / len(reference)


def evaluate_performance(metrics):
    temp_result = 0
    adjustment = 0
    
    # Core logic chain
    for k, v in metrics.items():
        if 'alpha' in k:
            temp_result += v * 1.5
        elif 'beta' in k:
            temp_result += v ** 1.2
        elif 'gamma' in k:
            adjustment += v // 3
    
    # Distractor: complex but unused computation
    decoy_map = {i: (i**2 + 3*i + 1) % 100 for i in range(1, 15)}
    outlier_check = set(decoy_map.values()) & {x for x in range(40, 60)}
    mask_value = sum(outlier_check) >> 2
    
    # Another red herring: recursive transformation with no impact
    def noise_function(n):
        if n <= 1:
            return n
        return noise_function(n-1) + noise_function(n-2)
    
    _ = [noise_function(i) for i in [6, 7, 8]]  # Computationally heavy but irrelevant
    
    # Actual critical path
    category_bonus = 0
    if 'alpha_3' in metrics and metrics['alpha_3'] > 10:
        category_bonus += 5
    
    temp_result -= adjustment
    temp_result += category_bonus
    
    # Final transformation using conditional expression and dict op
    scaling_factor = 2 if len(metrics.keys()) > 5 else 1.5
    final_score = temp_result * scaling_factor
    
    # Irrelevant string manipulation distraction
    status_flag = "OK" if final_score > 30 else "LOW"
    diagnostic = ''.join([c.upper() if c in 'aeiou' else c for c in status_flag])
    
    # Unused nested structure
    debug_info = {
        'version': '2.1',
        'flags': {f'f{i}': False for i in range(3)},
        'aux_data': [
            [i*j for j in range(3)] for i in range(2)
        ]
    }
    
    return int(final_score)

# Main execution context
raw_data = [12, 8, 15, 3, 9]
indicator_keys = [5, 6, 10, 12]
signal_inputs = [4, 7, 8, 11, 13]
reference_base = [18, 22, 14, 25]

# Irrelevant preprocessing steps
norm_vals, _ = analyze_metrics(raw_data, threshold=0.3)
transformed_ind = transform_key(indicator_keys)
filtered_sig = filter_signals(signal_inputs)
baseline = compute_baseline(reference_base)

# Core metric construction - only this matters ultimately
metric_set = {
    'alpha_1': 8,
    'alpha_2': 12,
    'alpha_3': 14,
    'beta_1': 5,
    'beta_2': 7,
    'gamma_1': 9,
    'extra_feature': 42  # This key does not affect logic
}

# Dead code path - never executed but looks important
if __debug__:
    verification_chain = []
    for i in range(3):
        verification_chain.append((i, i**3 + 2*i))

final_score = evaluate_performance(metric_set)
print(f"Target result: {final_score}")