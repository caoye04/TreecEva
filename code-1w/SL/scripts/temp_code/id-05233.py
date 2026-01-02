from collections import defaultdict, Counter
import math

# Simulated sensor data preprocessing pipeline
raw_readings = [145, 273, 91, 412, 88, 305, 177, 221, 64, 398]
offset_adjustment = 42
adjusted_readings = [x - offset_adjustment for x in raw_readings if x > 100]

# Irrelevant statistical summary (red herring)
mean_value = sum(adjusted_readings) / len(adjusted_readings)
variance_proxy = sum((x - mean_value) ** 2 for x in adjusted_readings) / len(adjusted_readings)
entropy_estimate = math.log(len(adjusted_readings))

# Data transformation phase
transformation_key = [math.sin(i * 0.1) for i in range(len(adjusted_readings))]
scaled_factors = [abs(math.cos(x * 0.01)) + 0.5 for x in adjusted_readings]
transformed_data = []
for i, val in enumerate(adjusted_readings):
    transformed = int(val * scaled_factors[i] + transformation_key[i] * 10)
    if transformed % 2 == 0:
        transformed_data.append(transformed // 2)
    else:
        transformed_data.append(transformed)

# Decoy pattern detection (dead path)
def detect_anomaly_sequence(data):
    if len(data) < 3:
        return False
    for i in range(len(data) - 2):
        if data[i] + data[i+1] == data[i+2]:
            return True
    return False

anomaly_flag = detect_anomaly_sequence(raw_readings)  # Unused result

# Threshold map construction with distractor logic
base_thresholds = {i: 100 + i*5 for i in range(1, 6)}
threshold_map = defaultdict(lambda: 200)
for k, v in base_thresholds.items():
    threshold_map[k] = v + int(math.sqrt(k * 10))

# Redundant frequency analysis
reading_frequencies = Counter(adjusted_readings)
dominant_count = max(reading_frequencies.values())

# Auxiliary diagnostic function with multiple concerns
def compute_health_score(seq, config):
    score = 0
    for i, x in enumerate(seq):
        if x > config.get(3, 115):
            score += 1
        if i % 3 == 0 and x < config.get(5, 125):
            score += 2
    return score - len(seq) // 4

# Another decoy function that is defined but not used
def legacy_diagnosis(arr):
    accumulated = 0
    for j in range(len(arr)):
        accumulated += arr[j] ^ (j * 3)
    return accumulated >> 2

# Core analysis logic
mask_sequence = [1 if x > 80 else 0 for x in transformed_data]
masked_sum = sum(val * mask_sequence[i] for i, val in enumerate(transformed_data))

# Conditional data slicing based on position and value
primary_segment = transformed_data[1:7:2]  # Every other from index 1 to 6
secondary_segment = transformed_data[::-1][:4]  # Last four reversed

fusion_score = 0
for a, b in zip(primary_segment, secondary_segment):
    fusion_score += (a & b) + (a >> 2)  # Bitwise combination

# Final control flow with short-circuit logic
health_baseline = compute_health_score(transformed_data, dict(threshold_map))
if len(transformed_data) > 5 and health_baseline > 3 or anomaly_flag:
    adjustment_factor = 1.25
else:
    adjustment_factor = 0.85

# Key computation chain
interim_result = (masked_sum + fusion_score) * adjustment_factor
rounded_diagnostics = [round(interim_result / (i+1)) for i in range(3)]
final_diagnostic = int(sum(rounded_diagnostics) // 1.5)

# Misleading intermediate printout (commented out, still distracting)
# print(f'Debug: {fusion_score=}, {entropy_estimate=}, {dominant_count=}')

Result: {final_diagnostic}