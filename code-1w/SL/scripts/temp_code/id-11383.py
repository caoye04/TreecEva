def analyze_traffic(flow_data, threshold=100):
    total_load = 0
    peak_moment = None
    temp_sum = 0  # distractor: used in dead code path

    for i, load in enumerate(flow_data):
        if load > threshold:
            total_load += load * 0.9
            if peak_moment is None:
                peak_moment = i
        else:
            temp_sum += load  # irrelevant accumulation

    avg_base = sum(flow_data) / len(flow_data)
    adjusted_avg = avg_base * 0.95  # semi-relevant: not used in final result

    return total_load, peak_moment


def calculate_redundancy(nodes):
    redundancy_score = 0
    for a, b in zip(nodes[:-1], nodes[1:]):
        redundancy_score += abs(a - b)
    return redundancy_score


def calculate_utilization(segments):
    raw_volumes = [sum(segment['traffic']) for segment in segments]
    scaling_factor = 1.1
    weighted_loads = [load * scaling_factor for load in raw_volumes]

    # Misleading intermediate calculation
    hypothetical_max = max(raw_volumes) * 1.5
    buffer_allocation = hypothetical_max * 0.2

    # Key logic with slicing and filtering
    active_segments = [vol for vol in weighted_loads if vol > 200]
    trimmed_analysis = active_segments[1:-1]  # slice operation

    base_utilization = sum(active_segments)
    if len(trimmed_analysis) > 0:
        base_utilization -= sum(trimmed_analysis) * 0.1

    return int(base_utilization)

# Simulate network infrastructure
segment_A = {'traffic': [120, 150, 200], 'node_id': 'A1'}
segment_B = {'traffic': [180, 220, 240], 'node_id': 'B2'}
segment_C = {'traffic': [90, 110, 130], 'node_id': 'C3'}
segment_D = {'traffic': [250, 260, 270], 'node_id': 'D4'}

network_segments = [segment_A, segment_B, segment_C, segment_D]

# Dead code block - misleading initialization
initial_audit = [s['node_id'] for s in network_segments]
redundant_check = calculate_redundancy([len(s['traffic']) for s in network_segments])

# Primary analysis (distractor)
baseline, first_peak = analyze_traffic([120, 150, 200, 180, 220, 240, 90, 110, 130, 250, 260, 270])

# Critical assignment
final_capacity = calculate_utilization(network_segments)

print(f"Result: {final_capacity}")