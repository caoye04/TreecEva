from collections import defaultdict

# Simulate a power grid load monitor over multiple regions and time slots
def calculate_peak_grid_load():
    # Historical data storage (not used in final result but adds cognitive load)
    historical_trends = defaultdict(list)
    maintenance_mode = False
    calibration_offset = 0.97

    # Grid configuration
    regions = ['north', 'south', 'east', 'west']
    base_capacity = {'north': 25, 'south': 30, 'east': 20, 'west': 35}
    peak_capacity = 0
    total_aggregate = 0  # Distractor: accumulates values not needed for answer

    # Simulated sensor readings over 4 time intervals
    sensor_data = [
        {'north': 22, 'south': 28, 'east': 18, 'west': 33},
        {'north': 26, 'south': 33, 'east': 19, 'west': 31},
        {'north': 24, 'south': 31, 'east': 21, 'west': 36},
        {'north': 27, 'south': 29, 'east': 20, 'west': 34}
    ]

    # Process each time interval
    for i, reading in enumerate(sensor_data):
        current_load = 0
        fluctuation_score = 0  # Irrelevant metric
        
        # Calculate combined load across regions
        for region in regions:
            raw_value = reading[region]
            adjusted_value = raw_value * calibration_offset  # Simulated correction
            current_load += int(adjusted_value)
            
            # Track trends (dead code path - never used later)
            if maintenance_mode:
                historical_trends[region].append(raw_value)
            
            # Extra computation that doesn't affect output
            if raw_value > base_capacity[region]:
                fluctuation_score += 1

        # Update peak only if current exceeds previous maximum
        if current_load > peak_capacity:
            peak_capacity = current_load

        # Accumulate total (distractor, not part of answer)
        total_aggregate += current_load

        # Early return simulation under rare condition (never triggered)
        if i == 10:
            return -1

    # Final adjustment unrelated to peak_capacity
    efficiency_ratio = total_aggregate / (len(sensor_data) * 100) if total_aggregate else 0

    # Output the target result
    print(f"Target result: {peak_capacity}")

    return peak_capacity

# Execute the function
calculate_peak_grid_load()