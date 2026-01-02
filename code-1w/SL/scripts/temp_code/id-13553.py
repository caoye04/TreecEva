def analyze_system_health(sensor_data, thresholds):
    cumulative_risk = 0
    risk_factors = []
    for i, reading in enumerate(sensor_data):
        if reading > thresholds[i % len(thresholds)]:
            cumulative_risk += (reading - thresholds[i % len(thresholds)]) ** 2

    adjustment_factor = 0.87
    adjusted_risk = cumulative_risk * adjustment_factor

    # Irrelevant transformation - red herring
    transformed_readings = [x * 1.05 + 2.1 for x in sensor_data if x < 50]
    avg_transformed = sum(transformed_readings) / len(transformed_readings) if transformed_readings else 0

    # Dead code path - never executed due to logic
    emergency_override = False
    if len(sensor_data) > 1000:
        emergency_override = True  # Impossible under current inputs

    return adjusted_risk


def evaluate_component_stress(load_profile):
    base_stress = 0
    peak_moments = []

    for j, load in enumerate(load_profile):
        if load > 75:
            base_stress += 1.5
            if j % 2 == 0:
                base_stress += 0.2
        elif load > 50:
            base_stress += 0.7

        # Misleading metric
        instantaneous_ratio = load / (j + 1) if j > 0 else 0
        if instantaneous_ratio > 10:
            peak_moments.append(j)

    # Unused complex calculation
    decay_weights = [(0.9 ** k) for k in range(len(load_profile))]
    weighted_decay_sum = sum(a * b for a, b in zip(load_profile, decay_weights))

    return base_stress


def aggregate_metrics(scores, logs):
    score_sum = sum(scores)
    log_weight = len(logs) * 0.3

    # Distractor: complex-looking but unused formula
    entropy_proxy = 0
    for s in scores:
        if s > 0:
            entropy_proxy -= s * __import__('math').log(s + 1e-8)

    # Real computation buried among noise
    scaling_factor = 1.25
    normalized_bias = 4.8
    result = (score_sum + log_weight) * scaling_factor - normalized_bias

    # Multiple assignments with decoy
    temp_a, temp_b, temp_c = 12, 24, 36
    temp_a = temp_b = temp_c = 0  # Reset - distractor

    return int(result)

# Simulated input data
reliability_scores = [8.3, 7.9, 8.1, 8.5, 7.7, 8.0, 8.2, 7.8]
system_load_log = [65, 70, 72, 68, 75, 73, 69]

# Irrelevant pre-processing - looks important
offset_map = list(enumerate([x - 60 for x in system_load_log if x > 65]))
dynamic_pairs = list(zip(reliability_scores[::2], reliability_scores[1::2]))
mean_pair_diff = sum(abs(a - b) for a, b in dynamic_pairs)

# Hidden critical call chain
raw_sensor_input = [45, 52, 61, 49, 70, 58]
threshold_settings = [40, 50, 60]

# Decoy function calls with side-effect-like appearance
analyze_system_health(raw_sensor_input, threshold_settings)
evaluate_component_stress(system_load_log)

# Key statement
final_diagnostic = aggregate_metrics(reliability_scores, system_load_log)

print(f"Result: {final_diagnostic}")