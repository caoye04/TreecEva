def analyze_water_flow():
    # Simulate sensor readings from irrigation zones
    zone_readings = [
        [12, 15, 14, 0, 13],
        [8, 0, 10, 11, 9],
        [20, 18, 0, 19, 21],
        [5, 7, 6, 0, 0]
    ]

    # Historical averages (irrelevant for final calculation)
    historical_avg = [14.0, 9.6, 19.8, 5.6]
    deviation_scores = []

    inflow_sum = 0
    outflow_sum = 0
    temp_buffer = []

    # Process each zone
    for i, readings in enumerate(zone_readings):
        daily_total = sum(readings)
        zero_count = readings.count(0)
        
        # Irrelevant deviation tracking
        avg = daily_total / len(readings) if readings else 0
        dev = abs(avg - historical_avg[i]) if i < len(historical_avg) else 0
        deviation_scores.append(round(dev, 2))

        # Only even-indexed zones contribute to inflow
        if i % 2 == 0:
            inflow_sum += daily_total
            # Buffering intermediate values (some never used)
            temp_buffer.append(daily_total * 0.95)
        else:
            # Odd-indexed zones are outflows
            corrected_total = daily_total - (zero_count * 2)
            outflow_sum += max(corrected_total, 0)

    # Additional irrelevant computation: simulate data validation
    validation_pass = True
    for idx, row in enumerate(zone_readings):
        for jdx, val in enumerate(row):
            if val < 0:
                validation_pass = False
    checksum = sum(len(row) for row in zone_readings)  # Unused

    # Key computational step: net flow calculation
    net_flow = inflow_sum - outflow_sum

    # Red herring: adjust based on buffer (but not actually applied)
    if temp_buffer and sum(temp_buffer) > 100:
        scaling_factor = 0.9
        # This branch does nothing to net_flow

    # Final result output
    print(f"Result: {net_flow}")

analyze_water_flow()