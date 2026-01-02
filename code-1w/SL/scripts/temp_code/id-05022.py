def process_metrics(raw_inputs):
    # Normalize input values using min-max scaling
    min_val = min(raw_inputs)
    max_val = max(raw_inputs)
    range_val = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / range_val for x in raw_inputs]

    # Apply activation function using lambda
    activate = lambda x: round(x ** 2 + 0.1 * x, 4)
    activated = [activate(val) for val in normalized]

    # Simulate redundant transformation (not used later)
    shifted = [val + 0.05 for val in normalized]  # distractor
    inverted = [1 - val for val in shifted]       # dead code path

    return normalized


def evaluate_redundant_checks(data):
    # Unnecessary validation pass
    valid_count = sum(1 for x in data if 0 <= x <= 1)
    total_count = len(data)
    consistency_rate = valid_count / total_count if total_count else 0

    # More distraction: string-based status tracking
    status_log = "".join(["H" if x > 0.5 else "L" for x in data])
    high_freq = status_log.count('H')
    low_freq = status_log.count('L')
    balance_ratio = high_freq / low_freq if low_freq else float('inf')

    # This function appears useful but returns unused metrics
    return consistency_rate, balance_ratio


def evaluate_performance(weights, inputs):
    # Weighted sum using zip and list comprehension
    weighted_sum = sum(w * x for w, x in zip(weights, inputs))

    # Additional processing with irrelevant intermediate steps
    squared_contributions = [w**2 * x for w, x in zip(weights, inputs)]  # semi-relevant
    penalty_factor = sum(squared_contributions) * 0.05                    # minor adjustment

    # Simulate conditional boost (never triggered due to data)
    boost = 0
    if all(x > 0.95 for x in inputs):  # impossible condition
        boost = 10
    elif len(inputs) > 100:             # dead branch
        boost = 5

    # Final score calculation
    base_score = weighted_sum - penalty_factor + boost
    final_score = round(base_score * 100, 2)

    # Extra logging (distractor)
    debug_info = {"base": base_score, "penalty": penalty_factor, "boost": boost}
    summary_tag = f"PERF-{int(final_score)}"

    return final_score

# Main execution
if __name__ == "__main__":
    # Input dataset representing sensor readings
    sensor_readings = [85, 60, 72, 90, 55, 88, 76, 93, 67, 81]

    # Metric weights for evaluation (aligned with 10 metrics)
    metric_weights = [0.1, 0.15, 0.05, 0.2, 0.1, 0.08, 0.12, 0.05, 0.08, 0.07]

    # Step 1: Normalize sensor data
    normalized_data = process_metrics(sensor_readings)

    # Step 2: Run redundant checks (result not used)
    _ = evaluate_redundant_checks(normalized_data)

    # Step 3: Compute final performance score
    final_score = evaluate_performance(metric_weights, normalized_data)

    # Output target result
    print(f"Result: {final_score}")