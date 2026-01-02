def calculate_optimal_harvest(plots, quality_map):
    base_yield = 10
    bonus_factor = 0.5
    penalty_factor = 0.3
    adjustment_tracker = []
    temp_results = []
    total_plots = len(plots)
    cumulative_score = 0

    for i, (plot_id, crop_type, area) in enumerate(plots):
        # Irrelevant computation: tracking enumeration index for no use
        _ = i * 2  
        
        # Real logic starts: get soil quality for this plot
        if plot_id in quality_map:
            soil_q = quality_map[plot_id]
        else:
            soil_q = 1.0

        # Base production model
        base_production = base_yield * area
        
        # Apply quality multiplier
        adjusted_production = base_production * soil_q
        
        # Bonus for large areas (over 15 units)
        if area > 15:
            adjusted_production += base_production * bonus_factor
        
        # Penalty for mixed crop type (distraction: not used later)
        if crop_type == "mixed":
            potential_penalty = adjusted_production * penalty_factor
            adjustment_tracker.append((plot_id, -potential_penalty))

        # Only certain crops are counted in final yield
        if crop_type in ["wheat", "corn"]:
            temp_results.append(adjusted_production)

    # Secondary loop: apply zip to combine with dummy weights
    weights = [1.1, 0.9, 1.0] * (len(temp_results) // 3 + 1)
    weighted_values = []
    for val, wt in zip(temp_results, weights):
        weighted_values.append(val * wt)

    # Final aggregation
    if weighted_values:
        average_weighted = sum(weighted_values) / len(weighted_values)
        peak = max(weighted_values)
        stability_ratio = average_weighted / peak if peak != 0 else 0
        # Final decision heuristic
        final_yield = int(average_weighted * stability_ratio * 1.2)
    else:
        final_yield = 0

    # Dead code: irrelevant sorting of unused list
    adjustment_tracker.sort(key=lambda x: x[0])
    
    return final_yield

# Main data setup
plots_data = [
    (101, "wheat", 12),
    (102, "mixed", 20),
    (103, "corn", 8),
    (104, "barley", 25),
    (105, "wheat", 18)
]

soil_quality = {
    101: 1.2,
    102: 0.8,
    103: 1.5,
    105: 1.1
}

# Execution point
final_yield = calculate_optimal_harvest(plots_data, soil_quality)
print(f"Target result: {final_yield}")