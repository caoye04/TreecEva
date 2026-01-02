def analyze_system_performance():
    # Sensor data from 5 monitoring stations over 3 time intervals
    raw_data = [
        [12.4, 18.9, 15.2],
        [14.1, 19.5, 16.8],
        [13.7, 17.3, 14.9],
        [15.6, 20.1, 18.4],
        [11.8, 16.7, 13.5]
    ]

    # Configuration thresholds (partially irrelevant)
    thresholds = {'min_val': 10.0, 'max_val': 25.0, 'tolerance': 1.5}
    temp_buffer = []
    cumulative_sum = 0.0

    # Extract middle column readings (index 1) for efficiency analysis
    mid_readings = []
    for i, station in enumerate(raw_data):
        mid_readings.append(station[1])
        cumulative_sum += sum(station)  # Distractor: used later in irrelevant calc

    # Normalize readings against average
    avg_reading = sum(mid_readings) / len(mid_readings)
    normalized = [x / avg_reading for x in mid_readings]

    # Compute efficiency scores using non-linear transformation
    efficiencies = []
    for val in normalized:
        if val >= 1.0:
            efficiency = 100 * (1 + 0.5 * (val - 1)) ** 2
        else:
            efficiency = 100 * (1 - 0.3 * (1 - val))
        efficiencies.append(round(efficiency, 3))

    # Irrelevant secondary processing: buffer simulation
    for reading_list in raw_data:
        temp_buffer.extend(reading_list[:2])
    temp_buffer.sort(reverse=True)
    spike_count = 0
    for i in range(1, len(temp_buffer)):
        if temp_buffer[i] > temp_buffer[i-1]:
            spike_count += 1  # Dead logic path – never executes due to sorting

    # Key computation point
    peak_efficiency = max(efficiencies)

    # Final reporting
    baseline = thresholds['min_val']
    adjustment_factor = cumulative_sum / 100  # Unused downstream

    print(f"Result: {peak_efficiency}")

analyze_system_performance()