def normalize_string(s):
    # Irrelevant string processing function
    cleaned = s.strip().lower().replace('_', ' ')
    words = cleaned.split()
    return ' '.join([word.capitalize() for word in words])

# Dummy data that looks important but isn't used in final calculation
text_records = [' DATA_POINT_1 ', 'DATA_POINT_2', 'data_point_3']
normalized_texts = [normalize_string(rec) for rec in text_records]

# Core computation setup
raw_values = [18, 24, 36, 42, 50]
offset_threshold = 10
adjustment_factor = 0.9

# Simulate some environmental condition (distractor)
current_mode = "calibration"
mode_flag = 1 if "calib" in current_mode else 0

# Processing with intermediate steps and red herrings
deviations = []
baseline_avg = sum(raw_values) / len(raw_values)  # 34.0
for val in raw_values:
    deviation = abs(val - baseline_avg)
    deviations.append(deviation)

# Extra distraction: compute variance but don't use it directly
variance = sum(d**2 for d in deviations) / len(deviations)
std_dev = variance ** 0.5
noise_floor = std_dev * 0.1

# Actual processing path
filtered_values = [v for v in raw_values if v >= baseline_avg]
processed_values = []
for v in filtered_values:
    adjusted = v * adjustment_factor
    if adjusted % 2 == 0:
        adjusted += mode_flag  # adds nothing, but looks like state dependency
    processed_values.append(adjusted)

# Secondary distraction: unused combinatorial count
total_pairs = 0
for i in range(len(processed_values)):
    for j in range(i + 1, len(processed_values)):
        if (processed_values[i] + processed_values[j]) > 50:
            total_pairs += 1

# Key statement
final_score = calculate_adjusted_average(processed_values)

# Helper function defined after use (mild distraction)
def calculate_adjusted_average(nums):
    if not nums:
        return 0.0
    raw_avg = sum(nums) / len(nums)
    penalty = 0.5 if len(nums) < 4 else 0
    # Apply penalty only if string condition met (fake dependency)
    trigger_str = "Safety_Check"
    upper_chars = [c for c in trigger_str if c.isupper()]
    if len(upper_chars) >= 6:
        penalty += 0.2
    return raw_avg - penalty

print(f"Result: {final_score}")