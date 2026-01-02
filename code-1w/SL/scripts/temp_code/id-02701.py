def analyze_readings(data, threshold):
    count_valid = 0
    sum_adjusted = 0.0
    temp_offset = 0.5  # Irrelevant offset for noise
    for val in data:
        adjusted_val = val - temp_offset
        if abs(adjusted_val) > threshold:
            count_valid += 1
            sum_adjusted += abs(adjusted_val)
    return count_valid, sum_adjusted if count_valid > 0 else 1  # Avoid div by zero


def normalize_value(x, min_val, max_val):
    # Dead function - never called
    return (x - min_val) / (max_val - min_val) if max_val != min_val else 0

baseline = [3.2, -1.4, 5.6, 2.8, -0.9]
readings = [4.1, -2.3, 6.7, 3.0, -1.1, 8.4, -5.0, 2.2]

# Extraneous variable computations
sum_baseline = sum([abs(x) for x in baseline])
avg_baseline = sum_baseline / len(baseline)
baseline_variance = sum((x - avg_baseline) ** 2 for x in baseline)

# Simulate sensor drift correction (partially irrelevant)
drift_correction = {}
correction_factor = 0.9
for i, val in enumerate(readings):
    drift_correction[i] = val * correction_factor if val > 4 else val

# Main logic disguised among distractions
count, total = analyze_readings(readings, 2.0)

# Secondary filtering path that isn't used
filtered = [v for v in readings if v > 0]
redundant_sum = sum(filtered) * 0.1  # Unused computation

scaling_constant = 1.75
intermediate_metric = total / scaling_constant if scaling_constant != 0 else 0

# Conditional expression with dictionary lookup
status_map = {0: 'low', 1: 'medium', 2: 'high'}
eval_category = status_map.get(count // 3, 'unknown')

# Key statement
final_score = calculate_performance(baseline, readings) if 'high' in eval_category else (intermediate_metric * 2)

# Definition placed after usage to increase cognitive load (but valid in Python due to def ordering)
def calculate_performance(base, inputs):
    base_len = len(base)
    input_len = len(inputs)
    ratio = input_len / base_len
    _, main_total = analyze_readings(inputs, 2.0)
    performance = main_total * ratio
    bonus = 10 if any(x < -4 for x in inputs) else 0  # Extra logic
    return int(performance + bonus)

print(f"Result: {final_score}")