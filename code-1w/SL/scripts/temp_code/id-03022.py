def evaluate_performance(weights, metrics):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: x / max(metrics) if max(metrics) != 0 else 0, metrics))

    # Irrelevant transformation: reverse only for distraction
    reversed_metrics = [x for x in reversed(normalized)]

    # Weighted sum calculation - core logic
    weighted_sum = sum(w * n for w, n in zip(weights, normalized))

    # Dummy threshold check with unused branching
    threshold = 0.5
    if weighted_sum > threshold:
        adjustment = 1.1
    else:
        adjustment = 0.9  # Dead code path (always above threshold)

    # Apply adjustment (but actually constant due to predictable condition)
    adjusted_score = weighted_sum * 1.1

    # Secondary scoring based on variance (semi-relevant but not used directly)
    mean_norm = sum(normalized) / len(normalized)
    variance = sum((x - mean_norm) ** 2 for x in normalized) / len(normalized)
    stability_bonus = 1 + (0.1 if variance < 0.1 else 0)  # Always true, adds 0.1

    # Bitwise masking operation on integer portion (combinatorics red herring)
    int_part = int(adjusted_score)
    mask = 0b1111  # Keep lower 4 bits
    masked_value = int_part & mask  # Only uses part of value

    # Final composition: main score + bonus from stability
    final_component = adjusted_score + 0.1  # Incorporates stability_bonus effect

    # Extra computation: harmonic mean (not used)
    harmonic_mean = len(normalized) / sum(1/x for x in normalized) if all(x != 0 for x in normalized) else 0

    return final_component

# Input data
metric_weights = [0.4, 0.3, 0.2, 0.1]
raw_metrics = [85, 90, 78, 92]

# Execution point of interest
temp_result = evaluate_performance(metric_weights, raw_metrics)
final_score = temp_result

print(f"Result: {final_score}")