import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.4, 25.1, 19.8, 30.2, 27.5, 22.3, 35.6, 28.9, 26.7, 24.0]
humidity_readings = [45, 52, 60, 33, 48, 55, 28, 50, 44, 58]
pressure_readings = [1013, 1009, 1015, 1020, 1012, 1018, 1005, 1014, 1016, 1010]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_OFFSET_X = 2.1
REFERENCE_VOLTAGE = 3.3
MAX_SENSOR_RANGE = 100

# Misleading intermediate processing (dead path)
def legacy_normalization(data):
    mean_val = sum(data) / len(data)
    return [0.95 * (x - mean_val) for x in data]  # Unused function

def compute_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probabilities)

# Unused entropy calculation on pressure (red herring)
entropy_pressure = compute_entropy([abs(x - 1013) for x in pressure_readings])

# Core diagnostic logic
valid_range = set(range(20, 31))  # Valid temperature range in whole degrees
threshold_set = {t for t in valid_range if t % 3 != 0}  # Filter: not divisible by 3

# String-based flag encoding (python idiom - string methods)
diagnostic_flags = "".join(["H" if h > 50 else "L" for h in humidity_readings])
flag_pattern = diagnostic_flags.replace("LL", "X").count("X")  # Distraction metric

# Data fusion and filtering
raw_mixed_data = [
    (temp, hum, press) 
    for temp, hum, press in zip(temperature_readings, humidity_readings, pressure_readings)
    if 25 <= temp <= 30 and hum < 55
]

# Extract filtered temperatures
filtered_data = [item[0] for item in raw_mixed_data]

# Decoy statistical analysis
mean_filtered = sum(filtered_data) / len(filtered_data) if filtered_data else 0
std_deviation = math.sqrt(sum((x - mean_filtered) ** 2 for x in filtered_data) / len(filtered_data)) if filtered_data else 0

# Secondary decoy: correlation attempt (irrelevant)
correlation_score = 0.0
if len(filtered_data) > 1:
    hum_subset = [h for t, h, p in raw_mixed_data]
    temp_avg = sum(filtered_data) / len(filtered_data)
    hum_avg = sum(hum_subset) / len(hum_subset)
    covariance = sum((t - temp_avg) * (h - hum_avg) for t, h in zip(filtered_data, hum_subset))
    correlation_score = covariance / (std_deviation * 2.5 + 1)

# Real computation path begins here
primary_candidates = {round(t) for t in filtered_data}  # Set of rounded temps
intersection_key = primary_candidates & threshold_set  # Match within threshold

# Conditional expression chain with nesting
adjustment_factor = 1.5 if len(intersection_key) > 2 else (
    0.8 if flag_pattern > 1 else (2.3 if std_deviation < 1.5 else 1.0)
)

# Final aggregation using min/max/average pattern
range_score = max(intersection_key) - min(intersection_key) if intersection_key else 0
base_metric = sum(intersection_key) / len(intersection_key) if intersection_key else 0

# Critical statement
final_diagnostic = int((base_metric * adjustment_factor) + range_score)

# Print required result
print(f"Result: {final_diagnostic}")