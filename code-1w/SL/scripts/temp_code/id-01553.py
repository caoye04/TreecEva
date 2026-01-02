def process_data(data_stream, criteria):
    temp_buffer = []
    accumulator = 0
    threshold = 42
    debug_flags = [False, True, False]
    
    # Irrelevant pre-processing (distractor)
    noise_filter = lambda x: (x + 1) * 0.5 if x % 2 else x // 2
    enhanced_stream = [noise_filter(val) for val in data_stream if val > 0]

    # Core logic with conditional filtering and accumulation
    for val in data_stream:
        if val == 0:
            continue
        meets_criteria = all(
            (val % factor == 0) != (val < threshold) 
            for factor in criteria
        )
        if meets_criteria:
            if val < threshold:
                accumulator += val ** 2
            else:
                accumulator -= val // 3

    # Secondary processing with red herring computation
    dummy_sum = sum(x * x for x in range(len(criteria)))
    correction_factor = len(enhanced_stream) - len(data_stream)
    adjusted_acc = accumulator + (correction_factor * 5)  # No real impact due to fixed lengths

    # Final transformation using lambda (required feature)
    transform = lambda x: x + 10 if x < 100 else x - 5
    final_output = transform(adjusted_acc)

    # Dead code path (misleading control flow)
    if debug_flags[2]:
        final_output *= 2

    return final_output

# Input setup
sensor_readings = [3, 6, 15, 45, 81, 0, 12]
filters = [3, 9]

result = process_data(sensor_readings, filters)
print(f"Target result: {result}")