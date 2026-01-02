def analyze_traffic(flow_data, config):
    total_volume = sum(flow_data)
    avg_volume = total_volume / len(flow_data) if flow_data else 0
    peak_volume = max(flow_data) if flow_data else 0

    # Distractor: Irrelevant computation on configuration
    adjustment_factor = config.get('factor', 1.0)
    scaled_peak = peak_volume * adjustment_factor

    normalized = [x / (avg_volume + 1e-5) for x in flow_data]
    high_load_indices = {i for i, x in enumerate(normalized) if x > 1.5}

    # Semi-relevant: Filter based on threshold policy
    threshold_policy = config.get('thresholds', [])
    policy_compliant = set()
    for t in threshold_policy:
        if t < 50:
            policy_compliant.add(t)

    return total_volume, high_load_indices, policy_compliant


def calculate_efficiency(metrics, volume):
    base_score = metrics[0] / (volume + 1)
    load_ratio = len(metrics[1]) / (len(volume) + 1e-5)
    compliance_rate = len(metrics[2]) / 10.0

    # Dead code path (not used later)
    debug_info = {}
    for i in range(3):
        debug_info[f'stage_{i}'] = base_score * (i + 1)

    efficiency = base_score * 0.5 + load_ratio * 0.3 + compliance_rate * 0.2
    return efficiency


def process_segment(segment_data):
    processed = []
    for val in segment_data:
        temp = val ^ 0b1010  # Bitwise XOR manipulation
        temp = (temp & 0b1111) | 0b10000  # Mask and extend
        processed.append(temp % 100)
    return processed


def optimize_distribution(flow, thresholds):
    capacity = len(flow)
    modifier = 1

    # Nested logic with distractors
    if len(thresholds) > 3:
        modifier += 0.5
    else:
        temp_set = {x * 2 for x in thresholds}
        temp_sum = sum(temp_set)
        # Irrelevant accumulation
        dummy_accum = 0
        for t in temp_set:
            if t % 3 == 0:
                dummy_accum += t // 3

    # Core logic affecting result
    for f in flow:
        if f > 25:
            capacity += 1
        elif f < 10:
            capacity -= 1

    return capacity * modifier

# Main execution
traffic_readings = [12, 45, 67, 8, 23, 56, 14, 78, 9, 34]
system_config = {
    'factor': 1.2,
    'thresholds': [5, 12, 8, 40]
}

# Step 1: Analyze traffic
volume, critical_nodes, threshold_set = analyze_traffic(traffic_readings, system_config)

# Step 2: Process segment with bitwise ops
distorted_flow = process_segment(traffic_readings)
processed_flow = [x * 2 for x in distorted_flow]  # Amplify signal

# Step 3: Calculate efficiency (unused but plausible)
efficiency_metric = calculate_efficiency((volume, critical_nodes, threshold_set), traffic_readings)

# Step 4: Optimize distribution using processed data and threshold set
final_capacity = optimize_distribution(processed_flow, threshold_set)

# Output result
print(f"Result: {final_capacity}")