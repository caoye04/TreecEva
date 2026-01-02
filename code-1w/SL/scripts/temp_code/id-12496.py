def main():
    # System performance evaluation with multiple metrics
    raw_responses = [85, 90, 78, 92, 88]
    response_times = [1.2, 0.9, 1.5, 0.7, 1.1]
    error_flags = [False, False, True, False, False]

    # Irrelevant scaling factor (distractor)
    legacy_multiplier = 1.05

    # Normalize responses to 0-1 scale
    max_response = max(raw_responses)
    min_response = min(raw_responses)
    normalized_responses = [(x - min_response) / (max_response - min_response) for x in raw_responses]

    # Normalize response times inversely (faster is better)
    max_time = max(response_times)
    min_time = min(response_times)
    normalized_times = [1 - (x - min_time) / (max_time - min_time) for x in response_times]

    # Compute reliability scores based on error flags
    reliability_scores = [0.5 if err else 1.0 for err in error_flags]

    # Introduce unrelated computation (dead code path - distractor)
    def calculate_historical_bias(data):
        return sum(x * 0.95**i for i, x in enumerate(reversed(data)))

    historical_adjustment = calculate_historical_bias(raw_responses)  # Not used later

    # Combine metrics into a single vector
    combined_metrics = []
    for i in range(len(raw_responses)):
        score = (
            normalized_responses[i] * 0.5 +
            normalized_times[i] * 0.3 +
            reliability_scores[i] * 0.2
        )
        combined_metrics.append(round(score, 4))

    # Bitwise integrity check (semi-relevant, adds complexity)
    checksum = 0
    for val in raw_responses:
        checksum ^= int(val)  # XOR all values

    # Only proceed if checksum passes a condition (adds control flow)
    if checksum & 1:  # Check if odd
        filtered_metrics = [m for m in combined_metrics if m > 0.7]
    else:
        filtered_metrics = combined_metrics

    # Normalize again after filtering
    if filtered_metrics:
        max_metric = max(filtered_metrics)
        min_metric = min(filtered_metrics)
        if max_metric != min_metric:
            normalized_metrics = [
                (m - min_metric) / (max_metric - min_metric) if max_metric != min_metric else 0.5
                for m in filtered_metrics
            ]
        else:
            normalized_metrics = [0.5] * len(filtered_metrics)
    else:
        normalized_metrics = [0.0]

    # Weighting scheme for different feedback dimensions
    feedback_weights = [0.4, 0.3, 0.2, 0.1]  # Diminishing importance

    # Aggregate performance using weighted combination
    def aggregate_performance(weights, metrics):
        # Use lambda to create dynamic weighting function
        weight_func = lambda idx: weights[idx % len(weights)]
        total = sum(metrics[i] * weight_func(i) for i in range(len(metrics)))
        weight_sum = sum(weight_func(i) for i in range(len(metrics)))
        return total / weight_sum if weight_sum else 0

    # Final score calculation point
    final_score = aggregate_performance(feedback_weights, normalized_metrics)

    # Unused diagnostic output (distractor)
    avg_response = sum(raw_responses) / len(raw_responses)
    median_time = sorted(response_times)[len(response_times)//2]

    # Print result as required
    print(f"Target result: {final_score}")

if __name__ == "__main__":
    main()