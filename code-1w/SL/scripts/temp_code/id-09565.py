def process_signals(data, limit):
    magnitude = lambda x: abs(x)
    adjusted = [magnitude(val) ** 0.5 for val in data if magnitude(val) > limit]
    if len(adjusted) == 0:
        return -1
    scaling_factor = sum(adjusted) / len(adjusted)
    normalized = [val / scaling_factor for val in adjusted]
    outlier_mask = [val > 2.0 for val in normalized]
    clean_data = [normalized[i] for i in range(len(normalized)) if not outlier_mask[i]]
    if not clean_data:
        clean_data = [0.0]
    avg_clean = sum(clean_data) / len(clean_data)
    return int(avg_clean * 100)

# Simulated sensor readings with noise
temp_readings = [-150, -89, 45, 102, 0, -3, 200, 75, 60, -20, 95]

# Irrelevant transformations (distractors)
distorted_copy = [x * 1.1 + 5 for x in temp_readings if x % 2 == 1]
placeholder_sum = sum(distorted_copy[:3]) if len(distorted_copy) >= 3 else 0
temp_stats = {"min": min(temp_readings), "max": max(temp_readings), "range": 0}
temp_stats["range"] = temp_stats["max"] - temp_stats["min"]

# Filtering logic with red herring condition
filter_bias = 50
use_dynamic_bias = False
if len(temp_readings) > 5 and temp_stats["range"] > 100:
    use_dynamic_bias = True
    dynamic_adjustment = len(temp_readings) // 2
    filter_bias += dynamic_adjustment  # This is never actually used

# Actual filtering based on static threshold
threshold = 40
filtered_data = [x for x in temp_readings if abs(x) >= threshold]

# Dead code path (never executed due to constant condition)
intermediate_result = None
if False:
    intermediate_result = [x for x in filtered_data if x < 0]
    intermediate_result = [abs(x) for x in intermediate_result]

# Key processing step
final_output = process_signals(filtered_data, threshold)

# Extraneous post-processing
checksum = sum([final_output % i for i in range(1, 6) if final_output % i == 0])
verification_flag = checksum > 10

print(f"Result: {final_output}")