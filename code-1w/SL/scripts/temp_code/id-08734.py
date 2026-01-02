import math

def preprocess_values(raw):
    adjusted = []
    offset = 1.5
    for val in raw:
        if val < 0:
            transformed = abs(val) ** 0.5 * offset
        else:
            transformed = val + offset
        adjusted.append(round(transformed, 3))
    return adjusted

# Irrelevant helper function (dead code path)
def unused_normalization(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return [round((x - mean) / (variance ** 0.5), 3) for x in data]

# Distractor computation with unused variables
tracking_log = []
total_iterations = 0
buffer_cache = []

raw_input = [4, -9, 16, -25, 36]
processed_data = preprocess_values(raw_input)

# Simulate redundant state tracking (not used in final result)
for idx, item in enumerate(processed_data):
    status_flag = "valid" if item > 3 else "marginal"
    log_entry = f"{idx}:{item}:{status_flag}"
    tracking_log.append(log_entry)
    total_iterations += 1
    if idx % 2 == 0:
        buffer_cache.append(item * 1.1)

# Key conditional expression usage (Python-specific feature)
threshold = 5.0
penalty_factor = 0.9 if any(x > threshold for x in processed_data) else 0.95

scaling_base = sum(math.sin(x) for x in processed_data if x < 10)
scale_correction = 1.05 if scaling_base < 0 else 1.0

# Core logic with multiple concepts: list processing, conditionals, arithmetic
intermediate_sum = sum(x for x in processed_data)
adjusted_sum = intermediate_sum * penalty_factor * scale_correction

# Secondary distractor: complex but unused calculation
shadow_weight = 0
for i in range(len(processed_data)):
    shadow_weight += processed_data[i] * (i + 1) ** 0.5
shadow_weight = round(shadow_weight, 4)

# Final score calculation using conditional expression
size_bonus = len(processed_data) * 0.25 if len(processed_data) >= 5 else 0

# Critical execution point
final_score = calculate_final_score(processed_data)

# Actual implementation of the required function
def calculate_final_score(data):
    base = sum(data)
    # Apply diminishing returns on large values
    bonus = sum(math.log(x + 1) for x in data if x > 4)
    penalty = sum(0.5 for x in data if x < 2)
    return round(base + bonus - penalty, 3)

# Recompute final_score after definition to ensure correctness
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")