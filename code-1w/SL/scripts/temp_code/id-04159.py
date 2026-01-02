def main():
    # Simulating a data processing pipeline with intermediate transformations
    raw_data = [3, 7, 12, 18, 25]
    processed = list(map(lambda x: (x ** 2) % 17, raw_data))

    # Irrelevant transformation chain (distractor)
    temp_analysis = [x for x in processed if x > 5]
    avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    normalized = [round(x / avg_temp, 3) for x in temp_analysis]  # Not used later

    # Core logic: filter and aggregate based on modular condition
    filtered = [x for x in processed if x % 3 == 2]
    base_accum = 0
    for val in filtered:
        base_accum += val * 2 if val < 10 else val + 3

    # Secondary path: statistical outlier detection (unused branch)
    mean_val = sum(processed) / len(processed)
    variance = sum((x - mean_val) ** 2 for x in processed) / len(processed)
    std_dev = variance ** 0.5
    outliers = [x for x in processed if abs(x - mean_val) > 1.5 * std_dev]  # Dead code

    # State tracking with dictionary-based counters (partial use)
    status_log = {}
    status_log['processed_count'] = len(processed)
    status_log['filtered_count'] = len(filtered)
    status_log['base_sum'] = base_accum

    # Conditional adjustment based on count parity
    if len(filtered) % 2 == 0:
        adjustment = 5
    else:
        adjustment = -3

    # Final computation through helper function
    def calculate_final(value):
        # Nested lambda for coefficient calculation
        coef_gen = lambda v: 2 if v > 20 else (1.5 if v > 10 else 1)
        scaling_factor = coef_gen(value)
        return int(value * scaling_factor) + adjustment

    pipeline_output = base_accum + status_log['filtered_count']

    # Key statement
    final_score = calculate_final(pipeline_output)

    # Extraneous logging (irrelevant)
    debug_info = {
        'raw_hash': sum(x * (i+1) for i, x in enumerate(raw_data)),
        'timestamp': 1698745230,
        'version': '2.1.0'
    }
    metadata_trace = [debug_info['raw_hash'], debug_info['version']]

    print(f"Result: {final_score}")

main()