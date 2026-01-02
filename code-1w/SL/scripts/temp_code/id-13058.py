import math

def process_metrics(raw_data):
    # Initialize tracking variables (some are distractions)
    total_samples = len(raw_data)
    valid_count = 0
    outlier_threshold = 3 * math.sqrt(sum([x**2 for x in raw_data]) / len(raw_data))  # RMS-based threshold
    filtered_data = []
    squared_errors = []
    temp_sum = 0
    cumulative_product = 1  # unused distractor
    intermediate_flag = False

    # First pass: filter outliers and collect valid data
    for value in raw_data:
        if abs(value) < outlier_threshold:
            filtered_data.append(value)
            valid_count += 1
            temp_sum += value
        else:
            squared_errors.append((value - temp_sum / max(valid_count, 1)) ** 2)  # misleading use

    # Compute mean and variance on filtered data
    mean_value = temp_sum / max(valid_count, 1)
    variance = sum([(x - mean_value) ** 2 for x in filtered_data]) / max(valid_count, 1)
    std_dev = math.sqrt(variance)

    # Simulate auxiliary calculation with dead code path
    adjustment_factor = 1.0
    if len(squared_errors) > 10:
        adjustment_factor = 0.9  # unreachable due to data size
    elif std_dev == 0:
        adjustment_factor = 1.1

    # Efficiency metric computation with conditional expression
    base_efficiency = (mean_value + 1e-5) / (std_dev + 1e-5)
    efficiency_score = base_efficiency if base_efficiency > 0 else -base_efficiency

    # Red herring: unused list comprehension
    _ = [math.log(abs(x) + 1) for x in raw_data if x != 0]

    # Additional distraction: nested loop that computes irrelevant metric
    correlation_proxy = 0
    for i in range(min(3, len(filtered_data))):
        for j in range(min(3, len(filtered_data))):
            if i != j:
                correlation_proxy += filtered_data[i] * filtered_data[j]

    # Final processing step
    final_output = {
        'efficiency_score': efficiency_score,
        'valid_ratio': valid_count / total_samples,
        'outlier_count': total_samples - valid_count
    }
    return final_output

# Input data
data_points = [12, 15, 14, 10, 13, 30, -5, 11, 14, 12, 13, 15]

# Execute main logic
result_dict = process_metrics(data_points)
efficiency_score = result_dict['efficiency_score']
print(f"Result: {efficiency_score}")