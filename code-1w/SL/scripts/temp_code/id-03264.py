def analyze_data_flow():
    # Simulate sensor data batches over time
    batch_1 = [12, 15, 23, 45, 38]
    batch_2 = [9, 14, 28, 31, 40, 50]
    batch_3 = [11, 22, 33, 44]

    # Combine all batches into a single timeline
    full_timeline = batch_1 + batch_2 + batch_3

    # Extract even-indexed measurements as calibration samples (irrelevant to final result)
    calibration_samples = full_timeline[::2]
    avg_calibration = sum(calibration_samples) / len(calibration_samples) if calibration_samples else 0

    # Identify active periods where values exceed threshold
    active_periods = [x for x in full_timeline if x > 30]

    # Split data into incoming and outgoing flows based on parity
    incoming = [x for x in active_periods if x % 3 == 0]
    outgoing = {x for x in active_periods if x % 4 == 0}  # Use set to remove duplicates

    # Misleading transformation: scale outgoing by 0.5 (not used in final logic)
    scaled_outgoing = [val * 0.5 for val in outgoing]

    # Unrelated statistical check (dead code path)
    if len(scaled_outgoing) > 5:
        outlier_count = len([v for v in scaled_outgoing if v < 10])
    else:
        temp_buffer = [0] * 5  # Allocated but unused

    # Core calculation: net flow is difference between total incoming and outgoing
    net_flow = sum(incoming) - sum(outgoing)

    # Additional irrelevant aggregation
    peak_ratio = max(incoming) / min(incoming) if incoming else 0

    # Final output
    print(f"Result: {net_flow}")

analyze_data_flow()