import itertools

def analyze_growth_cycles(data, threshold=0.75):
    """ Irrelevant function: analyzes growth cycles but not used in main logic """
    count = 0
    for seq in itertools.combinations(data, 3):
        if sum(seq) / len(seq) > threshold:
            count += 1
    return count

def normalize_readings(readings):
    """ Misleading preprocessing function that isn't actually used """
    base = max(readings)
    return [x / base for x in readings]

def generate_cluster_keys(n):
    """ Dead code path: generates keys but never utilized """
    return [hash(f'cluster_{i}') % 1000 for i in range(n)]

def simulate_failure_modes(states):
    """ Distractor: simulates system failures, no impact on result """
    failed = []
    for s in states:
        if s & 1:
            failed.append(s ^ 1)
    return failed

def extract_signatures(payload):
    # Unused feature extraction
    return {i: hash(str(v)) % 100 for i, v in enumerate(payload)}

def calculate_harvest_efficiency(clusters, performance_log):
    # Core relevant function with embedded distractions
    total_nodes = 0
    active_capacity = []
    decoy_sum = 0

    # Real logic begins
    for idx, (cid, nodes) in enumerate(clusters.items()):  
        if len(cid) < 5:  
            continue  # Skip small clusters
        load_factor = performance_log.get(cid, {}).get('load', 0)
        efficiency_rating = performance_log.get(cid, {}).get('efficiency', 1.0)

        # Irrelevant bit manipulation distraction
        masked_id = hash(cid) & 0xFFFF
        decoy_sum += masked_id >> 4

        if load_factor > 0.5 and efficiency_rating >= 0.8:
            total_nodes += nodes
            active_capacity.append(efficiency_rating * nodes)

    # Real calculation
    if total_nodes == 0:
        return 0.0

    average_yield = sum(active_capacity) / total_nodes

    # Fake complexity using sets and min/max
    capacity_set = set(active_capacity)
    fluctuation = max(capacity_set) - min(capacity_set) if len(capacity_set) > 1 else 0

    # Additional red herring: unused dictionary transformation
    stats_summary = {
        'peak': max(capacity_set),
        'floor': min(capacity_set),
        'volatility': fluctuation,
        'decoy_metric': decoy_sum / (total_nodes + 1)
    }

    # Final meaningful computation
    adjustment = 1.0 - (fluctuation * 0.1)
    adjusted_yield = average_yield * adjustment

    return round(adjusted_yield, 6)

# Main execution block
if __name__ == '__main__':
    # Real input data
    cluster_map = {
        'cluster_alpha': 120,
        'cluster_beta': 85,
        'cluster_gamma': 200,
        'cluster_delta': 95
    }

    metrics = {
        'cluster_alpha': {'load': 0.82, 'efficiency': 0.91},
        'cluster_beta': {'load': 0.45, 'efficiency': 0.75},  # Below load threshold
        'cluster_gamma': {'load': 0.91, 'efficiency': 0.87},
        'cluster_delta': {'load': 0.58, 'efficiency': 0.80}
    }

    # Irrelevant auxiliary data
    sensor_data = [0.81, 0.77, 0.83, 0.69, 0.74]
    node_states = [2, 3, 1, 0, 7]
    readings = [124, 118, 130, 120]

    # Unused operations (distractors)
    normalized = normalize_readings(readings)
    signatures = extract_signatures(readings)
    failure_scenarios = simulate_failure_modes(node_states)
    keys = generate_cluster_keys(10)
    cycle_analysis = analyze_growth_cycles(sensor_data)

    # Key statement
    final_yield = calculate_harvest_efficiency(cluster_map, metrics)

    print(f"Result: {final_yield}")