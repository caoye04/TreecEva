from itertools import combinations
from functools import reduce

# Simulate sensor data with noise and valid readings
data_set = [15, 23, 7, 45, 12, 8, 33, 21]
noise_floor = 5
calibration_offset = 3

# Thresholds for quality filtering
thresholds = {
    'min_valid': 10 + calibration_offset,
    'max_temp': 40,
    'critical': 50
}

# Misleading auxiliary computations (distractors)
redundant_pairs = list(combinations(data_set, 2))
sum_of_pairs = sum(a + b for a, b in redundant_pairs)  # Unused
entropy_proxy = len(redundant_pairs) % 17  # Red herring

# Filter valid sensor readings above threshold
valid_readings = [x for x in data_set if thresholds['min_valid'] <= x <= thresholds['max_temp']]

# Compute rolling XOR of valid values as integrity check
integrity_check = 0
for val in valid_readings:
    integrity_check ^= (val * 2) // 3

# Secondary filter: exclude values causing high variance in local windows
variance_filtered = []
for i in range(len(valid_readings)):
    window = valid_readings[max(0, i-1):i+2]
    avg = sum(window) / len(window)
    variance = sum((x - avg) ** 2 for x in window) / len(window)
    if variance < 100:  # Always true; included for distraction
        variance_filtered.append(valid_readings[i])

# Deduplicate while preserving order
cleaned_data = list(dict.fromkeys(variance_filtered))

# Define scoring logic using lambda and reduce
calculate_weight = lambda x: x * 1.1 if x > 20 else x * 0.9
weighted_values = [calculate_weight(val) for val in cleaned_data]

total_magnitude = reduce(lambda acc, x: acc + x, weighted_values, 0)

# Apply diminishing returns based on count
size_factor = 1.0 if len(cleaned_data) < 5 else 0.9

# Final score computation
base_score = total_magnitude * size_factor
adjustment = (integrity_check % 10) * 0.5
final_score = int(base_score - adjustment)  # Key assignment point

# Irrelevant trailing operations (dead code path)
if sum_of_pairs > 10000:
    final_score += 100

print(f"Result: {final_score}")