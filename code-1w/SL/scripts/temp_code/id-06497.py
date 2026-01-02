def analyze_workload():
    # Simulate a server workload analysis over time slots
    base_load = 45
    time_slots = [i for i in range(1, 13)]
    temperature_factor = 1.05
    maintenance_mode = False

    # Initialize various metrics (some are distractions)
    downtime_losses = []
    peak_history = []
    adjustment_log = {}

    raw_readings = [base_load + t * 2 - (t % 3) * 3 for t in time_slots]
    filtered_readings = [r for r in raw_readings if r > 40]  # Remove low anomalies

    # Apply conditional scaling based on simulated temperature
    scaled_readings = [r * temperature_factor if r > 60 else r for r in filtered_readings]

    # Simulate fluctuating capacity limits
    capacity_limits = [70 + 5 * (i % 4) for i in range(len(scaled_readings))]

    # Compute usage levels with safety clamping
    usage_levels = []
    for i, load in enumerate(scaled_readings):
        cap = capacity_limits[i]
        usage = load / cap * 100
        usage_levels.append(round(usage, 2))

        # Logging irrelevant intermediate state
        if usage > 90:
            adjustment_log[len(usage_levels)] = "High stress"
        elif usage < 60:
            downtime_losses.append(i)

    # Track historical peaks (distraction)
    peak_history.extend([max(usage_levels[:len(usage_levels)//2]), max(usage_levels[len(usage_levels)//2:])])

    # Key statement: determine peak capacity utilization
    peak_capacity = max(usage_levels)

    # Extra unused computations to increase interference
    avg_peak_history = sum(peak_history) / len(peak_history) if peak_history else 0
    projected_risk = avg_peak_history > 95

    # Final output
    print(f"Result: {peak_capacity}")

analyze_workload()