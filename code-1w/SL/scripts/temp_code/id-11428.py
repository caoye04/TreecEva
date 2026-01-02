def analyze_system_performance(metrics):
    convergence = 0
    stability = 0
    temp_buffer = []
    auxiliary_sum = 0

    for i, val in enumerate(metrics):
        if i % 2 == 0:
            convergence += val ** 2
        else:
            stability += val * (i + 1)

        # Distractor: irrelevant accumulation
        auxiliary_sum += val * (val % 3)

    # Semi-relevant transformation
    normalized_metrics = [x / (max(metrics) + 1e-5) for x in metrics]

    # Early return red herring (never triggered in practice)
    if len(metrics) > 100:
        return -1

    # Real computation begins
    avg_metric = sum(normalized_metrics) / len(normalized_metrics)
    
    # Additional distraction: unused list comprehension
    outlier_flags = [1 for x in normalized_metrics if abs(x - avg_metric) > 0.5]

    # Simulate state tracking with irrelevant counters
    state_counter = {
        'high': 0,
        'low': 0
    }
    for nm in normalized_metrics:
        if nm > 0.7:
            state_counter['high'] += 1
        elif nm < 0.3:
            state_counter['low'] += 1

    # Core logic hidden among distractions
    def calculate_rating(cvg, stb):
        base_rating = cvg * 0.6 + stb * 0.4
        adjustment = 0
        
        # Nested conditional with misleading branches
        if cvg > 100:
            if stb > 50:
                adjustment = 10
            else:
                adjustment = 5
        else:
            adjustment = -5  # This will actually execute

        # Redundant bitwise operation (distraction)
        mask = 0b1111 & int(base_rating)
        
        return int(base_rating + adjustment)  # Final result depends on this

    intermediate_flag = False
    if convergence > 0:
        intermediate_flag = True

    # Key statement
    final_score = calculate_rating(convergence, stability)

    # Unused but plausible-looking aggregation
    weighted_total = sum([a*b for a, b in zip(metrics, normalized_metrics)])

    print(f"Result: {final_score}")
    return final_score

# Input data with deterministic behavior
input_metrics = [3, 5, 2, 8, 1]
analyze_system_performance(input_metrics)