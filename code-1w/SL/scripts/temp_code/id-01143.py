def analyze_growth_patterns(data_log):
    total_entries = len(data_log)
    valid_records = [entry for entry in data_log if entry['status'] == 'active']
    
    # Irrelevant transformation (distractor)
    temp_weights = {k: v * 0.95 for k, v in enumerate([2, 4, 6, 8])}
    adjustment_factor = sum(temp_weights.values()) / 10.0
    
    # Real processing begins
    growth_cycles = []
    for record in valid_records:
        cycle_length = record.get('duration', 0)
        efficiency = record.get('output', 0) / (cycle_length if cycle_length > 0 else 1)
        growth_cycles.append({'eff': efficiency, 'len': cycle_length})

    # Unused helper function (dead code path)
    def smooth_data(seq):
        return [sum(seq[i:i+3])/3 for i in range(len(seq)-2)]

    # Set operations to filter high-efficiency cycles
    high_eff_indices = {i for i, gc in enumerate(growth_cycles) if gc['eff'] > 1.5}
    filtered_cycles = [gc for i, gc in enumerate(growth_cycles) if i in high_eff_indices}

    # Dictionary aggregation
    cluster_metrics = {}
    for i, cycle in enumerate(filtered_cycles):
        key = cycle['len'] // 2
        if key not in cluster_metrics:
            cluster_metrics[key] = []
        cluster_metrics[key].append(cycle['eff'])

    # Mean per cluster using lambda
    cluster_averages = {k: round(sum(v)/len(v), 4) for k, v in cluster_metrics.items()}

    # Final calculation
    baseline = len(cluster_averages.keys())
    bonus = sum(1 for avg in cluster_averages.values() if avg > 2.0)
    final_yield = calculate_harvest_efficiency(cluster_metrics, growth_cycles)
    
    # Unused but plausible variable (distractor)
    projected_next = adjustment_factor * final_yield
    
    print(f"Result: {final_yield}")


def calculate_harvest_efficiency(metrics, cycles):
    base_eff = sum(len(v) for v in metrics.values())
    penalty = 0
    for cycle in cycles:
        if cycle['len'] < 3:
            penalty += 0.5
    return int(base_eff * 1.75 - penalty)

# Input data
log_data = [
    {'status': 'active', 'duration': 4, 'output': 7},
    {'status': 'inactive', 'duration': 5, 'output': 6},
    {'status': 'active', 'duration': 2, 'output': 3},
    {'status': 'active', 'duration': 6, 'output': 10},
    {'status': 'active', 'duration': 3, 'output': 5},
    {'status': 'active', 'duration': 8, 'output': 14},
    {'status': 'active', 'duration': 2, 'output': 2},
]

analyze_growth_patterns(log_data)