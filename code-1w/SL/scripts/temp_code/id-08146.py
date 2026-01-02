def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [m / max(metrics) for m in metrics]
    high_performers = set()
    for i, metric in enumerate(metrics):
        if metric >= thresholds.get('high', 80):
            high_performers.add(i)

    # Misleading intermediate calculation (not used later)
    avg_normalized = sum(normalized) / len(normalized)
    below_avg_count = len([n for n in normalized if n < avg_normalized])

    # Relevant logic: count how many exceeded threshold with XOR-based condition
    strong_signal = 0
    for i in range(len(metrics)):
        above_base = metrics[i] >= thresholds.get('base', 60)
        has_variance = (metrics[i] ^ thresholds.get('base', 60)) > 15  # bitwise XOR check
        if above_base and has_variance:
            strong_signal += 1

    return strong_signal


def calculate_final_score(raw_data, config=None):
    if config is None:
        config = {'base': 60, 'high': 80, 'weight': 1.5}

    # Dead code path (never executed under current inputs)
    if len(raw_data) == 0:
        return -1

    # Real computation begins
    base_scores = [x * 2 for x in raw_data]  # Amplify signals
    filtered = [s for s in base_scores if s > 100]  # only strong base scores

    # Set operations: find indices that meet multiple criteria
    over_100 = {i for i, s in enumerate(base_scores) if s > 100}
    even_index = {i for i in range(len(base_scores)) if i % 2 == 0}
    relevant_indices = over_100 & even_index  # intersection

    # Secondary metric based on filtered positions
    bonus = 0
    for idx in sorted(relevant_indices):
        if idx < len(raw_data) and raw_data[idx] % 2 == 1:
            bonus += 5

    # Call helper function with distraction
    auxiliary_thresholds = {'base': 50, 'high': 85}
    performance_bonus = analyze_performance(base_scores, auxiliary_thresholds)

    # Final aggregation
    base_total = sum(filtered)
    adjustment = len(relevant_indices) * 3
    final_score = base_total + bonus + performance_bonus * config['weight'] - adjustment

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
data_stream = [45, 55, 60, 70, 80, 90]
settings = {'base': 60, 'weight': 1.5}

# Execute
final_score = calculate_final_score(data_stream, settings)