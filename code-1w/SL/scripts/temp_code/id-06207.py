def analyze_sensor_data():
    raw_readings = [105, 210, 150, 99, 256, 180, 201]
    scaling_factor = 0.75
    offset = 24

    # Normalize readings using linear transformation
    normalized_readings = [(x * scaling_factor) - offset for x in raw_readings]

    # Filter valid detections above noise floor
    valid_detections = [val for val in normalized_readings if val > 40]

    # Compute detection scores with additional adjustment
    detection_scores = []
    for score in valid_detections:
        adjusted = score * 0.9 + 10
        detection_scores.append(adjusted)

    # Apply outlier suppression using median threshold
    sorted_scores = sorted(detection_scores)
    median_index = len(sorted_scores) // 2
    median_score = sorted_scores[median_index]

    # Cap scores at 1.5 times the median
    capped_scores = [min(s, 1.5 * median_score) for s in detection_scores]

    # Final normalization step
    total_energy = sum(capped_scores)
    normalized_scores = [round(s / total_energy * 100, 2) for s in capped_scores]

    threshold_score = max(normalized_scores)
    return threshold_score

result = analyze_sensor_data()
print(f"Result: {result}")