def analyze_metrics(data_set):
    # Irrelevant transformation
    temp_adjustment = sum([x ** 0.5 for x in data_set if x > 10])
    normalized = [x / (sum(data_set) / len(data_set)) for x in data_set]

    # Distractor: unused filtering
    filtered_high = [x for x in data_set if x > 15]
    filtered_low = [x for x in data_set if x < 5]

    # Actual relevant logic begins
    base_weight = len(data_set) if len(data_set) > 0 else 1
    adjustment_factor = 1.0
    if any(x > 20 for x in data_set):
        adjustment_factor *= 1.1
    if all(x < 25 for x in data_set):
        adjustment_factor *= 1.05

    return base_weight, adjustment_factor


def calculate_performance(raw_data):
    # Slice to focus on core segment
    core_segment = raw_data[2:9]
    
    # Set operation to deduplicate (some duplicates exist)
    unique_values = set(core_segment)
    processed = [x * 1.1 for x in unique_values if x % 2 == 1]  # Only odd values scaled

    # Dummy aggregation with red herring variables
    phantom_sum = sum([x ** 2 for x in raw_data if x < 0])  # Irrelevant, no negatives
    shadow_count = len([x for x in raw_data if x == 7])      # Unused count

    # Conditional expression affecting weight
    bonus_applied = 1.2 if len(unique_values) >= 5 else 1.0

    # Main calculation chain
    base_score = sum(processed) * len(processed)
    weight, factor = analyze_metrics(core_segment)
    intermediate = base_score * factor * bonus_applied
    
    # Final adjustment using slicing-derived property
    if core_segment[0] in unique_values:
        intermediate += 10

    final_score = int(intermediate + 0.5)  # Rounded integer result
    
    # Dead code path - never executed due to data
    if False and sum(core_segment) < 0:
        final_score -= 100

    return final_score

# Input data with meaningful structure
benchmark_data = [3, 6, 8, 3, 12, 9, 15, 9, 4, 18, 21]
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")