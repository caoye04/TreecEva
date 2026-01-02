def measure_efficiency(threshold, data_stream):
    accumulator = 0
    temp_offset = 0.0
    scaling_factor = 1.0
    
    # Irrelevant pre-processing (distractor)
    baseline_correction = sum([x ** 0.5 for x in data_stream if x > 4])
    normalization_constant = len(data_stream) + 1
    dummy_result = [scaling_factor * (x - temp_offset) for x in data_stream]

    # Core logic with lambda-based filtering
    filter_func = lambda val: val > threshold and val % 2 == 1
    filtered_data = list(filter(filter_func, data_stream))

    # Secondary processing with red herring computation
    outlier_buffer = []
    running_total = 0
    for i, val in enumerate(filtered_data):
        if i % 2 == 0:
            running_total += val * 1.5
        else:
            # This block runs but doesn't impact final result
            outlier_buffer.append(val ** 2 - 10)

    # Critical accumulation step
    for val in filtered_data:
        accumulator += (val // 3) * 2

    # Unused branching (dead code path)
    if len(outlier_buffer) > 100:
        accumulator -= 500  # Never reached due to input size

    return int(accumulator)

# Initialization sequence
phase_array = [3, 7, 8, 9, 12, 15, 18, 21, 22, 25, 27]
logic_threshold = 6
auxiliary_weight = 4.3
reference_map = {i: i*2 for i in range(5)}

# Dummy computations to increase cognitive load
shadow_copy = phase_array[:]
shadow_copy = [x + 1 for x in shadow_copy if x < 20]
evaluation_score = sum(shadow_copy) / len(shadow_copy) if shadow_copy else 0

# Key statement
thermal_capacity = measure_efficiency(logic_threshold, phase_array)

# Final output
print(f"Result: {thermal_capacity}")