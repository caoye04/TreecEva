def analyze_system_performance(input_data):
    threshold = 0.75
    weights = [0.2, 0.35, 0.45]
    temp_results = []
    auxiliary_sum = 0

    for val in input_data:
        if val > threshold:
            temp_results.append(val ** 2)
        else:
            temp_results.append(val / 2)

    # Misleading normalization step (not used later)
    normalized = [x / sum(temp_results) for x in temp_results] if sum(temp_results) != 0 else temp_results

    convergence = sum(temp_results) / len(temp_results)
    fluctuation = max(temp_results) - min(temp_results)

    # Dead computation - irrelevant to final result
    noise_level = 0
    for i in range(len(temp_results)):
        if i % 2 == 0:
            noise_level += temp_results[i] * 0.1

    stability_factor = 1.0 if fluctuation < 0.5 else 0.6

    def calculate_rating(conv, stab):
        base_rating = conv * 100
        adjustment = 10 if stab == 1.0 else -25
        # Conditional expression usage
        penalty = 20 if any(x < 0.1 for x in temp_results) else 0
        return base_rating + adjustment - penalty

    intermediate_metric = convergence * stability_factor  # unused

    # Key statement
    final_score = calculate_rating(convergence, stability_factor)

    # Additional red herring: sorting unrelated data
    metadata_logs = [(i, temp_results[i]) for i in range(len(temp_results))]
    metadata_logs.sort(key=lambda x: x[1], reverse=True)

    # Output required format
    print(f"Result: {final_score}")
    return final_score

# Input data
data_stream = [0.8, 0.6, 0.9, 0.7, 0.65]
result = analyze_system_performance(data_stream)