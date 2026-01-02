def calculate_system_response(input_sequence):
    base_offset = 17
    temporal_weight = 0.85
    aggregate_transfer = 0
    phase_correction = 0
    transient_buffer = []
    auxiliary_sum = 0  # Distractor: used in dead code path

    # Dead code block (simulates unused diagnostic routine)
    if False:
        for k in range(len(input_sequence)):
            auxiliary_sum += input_sequence[k] * (k + 1)
        transient_buffer.append(auxiliary_sum)

    # Main processing with enumerate and conditional expressions
    for idx, value in enumerate(input_sequence):
        scaled_value = value * (temporal_weight ** idx)
        if idx % 2 == 0:
            adjusted = scaled_value + base_offset
        else:
            adjusted = scaled_value - (base_offset * 0.1)
        aggregate_transfer += int(adjusted)

    # Secondary correction using zip and lambda
    indices = list(range(len(input_sequence)))
    paired_data = zip(indices, input_sequence)
    transform_op = lambda x, y: (x ^ y) + 1 if (x + y) % 3 == 0 else 0  # Bitwise and condition

    correction_components = [
        transform_op(i, val) for i, val in paired_data
        if val > 0
    ]

    phase_correction = sum(correction_components) * 2

    # Spurious computation (distractor)
    temp_result = [val ** 0.5 for val in input_sequence if val > 10]
    mean_sqrt = sum(temp_result) / len(temp_result) if temp_result else 0

    # Key statement
    final_flux = aggregate_transfer + phase_correction
    
    # Output result as required
    print(f"Result: {final_flux}")
    return final_flux

# Input data
data_stream = [12, -5, 8, 14, 3]
calculate_system_response(data_stream)