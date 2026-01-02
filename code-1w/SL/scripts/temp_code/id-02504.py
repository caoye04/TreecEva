def normalize_readings(readings):
    max_val = max(readings)
    return [round(x / max_val, 4) for x in readings]


def validate_string_format(s):
    if not isinstance(s, str):
        return False
    return s.isalnum() and len(s) > 0

process_tags = ['THERM-202', 'PRESS-401', 'FLOW-305']
raw_sensor_data = [850, 910, 790, 1020, 880]

# Normalize sensor inputs
normalized_data = normalize_readings(raw_sensor_data)

# Simulate intermediate diagnostic checks (distractor block)
diagnostic_flags = []
for i, val in enumerate(normalized_data):
    status_code = "OK" if val > 0.8 else "CALIBRATE"
    diagnostic_flags.append(f"{process_tags[i % 3]}:{status_code}")

# Misleading capacity estimate (not used in final calculation)
potential_capacity_estimate = sum([int(d * 100) for d in normalized_data])

# Actual processing sequence with string-based control logic
process_sequence = ""
for tag in process_tags:
    clean_tag = tag.replace("-", "_").lower()
    if validate_string_format(clean_tag):
        process_sequence += clean_tag

auxiliary_sum = 0
for char in process_sequence:
    auxiliary_sum += ord(char) % 10

# Core logic: calculate thermal output based on normalized data
base_index = 0
for val in normalized_data:
    if val >= 0.9:
        base_index += 1

scaling_factor = len(process_sequence) + base_index

# Red herring computation: unrelated average
unrelated_avg = sum(raw_sensor_data) / len(raw_sensor_data)

# Key function that computes the actual result
def calculate_thermal_output(tag_str):
    length_component = len(tag_str)
    char_value = 0
    for c in tag_str:
        if c in 'aeiou':
            char_value += 1
        elif c.isnumeric():
            char_value += int(c) * 2
    return length_component * 15 + char_value

# Critical statement
thermal_capacity = calculate_thermal_output(process_sequence)

# Print result for evaluation
print(f"Result: {thermal_capacity}")