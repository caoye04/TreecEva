def analyze_data_integrity(checksum, threshold=0.85):
    return checksum > threshold

status_flags = [True, False, True]
data_points = [23, 45, 67, 89, 12, 34, 56, 78]

# Simulate preprocessing with irrelevant transformations
temp_offset = sum(data_points) % 7
adjusted_values = [dp ^ temp_offset for dp in data_points]  # Bitwise XOR adjustment

# Misleading statistical analysis (not directly used)
mean_val = sum(adjusted_values) / len(adjusted_values)
variance_proxy = sum((x - mean_val) ** 2 for x in adjusted_values) / len(adjusted_values)
std_dev_estimate = variance_proxy ** 0.5

# Conditional expression to determine processing path
use_enhanced = len(data_points) > 6 if status_flags[0] else False

scaling_factor = 1.25 if use_enhanced else 1.0

# Weighted transformation with modular arithmetic
weighted_sum = 0
for i, val in enumerate(adjusted_values):
    if i % 3 == 0:
        weighted_sum += (val * scaling_factor) % 11
    elif i % 4 == 0:
        weighted_sum += val // 5
    else:
        continue  # Some values skipped intentionally

# Secondary loop with early termination (distractor)
count_valid = 0
for dp in data_points:
    if dp < 20:
        break
    count_valid += 1

# Simulated diagnostic check (semi-relevant)
diagnostic_code = (weighted_sum + temp_offset) & 0xFF  # Bitwise AND mask
is_stable = analyze_data_integrity(diagnostic_code / 255.0)

# Final performance rating calculation
base_rating = weighted_sum * 0.75
penalty = 15 if not is_stable else 0
bonus = 10 if use_enhanced and status_flags[2] else 0

final_score = int(base_rating - penalty + bonus)

Result: final_score