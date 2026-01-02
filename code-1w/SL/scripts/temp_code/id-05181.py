def analyze_workload_intensity(load_profile):
    peak_load = max(load_profile)
    avg_load = sum(load_profile) / len(load_profile)
    intensity_score = (peak_load - avg_load) / avg_load if avg_load > 0 else 0
    normalized_score = min(intensity_score * 2.5, 1.0)
    return normalized_score

def evaluate_node_reliability(uptime_history):
    total_uptime = sum(uptime_history)
    max_possible = len(uptime_history) * 100
    reliability_ratio = total_uptime / max_possible
    adjusted_ratio = reliability_ratio * 0.8 + 0.2
    return adjusted_ratio

def optimize_system_resources(efficiency_metrics, contingency_buffer):
    base_efficiency = sum(efficiency_metrics) / len(efficiency_metrics)
    buffered_efficiency = base_efficiency * (1 + contingency_buffer)
    scaling_factor = 1.0
    if buffered_efficiency < 0.6:
        scaling_factor = 1.8
    elif buffered_efficiency < 0.8:
        scaling_factor = 1.4
    final_capacity = int(buffered_efficiency * scaling_factor * 1000)
    
    # Distractor: irrelevant computation on set operations
    temp_set_a = {x for x in range(10, 18)}
    temp_set_b = {x for x in range(14, 22)}
    temp_intersection = temp_set_a & temp_set_b
    temp_union = temp_set_a | temp_set_b
    temp_diff = temp_set_a - temp_set_b
    dummy_result = len(temp_intersection) * len(temp_union) // (len(temp_diff) or 1)
    
    return final_capacity

# Simulated system telemetry
current_loads = [45, 67, 52, 71, 58]
node_uptimes = [98, 95, 99, 90, 97]

# Irrelevant preprocessing (distraction)
processed_loads = [x * 1.02 for x in current_loads]
decay_weights = [0.9**i for i in range(len(processed_loads))]
weighted_sum = sum(processed_loads[i] * decay_weights[i] for i in range(len(processed_loads)))
smoothed_value = weighted_sum / sum(decay_weights)

# Core logic chain
intensity = analyze_workload_intensity(current_loads)
reliability = evaluate_node_reliability(node_uptimes)
efficiency_pool = [intensity * 0.7, reliability * 0.9, 0.75]
reserve_margin = 0.15

# Key statement
final_capacity = optimize_system_resources(efficiency_pool, reserve_margin)

# Print result
print(f"Result: {final_capacity}")