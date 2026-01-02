def analyze_traffic(flow_data, config):
    total_load = sum(flow_data)
    normalized = [x / total_load for x in flow_data]
    
    # Irrelevant transformation (distractor)
    inverted = [1 / (x + 1e-5) for x in normalized]
    avg_inverted = sum(inverted) / len(inverted)

    # Real processing begins
    filtered = [x for x in normalized if x > config['threshold']]
    scaled = [int(x * 1000) for x in filtered]
    
    # Set operation: track unique high-flow nodes
    unique_scaled = set(scaled)
    outlier_set = {x for x in unique_scaled if x > 500}

    # Slicing to simulate window analysis (only middle 60% used)
    mid_section = scaled[len(scaled)//5 : 4*len(scaled)//5]
    peak_window = max(mid_section) if mid_section else 0

    # Simulate capacity allocation
    base_alloc = [x * config['multiplier'] for x in mid_section]
    adjusted_alloc = [x + config['offset'] for x in base_alloc]
    
    # Dead code path (never executed due to logic)
    if len(outlier_set) > 100:
        adjusted_alloc = [x * 2 for x in adjusted_alloc]  # unreachable

    return adjusted_alloc, unique_scaled, outlier_set


def optimize_distribution(processed_flow, threshold_set):
    cumulative = 0
    for val in processed_flow:
        if val in threshold_set:
            cumulative += val * 1.1
        else:
            cumulative += val * 0.9
    
    # Extra irrelevant calculation
    dummy_sum = sum([x**2 for x in processed_flow[:3]]) if len(processed_flow) >= 3 else 0
    adjustment_factor = 1.05 if dummy_sum < 10000 else 1.0
    
    # Final result
    final_capacity = int(cumulative * adjustment_factor)
    return final_capacity

# Main execution
traffic_pattern = [120, 150, 80, 200, 90, 160, 110, 140, 95, 130]
params = {
    'threshold': 0.08,
    'multiplier': 3.5,
    'offset': 12
}

allocations, all_peaks, critical_peaks = analyze_traffic(traffic_pattern, params)
final_capacity = optimize_distribution(allocations, critical_peaks)
print(f"Target result: {final_capacity}")