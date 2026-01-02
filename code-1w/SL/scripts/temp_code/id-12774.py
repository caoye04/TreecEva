def analyze_patient_vitals(vital_signs):
    # Irrelevant preprocessing
    normalized = [v / max(vital_signs) for v in vital_signs]
    anomalies = []
    for val in vital_signs:
        if val > 100 or val < 60:
            anomalies.append(val)
    # Distractor: unused computation
    avg_anomaly_gap = sum(anomalies) / len(anomalies) if anomalies else 0
    return sum(vital_signs) // len(vital_signs)

# Decoy function - looks important but unused in final path
def compute_stability_index(readings):
    diff = [abs(readings[i] - readings[i-1]) for i in range(1, len(readings))]
    return sum(diff) / len(diff) if diff else 0

# Real processing chain
transform = lambda x: (x ** 2 + 3 * x + 1) % 107

health_data = [72, 85, 91, 64, 77, 88, 95]

# Early filtering with misleading condition
if any(x > 90 for x in health_data):
    filtered_data = [x for x in health_data if x <= 90]
else:
    filtered_data = health_data[:]

# Bit manipulation decoy
obfuscated_key = 0
for val in health_data:
    obfuscated_key ^= (val << 2) | (val >> 1)
obfuscated_key = obfuscated_key & 0xFF  # Truncate to 8 bits

# Unused recursive distraction
def count_subsequences(arr, target=75):
    if len(arr) == 0:
        return 1
    if arr[0] < target:
        return count_subsequences(arr[1:], target) + count_subsequences(arr[1:], target - arr[0])
    else:
        return count_subsequences(arr[1:], target)

# Real threshold logic
baseline = analyze_patient_vitals(filtered_data)
threshold_fn = lambda x: x > baseline + 5

# Data transformation using lambda and conditional logic
diagnostic_scores = []
for entry in filtered_data:
    score = transform(entry)
    adjusted = score + 10 if threshold_fn(entry) else score - 2
    diagnostic_scores.append(adjusted)

# Complex aggregation with red herring intermediate
weighted_sum = 0
weight_sequence = [1, 2, 1, 3, 2, 1]
for i, s in enumerate(diagnostic_scores):
    weight = weight_sequence[i % len(weight_sequence)]
    weighted_sum += s * weight

# Dead code branch - never executed due to data
if len(diagnostic_scores) > 10:
    weighted_sum = int(weighted_sum / 2)

# Final computation path
checksum = sum(diagnostic_scores) ^ weighted_sum
checksum = checksum + 5 if checksum % 2 == 0 else checksum + 3

# Critical execution point
final_diagnostic = process_metrics(health_data, threshold_fn)

# Supporting function defined late (misdirection)
def process_metrics(data, condition):
    base = sum(transform(x) for x in data if condition(x))
    penalty = len([x for x in data if not condition(x)]) * 3
    return base - penalty + len(data)

print(f"Result: {final_diagnostic}")