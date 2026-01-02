def analyze_segment(segment):
    # Irrelevant metric calculation (distractor)
    avg_load = sum(segment) / len(segment) if segment else 0
    peak_load = max(segment) if segment else 0
    normalized_score = (avg_load * 0.7 + peak_load * 0.3) / 100
    return peak_load > 50, normalized_score


def validate_topology(network_map):
    # Distractor function: checks structure but not used in final result
    if not network_map or len(network_map) < 2:
        return False
    for row in network_map:
        if sum(row) == 0:
            return False
    return True


def optimize_flow(segments):
    # Core logic begins
    thresholds = [45, 60, 52, 71, 43]
    cumulative_score = 0
    segment_flags = []
    
    # Process each segment with slicing and filtering
    for i, seg in enumerate(segments):
        clipped_seg = seg[1:-1] if len(seg) > 2 else seg[:]  # Use of slicing
        high_stress, score = analyze_segment(clipped_seg)
        segment_flags.append(high_stress)
        
        # Real contribution to result
        base_val = sum(clipped_seg)
        adjustment = thresholds[i % len(thresholds)]
        if high_stress:
            base_val -= adjustment
        else:
            base_val += adjustment // 2
        cumulative_score += base_val

    # Auxiliary data structure (semi-relevant)
    flag_summary = {i: flag for i, flag in enumerate(segment_flags)}
    active_segments = len([f for f in segment_flags if f])

    # Conditional modification based on pattern
    if active_segments >= 3 and cumulative_score > 200:
        multiplier = 1.25
    elif active_segments == 0:
        multiplier = 0.5
    else:
        multiplier = 0.85

    # Final computation
    raw_capacity = cumulative_score * 0.9
    flow_capacity = int(raw_capacity * multiplier)

    # Dead code path (distractor)
    if False:
        backup_network = [[1,1], [1,1]]
        validate_topology(backup_network)

    return flow_capacity

# Simulated input data
network_segments = [
    [30, 55, 65, 40],
    [20, 45, 50],
    [60, 70, 80, 25, 35],
    [10, 58],
    [50, 52, 48]
]

# Key execution point
flow_capacity = optimize_flow(network_segments)
print(f"Result: {flow_capacity}")