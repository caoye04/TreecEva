def analyze_flow():
    # Simulate sensor readings from a fluid dynamics system
    raw_readings = [102, 115, 98, 203, 155, 88, 190, 178, 95, 210]
    
    # Filter valid inflow and outflow based on thresholds
    inflows = [x for x in raw_readings if 100 <= x <= 200]
    outflows = [x for x in raw_readings if x > 150]

    # Misleading intermediate processing: irrelevant transformation
    processed_readings = list(map(lambda x: (x * 1.05) + 7.3, raw_readings))
    avg_processed = sum(processed_readings) / len(processed_readings)
    deviation_score = sum(abs(x - avg_processed) for x in processed_readings) / avg_processed

    # Red herring: counting occurrences above arbitrary threshold
    high_count = 0
    for idx, val in enumerate(raw_readings):
        if val > 190:
            high_count += 1

    # Distractor: unused nested loop simulating multi-sensor correlation
    correlations = []
    for i in range(2):  # Only first two sensors considered
        row = []
        for j in range(len(raw_readings)):
            row.append((raw_readings[i] * raw_readings[j]) % 50)
        correlations.append(row)

    # Actual critical computation
    temp_buffer = [x for x in inflows if x not in outflows]  # unique inflows
    backup_capacity = len(temp_buffer) * 15

    net_flow = sum(inflows) - sum(outflows)

    # Unrelated health metric (dead code path)
    system_health = 'Stable' if deviation_score < 1.0 else 'Unstable'

    # Print final result as required
    print(f"Result: {net_flow}")

analyze_flow()