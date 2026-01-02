def transform_signal(raw_values, factor):
    """Irrelevant signal transformation (dead function)"""
    return [x * factor % 256 for x in raw_values if x > 0]


def evaluate_health_index(metrics):
    """Misleading health evaluation (distractor logic)"""
    base = sum(metrics) / len(metrics)
    adjustment = 0
    for val in metrics:
        if val > 75:
            adjustment += 10
        elif val < 25:
            adjustment -= 5
    return base + adjustment

# Irrelevant sensor constants (red herring)
SENSOR_BIAS_CORRECTION = [0.1, -0.3, 0.4, -0.2]
CALIBRATION_OFFSET = 42

# Simulated raw diagnostic readings (some relevant, some not)
raw_diagnostics = [88, 53, 71, 94, 62, 77, 81, 66]

# Extra processing with decoy transformations
shifted_readings = [(x + 5) // 3 * 2 for x in raw_diagnostics]
filtered_noise = [x for x in shifted_readings if x % 2 == 0]
decoy_aggregate = sum(filtered_noise) // len(filtered_noise) if filtered_noise else 0

# Real processing begins here — actual relevant data path
processed_data = [x for x in raw_diagnostics if 60 <= x <= 90]
sorted_diagnostics = sorted(processed_data, reverse=True)

# Threshold mapping using enumerate and zip (required Python features)
base_thresholds = [90, 80, 70, 60]
adjustment_factors = [0.95, 1.05, 1.1, 0.85]
threshold_map = {level: adj for level, adj in zip(base_thresholds, adjustment_factors)}

# Auxiliary calculation — looks important but only partially used
aux_scores = []
for i, val in enumerate(sorted_diagnostics):
    contribution = val * (0.9 + i * 0.05)
    aux_scores.append(round(contribution, 2))

# Conditional expression chain (required feature)
primary_weight = 1.1 if len(processed_data) > 4 else 0.9
secondary_weight = 0.8 if sum(processed_data) > 300 else 1.2

# Critical recursive filtering function (simple recursion, nesting depth 3)
def recursive_filter(values, limit):
    if limit <= 0 or len(values) < 2:
        return values
    mid = len(values) // 2
    left = values[:mid]
    right = [x - 1 for x in values[mid:] if x > 65]
    return recursive_filter(left + right, limit - 1)

filtered_stages = recursive_filter(sorted_diagnostics, 3)

# Real computation path: weighted average with threshold adjustment
adjusted_values = []
for val in filtered_stages:
    # Find closest threshold ceiling
    applicable = None
    for t in sorted(base_thresholds, reverse=True):
        if val <= t:
            applicable = t
            break
    multiplier = threshold_map.get(applicable, 1.0)
    adjusted_values.append(val * multiplier)

# Final aggregation logic
aggregate_score = sum(adjusted_values)

# Secondary influence from auxiliary path (minor real use)
feedback_factor = len(aux_scores) / len(adjusted_values) if adjusted_values else 1.0

# Final diagnostic computed here — this is the target answer
final_diagnostic = int((aggregate_score * primary_weight + feedback_factor * 10) // 1)

# Print result for execution visibility
print(f"Result: {final_diagnostic}")