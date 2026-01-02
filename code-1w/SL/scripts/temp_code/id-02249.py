def analyze_component(reading, threshold=75):
    return reading > threshold

# Irrelevant sensor simulation (distractor)
def simulate_sensor_drift(base_val, noise_factor=0.05):
    import math
    return base_val * (1 + noise_factor * math.sin(0.1))

# Unused function - dead code path
def deprecated_normalization(x):
    return x / sum(x)

# Core data processing with red herrings
def transform_readings(raw_data):
    processed = []
    offset = 10
    for val in raw_data:
        if val < 50:
            adjusted = val * 1.2 + offset
        elif val >= 80:
            adjusted = val * 0.9 + offset
        else:
            adjusted = val + 5
        processed.append(int(adjusted))
    return processed

# Misleading aggregation function
def compute_avg_exc_outliers(data, cutoff=100):
    filtered = [x for x in data if x < cutoff]
    return sum(filtered) / len(filtered) if filtered else 0

# Bit manipulation decoy
def scramble_bits(value):
    return ((value << 3) & 0xFF) ^ 0xAA

# Key weighting mechanism
def apply_weights(values, multipliers):
    return [v * w for v, w in zip(values, multipliers)]

# Central logic with distractions
def aggregate_performance(metrics, weights):
    # Irrelevant normalization step (not actually used)
    normalized_metrics = [m / max(metrics) for m in metrics]  

    # Distractor: complex but unused transformation
    transformed_metrics = transform_readings(metrics)
    temp_result = compute_avg_exc_outliers(transformed_metrics)
    _ = scramble_bits(int(temp_result))  # Red herring operation

    # Critical weighted sum calculation
    weighted_vals = apply_weights(metrics, weights)
    
    # Additional distraction: unused conditional chain
    if len(weighted_vals) > 4:
        ceiling_limit = 95
        clamped = [min(w, ceiling_limit) for w in weighted_vals]
        fallback_score = sum(clamped) // len(clamped)
    elif len(weighted_vals) == 4:
        fallback_score = sum(weighted_vals) * 0.95
    else:
        fallback_score = sum(weighted_vals)

    # Real computation buried in logic
    base_score = sum(weighted_vals)
    penalty = 0
    for m in metrics:
        if m < 60:
            penalty += 5
    final_raw = base_score - penalty
    
    # Final adjustment using integer division and rounding
    final_score = int(final_raw // 1.0) if final_raw >= 0 else -(-final_raw // 1.0)
    
    # This print is required
    print(f"Result: {final_score}")
    return final_score

# Main execution with decoy data
if __name__ == "__main__":
    # Real input data (camouflaged among irrelevant ones)
    system_metrics = [88, 72, 91, 64, 77]  # Performance scores out of 100
    importance_weights = [0.2, 0.3, 0.1, 0.25, 0.15]
    
    # Distractor variables
    calibration_data = [simulate_sensor_drift(x) for x in range(10, 100, 10)]
    baseline_ref = tuple([round(x * 0.85, 2) for x in system_metrics])
    outlier_flags = [analyze_component(m, 85) for m in system_metrics]
    
    # Unused nested structure
    metadata_bundle = {
        'version': '2.1',
        'components': ['A', 'B', 'C', 'D', 'E'],
        'thresholds': {k: v for k, v in zip(['A','B','C','D','E'], baseline_ref)}
    }
    
    # Actual critical call
    final_score = aggregate_performance(system_metrics, importance_weights)