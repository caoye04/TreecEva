def analyze_system_load():
    # Simulated sensor data: timestamps and load values (in MW)
    timestamps = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    load_data = [23.5, 24.1, 25.3, 24.9, 26.7, 27.2, 26.8, 28.1, 27.5, 26.3]

    # Redundant temperature readings (not used in final calculation)
    temp_readings = [22.1, 22.5, 23.0, 22.8, 23.2, 24.0, 23.9, 24.1, 23.7, 23.3]
    avg_temp = sum(temp_readings) / len(temp_readings)
    temp_variance = sum((t - avg_temp) ** 2 for t in temp_readings) / len(temp_readings)

    # Misleading preprocessing: smoothing load data (unused path)
    smoothed_loads = []
    for i in range(len(load_data)):
        if i == 0 or i == len(load_data) - 1:
            smoothed_loads.append(load_data[i])
        else:
            smoothed_loads.append((load_data[i-1] + load_data[i] + load_data[i+1]) / 3)

    # Core analysis: group loads by even/odd indices (arbitrary segmentation)
    even_index_loads = []
    odd_index_loads = []
    for idx, load in enumerate(load_data):
        if idx % 2 == 0:
            even_index_loads.append(load)
        else:
            odd_index_loads.append(load)

    # Compute rolling 3-period aggregate loads (primary metric)
    aggregate_loads = []
    for i in range(2, len(load_data)):
        window_sum = load_data[i-2] + load_data[i-1] + load_data[i]
        aggregate_loads.append(round(window_sum, 2))

    # Secondary computation: unused trend analysis
    trends = []
    for i in range(1, len(load_data)):
        change = load_data[i] - load_data[i-1]
        trends.append('up' if change > 0 else 'down')

    # State tracking: peak detection in trend (distractor)
    up_streak = 0
    max_up_streak = 0
    for direction in trends:
        if direction == 'up':
            up_streak += 1
            max_up_streak = max(max_up_streak, up_streak)
        else:
            up_streak = 0

    # Key assignment: find maximum 3-period aggregate load
    peak_capacity = max(aggregate_loads)

    # Extraneous set operation: finding overlap between index sets (irrelevant)
    even_indices = {i for i, _ in enumerate(even_index_loads)}
    shifted_indices = {i+1 for i, _ in enumerate(odd_index_loads)}
    common_positions = even_indices & shifted_indices  # Unused

    # Zip-based pairing for logging (not affecting result)
    timestamp_load_pairs = list(zip(timestamps[1:-1], aggregate_loads))

    return peak_capacity

result = analyze_system_load()
print(f"Result: {result}")