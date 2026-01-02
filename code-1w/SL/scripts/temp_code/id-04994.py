def analyze_workload_efficiency(timestamps, loads, thresholds):
    # Simulate monitoring system that tracks resource utilization over time
    cumulative_load = 0
    load_moments = []
    adjusted_timestamps = [t % 86400 for t in timestamps]  # Normalize to daily cycle

    # Irrelevant preprocessing: sort loads by threshold proximity (not used later)
    sorted_by_threshold_proximity = sorted(loads, key=lambda x: min(abs(x - th) for th in thresholds))
    dummy_aggregation = sum(sorted_by_threshold_proximity[:len(thresholds)])

    # Core logic: compute rolling weighted usage
    weighted_usage = []
    for i, (ts, load) in enumerate(zip(adjusted_timestamps, loads)):
        if load > thresholds[0]:
            weight = 1.5 if ts < 43200 else 1.2  # Higher weight for early high-load periods
        else:
            weight = 0.8
        weighted_usage.append(load * weight)
        
        # Track moments of inertia in system (unused)
        moment = load * (ts ** 2)
        load_moments.append(moment)

    # Secondary analysis: detect stable periods (distractor)
    stability_score = 0
    for i in range(1, len(weighted_usage)):
        if abs(weighted_usage[i] - weighted_usage[i-1]) < 5:
            stability_score += 1

    # Destructuring assignment: extract first and last high-impact windows
    first_high, *middle_loads, last_high = [w for w in weighted_usage if w > 75]

    # Calculate usage trends with slicing
    trend_window = weighted_usage[::3]  # Every third measurement for trend analysis
    usage_trends = [sum(trend_window[i:i+2]) for i in range(0, len(trend_window), 2)]

    # Add padding to trends for alignment (some values are irrelevant)
    while len(usage_trends) < 10:
        usage_trends.append(usage_trends[-1] * 0.9)

    # Key statement: determine peak capacity from usage trends
    peak_capacity = max(usage_trends)

    # Final red herring computation: normalized entropy (unused)
    total = sum(usage_trends)
    entropy = sum(-(x/total)*((x/total)**0.5) for x in usage_trends if x > 0)

    # Output the required result
    print(f"Result: {peak_capacity}")

# Input data
timestamps = [3600, 7200, 10800, 14400, 18000, 21600, 25200, 28800, 32400, 36000]
loads = [50, 80, 90, 60, 95, 100, 70, 85, 75, 90]
thresholds = [75, 85, 95]

analyze_workload_efficiency(timestamps, loads, thresholds)