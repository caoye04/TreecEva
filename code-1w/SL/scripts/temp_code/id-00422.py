def process_data(data, cfg):
    # Lambda for scaling sensor values
    scale = lambda x: x * cfg['multiplier'] if x > 0 else x * 0.5

    # Dictionary to track state transitions
    state_map = {'idle': 0, 'active': 1, 'paused': 2, 'error': -1}
    transition_count = 0
    scaled_values = []

    temp_accumulator = 0  # Irrelevant accumulator (distractor)
    debug_flag = False    # Unused flag (distractor)

    for entry in data:
        raw_value = entry.get('value', 0)
        status = entry.get('status', 'idle')

        # State transition logic
        if status in state_map and state_map[status] > 0:
            transition_count += 1

        # Scale only valid readings
        if raw_value != -999:  # -999 indicates faulty reading
            adjusted = scale(raw_value)
            scaled_values.append(adjusted)

        # Dead code path (misleading)
        if raw_value < 0 and status == 'error':
            temp_accumulator += abs(raw_value)
            break  # This never triggers due to data design

    # Secondary processing: filter and aggregate
    filtered = [v for v in scaled_values if v > 10]

    # Counting valid high-magnitude events
    event_counter = 0
    magnitude_sum = 0
    for val in filtered:
        if val > 20:
            event_counter += 1
        magnitude_sum += val

    # Final computation with distractor variables not affecting outcome
    baseline = len(data) * 0.75
    adjustment_factor = 1 + (transition_count * 0.05)
    final_output = int((magnitude_sum / (event_counter or 1)) * adjustment_factor) if event_counter > 0 else 0

    return final_output

# Simulated sensor stream
data_stream = [
    {'value': 15, 'status': 'active'},
    {'value': -999, 'status': 'idle'},      # Invalid reading
    {'value': 25, 'status': 'active'},
    {'value': 8, 'status': 'active'},       # Below filter threshold
    {'value': 30, 'status': 'paused'},     # Still valid data even if paused
    {'value': 22, 'status': 'active'}
]

config = {
    'multiplier': 1.2,
    'threshold': 10
}

final_output = process_data(data_stream, config)
print(f"Result: {final_output}")