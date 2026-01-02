def analyze_component(values, threshold):
    count_above = 0
    sum_filtered = 0
    temp_result = []
    for i, val in enumerate(values):
        if val > threshold:
            count_above += 1
            sum_filtered += val
            temp_result.append(val * 0.9)
    avg = sum_filtered / count_above if count_above > 0 else 0
    return avg, count_above


def validate_inputs(data_list):
    # Distractor: this function is called but doesn't affect final result
    if not all(isinstance(x, (int, float)) for x in data_list):
        return False
    return len(data_list) > 0


def calculate_performance(raw_data):
    # Misleading variable names and irrelevant computations
    processed = [x for x in raw_data if x >= 0]
    normalized = [round(x ** 0.5, 2) for x in processed]
    
    # Real computation begins
    high_perf = [x for x in normalized if x > 3.0]
    low_perf = [x for x in normalized if x <= 3.0]
    
    # Use of zip and enumerate (required Python features)
    indexed_high = list(enumerate(high_perf))
    paired_data = list(zip(high_perf, reversed(low_perf)))

    total_impact = 0
    for idx, val in indexed_high:
        if idx % 2 == 0:
            total_impact += val * 1.5
        else:
            total_impact += val * 0.8

    # Additional distractor: dead code path due to fixed condition
    debug_mode = False
    if debug_mode:
        print("Debug info:", len(paired_data))

    # Set operations (required feature): find overlap between rounded sets
    set_a = {round(x) for x in high_perf}
    set_b = {round(y) for y in low_perf}
    common_levels = set_a & set_b  # intersection

    # Final score influenced by multiple factors
    base_score = sum(high_perf)
    penalty = len(common_levels) * 2.5
    bonus = len(indexed_high) * 1.2
    
    # Irrelevant string processing (distractor)
    status_log = "System operational"
    log_upper = status_log.upper()
    log_length = len(log_upper.replace(" ", ""))

    final_score = base_score + bonus - penalty
    
    # This variable is printed at the end
    return final_score

# Main execution
benchmark_data = [16, 25, 9, 4, 36, 8, 7, 12, 14, 2]
validate_inputs(benchmark_data)
calculate_performance(benchmark_data)
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")