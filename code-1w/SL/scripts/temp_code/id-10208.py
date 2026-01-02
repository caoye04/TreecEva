from collections import defaultdict, Counter
import math

# Simulated system metrics with irrelevant and relevant data
def generate_metrics():
    raw_data = [15, 23, 8, 42, 7, 16, 4, 31, 12, 19]
    stats = defaultdict(float)
    temp_cache = {}

    # Real metric: sum of squares above threshold
    high_vals = [x for x in raw_data if x > 15]
    stats['signal_strength'] = sum(x**2 for x in high_vals)

    # Distractor: unused transformation
    inverted = [round(100 / (x + 1)) for x in raw_data]
    temp_cache['inverted_norm'] = inverted

    # Real metric: entropy-like dispersion measure
    total = sum(raw_data)
    probs = [(x / total) for x in raw_data]
    stats['entropy_index'] = -sum(p * math.log(p) for p in probs if p > 0)

    # Distractor: irrelevant string encoding
    labels = [chr(97 + (x % 26)) for x in raw_data]
    encoded_str = ''.join(labels)
    stats['dummy_tag'] = hash(encoded_str) % 1000  # Not used later

    # Real metric: oscillation frequency in sequence
    diffs = [abs(raw_data[i] - raw_data[i-1]) for i in range(1, len(raw_data))]
    stats['oscillation_rate'] = sum(1 for d in diffs if d > 10)

    # Distractor: unused recursive function inside generator
    def _spurious_recurse(n):
        if n <= 1:
            return 1
        return _spurious_recurse(n-1) + _spurious_recurse(n-2)

    stats['placeholder'] = _spurious_recurse(5)  # Value not used

    return stats

# Weighting engine with decoy logic
def apply_weights(data):
    # Real weights
    weights = {
        'signal_strength': 0.35,
        'entropy_index': 0.40,
        'oscillation_rate': 0.25
    }

    # Distractor: elaborate but unused weight sets
    alt_weights_v1 = {k: w * 0.1 for k, w in weights.items()}
    alt_weights_v2 = {k: w * 2.5 for k, w in weights.items()}

    fallback_map = defaultdict(lambda: 0.05)
    for k in ['dummy_tag', 'placeholder']:
        fallback_map[k] = 0.01  # Misleading path

    # Real weighted score computation
    composite = 0.0
    for key in weights:
        if key in data:
            composite += weights[key] * data[key]

    # Distractor: unused normalization chain
    max_possible = sum(weights[k] * 1000 for k in weights)  # Arbitrary scale
    normalized_score = (composite / max_possible) * 100 if max_possible != 0 else 0

    # Dead code path: never executed due to fixed condition
    debug_mode = False
    if debug_mode and 'extra_flag' in data:
        scaling_factor = data.get('extra_flag', 1.0)
        composite *= scaling_factor

    return composite

# Final evaluation with red herring inputs
def evaluate_performance(metrics, weights=None):
    base_value = apply_weights(metrics)

    # Real adjustment: exponential sensitivity boost
    adjustment = math.exp(-0.1 * metrics['entropy_index'])
    adjusted_score = base_value * (1 + adjustment)

    # Distractor: complex but unused data structure
    history_log = []
    for i in range(5):
        entry = {
            'iter': i,
            'value': round(adjusted_score / (i + 1), 3),
            'flagged': False
        }
        if i % 4 == 0:
            entry['flagged'] = True
        history_log.append(entry)

    # Distractor: misleading intermediate that looks important
    summary_stats = Counter(history_log[0])
    summary_stats['total_entries'] = len(history_log)

    # Real final transformation
    ceiling_limit = 1000
    final_score = min(adjusted_score, ceiling_limit)

    # Another dead path with confusing logic
    if 'placeholder' in metrics and metrics['placeholder'] > 10:
        outlier_comp = math.sqrt(metrics['placeholder'])
        final_score -= outlier_comp  # Never actually affects result

    return final_score

# Execution flow
metrics = generate_metrics()
final_score = evaluate_performance(metrics)
print(f"Result: {final_score}")