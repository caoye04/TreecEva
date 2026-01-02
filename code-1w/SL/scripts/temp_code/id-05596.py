def calculate_thermal_output(sequence):
    base_factor = 1.5
    adjustment = 0.85
    temp_result = 0
    cumulative_shift = 0

    for i, val in enumerate(sequence):
        if i % 2 == 0:
            temp_result += val * base_factor
        else:
            temp_result -= val * adjustment

        # Misleading intermediate calculation (dead-end)
        phantom_score = (val ** 2) / (i + 1) if i > 0 else 0
        noise_buffer = [phantom_score * k for k in range(3)]  # Irrelevant list comprehension

        # Nested logic with distractor state
        if temp_result > 100:
            cumulative_shift += 1
            temp_result *= 0.95

    # Additional red herring: unused helper computation
    final_magnitude = sum([x * x for x in sequence]) // len(sequence) if sequence else 0

    # Core result unaffected by above distractions
    return int(temp_result) + 10

# Simulation parameters
efficiency_log = [12, 18, 25, 30, 22]
scaling_constant = 7.0
offset_tracker = {"init": 0, "peak": None, "final": None}

# Unused but plausible-looking preprocessing
processed_data = [x + scaling_constant for x in efficiency_log]
filtered_results = [x for x in processed_data if x > 20]

# Key statement
thermal_capacity = calculate_thermal_output(efficiency_log)

Result: {thermal_capacity}