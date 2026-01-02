def analyze_system_logs():
    # Simulated system log entry: (timestamp, cpu_load, memory_usage, disk_io)
    log_entries = [
        (100, 0.45, 0.60, 120),
        (101, 0.50, 0.62, 135),
        (102, 0.75, 0.70, 150),
        (103, 0.80, 0.85, 140),
        (104, 0.60, 0.55, 110),
        (105, 0.30, 0.40, 95),
        (106, 0.35, 0.42, 100),
        (107, 0.90, 0.95, 160)
    ]

    # Irrelevant statistical placeholder
    avg_temporal_gap = sum(log_entries[i+1][0] - log_entries[i][0] for i in range(len(log_entries)-1)) / (len(log_entries)-1)

    # Filter high-load entries
    high_load_threshold = 0.7
    high_load_entries = [entry for entry in log_entries if entry[1] > high_load_threshold]

    # Compute rolling memory average over windows of size 2 (semi-relevant)
    rolling_memory_avg = []
    for i in range(len(log_entries) - 1):
        avg_mem = (log_entries[i][2] + log_entries[i+1][2]) / 2
        rolling_memory_avg.append(avg_mem)

    # Disk I/O outlier detection using lambda (used later)
    is_outlier = lambda x, threshold: x > threshold
    io_threshold = 130
    outliers_detected = [entry for entry in log_entries if is_outlier(entry[3], io_threshold)]

    # Helper function to compute load severity
    def compute_severity(cpu, mem):
        return (cpu ** 1.5) + (mem ** 1.2)

    # Calculate cumulative severity for high-load periods
    total_severity = 0
    for entry in high_load_entries:
        total_severity += compute_severity(entry[1], entry[2])

    # Efficiency score based on ratio of severe events to total logs
    efficiency_score = len(high_load_entries) / len(log_entries)

    # Distractor: unused data transformation
    transformed_data = list(map(lambda x: (x[0], round(x[1]*100)), log_entries))

    # Unused conditional branch with misleading comment
    if len(outliers_detected) > 3:
        # This path is not taken, but adds cognitive load
        efficiency_score *= 0.8
    else:
        efficiency_score += 0.05  # Minor adjustment

    # Final performance calculation
    def calculate_performance(logs):
        base_score = efficiency_score
        penalty = 0
        for log in logs:
            if log[1] > 0.8 and log[2] > 0.9:
                penalty += 0.02
        return base_score - penalty

    final_output = calculate_performance(log_entries)

    # Print target result
    print(f"Result: {efficiency_score}")

analyze_system_logs()