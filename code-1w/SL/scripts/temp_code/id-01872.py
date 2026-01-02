def analyze_workload_efficiency():
    # Simulated hourly resource usage (in percentage) over a day
    raw_usage_data = [23, 45, 67, 89, 12, 34, 56, 78, 90, 23, 45, 67, 89, 12]

    # Filter out invalid entries (e.g., negative or above 100)
    sanitized_usage = [x for x in raw_usage_data if 0 <= x <= 100]

    # Apply smoothing: average with neighbors for noise reduction (except edges)
    smoothed_usage = []
    for i in range(len(sanitized_usage)):
        if i == 0 or i == len(sanitized_usage) - 1:
            smoothed_usage.append(sanitized_usage[i])
        else:
            avg_val = (sanitized_usage[i-1] + sanitized_usage[i] + sanitized_usage[i+1]) / 3
            smoothed_usage.append(round(avg_val))

    # Misleading transformation: invert values (not used in final logic)
    inverted_usage = [100 - x for x in smoothed_usage]
    total_inverted = sum(inverted_usage)  # Distractor variable

    # Extract trends at odd hours only (simulating peak-hour analysis)
    usage_trends = []
    for idx, val in enumerate(smoothed_usage):
        if idx % 2 == 1:  # Odd-indexed hours (1, 3, 5, ...)
            adjusted_val = val * 1.1  # Simulate scaling due to load type
            usage_trends.append(int(adjusted_val))

    # Secondary distractor: even-hour stats
    even_hour_avg = sum(smoothed_usage[i] for i in range(0, len(smoothed_usage), 2)) / len(smoothed_usage[::2])
    fluctuation_index = max(smoothed_usage) - min(smoothed_usage)  # Unused metric

    # Key computation: find maximum among odd-indexed trend values
    peak_capacity = max(usage_trends[i] for i in range(len(usage_trends)) if i % 2 == 1)

    # Additional red herring: cumulative projection
    projected_weekly = peak_capacity * 7
    growth_factor = 1.05

    # Final output
    print(f"Result: {peak_capacity}")

analyze_workload_efficiency()