def process_metrics(log_entries, config):
    baseline = 1.0
    adjustments = []
    temp_cache = {}
    efficiency_score = 0
    
    for idx, entry in enumerate(log_entries):
        raw_value = entry['value']
        weight = config.get(f'weight_{idx}', 1.0)
        
        # Irrelevant transformation (distractor)
        transformed = raw_value ** 0.5 * weight
        if idx not in temp_cache:
            temp_cache[idx] = transformed ** 2
        
        # Relevant computation path
        normalized = raw_value / (entry['base'] + 1e-5)
        if normalized > config['threshold_high']:
            adjustments.append(1.2)
        elif normalized < config['threshold_low']:
            adjustments.append(0.8)
        else:
            adjustments.append(1.0)

    # Secondary loop with zip usage (mixing concepts)
    trend_pairs = list(zip(adjustments, adjustments[1:]))
    trend_factor = 1.0
    for prev, curr in trend_pairs:
        if curr > prev:
            trend_factor *= 1.05
        elif curr < prev:
            trend_factor *= 0.98

    # Dummy filtering (dead code path - distractor)
    valid_entries = [e for e in log_entries if e['value'] > 0]
    unused_sum = sum(e['value'] for e in valid_entries if e['base'] < 50)

    # Core logic affecting final result
    avg_adjustment = sum(adjustments) / len(adjustments) if adjustments else 1.0
    efficiency_score = int(baseline * avg_adjustment * trend_factor * 100)

    # Final assignment (target execution point)
    final_output = efficiency_score + 5  # minor offset (not part of target var)
    return final_output

# Input data
log_data = [
    {'value': 45, 'base': 30},
    {'value': 60, 'base': 30},
    {'value': 30, 'base': 30},
    {'value': 75, 'base': 30}
]

tuning_params = {
    'threshold_low': 0.8,
    'threshold_high': 1.5,
    'weight_0': 1.1,
    'weight_1': 0.9
}

efficiency_score = 0
final_output = process_metrics(log_data, tuning_params)
print(f"Target result: {efficiency_score}")