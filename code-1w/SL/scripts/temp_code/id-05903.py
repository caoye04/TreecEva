def analyze_metrics(data, config):
    # Irrelevant preprocessing
    temp_buffer = [x * 2 for x in data if x < 50]
    offset = sum(temp_buffer) % 7

    # Distractor: unused transformation
    transformed = []
    for i, val in enumerate(data):
        if i % 3 == 0:
            transformed.append(val ** 0.5 + offset)

    # Real processing begins
    filtered = [x for x in data if x > 10]
    normalized = [round(x / sum(filtered), 6) for x in filtered]

    # Simulate multiple metric types
    metrics = {}
    for idx, val in enumerate(normalized):
        key = f'metric_{idx % 4}'
        metrics[key] = metrics.get(key, 0) + val

    # Misleading aggregation (never used)
    dummy_total = 0
    for k, v in metrics.items():
        if '3' in k:
            dummy_total += v * 1.5
        else:
            dummy_total += v * 0.7

    # Actual path: extract specific pattern
    valid_keys = [k for k in metrics.keys() if int(k.split('_')[1]) in [1, 2]]
    valid_entries = [metrics[k] for k in valid_keys]

    return valid_entries


def apply_correction(values, factor=1.1):
    # Dead code path — not called but looks important
    corrected = []
    for v in values:
        if v > 0.5:
            corrected.append(v / factor)
        else:
            corrected.append(v * factor)
    return corrected


def process_results(inputs, scaling_factors):
    # Core logic hidden among red herrings
    base = 0.0
    for i, val in enumerate(inputs):
        # Use of zip with unrelated padding
        factors_extended = scaling_factors * (len(inputs) // len(scaling_factors) + 1)
        paired = list(zip(inputs, factors_extended))
        
        contribution = 0
        for j, (v, f) in enumerate(paired):
            if j <= i:  # Only cumulative up to current index
                contribution += v * f
        base += contribution * (0.9 ** i)
    
    # Secondary adjustment based on length parity
    if len(inputs) % 2 == 0:
        base *= 1.25
    else:
        base *= 0.8

    # Decoy operation (no effect due to conditional)
    backup_modes = ['safe', 'audit', 'debug']
    override_flag = False
    for mode in backup_modes:
        if mode == 'production':
            base = max(base, 1.0)
            override_flag = True

    return int(round(base * 1000))


# Main execution
raw_data = [15, 25, 35, 45, 55, 65, 75]
config_params = {'mode': 'standard', 'buffer_size': 128}

# Unused alternative dataset (red herring)
dummy_data = [10, 20, 30, 40]

# Trigger main analysis
results = analyze_metrics(raw_data, config_params)

# Weight vector — only this matters
weights = [0.1, 0.3, 0.6]

# Critical statement
final_score = process_results(results, weights)

# Output result as required
print(f"Target result: {final_score}")