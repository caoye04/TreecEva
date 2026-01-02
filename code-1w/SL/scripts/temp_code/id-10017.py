from collections import defaultdict

# Simulate hourly resource usage across multiple servers
def analyze_resource_utilization():
    hourly_data = [
        ('server_a', [('00:00', 45), ('01:00', 52), ('02:00', 61), ('03:00', 58)]),
        ('server_b', [('00:00', 39), ('01:00', 48), ('02:00', 63), ('03:00', 71)]),
        ('server_c', [('00:00', 55), ('01:00', 65), ('02:00', 65), ('03:00', 60)]),
        ('server_d', [('00:00', 40), ('01:00', 50), ('02:00', 55), ('03:00', 65)])
    ]

    # Track cumulative usage per hour across all servers
    usage_tracker = defaultdict(int)
    peak_log = []
    temp_aggregator = []

    for server_name, records in hourly_data:
        server_total = 0
        max_hourly = 0
        for timestamp, usage in records:
            hour = timestamp.split(':')[0]
            usage_tracker[hour] += usage
            server_total += usage
            if usage > max_hourly:
                max_hourly = usage

        # Irrelevant aggregation (distractor)
        temp_aggregator.append((server_name, server_total, max_hourly))

    # Compute average utilization per hour (semi-relevant but not used in final answer)
    avg_per_hour = {h: round(total / 4, 2) for h, total in usage_tracker.items()}

    # Identify peak capacity across all hours
    peak_capacity = max(usage_tracker.values())

    # Redundant filtering step (dead code path - distractor)
    filtered_peaks = [v for v in usage_tracker.values() if v > 200]
    if filtered_peaks:
        peak_log.append(max(filtered_peaks))

    # Misleading secondary calculation
    weighted_sum = sum(usage_tracker[h] * (int(h) + 1) for h in usage_tracker)
    scaling_factor = len(hourly_data) / 4.0
    adjusted_peak = weighted_sum * scaling_factor / 100

    # Final result output
    print(f"Result: {peak_capacity}")

    return peak_capacity

# Execute function
analyze_resource_utilization()