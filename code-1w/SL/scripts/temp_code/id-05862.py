def main():
    # Simulated sensor data processing with performance scoring
    raw_readings = [127, 240, 95, 180, 210, 60, 140]
    baseline = 100
    threshold = 50

    # Irrelevant transformation (distractor)
    adjusted_offsets = list(map(lambda x: (x - baseline) ** 0.5, raw_readings))
    offset_sum = sum(adjusted_offsets)

    # Core data processing
    deviations = [abs(r - baseline) for r in raw_readings]
    filtered_deviation = [d for d in deviations if d > threshold]

    # Statistical summary (some used, some not)
    avg_deviation = sum(deviations) / len(deviations)
    peak_deviation = max(deviations)
    deviation_variance = sum((d - avg_deviation) ** 2 for d in deviations) / len(deviations)

    # Normalization step
    normalized_data = [d / peak_deviation for d in deviations]

    # Weight assignment for multi-metric evaluation
    metric_weights = {'stability': 0.4, 'consistency': 0.35, 'drift': 0.25}

    # Red herring: unused weight combination
    auxiliary_weights = {'noise': 0.1, 'jitter': 0.15}
    total_aux = sum(auxiliary_weights.values())
    temp_ratio = total_aux / (sum(metric_weights.values()) + 1e-8)

    # Performance model definition (uses lambda)
    score_model = lambda w, n: sum(w[k] * (1 - val) for k, val in zip(w.keys(), n[:len(w)]))

    # Secondary distractor: simulate calibration chain
    calibration_steps = 0
    for i in range(len(raw_readings)):
        if raw_readings[i] > baseline:
            calibration_steps += 1
            for j in range(i):
                if deviations[j] < avg_deviation:
                    calibration_steps -= 0.5  # fractional adjustment

    # Final evaluation using correct path
    def evaluate_performance(weights, norm_vals):
        base_score = score_model(weights, norm_vals)
        penalty_factor = 0.9 if len(filtered_deviation) > 3 else 1.0
        return base_score * penalty_factor * 100

    final_score = evaluate_performance(metric_weights, normalized_data)

    # Dead code branch (never executed but looks relevant)
    if False:
        debug_log = []
        for idx, val in enumerate(raw_readings):
            debug_log.append(f"{idx}:{val}")

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()