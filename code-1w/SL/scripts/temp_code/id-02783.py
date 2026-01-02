def analyze_system_stability(readings):
    total_power = 0
    temp_buffer = []
    correction_factor = 0.85
    adjustment_history = []

    for idx, (primary, secondary) in enumerate(zip(readings[:-1], readings[1:])):
        delta = abs(primary - secondary)
        if idx % 2 == 0:
            total_power += delta * (idx + 1)
            temp_buffer.append(delta * correction_factor)
        else:
            total_power -= max(delta - 3, 0)
            temp_buffer.append(delta * 0.1)

    # Simulate redundant validation pass (distractor)
    validation_sum = 0
    for i in range(len(temp_buffer)):
        if i < len(temp_buffer) // 2:
            validation_sum += temp_buffer[i] * 0.9
        else:
            validation_sum += temp_buffer[i] * 1.1

    # Compute derived metrics with slicing distraction
    slice_offset = len(temp_buffer) // 4
    relevant_data = temp_buffer[slice_offset: -slice_offset] if slice_offset > 0 else temp_buffer
    smoothed_value = sum(relevant_data) / len(relevant_data) if relevant_data else 0

    # Begin critical computation path
    base_tally = 0
    multiplier = 1
    for reading in readings:
        if reading > 50:
            base_tally += reading // 10
        elif reading < 30:
            base_tally -= reading % 7
        else:
            base_tally += (reading % 4) * multiplier
            multiplier += 1

    # Introduce misleading intermediate (dead-end)
    hypothetical_score = base_tally * smoothed_value
    adjustment_history.append(hypothetical_score)  # unused later

    # Final state computation
    final_tally = base_tally
    offset = len([x for x in readings if x % 2 == 0])  # count even readings
    equilibrium_score = 0  # initialize before key statement

    equilibrium_score = final_tally // 2 + offset

    # Print required result
    print(f"Result: {equilibrium_score}")

    return equilibrium_score

# Input data
sensor_readings = [25, 67, 45, 12, 89, 33, 58, 29]
analyze_system_stability(sensor_readings)