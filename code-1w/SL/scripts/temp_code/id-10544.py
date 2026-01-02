def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    final_score = 0
    temp_accum = 0
    score_cache = []

    for i, (name, metrics) in enumerate(data.items()):  # Using enumerate
        raw_score = sum(metrics)
        rank_adjustment = (i + 1) * 0.1

        if raw_score >= bonus_threshold:
            raw_score *= base_multiplier

        for j, val in enumerate(metrics):
            if j % 2 == 0:
                temp_accum += val * 0.1  # Minor side computation

        # Simulate some string-based metadata tagging (irrelevant to final score)
        tag = f"{name}-{len(metrics)}-RUN".lower().replace("run", "eval")
        tag_checksum = len(tag) + sum(ord(c) for c in tag[:3])  # Distractor

        processed_metrics = [m ** 0.5 for m in metrics if m > 0]
        smoothed = sum(processed_metrics) / len(processed_metrics) if processed_metrics else 0

        final_score += smoothed * 10 + rank_adjustment

        # Dead code: this block never executes due to fixed condition
        anomaly_detected = False
        if anomaly_detected and len(metrics) > 10:
            final_score -= 5  # Irrelevant path

        score_cache.append(smoothed)  # Stored but not used later

    # Additional irrelevant transformation
    max_cache = max(score_cache) if score_cache else 0
    cache_variance_proxy = (max_cache - min(score_cache)) * 0.5 if score_cache else 0

    final_score -= cache_variance_proxy  # Minor adjustment based on unused data

    return int(final_score)


# Benchmark dataset
benchmark_data = {
    "system_alpha": [78, 88, 92],
    "system_beta": [80, 85, 87, 90],
    "system_gamma": [70, 75],
    "system_delta": [95, 90, 85, 80, 75]
}

# Key execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")