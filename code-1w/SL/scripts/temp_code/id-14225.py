import itertools

# Domain-specific simulation: Air filtration system efficiency analysis
def analyze_filtration_efficiency(flow_rates, particle_sizes, maintenance_log):
    base_efficiency = 0.87
    degradation_factor = 0.003
    calibration_offset = 0.012

    # Irrelevant preprocessing: normalize flow rates (not used later)
    normalized_flows = [round((fr - min(flow_rates)) / (max(flow_rates) - min(flow_rates) + 1e-8), 6) for fr in flow_rates]
    adjusted_flows = [fr * 1.08 for fr in flow_rates]  # Distractor adjustment

    # Critical data transformation: weight calculation based on particle size and flow
    weighted_impact = []
    for i, size in enumerate(particle_sizes):
        impact = 0
        if size < 2.5:
            impact += size * 3.1
        elif size < 10:
            impact += size * 1.8
        else:
            impact += size * 0.9
        # Combine with flow rate influence
        impact *= flow_rates[i % len(flow_rates)]
        weighted_impact.append(round(impact, 6))

    # Decoy statistical analysis (dead path)
    mean_impact = sum(weighted_impact) / len(weighted_impact) if weighted_impact else 0
    variance_proxy = sum((x - mean_impact) ** 2 for x in weighted_impact) / len(weighted_impact) if weighted_impact else 0

    # Simulate maintenance-based efficiency decay over time
    cumulative_degradation = 0
    for entry in maintenance_log:
        if 'filter_change' not in entry:
            cumulative_degradation += degradation_factor

    current_efficiency = base_efficiency - cumulative_degradation + calibration_offset

    # Generate combinatorial exposure scenarios (distractor structure)
    exposure_combinations = list(itertools.combinations_with_replacement(particle_sizes, 2))
    exposure_scores = []
    for combo in exposure_combinations:
        score = abs(combo[0] - combo[1]) * 0.5
        exposure_scores.append(score)

    # Real logic: filter weights by safety threshold and calculate final score
    safety_threshold = 4.7
    filtered_weights = []
    for w in weighted_impact:
        if w > safety_threshold:
            filtered_weights.append(w * current_efficiency)

    # Secondary filtering based on character count in log entries (red herring)
    total_chars = sum(len(entry) for entry in maintenance_log)
    char_adjustment = total_chars % 7

    # Final score computation
    filtration_score = sum(filtered_weights)
    
    # Extra misleading operation (no effect on answer)
    adjusted_score = filtration_score * (1 + char_adjustment * 0.01) if char_adjustment > 5 else filtration_score
n
    return filtration_score

# Input data
flow_rates_input = [12.1, 14.3, 11.9, 13.0, 12.7]
particle_sizes_input = [1.2, 3.4, 12.1, 5.5, 2.8, 9.3, 4.1]
maintenance_log_input = [
    'filter_clean_2023',
    'status_check_2023',
    'fan_alignment_2024',
    'sensor_calib_2024'
]

# Execute function
result = analyze_filtration_efficiency(flow_rates_input, particle_sizes_input, maintenance_log_input)
print(f"Result: {result}")