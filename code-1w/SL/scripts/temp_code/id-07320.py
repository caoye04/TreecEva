def analyze_network_load():
    # Simulated network segment bandwidth usage (in Mbps)
    raw_bandwidth_data = [45, 67, 23, 89, 54, 76, 38, 91, 65, 58]

    # Segment health indicators (arbitrary score)
    health_scores = [88, 76, 90, 65, 82, 74, 69, 85, 71, 67]

    # Irrelevant transformation: normalized scores (not used in final logic)
    normalized_health = [score / 100 for score in health_scores]

    # Identify active segments based on threshold
    threshold = 50
    active_mask = [bw > threshold for bw in raw_bandwidth_data]

    # Extract indices of active segments
    active_indices = []
    for i in range(len(active_mask)):
        if active_mask[i]:
            active_indices.append(i)

    # Slice first and last few active segments for analysis (partial use)
    trimmed_active = active_indices[1:-1] if len(active_indices) > 2 else active_indices

    # Misleading intermediate: average of high-usage segments (unused)
    high_usage_avg = sum([bw for bw in raw_bandwidth_data if bw > 70]) / 4

    # Distractor: secondary list with shifted values
    shifted_loads = [raw_bandwidth_data[i-1] for i in range(1, len(raw_bandwidth_data))]
    shifted_loads.append(0)  # padding

    # Core logic: map active segment indices to current usage levels
    usage_levels = {}
    for idx in active_indices:
        usage_levels[idx] = raw_bandwidth_data[idx]

    # Critical operation: determine peak capacity among active segments
    if active_indices:
        peak_capacity = max(usage_levels[seg] for seg in active_indices)
    else:
        peak_capacity = 0

    # Red herring: calculate utilization variance (not affecting result)
    mean_active = sum(usage_levels.values()) / len(usage_levels) if usage_levels else 0
    variance = sum((v - mean_active) ** 2 for v in usage_levels.values()) / len(usage_levels) if usage_levels else 0

    # Final output
    print(f"Result: {peak_capacity}")

analyze_network_load()