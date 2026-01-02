from collections import defaultdict, Counter

# Simulate time-series resource monitoring across zones
def monitor_resource_allocation():
    timestamps = [100, 105, 110, 115, 120, 125, 130]
    raw_data = [
        ('zone-alpha', 23), ('zone-beta', 45), ('zone-gamma', 31),
        ('zone-alpha', 19), ('zone-beta', 52), ('zone-delta', 18),
        ('zone-gamma', 41), ('zone-alpha', 27), ('zone-beta', 55),
        ('zone-gamma', 39), ('zone-delta', 23), ('zone-alpha', 33)
    ]

    # Track cumulative usage per zone
    usage_tracker = defaultdict(int)
    
    # Auxiliary tracking structures (some used, some not)
    event_counter = Counter()
    peak_moments = []
    temp_aggregates = []
    total_events = 0
    running_avg_buffer = []

    # Misleading initialization
    baseline_offset = 17
    scaling_factor = 1.05
    debug_flags = [False, True, False]

    for i, ts in enumerate(timestamps):
        chunk = raw_data[i*2 : i*2 + 2] if i < 6 else []
        
        # Process each record in current time window
        for zone, load in chunk:
            usage_tracker[zone] += load
            event_counter[zone] += 1
            total_events += 1
            
            # Irrelevant intermediate calculation
            adjusted_load = (load * scaling_factor) - baseline_offset
            running_avg_buffer.append(adjusted_load)
            
            if load > 40 and zone not in peak_moments:
                peak_moments.append(zone)

        # Dead code path - never reached due to loop bounds
        if i == 10:
            fallback_zone = 'zone-omega'
            usage_tracker[fallback_zone] = 999

        # Semi-relevant aggregation
        if len(running_avg_buffer) > 0:
            temp_aggregates.append(sum(running_avg_buffer) / len(running_avg_buffer))

    # Key computational step with distractor variables in scope
    avg_fluctuation = max(temp_aggregates) - min(temp_aggregates) if temp_aggregates else 0
    zone_diversity = len(event_counter)

    # Core result determination
    peak_capacity = max(usage_tracker.values())

    # Final red herring computation that doesn't affect answer
    synthetic_index = avg_fluctuation * zone_diversity + baseline_offset

    print(f"Result: {peak_capacity}")

monitor_resource_allocation()