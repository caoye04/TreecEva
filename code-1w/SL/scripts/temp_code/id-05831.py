from itertools import combinations

def analyze_traffic(flow_data, threshold=150):
    peak_periods = []
    total_load = 0
    for period, load in flow_data:
        if load > threshold:
            peak_periods.append(period)
        total_load += load
    avg_load = total_load / len(flow_data) if flow_data else 0
    return peak_periods, avg_load

def generate_patterns(elements):
    # Irrelevant helper: generates all 2-element combos (not used in final result)
    return list(combinations(elements, 2))

def calculate_efficiency(routing_matrix):
    efficiency_scores = []
    dummy_accumulator = 0
    for row in routing_matrix:
        row_sum = sum(row)
        if row_sum > 0:
            efficiency = row.count(1) / row_sum
            efficiency_scores.append(round(efficiency, 4))
        dummy_accumulator += len(row)  # Distractor operation
    return efficiency_scores

def optimize_allocation():
    # Simulated network node loads (in Mbps)
    node_loads = [('A', 120), ('B', 180), ('C', 95), ('D', 210), ('E', 135)]
    
    # Extract names and loads
    node_names = [n for n, _ in node_loads]
    loads = [l for _, l in node_loads]
    
    # Misleading pattern generation (irrelevant to final answer)
    unused_combinations = generate_patterns(node_names)
    unused_count = len(unused_combinations)
    
    # Real processing begins
    traffic_data = [(i, load) for i, load in enumerate(loads)]
    peak_times, average_load = analyze_traffic(traffic_data, threshold=130)
    
    # Construct routing matrix based on thresholds (simulated)
    routing_matrix = []
    for load in loads:
        row = [1 if load > 100 else 0, 1 if load > 150 else 0, 0]  # 3-tier routing
        routing_matrix.append(row)
    
    # Compute efficiency (partially relevant)
    scores = calculate_efficiency(routing_matrix)
    avg_score = sum(scores) / len(scores) if scores else 0
    
    # State tracking with distractors
    temp_state = {'max_load': max(loads), 'threshold': 150, 'scale_factor': 1.25}
    adjustment = 0.1 * temp_state['max_load'] if temp_state['max_load'] > 200 else 0
    
    # Key computation chain
    base_capacity = sum(loads)
    overhead = len([l for l in loads if l > 150]) * 10
    adjusted_capacity = base_capacity - overhead + 5  # Fixed correction term
    
    # Secondary adjustment using average score (actual dependency)
    final_bandwidth = int(adjusted_capacity * (1 + avg_score * 0.5))
    
    # Dead code branch (never executed but looks meaningful)
    if False:
        fallback = sum(loads) // len(loads)
        final_bandwidth = fallback * 3
    
    return final_bandwidth

# Execution entry point
def main():
    result = optimize_allocation()
    print(f"Target result: {result}")

main()