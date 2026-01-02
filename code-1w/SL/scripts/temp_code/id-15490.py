def calculate_water_flow():
    # Sensor readings (in liters per minute)
    sensor_readings = [120, 135, 128, 142, 130, 137, 125]

    # Historical baseline and thresholds
    baseline_avg = 130.5
    threshold = 132
    adjustment_factor = 0.95

    # Simulate calibration offset (distraction)
    calibration_log = []
    for i, reading in enumerate(sensor_readings):
        calibrated = reading * adjustment_factor
        calibration_log.append(calibrated)

    # Compute moving average over valid windows (semi-relevant computation)
    moving_averages = []
    for i in range(len(calibration_log) - 2):
        window_avg = sum(calibration_log[i:i+3]) / 3
        moving_averages.append(window_avg)

    # Identify high-flow periods
    high_flow_periods = [avg for avg in moving_averages if avg > threshold]

    # Primary flow analysis
    inflow_sources = [128, 140, 136, 132]
    outflow_sinks = [68, 72, 70]

    # Distractor: energy consumption estimation (irrelevant)
    energy_per_liter = 0.045
    total_energy = sum(inflow_sources) * energy_per_liter

    # Main computation
    inflow_sum = sum(inflow_sources)
    outflow_sum = sum(outflow_sinks)
    backup_flow = 50

    # Key decision point
    net_flow = inflow_sum - outflow_sum if inflow_sum > threshold else backup_flow

    # Additional logging (dead code path)
    status_flag = "NORMAL" if net_flow > 0 else "WARNING"
    if status_flag == "DEBUG":
        print("Debug mode active")

    print(f"Result: {net_flow}")

calculate_water_flow()