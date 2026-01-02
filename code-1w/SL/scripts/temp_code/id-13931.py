def main():
    # Simulate sensor data processing with weighted scoring
    raw_readings = [127, 255, 64, 192, 32]
    offset = 3
    adjusted_readings = [x - offset for x in raw_readings]

    # Irrelevant transformation (distractor)
    inverted = list(map(lambda val: 255 - val, raw_readings))
    avg_inverted = sum(inverted) / len(inverted)

    # Core metrics calculation
    magnitude = sum(adjusted_readings) / len(adjusted_readings)
    peak = max(adjusted_readings)
    stability = min(adjusted_readings) / (sum(adjusted_readings) / len(adjusted_readings))
    variance_proxy = (peak - magnitude) / magnitude

    # Additional red herring variables
    dummy_flags = [True if x > 100 else False for x in raw_readings]
    flagged_count = dummy_flags.count(True)
    unused_threshold = 0.75 * peak

    # Weight assignment (some weights are misleading)
    weights = {
        'magnitude': 0.4,
        'stability': 0.3,
        'variance': 0.2,
        'bonus': 0.1  # Unused in final formula
    }

    metrics = {
        'magnitude': magnitude,
        'stability': stability,
        'variance': variance_proxy
    }

    # Dead code path (never executed)
    if False:
        for i in range(len(raw_readings)):
            raw_readings[i] *= 2

    # Helper function defined inside to increase nesting
    def calculate_aggregate(data, weight_map):
        score = 0.0
        for key in data:
            if key in weight_map:
                score += data[key] * weight_map[key]
        # Apply non-linear adjustment
        if score > 50:
            score = score * 0.95 + 2.5
        else:
            score = score * 1.05 - 1.5
        return score

    final_score = calculate_aggregate(metrics, weights)

    # Extra computation that doesn't affect result
    outlier_check = [x for x in adjusted_readings if x > 200]
    debug_log = f"Outliers found: {len(outlier_check)}"

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()