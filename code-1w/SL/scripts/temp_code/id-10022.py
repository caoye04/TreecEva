def analyze_system_performance(raw_metrics, config_params):
    base_multiplier = config_params.get('multiplier', 1.5)
    threshold = config_params.get('threshold', 0.75)
    scaling_factor = config_params.get('scale', 100)

    # Normalize raw metrics using list comprehension
    normalized = [x / max(raw_metrics) for x in raw_metrics]

    # Filter relevant metrics above threshold
    filtered_metrics = [val for val in normalized if val >= threshold]

    # Simulate auxiliary calculation with no impact on final result
    phantom_sum = 0
    for i in range(len(normalized)):
        if i % 2 == 0:
            phantom_sum += normalized[i] * base_multiplier
        else:
            phantom_sum -= normalized[i] / base_multiplier

    # Misleading secondary transformation (dead-end path)
    transformed = set()
    for val in normalized:
        transformed.add(round(val * scaling_factor))
    
    excess_values = {x for x in transformed if x > 80}  # unused set operation

    # Actual processing begins: detect anomalies and compute density
    anomaly_count = 0
    cumulative_density = 0.0
    for val in normalized:
        if val < 0.1:
            anomaly_count += 1
        cumulative_density += val ** 1.5

    # Prepare data structure for efficiency calculation
    processed_data = {
        'anomalies': anomaly_count,
        'density': cumulative_density,
        'count': len(filtered_metrics)
    }

    # Dummy tracking state (not used later)
    tracking_log = []
    for idx, val in enumerate(filtered_metrics):
        tracking_log.append(f"Item_{idx}: {val:.3f}")

    # Irrelevant sorting operation on keys that are never accessed
    sorted_keys = sorted(processed_data.keys(), reverse=True)

    def calculate_efficiency(data, thresh):
        base = data['density']
        penalty = data['anomalies'] * 10
        boost = data['count'] * 5

        # Red herring computation
        hypothetical_gain = (base + boost) * (1 - thresh) if thresh > 0.5 else base

        # Actual formula
        score = (base + boost - penalty) * scaling_factor  # uses outer scope variable
        return int(score)

    efficiency_score = calculate_efficiency(processed_data, threshold)
    
    # Unrelated post-processing
    summary_stats = {
        'total': sum(normalized),
        'avg': sum(normalized) / len(normalized),
        'peak': max(normalized)
    }

    # Output the target variable
    print(f"Result: {efficiency_score}")
    return efficiency_score

# Inputs
metrics = [85, 12, 93, 4, 67, 88, 23, 95]
params = {'threshold': 0.72, 'multiplier': 1.8}

result = analyze_system_performance(metrics, params)