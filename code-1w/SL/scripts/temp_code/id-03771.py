import math

# Simulated sensor fusion system for environmental monitoring
base_readings = [0.82, 0.71, 0.93, 0.64, 0.55]
adjusted_readings = [round(r ** 1.5, 3) for r in base_readings]

# Irrelevant calibration data (distractor)
calibration_matrix = [
    [1.1, 0.9, 1.0],
    [0.8, 1.2, 0.95],
    [1.0, 1.0, 1.1]
]
offset_correction = sum([sum(row) for row in calibration_matrix]) / 9

# Noise filtering using moving window (partially relevant but overcomplicated)
filtered_data = []
for i in range(len(adjusted_readings)):
    window = adjusted_readings[max(0, i-1):min(i+2, len(adjusted_readings))]
    filtered_data.append(sum(window) / len(window))

# Simulated time-series anomalies (dead code path)
anomalies_detected = 0
for reading in filtered_data:
    if reading > 0.8 or reading < 0.6:
        anomalies_detected += 1

# Decoy function that looks important but isn't used
def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return total

# Actual signal confidence weighting (critical path)
weights = [0.3, 0.5, 0.7, 0.4, 0.6]
confidence_adjusted = [filtered_data[i] * weights[i] for i in range(len(filtered_data))]

# Red herring: unused transformation chain
temp_transform = list(reversed(confidence_adjusted))
temp_transform = [t + 0.1 for t in temp_transform if t < 0.5]
aggregate_fusion = sum(temp_transform) * 0.9  # Misleading intermediate result

# Ground truth references for validation (irrelevant to final result)
ground_truth = {"A": 0.81, "B": 0.72, "C": 0.89, "D": 0.63, "E": 0.54}
deviations = {k: abs(confidence_adjusted[i] - v) for i, k, v in enumerate(ground_truth.items())}

# Core evaluation logic disguised among distractors
metric_weights = (0.25, 0.35, 0.4)
raw_outcomes = (
    sum(confidence_adjusted),
    max(confidence_adjusted),
    len([x for x in confidence_adjusted if x >= 0.5])
)

# Complex scoring with conditional adjustments
threshold_breach = any(d > 0.1 for d in deviations.values())
penalty_factor = 0.8 if threshold_breach else 1.0

# Final performance evaluation (key statement)
def evaluate_performance(weights, outcomes):
    base_score = 0
    for i, w in enumerate(weights):
        if i == 0:
            base_score += w * outcomes[i]
        elif i == 1:
            base_score += w * (outcomes[i] ** 2)
        else:
            base_score += w * (outcomes[i] * 10)
    
    # Additional decoy computation inside function
    debug_checksum = 0
    for j in range(len(str(int(base_score * 100)))):
        debug_checksum ^= j * 3
    
    return base_score * penalty_factor

final_score = evaluate_performance(metric_weights, raw_outcomes)
print(f"Result: {final_score}")