def analyze_contributions(values):
    weighted = [v * (i + 1) for i, v in enumerate(values)]
    normalized = sum(weighted) / sum(values) if sum(values) != 0 else 0
    return normalized

# Irrelevant utility function (decoy)
def calculate_robustness(data):
    return all(d > 0 for d in data) and len(set(data)) > 2

# Another decoy transformation
def transform_sequence(seq):
    shifted = [(x >> 1) ^ 3 for x in seq]
    return [s % 7 for s in shifted]

# Misleading metric with partial relevance
def compute_bias_factor(arr):
    factor = 1.0
    for i, val in enumerate(arr):
        if i % 2 == 0 and val > 5:
            factor *= 0.9
    return round(factor, 4)

# Core logic disguised among distractors
def evaluate_performance(metrics):
    # Real computation begins here
    base_scores = [m['score'] for m in metrics]
    adjustments = [m['penalty'] for m in metrics]
    
    # Distractor: unused but plausible computation
    temporal_weights = [0.8 ** i for i in range(len(metrics))]
    decayed = [base_scores[i] * temporal_weights[i] for i in range(len(base_scores))]
    
    # Actual relevant calculation
    raw_total = sum(base_scores) - sum(adjustments)
    
    # Conditional expression used idiomatically
    scaling = 1.5 if raw_total > 30 else (0.8 if raw_total < 10 else 1.1)
    
    # Dictionary operation for dynamic mapping
    level_map = {range(0, 15): 'low', range(15, 30): 'medium', range(30, 100): 'high'}
    performance_level = next((v for r, v in level_map.items() if raw_total in r), 'unknown')
    
    # Real dependency on external-looking but internal logic
    bonus = 7 if performance_level == 'high' and len(metrics) >= 3 else 0
    
    # Final score influenced by bit manipulation red herring
    # The XOR with 0 ensures no change — a red herring
    final_raw = (raw_total * scaling + bonus) ^ 0  # Bitwise XOR as distraction
    
    # Dead code path (never executed due to prior logic)
    if performance_level == 'unknown':
        fallback = analyze_contributions(base_scores)
        final_raw += fallback
    
    return int(final_raw)

# Setup with realistic domain context (project evaluation metrics)
metric_data = [
    {'score': 12, 'penalty': 2},
    {'score': 15, 'penalty': 4},
    {'score': 18, 'penalty': 3}
]

# Unused but plausible alternate data path
test_data = [
    {'score': 8, 'penalty': 1},
    {'score': 6, 'penalty': 0}
]

# Decoy list transformation
encoded = [x['score'] * 2 + 5 for x in metric_data]
processed = transform_sequence(encoded)

# Real execution buried in noise
bias_correction = compute_bias_factor([item['score'] for item in metric_data])
baseline = sum(item['score'] for item in metric_data)

# Critical statement
final_score = evaluate_performance(metric_data)

# Print required result
print(f"Result: {final_score}")