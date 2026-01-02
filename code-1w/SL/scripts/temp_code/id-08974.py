def analyze_traffic_data():
    # Simulated network traffic data (in MB)
    morning_data = [125, 203, 98, 144, 301, 89, 167]
    evening_data = [210, 95, 134, 88, 199, 112, 177]

    # Extra processing - irrelevant to final result
    avg_morning = sum(morning_data) / len(morning_data)
    peak_evening = max(evening_data)
    growth_projection = [int(x * 1.08) for x in evening_data]  # projected next day

    # Categorize flows
    high_volume_threshold = 150
    inflow_candidates = set(morning_data)
    outflow_candidates = set(evening_data)

    # Misleading filtering (only some values used later)
    significant_inflows = {x for x in inflow_candidates if x > high_volume_threshold}
    significant_outflows = {x for x in outflow_candidates if x >= high_volume_threshold}

    # Distractor: string-based tagging (not used in calculation)
    tag_map = {}
    for val in morning_data + evening_data:
        tag = "high" if val >= high_volume_threshold else "low"
        label = f"{tag}_vol_{val % 10}"
        tag_map[val] = label

    # Slicing operation to extract core analysis window (middle 5)
    trimmed_morning = morning_data[1:-1]  # Remove first and last
    trimmed_evening = evening_data[1:-1]

    # Secondary distractor: unused recursive helper
    def count_above_recursive(arr, threshold, idx=0):
        if idx == len(arr):
            return 0
        return (1 if arr[idx] > threshold else 0) + count_above_recursive(arr, threshold, idx + 1)

    # Actual relevant logic begins here
    inflow_filtered = [x for x in trimmed_morning if x in significant_inflows]
    outflow_filtered = [x for x in trimmed_evening if x in significant_outflows]

    # Summation with distractions
    dummy_shift = 3
    inflow_sum = sum(inflow_filtered) << dummy_shift >> dummy_shift  # No-op bit shift
    outflow_sum = sum(outflow_filtered)

    # Key assignment point
    net_flow = inflow_sum - outflow_sum

    # Red herring: unused dictionary aggregation
    stats_bundle = {
        'inflow_count': len(inflow_filtered),
        'outflow_count': len(outflow_filtered),
        'balance_check': net_flow > 0,
        'phantom_metric': len(tag_map.keys()) ** 2
    }

    # Final output
    print(f"Result: {net_flow}")

analyze_traffic_data()