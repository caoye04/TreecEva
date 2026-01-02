def analyze_component(reading, threshold=75):
    if reading < threshold:
        return (reading * 1.2) + 5
    else:
        return (reading * 0.9) - 10

# Irrelevant sensor calibration data (distractor)
calibration_offsets = [0.1, -0.3, 0.05, 0.4]
adjusted_readings = []
for i in range(4):
    adjusted_readings.append(calibration_offsets[i] * 100)

# Simulated system metrics from different subsystems
raw_metrics = [68, 82, 74, 91, 65]
processed_metrics = []

# Misleading pre-processing with dead logic branch
scaling_factor = 1.0
if len(raw_metrics) > 10:
    scaling_factor = 0.5  # Dead code path

for val in raw_metrics:
    processed_val = analyze_component(val)
    processed_metrics.append(round(processed_val))

# Decoy function that is never called
def deprecated_analysis(x):
    return sum([i**2 for i in x]) // len(x)

# Weight configuration for evaluation (critical)
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Red herring: unused backup weights
backup_weights = [0.1, 0.4, 0.2, 0.2, 0.1]
total_weight = sum(backup_weights)  # Misleading computation

# Auxiliary transformation using enumerate and zip (required python features)
indexed_transform = []
for idx, (metric, weight) in enumerate(zip(processed_metrics, weights)):
    if idx % 2 == 0:
        indexed_transform.append(metric * weight * 1.1)
    else:
        indexed_transform.append(metric * weight * 0.95)

# Conditional early exit simulation (not triggered)
if min(processed_metrics) < 0:
    final_score = -999
    print("Error: Invalid metric")
    exit()

# Core evaluation logic
weighted_sum = 0.0
max_deviation = 0.0
base_avg = sum(processed_metrics) / len(processed_metrics)

for m in processed_metrics:
    deviation = abs(m - base_avg)
    if deviation > max_deviation:
        max_deviation = deviation

# Apply penalty if high variance detected
variance_penalty = 0
if max_deviation > 20:
    variance_penalty = 15
elif max_deviation > 10:
    variance_penalty = 5

# Final performance scoring
final_components = []
for i, (proc, w) in enumerate(zip(processed_metrics, weights)):
    contribution = proc * w
    final_components.append(contribution)

raw_final = sum(final_components)
final_score = int(raw_final - variance_penalty)

# Distractor: unused accumulation
rolling_total = 0
for j in range(len(final_components)):
    rolling_total += final_components[j] * (j + 1)

# Output result as required
print(f"Result: {final_score}")