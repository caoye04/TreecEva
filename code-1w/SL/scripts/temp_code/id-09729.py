from collections import defaultdict, Counter

# Simulate time-series resource monitoring across zones
def monitor_resource_allocation():
    raw_logs = [
        'Z1_CPU_90_T1000', 'Z2_MEM_45_T1001', 'Z1_DISK_60_T1002',
        'Z3_CPU_85_T1003', 'Z2_CPU_92_T1004', 'Z3_MEM_30_T1005',
        'Z1_CPU_70_T1006', 'Z2_DISK_80_T1007', 'Z3_DISK_85_T1008',
        'Z1_MEM_50_T1009', 'Z2_CPU_95_T1010', 'Z3_CPU_93_T1011'
    ]

    # Track usage per zone and resource type
    usage_tracker = defaultdict(lambda: defaultdict(list))
    temp_aggregates = []
    spike_moments = []

    for log in raw_logs:
        parts = log.split('_')
        zone, resource, level_str, timestamp = parts[0], parts[1], parts[2], parts[3]
        level = int(level_str)
        
        # Store time-series data
        usage_tracker[zone][resource].append(level)
        
        # Capture high-usage events (red herring)
        if level > 90:
            spike_moments.append(timestamp)
        
        # Irrelevant aggregation (distractor)
        if resource == 'CPU':
            temp_aggregates.append(level * 1.1)  # fake adjusted values

    # Compute average usage per zone (semi-relevant but not used in answer)
    avg_usage_per_zone = {}
    for zone in usage_tracker:
        all_values = []
        for resource in usage_tracker[zone]:
            all_values.extend(usage_tracker[zone][resource])
        avg_usage_per_zone[zone] = sum(all_values) / len(all_values)

    # Character analysis of zone names (distractor)
    zone_chars = ''.join(usage_tracker.keys())
    char_freq = Counter(zone_chars)
    vowel_count = sum(1 for c in zone_chars if c in 'AEIOU')

    # Case transformation chain (irrelevant)
    upper_zones = [z.upper() for z in usage_tracker.keys()]
    flipped = ''.join([c.lower() if c == 'Z' else c for c in ''.join(upper_zones)])

    # Critical computation: total peak capacity across all resources
    cumulative_maxes = []
    for zone in usage_tracker:
        for resource in usage_tracker[zone]:
            if usage_tracker[zone][resource]:
                cumulative_maxes.append(max(usage_tracker[zone][resource]))
    
    # Secondary tracker with redundant logic (distractor)
    fallback_tracker = defaultdict(int)
    for zone in usage_tracker:
        fallback_tracker[zone] += sum(len(v) for v in usage_tracker[zone].values())

    # Key statement - what we're evaluating
    peak_capacity = max(usage_tracker.values()) if usage_tracker else 0
    
    # More red herrings: slicing and unused transformations
    recent_logs = raw_logs[-5:]
    sliced_peaks = [max(usage_tracker[z]['CPU']) for z in ['Z1', 'Z2', 'Z3'] if 'CPU' in usage_tracker[z]]
    derived_metric = sum(sliced_peaks) / len(sliced_peaks) if sliced_peaks else 0

    # Final distraction: recursive helper that isn't used
    def calculate_depth(data, depth=0):
        return depth if not data else calculate_depth(data[1:] if isinstance(data, list) else [], depth + 1)
    
    recursion_test = calculate_depth(temp_aggregates)

    print(f"Result: {max(cumulative_maxes)}")
    return max(cumulative_maxes)

result = monitor_resource_allocation()
