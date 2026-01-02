def calculate_thermal_buffer(load_profile):
    base_factor = 1.75
    peak_stress = max(load_profile)
    avg_stress = sum(load_profile) / len(load_profile)
    stress_ratio = peak_stress / avg_stress if avg_stress != 0 else 0

    # Irrelevant signal smoothing (distractor)
    smoothed = [load_profile[i] * 0.9 + 0.1 * load_profile[i-1] for i in range(1, len(load_profile))]
    noise_floor = sum(smoothed) / len(smoothed) if smoothed else 0

    # Real computation path
    efficiency_drop = stress_ratio * 0.15
    adjusted_base = base_factor * (1 - efficiency_drop)
    buffer_score = adjusted_base * peak_stress

    # Dead code: never used (distractor)
    diagnostic_trace = {"max": peak_stress, "noise": noise_floor, "samples": len(smoothed)}
    temp_history = load_profile[::-1]  # slicing - not used

    return int(buffer_score)

# System load simulation (real data)
node_metrics = [23, 45, 67, 89, 91, 76, 54, 32]

# Auxiliary irrelevant calculations (distractor)
redundant_sum = sum([n**2 for n in node_metrics if n < 50])
scaling_factor = 0.88
phantom_threshold = redundant_sum * scaling_factor / (len(node_metrics) + 1)

# Core execution path
cluster_load = [n for n in node_metrics if n > 40]  # filtering relevant nodes
intermediate_peak = max(cluster_load) // 3  # misleading but harmless

# Key statement
thermal_capacity = calculate_thermal_buffer(cluster_load)

# Output result as required
print(f"Result: {thermal_capacity}")