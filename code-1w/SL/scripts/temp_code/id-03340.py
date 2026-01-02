def process_segments(data, limit):
    temp_result = []
    cumulative = 0
    overflow_flag = False

    for i in range(len(data)):
        segment = data[i]
        segment_sum = sum(segment)
        
        # Irrelevant transformation (distractor)
        inverted = [1.0 / (x + 1) for x in segment if x != 9]
        normalized = [x / (segment_sum + 1e-5) for x in segment]

        if segment_sum > limit:
            temp_result.append(segment_sum * 0.9)
        else:
            temp_result.append(segment_sum)

        # Dead code path (misleading)
        if len(segment) > 10:
            overflow_flag = True

    # Additional irrelevant computation
    avg_temp = sum(temp_result) / len(temp_result) if temp_result else 0
    squared_devs = [(x - avg_temp) ** 2 for x in temp_result]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    # Actual logic: sum filtered segments above median
    sorted_vals = sorted(temp_result)
    mid = len(sorted_vals) // 2
    median_val = sorted_vals[mid]

    filtered_contribution = 0
    for val in temp_result:
        if val >= median_val:
            filtered_contribution += val

    # Key transformation using slicing
    history_log = [cumulative + x for x in temp_result]
    recent_history = history_log[-3:]  # Last three entries (slicing)

    adjustment_factor = 1.0
    if len(recent_history) == 3:
        adjustment_factor = (recent_history[0] + recent_history[2]) / (recent_history[1] + 1)

    final_score = int(filtered_contribution * adjustment_factor)
    return final_score

# Main execution
raw_input = [[3, 7, 2], [8, 1, 4, 6], [5, 5], [9, 0, 1, 1], [2, 3, 5]]
threshold = 12
temp_cache = {i: sum(raw_input[i]) for i in range(len(raw_input))}  # Unused cache

# Misleading pre-check
valid_count = sum(1 for s in raw_input if len(s) >= 2 and sum(s) > 0)

final_score = process_segments(raw_input, threshold)
print(f"Result: {final_score}")