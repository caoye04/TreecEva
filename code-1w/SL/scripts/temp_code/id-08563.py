def process_signals(data, limit):
    magnitude_sum = 0
    temp_buffer = []
    scaling_factor = 1.75
    offset_correction = -0.25

    for val in data:
        if abs(val) > limit:
            corrected = val + offset_correction
            scaled = corrected * scaling_factor
            if scaled > 0:
                magnitude_sum += int(scaled)
                temp_buffer.append(scaled)

    return magnitude_sum


def analyze_pattern(sequence):
    pattern_score = 0
    for ch in sequence:
        if ch.isupper():
            pattern_score += ord(ch) % 10
        elif ch.isdigit():
            pattern_score -= int(ch) // 2
    return pattern_score  # Unused in final logic

# Simulated sensor readings
raw_readings = [12.4, -8.3, 9.7, 15.1, -3.2, 18.9, 7.6]
filter_threshold = 8.0

# Irrelevant transformation (distractor)
decoded_tag = "SIG_2024"
checksum_value = analyze_pattern(decoded_tag)

# Filtering relevant signals
filtered_data = []
for reading in raw_readings:
    adjusted = abs(reading)  # Use absolute magnitude
    normalized = round(adjusted, 1)
    if normalized >= filter_threshold:
        filtered_data.append(normalized)

# Additional irrelevant variables
diagnostic_log = [f"Entry_{i}" for i in range(len(filtered_data))]
metadata_flag = diagnostic_log[-1].startswith("Entry")

# Key computation path
baseline_reference = sum(filtered_data) / len(filtered_data) if filtered_data else 0
threshold = baseline_reference * 0.65

intermediate_result = 0
for x in filtered_data:
    if x > threshold:
        intermediate_result += 1

# Final output depends only on process_signals
final_output = process_signals(filtered_data, threshold)

print(f"Result: {final_output}")