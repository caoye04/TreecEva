def main():
    raw_values = [3, 7, 12, 15, 21, 22, 30]
    thresholds = {'low': 10, 'high': 20}
    temp_sum = 0
    filtered = []

    # Irrelevant accumulation
    for val in raw_values:
        temp_sum += val * 0.1  # Distractor: not used later

    # Actual filtering based on range
    for val in raw_values:
        if thresholds['low'] < val <= thresholds['high']:
            filtered.append(val)

    # Transform via lambda (used)
    transform_fn = lambda x: (x ** 2) % 9
    transformed = [transform_fn(x) for x in filtered]

    # Dead code path (misleading)
    if len(filtered) > 10:
        backup_result = sum([x // 3 for x in transformed])
    else:
        pass  # No effect

    # Weighting scheme with modular arithmetic
    base_weights = [1, 2, 3]
    weights = []
    for i in range(len(transformed)):
        weights.append(base_weights[i % len(base_weights)] + (i // 3))

    # Unused helper computation (distractor)
    avg_weight = sum(weights) / len(weights) if weights else 0
    weighted_pairs = []

    for i in range(min(len(transformed), len(weights)))):
        weighted_pairs.append(transformed[i] * weights[i])

    # Core processing function
    def process_data(data, w):
        result = 0
        for i, val in enumerate(data):
            result += val * w[i] * ((i + 1) % 4)  # Position-weighted contribution
        return result % 1000  # Normalize output

    final_output = process_data(transformed, weights)
    
    # Additional irrelevant state tracking
    stats = {
        'count': len(raw_values),
        'max_raw': max(raw_values),
        'unused_flag': False
    }

    print(f"Result: {final_output}")

main()