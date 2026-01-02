def analyze_signal_strength(signal_data, baseline=1.5):
    # Irrelevant helper function (dead code path)
    def normalize(v):
        return [x / sum(v) for x in v]

    # Distractor: complex but unused computation
    peak_magnitude = max(signal_data) if signal_data else 0
    avg_magnitude = sum(signal_data) / len(signal_data) if signal_data else 0
    deviation_score = (peak_magnitude - avg_magnitude) * 0.75

    # Unused transformation chain
    transformed = [x ** 0.5 for x in signal_data if x > 0]
    filtered = [t for t in transformed if t < 2.0]
    compression_ratio = len(filtered) / len(signal_data) if signal_data else 0

    # Real logic begins: determine dominant frequency band
    low_band = [x for x in signal_data if x < 1.0]
    mid_band = [x for x in signal_data if 1.0 <= x <= 3.0]
    high_band = [x for x in signal_data if x > 3.0]

    band_distribution = {
        'low': len(low_band),
        'mid': len(mid_band),
        'high': len(high_band)
    }

    # Determine primary band using set operations
    active_bands = {k for k, v in band_distribution.items() if v > 0}
    critical_bands = {'high', 'mid'}
    overlapping_bands = active_bands & critical_bands

    # Early return if no relevant activity
    if not overlapping_bands:
        return 0.0

    # Compute weighted risk index
    weight_map = {'high': 3.0, 'mid': 1.8, 'low': 0.5}
    total_weight = sum(band_distribution[band] * weight_map[band] for band in band_distribution)

    # Conditional expression based on threshold
    adjustment_factor = 0.9 if len(overlapping_bands) > 1 else 1.1

    # Simulate recursive filtering (simple recursion)
    def smooth_value(val, depth=2):
        if depth == 0:
            return val
        return smooth_value((val + 1.0) / 2.0, depth - 1)

    adjusted_weight = smooth_value(total_weight)

    # Apply adjustment and calculate final score
    risk_index = adjusted_weight * adjustment_factor

    # Final threshold classification
    return risk_index if risk_index > baseline else baseline


def compute_threshold_analysis():
    # Input data with meaningful structure
    readings = [0.8, 1.2, 1.4, 3.1, 3.5, 0.9, 2.2, 4.0, 1.1]

    # Decoy variables and operations
    calibration_offset = 0.17
    noise_floor = [x * 0.01 for x in range(len(readings))]
    adjusted_readings = [a + b for a, b in zip(readings, noise_floor)]  # Unused

    # Misleading statistical summary
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    entropy_proxy = -sum(x * __import__('math').log(x) for x in readings if x > 0)  # Red herring

    # Key analysis call
    diagnostic_score = analyze_signal_strength(readings, baseline=1.6)

    # Secondary distractor: set-based anomaly detection (unused)
    unique_values = set(readings)
    duplicates_exist = len(unique_values) < len(readings)
    anomaly_flags = {v for v in readings if v > 3.0}  # Not used

    # Final adjustment using conditional expression
    final_diagnostic = diagnostic_score * 1.2 if diagnostic_score > 2.0 else diagnostic_score * 0.8

    return final_diagnostic

# Execution point
final_diagnostic = compute_threshold_analysis()
print(f"Result: {final_diagnostic}")