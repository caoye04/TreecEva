def calculate_network_utilization():
    base_nodes = 8
    expansion_factor = 3
    peak_capacity = 0
    total_handled = 0
    temporal_buffer = 0

    for hour in range(1, 25):
        if hour % 6 == 0:
            base_nodes += 1

        # Simulate load fluctuation with diurnal pattern
        time_weight = (1 + 0.5 * (hour // 12))
        activity_spike = 1 if 7 <= hour <= 9 or 18 <= hour <= 20 else 0.6

        current_load = int(base_nodes * expansion_factor * time_weight * activity_spike)
        
        # Update total handled traffic (irrelevant to peak)
        total_handled += current_load

        # Buffer adjustment based on hour (distractor logic)
        if hour > 12:
            temporal_buffer += (current_load * 0.1)

        # Critical update point
        peak_capacity = max(peak_capacity, current_load)

        # Secondary capacity metric (misleading)
        fallback_capacity = base_nodes * 4

        # Red herring: unused conditional affecting no variables
        if current_load > 50 and fallback_capacity < 40:
            temporal_buffer -= 5

    Result: peak_capacity

# Execute function
calculate_network_utilization()