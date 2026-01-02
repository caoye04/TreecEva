def optimize_resources(matrix, threshold):
    # Initialize tracking variables
    total_resources = 0
    temp_sum = 0
    debug_log = []

    # Precompute scaling factor (semi-relevant)
    scaling_factor = sum(len(row) for row in matrix) / (len(matrix) + 1e-5)

    # Secondary helper to simulate overhead
    overhead_calculator = lambda x: (x ** 2 + 1) // (x + 1) if x > 0 else 0

    for row in matrix:
        row_valid_count = 0
        row_efficiency = 0.0

        for val in row:
            # Simulate sensor reading with noise filtering
            clean_val = val if val >= 0 else 0
            temp_sum += clean_val  # Distractor accumulator

            # Track valid resource units above zero
            if clean_val > 0:
                row_efficiency += clean_val
                row_valid_count += 1

        # Compute row-level metric (only some affect final result)
        if row_valid_count > 0:
            avg_efficiency = row_efficiency / row_valid_count
            if avg_efficiency >= threshold:
                total_resources += overhead_calculator(row_valid_count)

        # Debug entry that doesn't impact logic
        debug_log.append(f"Processed {row_valid_count} units")

    # Final adjustment based on global constraints
    adjustment = len(debug_log) % 5 if len(debug_log) > 3 else 0
    total_resources += adjustment

    return int(total_resources)

# Define system parameters
allocation_matrix = [
    [3, -1, 4, 0, 5],
    [2, 2, -3, 1],
    [0, 0, 0],
    [1, 1, 1, 1]
]
efficiency_threshold = 2.0

# Misleading pre-analysis (distractor)
baseline_estimate = sum(sum(1 for x in row if x > 1) for row in allocation_matrix)
shadow_buffer = [baseline_estimate * i for i in range(3)]  # Dead code path

# Key computation
final_capacity = optimize_resources(allocation_matrix, efficiency_threshold)

# Output result as required
print(f"Target result: {final_capacity}")