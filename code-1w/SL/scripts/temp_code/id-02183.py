import math

# Irrelevant helper function (dead code path)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v]

# Misleading performance metric that is never used
def legacy_scorer(data):
    return sum(d * 0.7 for d in data) % 97

# Core system: Sensor fusion scoring with weighted evaluation
def evaluate_performance(sensor_metrics, weight_profile):
    # Step 1: Validate input dimensions
    if len(sensor_metrics) != len(weight_profile):
        raise ValueError("Mismatched dimensions")

    # Step 2: Apply dynamic gain adjustment based on signal stability
    adjusted = []
    for i, metric in enumerate(sensor_metrics):
        stability_factor = 1.0 + (math.sin(i + 0.5) * 0.1)  # Small perturbation
        boosted = metric * stability_factor
        adjusted.append(boosted)

    # Step 3: Mask certain sensors under threshold condition (red herring logic)
    masked = [
        adj if met > 20 else adj * 0.1
        for adj, met in zip(adjusted, sensor_metrics)
    ]

    # Step 4: Apply nonlinear compression on high readings
    compressed = [
        val if val <= 50 else 50 + math.log10(val - 49)
        for val in masked
    ]

    # Step 5: Compute weighted sum using lambda-transformed weights
    smooth_weight = lambda w: (w ** 1.1) / 1.5
    enhanced_weights = list(map(smooth_weight, weight_profile))

    # Step 6: Normalize weights to prevent inflation
    total_weight = sum(enhanced_weights)
    normalized_weights = [w / total_weight for w in enhanced_weights]

    # Step 7: Dot product simulation using tuples and index alignment
    contributions = tuple(
        comp * norm_w
        for comp, norm_w in zip(compressed, normalized_weights)
    )

    # Step 8: Aggregate final score with precision floor
    raw_score = sum(contributions)
    final_score = math.floor(raw_score * 1000) / 1000  # Milliprecision

    # Decoy computation (never used)
    outlier_count = sum(1 for c in compressed if c > 60)
    penalty = outlier_count * 2.5

    return final_score

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
temp_calibration = [0.88, 0.91, 0.85, 0.94]
reference_baseline = {'alpha': 42.0, 'beta': 38.5}

# Key data inputs
primary_metrics = [45, 32, 67, 23, 55]
weight_scheme = [0.2, 0.15, 0.3, 0.1, 0.25]

# Unused but plausible alternate configuration (misdirection)
alternate_weights = [w * 1.2 for w in weight_scheme]

# Core execution point
final_score = evaluate_performance(primary_metrics, weight_scheme)

# Output result as required
print(f"Result: {final_score}")