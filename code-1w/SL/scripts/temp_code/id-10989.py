def process_signals(data):
    temp_result = 0
    correction_factor = 0.85
    for val in data:
        if val < 0:
            temp_result += abs(val) * 0.1
        else:
            temp_result += int(val // 2) if val > 10 else round(val * 0.7)
    return int(temp_result * correction_factor)

# Signal acquisition and preprocessing
raw_input = [12, -4, 15, 8, -7, 23, 6]
dummy_offset = sum(x ** 2 for x in raw_input if x % 2 == 0)
threshold = len(raw_input) * 2
intermediate_stats = [x for x in raw_input if x > threshold // 4]

# Filtering logic with conditional expression
filtered_data = [x for x in raw_input if x > 5] if len(intermediate_stats) > 3 else [x for x in raw_input if x <= 0]

# Misleading normalization (not used in final result)
normalized = [round((x - min(raw_input)) / (max(raw_input) - min(raw_input)), 3) for x in raw_input]
scaling_constant = sum(normalized) / len(normalized) if normalized else 0

# Critical computation point
final_output = process_signals(filtered_data)

# Extraneous state tracking
count_positive = len([x for x in filtered_data if x > 0])
running_avg = 0
for i, x in enumerate(filtered_data):
    running_avg = (running_avg * i + x) / (i + 1) if i > 0 else x

print(f"Result: {final_output}")