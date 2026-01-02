def analyze_workload(intensity_log, threshold_multiplier=1.5):
    peak_load = max(intensity_log)
    avg_load = sum(intensity_log) / len(intensity_log)
    fluctuation_index = (peak_load - avg_load) / avg_load
    
    # Irrelevant derived metrics (distractors)
    normalized_scores = [x / peak_load for x in intensity_log]
    score_variance = sum((x - avg_load)**2 for x in intensity_log) / len(intensity_log)
    high_load_segments = [x for x in intensity_log if x > threshold_multiplier * avg_load]
    
    return fluctuation_index, avg_load, len(high_load_segments)


def calculate_efficiency_factor(nodes, latency_profile):
    base_efficiency = 0.8
    penalty_rate = 0.02
    
    total_penalty = 0
    for i, latency in enumerate(latency_profile):
        if latency > 150:
            total_penalty += penalty_rate * (latency - 150)
    
    efficiency = base_efficiency - total_penalty
    efficiency = max(efficiency, 0.3)  # Minimum floor
    
    # Dead computation: unused path
    if nodes > 10:
        backup_mode = "redundant"
        recovery_window = 300
    else:
        backup_mode = "standard"
        recovery_window = 120
    
    return efficiency


def optimize_allocation(config, usage):
    # Core logic starts here
    base_capacity = config['base_unit'] * config['replicas']
    reserve_margin = config.get('reserve', 0.2)
    
    # Slice recent usage for trend analysis
    recent_usage = usage[-7:]  # Last 7 periods
    growth_trend = (recent_usage[-1] - recent_usage[0]) / recent_usage[0]
    
    # Set operations to identify usage patterns
    high_demand_days = {i for i, x in enumerate(recent_usage) if x > 1.3 * sum(recent_usage)/len(recent_usage)}
    weekend_indices = {5, 6}
    weekend_load_interference = len(high_demand_days & weekend_indices)  # Overlap count
    
    # Main allocation logic
    if growth_trend > 0.1:
        scaling_factor = 1.4
    elif growth_trend < -0.05:
        scaling_factor = 0.9
    else:
        scaling_factor = 1.1
    
    projected_load = base_capacity * scaling_factor
    adjusted_capacity = projected_load * (1 + reserve_margin)
    
    # Efficiency correction based on system profile
    sys_latency = config['performance']['latency_history']
    efficiency = calculate_efficiency_factor(config['nodes'], sys_latency)
    final_capacity = int(adjusted_capacity * efficiency)
    
    # Unused intermediate variables (distraction)
    theoretical_max = base_capacity * 2.5
    utilization_ratio = adjusted_capacity / theoretical_max
    saturation_level = 'high' if utilization_ratio > 0.8 else 'moderate'
    
    return final_capacity

# Main execution
base_config = {
    'base_unit': 120,
    'replicas': 3,
    'reserve': 0.25,
    'nodes': 8,
    'performance': {
        'latency_history': [120, 110, 155, 130, 145, 160, 115, 138],
        'uptime': 99.95
    }
}

usage_pattern = [280, 300, 310, 295, 320, 410, 430, 380, 390, 405]

fluctuation_index, avg_load, spike_count = analyze_workload(usage_pattern)

# Key statement
final_capacity = optimize_allocation(base_config, usage_pattern)

print(f"Result: {final_capacity}")