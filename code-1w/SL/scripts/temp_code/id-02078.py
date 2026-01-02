def analyze_system_performance(input_sequence):
    base_rating = 0
    efficiency_factor = 1.0
    transient_load = 0
    cumulative_shift = 0
    debug_flag = False

    for index, value in enumerate(input_sequence):
        if index % 2 == 0:
            base_rating += value ** 2
        else:
            base_rating -= value

        # Simulate auxiliary monitoring (distractor logic)
        temp_monitor = (value + index) % 7
        if temp_monitor > 5:
            debug_flag = True
            transient_load += temp_monitor

    # Secondary loop with zip – processes paired elements (real contribution)
    offset_sequence = [x // 2 for x in input_sequence[1:]]
    for raw_val, adj in zip(input_sequence, offset_sequence):
        if raw_val > adj:
            efficiency_factor *= 1.05
        else:
            efficiency_factor *= 0.98

    # Dead code path – never alters final result
    if len(input_sequence) > 100:
        cumulative_shift = sum(offset_sequence) >> 2

    # Key assignment point
    thermal_capacity = base_rating * efficiency_factor

    # Extraneous transformation (no effect on answer)
    if debug_flag:
        thermal_capacity = round(thermal_capacity, 2) + transient_load

    return thermal_capacity

# Main execution
data_stream = [3, 7, 2, 8, 1, 9, 4]
result = analyze_system_performance(data_stream)
print(f"Result: {result}")