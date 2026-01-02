from itertools import compress, cycle

# Simulate sensor data quality assessment in an environmental monitoring system
def analyze_sensor_data(stability, accuracy, latency):
    # Stability: fluctuation index (lower is better)
    # Accuracy: deviation from ground truth (lower is better)
    # Latency: response delay in ms (lower is better)

    base_rating = 100
    penalty = 0

    # Irrelevant intermediate calculation - distractor
    temp_buffer = [x * 0.95 for x in stability]
    avg_latency = sum(latency) / len(latency)

    if avg_latency > 50:
        penalty += 15
    elif avg_latency > 30:
        penalty += 8

    # Accuracy-based adjustment
    total_deviation = sum(accuracy)
    if total_deviation > 20:
        penalty += 20
    else:
        penalty += 10

    # Logical combination with short-circuit evaluation
    high_stability = all(s < 5 for s in stability) and len(stability) > 0
    if high_stability or (total_deviation < 15 and avg_latency < 40):
        base_rating += 25

    # Dead code path - misleading
    debug_mode = False
    if debug_mode:
        print("Debug: Performing deep analysis")
        for i in range(len(stability)):
            stability[i] *= 1.1  # Never executed

    return base_rating - penalty

# Weighted performance evaluator
def evaluate_performance(metrics, weights):
    weighted_sum = 0
    weight_total = 0

    # Use of itertools.cycle - relevant but slightly obscured
    weight_cycler = cycle(weights)

    for i, metric in enumerate(metrics):
        w = next(weight_cycler)
        weighted_sum += metric * w
        weight_total += w

    # Normalize the score
    normalized = weighted_sum / weight_total if weight_total != 0 else 0

    # Additional logic step: bonus for balanced metrics
    if max(metrics) - min(metrics) < 15:
        normalized += 7.5

    return round(normalized, 2)

# Main execution
if __name__ == "__main__":
    # Sensor readings over 6-hour period (simulated)
    stability_data = [4.2, 3.8, 5.1, 4.0, 3.9, 4.3]
    accuracy_data = [3.1, 2.9, 3.6, 4.0, 3.2, 3.8]
    response_latency = [28, 32, 35, 29, 33, 31]

    # Compute individual component ratings
    sensor_health = analyze_sensor_data(stability_data, accuracy_data, response_latency)
    network_health = 88  # External factor, not computed here
    power_efficiency = 92  # Another independent metric

    # Composite metrics - some are distractions
    auxiliary_metrics = [sensor_health, 76, 81, 88, 91]  # 76 and 81 are fake placeholders
    filtered_metrics = list(compress(auxiliary_metrics, [True, False, False, True, True]))  # Keep sensor, network, power

    # Final integration
    metrics = [sensor_health, network_health, power_efficiency]
    weights = [0.5, 0.3, 0.2]

    final_score = evaluate_performance(metrics, weights)

    # Print result as required
    print(f"Result: {final_score}")