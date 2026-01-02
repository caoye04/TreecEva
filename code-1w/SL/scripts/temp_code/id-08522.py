def main():
    # Simulate sensor readings with noise and calibration
    raw_readings = [12, 15, 10, 18, 22, 8, 14]
    calibrated = list(map(lambda x: x * 1.05 if x > 10 else x * 0.95, raw_readings))

    # Irrelevant preprocessing: normalize to percentages (not used later)
    total_signal = sum(calibrated)
    percentages = [round((val / total_signal) * 100, 2) for val in calibrated]
    avg_percentage = sum(percentages) / len(percentages)  # Dead computation

    # Focus detection based on threshold crossings
    focus_peaks = []
    threshold = 13.5
    for i in range(1, len(calibrated)):
        if calibrated[i-1] < threshold <= calibrated[i]:
            focus_peaks.append(i)

    # Simulate feedback loop with stateful corrections
    feedback_loop = []
    adjustment_factor = 1.1
    for val in calibrated:
        adjusted = val * adjustment_factor
        if adjusted < 12.0:
            adjusted = 12.0  # Enforce minimum baseline
        feedback_loop.append(round(adjusted, 2))
        adjustment_factor *= 0.98  # Decay factor (semi-relevant)

    # Additional irrelevant transformation
    inverted_signals = [round(100 - v, 2) for v in feedback_loop[:len(feedback_loop)//2]]
    compression_ratio = len(inverted_signals) / len(raw_readings)  # Not used

    # Core logic: performance aggregation based on windowed variance
    def aggregate_performance(data):
        if len(data) < 3:
            return 0
        # Use slicing to analyze recent segment only
        recent = data[-5:] if len(data) >= 5 else data
        mean = sum(recent) / len(recent)
        variance = sum((x - mean) ** 2 for x in recent) / len(recent)
        stability_bonus = 10 if variance < 8.0 else 5
        # Apply non-linear scaling
        base_score = sum(recent) * 0.75
        return int(base_score + stability_bonus)

    # Trigger point of interest
    final_score = aggregate_performance(feedback_loop)

    # Unused health diagnostics
    def health_check(seq):
        return all(x > 5 for x in seq) and len(seq) > 0
    
    system_health = health_check(feedback_loop)  # Computed but unused

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()