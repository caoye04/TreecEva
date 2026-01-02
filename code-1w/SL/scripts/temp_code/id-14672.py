def analyze_flow_dynamics(flow_data, tolerance=0.001):
    # Simulate a fluid dynamics scoring system with irrelevant transformations
    normalized_flows = [round(x / sum(flow_data), 5) for x in flow_data]
    weighted_sum = sum([x * (i + 1) for i, x in enumerate(normalized_flows)])
    
    # Distractor: unused transformation chain
    scaled_offsets = list(map(lambda x: x * 1.5 + 0.2, normalized_flows))
    offset_correction = sum(scaled_offsets[:3]) if len(scaled_offsets) > 3 else 0.0
    
    # Real computation begins: identify stable zones
    stable_indices = []
    for i in range(1, len(normalized_flows) - 1):
        if abs(normalized_flows[i] - normalized_flows[i-1]) < tolerance and \
           abs(normalized_flows[i] - normalized_flows[i+1]) < tolerance:
            stable_indices.append(i)
    
    # Distractor: dead code path (never reached due to logic)
    if len(stable_indices) == 0 and offset_correction > 1.0:
        fallback_value = sum(scaled_offsets) * 0.1
        return int(fallback_value)

    # Construct flow matrix using zip and enumerate
    flow_matrix = []
    for idx, (a, b) in enumerate(zip(normalized_flows, normalized_flows[1:])):
        row = [a * b + (idx * 0.01), a + b - (idx * 0.005)]
        flow_matrix.append(row)
    
    # Thresholds derived from stable regions
    base_threshold = sum(normalized_flows) / len(normalized_flows)
    thresholds = set()
    for i in stable_indices:
        thresholds.add(round(normalized_flows[i], 4))
    thresholds.add(round(base_threshold, 4))

    # Critical function call
    equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)
    
    # Additional red herring variables
    dynamic_entropy = -sum([p * __import__('math').log(p) for p in normalized_flows if p > 0])
    adjustment_factor = len(thresholds) * 0.05
    
    return equilibrium_score


def calculate_equilibrium(matrix, thres_set):
    score = 0
    threshold_list = sorted(thres_set)
    
    # Use of lambda in filtering
    valid_cells = list(filter(lambda x: x > threshold_list[0], [cell for row in matrix for cell in row]))
    
    # Core logic: count how many exceed second smallest threshold
    if len(threshold_list) >= 2:
        pivot = threshold_list[1]
        for val in valid_cells:
            if val > pivot:
                score += 1
        # Introduce minor distraction
        score = score * 2 if len(valid_cells) > 5 else score + 3
    else:
        score = len(valid_cells)
    
    # Final adjustment based on matrix structure
    for i, row in enumerate(matrix):
        if i % 2 == 0 and len(row) > 1:
            score -= (row[0] > row[1])  # boolean as int
    
    return score

# Execute simulation
flow_input = [12, 8, 9, 8, 10, 8, 7, 8]
equilibrium_score = analyze_flow_dynamics(flow_input)
print(f"Result: {equilibrium_score}")