def analyze_traffic(data_stream):
    raw_segments = data_stream.split(',')
    parsed_values = [int(x.strip()) for x in raw_segments]
    
    # Irrelevant transformation (distractor)
    reversed_chunks = [x * 2 for x in parsed_values if x < 50]
    temp_offset = sum(reversed_chunks) // len(reversed_chunks) if reversed_chunks else 0

    # Core logic: filter, scale, and reduce
    filtered_load = [x for x in parsed_values if x > 20]
    scaled_bandwidth = list(map(lambda x: x * 1.5, filtered_load))
    average_load = sum(scaled_bandwidth) / len(scaled_bandwidth) if scaled_bandwidth else 0

    # State tracking with misleading counters
    peak_count = 0
    for val in scaled_bandwidth:
        if val > average_load:
            peak_count += 1

    baseline = average_load * 0.8
    fluctuation = abs(scaled_bandwidth[-1] - baseline)
    optimized_flow = int(average_load - fluctuation + peak_count)

    # Dead code path (never executed due to fixed condition)
    emergency_override = False
    if len(parsed_values) > 1000:
        emergency_override = True
        optimized_flow = -999
    
    def apply_correction(flow):
        correction_factor = 1.05
        return int(flow * correction_factor)
    
    final_adjustment = apply_correction(optimized_flow)
    
    # Print required result
    print(f"Result: {optimized_flow}")
    return final_adjustment

# Input with realistic network traffic-like values
data_input = "30, 15, 45, 60, 25, 10, 55"
analyze_traffic(data_input)