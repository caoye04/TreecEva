def analyze_data(records):
    totals = {}
    counts = {}
    for r in records:
        key = r['category']
        val = r['value']
        if key not in totals:
            totals[key] = 0
            counts[key] = 0
        totals[key] += val
        counts[key] += 1

    averages = {k: totals[k] / counts[k] for k in totals}
    return averages

# Irrelevant helper (decoy)
def compute_zscore(data, mean, std):
    return [(x - mean) / std for x in data]

# Unused function (dead code path)
def legacy_transform(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading normalization function
def normalize(v):
    mag = sum(x**2 for x in v) ** 0.5
    return [x / mag for x in v] if mag else v

# Core logic disguised among distractions
def evaluate_performance(metrics, weights):
    base_score = 0
    adjustment_factor = 1.0
    
    # Simulated historical baseline (irrelevant)
    historical_max = 98.4
    decay_rate = 0.95
    
    # Distractor: complex-looking but unused computation
    temp_matrix = [[i * j for j in range(1, 5)] for i in range(1, 5)]
    checksum = sum(sum(row) for row in temp_matrix) % 100
    
    # Real logic begins
    weighted_components = []
    for idx, (metric, weight) in enumerate(zip(metrics, weights)):
        # Artificial complexity with enumerate
        if idx % 2 == 0:
            adjusted = metric * weight * 1.1
        else:
            adjusted = metric * weight * 0.9
        weighted_components.append(adjusted)
    
    raw_total = sum(weighted_components)
    
    # Conditional bonus (depends on pattern in metrics)
    is_consistent = all(abs(metrics[i] - metrics[i-1]) < 5 for i in range(1, len(metrics)))
    if is_consistent and len(metrics) > 3:
        raw_total += 7.5
    
    # Artificial string-based switch (distractor)
    mode_flag = 'performance_active'
    if 'active' in mode_flag:
        raw_total *= 1.05
    
    # Actual score calculation
    base_score = round(raw_total, 3)
    
    # Final adjustment based on dictionary lookup (real logic)
    tier_map = {'low': 0.8, 'medium': 1.0, 'high': 1.2}
    performance_tier = 'medium'
    adjustment_factor = tier_map[performance_tier]
    
    final_value = base_score * adjustment_factor
    
    # Dead code: never reached
    if final_value < 0:
        final_value = 0
    
    return int(round(final_value))

# Auxiliary data processing (partially irrelevant)
def prepare_input(raw_strings):
    cleaned = []
    for s in raw_strings:
        s = s.strip().lower()
        if s.endswith('x'):
            continue
        num_part = ''.join(filter(str.isdigit, s))
        if num_part:
            cleaned.append(int(num_part))
    return cleaned

# Unused list manipulation
dummy_list = [3, 1, 4, 1, 5]
dummy_pairs = list(zip(dummy_list, enumerate(dummy_list)))
processed_pairs = [a * b for b, a in dummy_pairs if a > 1]

# Actual input setup
raw_metrics_source = ['m98x', 'm85', 'm92', 'm88', 'm90']
extracted_values = prepare_input(raw_metrics_source)

# Key variables
metrics = [85, 92, 88, 90]  # Aligned with extracted_values after filtering
weights = [0.2, 0.3, 0.25, 0.25]

# Critical execution point
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")