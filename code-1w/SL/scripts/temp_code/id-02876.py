def main():
    # Simulate sensor data processing with performance evaluation
    raw_readings = [145, 203, 98, 167, 255, 73]
    threshold = 100
    high_sensitivity_mode = True

    # Irrelevant transformation (distractor)
    adjusted_readings = [x * 1.05 for x in raw_readings]
    clipped_values = [min(x, 200) for x in adjusted_readings]

    # Core logic: filter and normalize relevant data
    filtered_data = [x for x in raw_readings if x > threshold]
    max_value = max(filtered_data) if filtered_data else 1
    normalized_data = [round(x / max_value, 3) for x in filtered_data]

    # Define metric weights using lambda (key python feature)
    weight_function = lambda base: [base, base * 1.2, base * 0.8]
    metric_weights = weight_function(0.25)

    # Auxiliary calculation with set operations (another key feature)
    unique_normalized = set(round(x, 1) for x in normalized_data)
    baseline_set = {0.4, 0.6, 0.8}
    overlap_count = len(unique_normalized & baseline_set)

    # Dummy state tracker (distraction)
    processing_log = []
    for i, val in enumerate(normalized_data):
        status = "HIGH" if val > 0.7 else "LOW"
        processing_log.append(f"{i}:{status}")

    # Evaluate performance based on weighted metrics
    def evaluate_performance(weights, data):
        w1, w2, w3 = weights[:3]  # Only three weights used
        avg_val = sum(data) / len(data) if data else 0
        peak_val = max(data) if data else 0
        variance_proxy = peak_val - min(data)

        # Red herring computation (not affecting final result)
        hypothetical_score = (w1 + w3) * 100
        scaling_factor = 1.0 + (overlap_count * 0.05)  # Uses overlap but fixed due to const

        # Actual score computation
        raw_score = (avg_val * w1) + (peak_val * w2) + (variance_proxy * w3)
        return int(raw_score * 100)  # Final deterministic integer result

    final_score = evaluate_performance(metric_weights, normalized_data)
    
    # Dead code path (distractor)
    if False:
        fallback = sum(clipped_values) // len(clipped_values)
        final_score = fallback

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()