def analyze_sensor(input_val, threshold=100):
    if input_val < threshold:
        return (input_val * 3) + 7
    else:
        return (input_val // 2) ^ 5

# Simulated environmental sensor readings
temp_readings = [23, 45, 102, 67, 200, 89, 150]

# Irrelevant calibration data (distractor)
calibration_matrix = [[1, 0], [0, 1]]
scaling_factor = 1.003
offset_adjustment = -0.05

# Secondary processing chain with misleading intermediate steps
adjusted_values = []
for val in temp_readings:
    adjusted = val + 2
    adjusted_values.append(adjusted)

# Apply analysis function conditionally using list comprehension
analyzed_data = [analyze_sensor(x) for x in adjusted_values if x != 89]

# Decoy transformation - never used but looks important
def transform_sequence(seq):
    return [x << 1 for x in seq if x % 2 == 0]

transformed = transform_sequence(analyzed_data)

# Filter based on bitwise condition (relevant path)
filtered_data = []
for num in analyzed_data:
    if (num & 1) == 1 and num > 20:  # Keep odd numbers greater than 20
        filtered_data.append(num)

# Red herring: unused statistical computation
mean_fake = sum(analyzed_data) / len(analyzed_data) if analyzed_data else 0
deceptive_median = sorted(analyzed_data)[len(analyzed_data)//2]

# Core logic disguised among noise
running_total = 0
for i, v in enumerate(filtered_data):
    running_total += v * (i + 1)

# Conditional expression determining final input
primary_input = running_total if len(filtered_data) > 3 else running_total * 2

# Final processing function with mixed operations
def process_readings(data_list):
    accumulator = 0
    multiplier = 1
    for item in data_list:
        if item % 3 == 0:
            accumulator += item >> 1
        elif item % 5 == 0:
            accumulator -= item & 7
        else:
            accumulator += (item ^ multiplier) % 100
        multiplier = (multiplier * 2) % 97
    return accumulator * len(data_list)

# Misleading post-processing (dead code path)
final_correction = None
if primary_input > 1000:
    final_correction = primary_input * 0.95
else:
    final_correction = primary_input + 50  # Never used

# Key execution point
final_diagnostic = process_readings(filtered_data)

# Output result as required
print(f"Target result: {final_diagnostic}")