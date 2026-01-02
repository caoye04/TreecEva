import math

# Simulated sensor data with noise and redundant metrics
temperature_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 23.9, 24.4]
humidity_readings = [45, 48, 50, 44, 60, 55, 52]
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016, 1011]

# Irrelevant auxiliary data (distractor)
sound_levels = [32, 35, 30, 40, 38, 33, 36]  # Unused in logic
distance_meters = [1.2, 1.5, 1.1, 1.8, 1.4, 1.3, 1.6]  # Dead variable

# Preprocessing: filter anomalies using arbitrary threshold (red herring function)
def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    return [x for x in data if abs(x - mean_val) <= threshold]

# Misleading transformation chain (partially used)
normalized_temp = [round((t - 20) * 1.8 + 32, 2) for t in temperature_readings]  # Fahrenheit conversion, unused later
corrected_humidity = [(h + 5 if h < 50 else h - 3) for h in humidity_readings]  # Modified but not final

# Core processing pipeline
smoothed_pressure = [round((p - 1000), 1) for p in pressure_readings]  # Normalize to baseline

# Conditional data refinement based on dual criteria (real path starts here)
valid_indices = [
    i for i in range(len(temperature_readings))
    if temperature_readings[i] > 23.0 and humidity_readings[i] < 55
]

# Extract relevant subset
filtered_temp = [temperature_readings[i] for i in valid_indices]
filtered_humid = [corrected_humidity[i] for i in valid_indices]
filtered_press = [smoothed_pressure[i] for i in valid_indices]

# Decoy statistical computation (dead end)
mean_sound = sum(sound_levels) / len(sound_levels)
amplitude_ratio = max(distance_meters) / min(distance_meters)

# Real data transformation tree
baseline_offset = 10.0
adjusted_metrics = []
for i in range(len(filtered_temp)):
    temp_factor = math.log(filtered_temp[i] + 1)  # Non-linear scaling
    humid_weight = filtered_humid[i] / 100
    press_delta = abs(filtered_press[i] - 10)  # Deviation from expected norm

    # Composite score with weighted sum
    metric = (
        temp_factor * 0.5 +
        humid_weight * 0.3 +
        (1 / (1 + press_delta)) * 0.2  # Inverse impact
    )
    adjusted_metrics.append(round(metric * baseline_offset, 3))

# Secondary filtering: only high-confidence readings
high_confidence_metrics = [m for m in adjusted_metrics if m > 3.5]

# Mock AI confidence estimator (distractor)
def estimate_confidence(values):
    if len(values) == 0:
        return 0.0
    variance = sum([(v - sum(values)/len(values))**2 for v in values]) / len(values)
    return round(1 / (1 + variance), 4)

confidence_score = estimate_confidence(high_confidence_metrics)  # Computed but unused

# Accumulation via recursive summation (key logic)
def recursive_sum(lst, idx=0):
    if idx >= len(lst):
        return 0
    return lst[idx] + recursive_sum(lst, idx + 1)

raw_aggregate = recursive_sum(high_confidence_metrics)

# Final adjustment layer
scaling_curve = [math.sin(i * 0.5) + 1 for i in range(len(high_confidence_metrics))]
weighted_sum = sum(
    high_confidence_metrics[i] * scaling_curve[i]
    for i in range(len(high_confidence_metrics))
)

# Critical calculation point
intermediate_result = weighted_sum + math.sqrt(baseline_offset)

# Final scoring function
def calculate_final_score(data):
    if not data:
        return -1
    base = recursive_sum(data)
    penalty = len(data) * 0.1
    bonus = math.ceil(math.log(len(data) + 1)) * 0.5
    return round(base - penalty + bonus, 6)

# Execute key statement
evaluation_cohort = high_confidence_metrics[:]  # Copy of filtered data
processed_data = evaluation_cohort
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")