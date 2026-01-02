def analyze_sequence(values):
    total_elements = len(values)
    valid_count = 0
    temp_sum = 0
    squared_cache = [x ** 2 for x in values]  # distractor: not used later

    for val in values:
        if val > 0 and val % 2 == 1:
            valid_count += 1
            temp_sum += val

    average_positive_odd = temp_sum / valid_count if valid_count else 0
    return total_elements, average_positive_odd


def calculate_spread(data):
    if len(data) < 2:
        return 0
    sorted_data = sorted(data)
    spread = sorted_data[-1] - sorted_data[0]
    mid_value = sorted_data[len(sorted_data) // 2]
    return spread, mid_value

processed_data = [3, 7, 2, 8, 5, 11, 9, 4]

# Distractor block: unrelated statistical computation
mean_val = sum(processed_data) / len(processed_data)
variance_proxy = sum((x - mean_val) ** 2 for x in processed_data)
std_dev_estimate = variance_proxy ** 0.5

# Real logic begins
size, avg_odd = analyze_sequence(processed_data)
spread, median_val = calculate_spread(processed_data)

baseline = 10
threshold = avg_odd + (spread / 2)  # depends on prior analysis

scaling_factor = 2 if median_val > 6 else 1.5

# Conditional expression usage (required feature)
adjustment = 5 if size > 6 else 3

# Set operations (required feature): simulate unique category mapping
unique_categories = set(range(1, size + 1))
overlap_check = unique_categories & {4, 5, 6, 7}
penalty = len(overlap_check) if len(overlap_check) > 2 else 0

# Core efficiency formula
raw_efficiency = (avg_odd * scaling_factor) + (baseline - penalty)

# Final adjustment using conditional logic
final_boost = 8 if raw_efficiency >= 15 else 4

# Key statement
efficiency_score = calculate_efficiency(processed_data, threshold)

# Helper function defined after use (minor distraction)
def calculate_efficiency(data, limit):
    _, computed_avg = analyze_sequence(data)
    magnitude = sum(1 for x in data if x > limit)
    return int(computed_avg * 3 + magnitude - 2)

print(f"Result: {efficiency_score}")