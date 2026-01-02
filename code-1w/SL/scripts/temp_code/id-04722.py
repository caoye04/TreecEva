def analyze_data(records):
    # Irrelevant preprocessing block (dead path)
    temp_analysis = {}
    for r in records:
        if r['status'] == 'inactive':
            temp_analysis[r['id']] = sum(ord(c) for c in r['name']) // len(r['name'])

    # Distractor: complex but unused transformation
    encoded = [r['id'] ^ 255 for r in records if r['type'] == 'legacy']
    sorted_encoded = sorted(encoded, reverse=True)

    # Real data pipeline starts here
    valid_records = [r for r in records if r['status'] == 'active']
    base_scores = [len(r['name']) * r['value'] for r in valid_records]

    # Bit manipulation red herring
    bit_flags = 0
    for score in base_scores:
        bit_flags ^= score & 0xF

    adjusted_scores = [s + (s >> 3) - (s & 0x3) for s in base_scores]

    return adjusted_scores


def compute_threshold(data):
    # Unused function — misleading dependency
    return sum(data) // len(data) if data else 0


def filter_outliers(values, limit=100):
    # Called but result ignored — distraction
    filtered = [v for v in values if v < limit]
    if len(filtered) < 3:
        return values  # fallback
    return filtered


def evaluate_performance(metrics, weights):
    # Core logic buried in noise

    # Irrelevant set operations (distractor)
    unique_magnitude = len(set(abs(m) for m in metrics))
    shift_key = unique_magnitude % 7

    # Fake normalization path
    normalized = [m / (abs(m) + 1e-8) for m in metrics]
    polarity = sum(1 for n in normalized if n > 0) - sum(1 for n in normalized if n < 0)

    # Actual computation begins
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    penalty = 0

    # Conditional penalty based on pattern
    for i in range(len(metrics)):
        if i > 0 and metrics[i] < metrics[i-1]:
            penalty += weights[i] * 0.1

    # Key statement
    final_score = weighted_sum - penalty

    # Dead code: post-processing never used
    if final_score > 50:
        final_score = (final_score * 0.95) + 5
    elif final_score < 0:
        final_score = abs(final_score) * 1.1

    return final_score

# Main execution context
records_db = [
    {'id': 101, 'name': 'Alpha', 'value': 12, 'status': 'active', 'type': 'modern'},
    {'id': 102, 'name': 'Beta', 'value': 8, 'status': 'inactive', 'type': 'legacy'},
    {'id': 103, 'name': 'Gamma', 'value': 15, 'status': 'active', 'type': 'modern'},
    {'id': 104, 'name': 'Delta', 'value': 5, 'status': 'active', 'type': 'modern'},
    {'id': 105, 'name': 'Epsilon', 'value': 20, 'status': 'inactive', 'type': 'modern'}
]

weights_config = [0.4, 0.35, 0.25]

# Trigger analysis (result partially ignored)
scores_list = analyze_data(records_db)
trimmed_scores = filter_outliers(scores_list, limit=150)

# Introduce decoy variable with similar name
final_scores = [s * 1.05 for s in trimmed_scores]  # unused

metrics_input = [s * 0.1 for s in scores_list]  # actual input source

# Key statement
final_score = evaluate_performance(metrics_input, weights_config)

print(f"Result: {final_score}")