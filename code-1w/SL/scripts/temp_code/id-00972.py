def analyze_system_throughput(input_stream, threshold=50):
    # Irrelevant pre-processing block (dead computation)
    temp_buffer = [x ** 2 for x in input_stream if x < 30]
    temp_buffer = [x for x in temp_buffer if x % 7 != 0]  # Unused downstream

    # Core data: system node identifiers and performance metrics
    node_ids = set(range(100, 200, 3))
    active_nodes = set(range(105, 195, 5))
    stable_nodes = set(range(110, 180, 7))

    # Derived set operations with distractor usage
    overlapping_operational = node_ids & active_nodes | stable_nodes
    deprecated_nodes = node_ids - active_nodes
    critical_nodes = active_nodes & stable_nodes  # Only this is used later

    # Simulated sensor readings (distraction: complex generation, minimal use)
    sensor_readings = []
    for i in range(len(input_stream)):
        if i % 4 == 0:
            reading = (input_stream[i] + i) * 0.7 + 10
        elif i % 4 == 1:
            reading = (input_stream[i] - i) * 0.3
        else:
            reading = input_stream[i] / 2.5
        sensor_readings.append(reading)

    # Dead path: never accessed
    def calibrate_signal(x):
        return (x + 5) * 1.2 if x < 0 else (x - 3) * 0.8

    calibrated = [calibrate_signal(r) for r in sensor_readings if r > 100]  # Unused list

    # Actual signal filter logic (key path)
    filtered_readings = [r for r in sensor_readings if r > threshold]
    normalized = [int(r // 1.5) for r in filtered_readings]

    # Mapping to node space via modulo (red herring: appears significant)
    mapped_nodes = set()
    for val in normalized:
        mapped_nodes.add((val + 5) % 99 + 100)

    # Real logic: only values above threshold and even contribute
    qualified_elements = []
    for val in input_stream:
        if val > threshold and val % 2 == 0:
            # Additional condition tied to node presence
            node_tag = (val % 50) + 100
            if node_tag in critical_nodes:  # depends on set intersection
                qualified_elements.append(val)

    # Decoy transformation chain
    transformed = []
    for x in qualified_elements:
        step1 = x ^ 255  # Bitwise distraction
        step2 = step1 + 100
        step3 = step2 >> 2
        transformed.append(step3)  # Never used

    # Correction factor based on recursive depth calculation
    def compute_depth(n):
        if n <= 1:
            return 1
        return compute_depth(n // 3) + 2

    depth = compute_depth(len(qualified_elements))
    correction_factor = depth if depth > 0 else 1

    # KEY STATEMENT — target of evaluation
    filtration_score = len(qualified_elements) * correction_factor

    # Final output
    print(f"Result: {filtration_score}")

# Execute with deterministic input
data_stream = [45, 52, 60, 33, 70, 58, 44, 81, 92, 57, 63, 74, 88, 95, 67]
analyze_system_throughput(data_stream)