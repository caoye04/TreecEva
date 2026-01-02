def preprocess_input(raw_sequence):
    normalized = [x % 256 for x in raw_sequence]
    shifted = [(x << 1) & 255 for x in normalized]
    return shifted

raw_data = [120, 240, 350, 400, 512, 600]
filtered_data = [x for x in raw_data if x < 500]
processed_data = preprocess_input(filtered_data)

# Irrelevant transformation (distractor)
temporary_map = {i: chr(ord('A') + (i % 26)) for i in range(100)}
lookup_result = temporary_map.get(len(processed_data), 'Z')

# Secondary processing path with red herring
shadow_buffer = []
for val in processed_data:
    shadow_buffer.append(val ^ 255)

# Actual computation chain begins
sum_primary = sum(processed_data)
sum_inverted = sum(shadow_buffer)
entropy_proxy = abs(sum_primary - sum_inverted)

# Use of slicing and set operations (required features)
segment_a = processed_data[:3]
segment_b = processed_data[1:4]
duplicate_check = set(segment_a) & set(segment_b)
overlap_count = len(duplicate_check)

# Conditional logic affecting final result
if overlap_count > 1:
    base_score = entropy_proxy // 3
else:
    base_score = entropy_proxy // 4

# Case conversion as part of a misleading string operation (suggested paradigm)
status_flag = "Active"
flag_lower = status_flag.lower()
activation_code = len(flag_lower) * 100  # unused distractor

# Final calculation using dictionary lookup (required feature)
correction_map = {2: 15, 3: 12, 4: 8}
correction_factor = correction_map.get(overlap_count, 5)

# Key statement
final_score = calculate_final_score(processed_data)

# Function defined after usage to increase cognitive load
def calculate_final_score(data):
    temp_sum = sum(x * x for x in data)
    mean_square = temp_sum / len(data)
    adjusted = int(mean_square - correction_factor * base_score)
    return adjusted

print(f"Result: {final_score}")