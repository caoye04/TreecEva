import math

# Sensor calibration and diagnostic system for environmental monitoring
raw_data = [23.4, 19.5, 20.1, 25.6, 18.2, 27.3, 22.8, 19.9, 24.1, 26.5]
baseline_offset = 1.2
noise_floor = 0.8

def apply_calibration(data, offset):
    """Apply sensor-specific calibration offset."""
    calibrated = []
    for x in data:
        calibrated.append(round(x + offset, 2))
    return calibrated

def compute_entropy(values):
    """Calculate Shannon entropy (unused distractor function)."""
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probabilities)
    return round(entropy, 4)

def detect_outliers(sequence, threshold=2.0):
    """Identify outlier indices using standard deviation (dead code path)."""
    mean_val = sum(sequence) / len(sequence)
    std_dev = (sum((x - mean_val) ** 2 for x in sequence) / len(sequence)) ** 0.5
    outliers = [i for i, x in enumerate(sequence) if abs(x - mean_val) > threshold * std_dev]
    return outliers  # Never used

def filter_anomalies(readings):
    """Remove values outside acceptable physiological range with hysteresis."""
    valid_range = (20.0, 25.5)
    buffer_zone = 1.5
    trend_direction = []
    
    for i in range(1, len(readings)):
        trend_direction.append(1 if readings[i] > readings[i-1] else -1)
    
    filtered = []
    in_hysteresis = False
    last_valid = None
    
    for val in readings:
        if valid_range[0] <= val <= valid_range[1]:
            filtered.append(val)
            in_hysteresis = False
            last_valid = val
        elif in_hysteresis and abs(val - last_valid) <= buffer_zone:
            filtered.append(val)
        elif not in_hysteresis:
            if abs(val - valid_range[1]) <= buffer_zone or abs(val - valid_range[0]) <= buffer_zone:
                filtered.append(val)
                in_hysteresis = True
    
    # Irrelevant slicing transformation (distractor)
    midpoint = len(filtered) // 2
    swapped_halves = filtered[midpoint:] + filtered[:midpoint]
    
    # Return original order (swapped_halves is a red herring)
    return filtered

def analyze_readings(cleaned):
    """Compute final diagnostic index using weighted moving average and decay factor."""
    if len(cleaned) == 0:
        return 0.0
    
    weights = [math.exp(-i * 0.2) for i in range(len(cleaned))]
    weighted_sum = sum(w * v for w, v in zip(weights, cleaned))
    normalizer = sum(weights)
    
    raw_diagnostic = weighted_sum / normalizer
    
    # Apply non-linear correction based on trend persistence (computed earlier)
    rising_trend = sum(1 for i in range(1, len(cleaned)) if cleaned[i] > cleaned[i-1])
    stability_factor = rising_trend / (len(cleaned) - 1) if len(cleaned) > 1 else 0
    
    # Final adjustment using bit manipulation as pseudo-checksum (distractor logic)
    checksum_seed = int(sum(cleaned))
    masked = checksum_seed & 0xFF  # Only use lower 8 bits
    inverted = (~masked) & 0xFF
    decoy_metric = (masked ^ inverted) >> 4  # Always results in 0 due to XOR with inverse
    
    # Actual result is independent of decoy_metric
    final_score = raw_diagnostic * (1 + 0.1 * stability_factor)
    
    # Additional irrelevant set operations (distractor)
    unique_values = set(round(x) for x in cleaned)
    expected_set = {20, 21, 22, 23, 24, 25}
    missing_vals = expected_set - unique_values
    extra_vals = unique_values - expected_set
    consistency_bonus = 5 if not missing_vals and not extra_vals else 0  # Unused
    
    return round(final_score + 10, 2)  # Base offset added

# Main processing pipeline
adjusted_baseline = baseline_offset * 1.05
attenuation_factor = noise_floor * 0.75  # Unused parameter
reference_marks = [20.5, 21.0, 22.5, 24.0]  # Unused list

# Primary data flow
calibrated_samples = apply_calibration(raw_data, baseline_offset)

# Spurious intermediate computation (red herring)
dummy_analysis = [math.sin(x * 0.1) for x in calibrated_samples]
entropy_value = compute_entropy(calibrated_samples)  # Computed but unused

# Critical execution point
final_diagnostic = analyze_readings(filter_anomalies(calibrated_samples))

# Print target result
print(f"Result: {final_diagnostic}")