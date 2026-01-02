def analyze_component(x, threshold=5):
    if x < threshold:
        return x * 1.5
    else:
        return x * 0.8 + 3

# Irrelevant helper function (decoy)
def deprecated_calib(value):
    return (value >> 2) ^ 7

# Unused data structure (red herring)
legacy_mapping = {1: 'A', 2: 'B', 5: 'E', 8: 'H'}

# Simulated sensor readings – misleading context
raw_readings = [3, 7, 4, 9, 2, 8, 6]
adjusted_readings = [analyze_component(x) for x in raw_readings]

# Intermediate transformation with distractor variables
offset_correction = sum(adjusted_readings) / len(adjusted_readings)
dummy_weight = 0.95

# Core logic disguised among noise
base_metrics = [round(r * offset_correction * 0.1) for r in adjusted_readings]

# Bit manipulation decoy
flag_mask = 0b101010
activation_flag = (len(base_metrics) << 2) & flag_mask

# Real computation hidden in list operations
evaluation_pool = []
for i, val in enumerate(base_metrics):
    if i % 2 == 0:
        evaluation_pool.append(val + i)
    else:
        evaluation_pool.append(val - 1)

# Conditional expression usage
feedback_candidates = [x if x > 4 else 4 for x in evaluation_pool]

# Set operation to remove duplicates (key step)
feedback_set = set(feedback_candidates)

# Distractor: unused zip with enumerate
misleading_pairs = list(zip(enumerate(raw_readings), legacy_mapping.keys()))

# Fake aggregation path (dead code)
temp_aggregate = 0
for idx, val in enumerate(feedback_candidates):
    temp_aggregate += val * (idx % 4 + 1)

# Another irrelevant bit op
checksum = activation_flag ^ 0b1111

# Real final computation
summed = sum(feedback_set)
counted = len([x for x in feedback_set if x > 5])

# Key statement with conditional expression
final_score = summed if counted >= 3 else summed * 0.7

# Print required output
print(f"Result: {final_score}")