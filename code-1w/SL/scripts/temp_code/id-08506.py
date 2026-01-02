from itertools import compress

def analyze_soil_quality(plots):
    # Returns a list indicating whether each plot has adequate nutrients
    return [sum(plot) / len(plot) > 0.6 for plot in plots]

def estimate_water_retention(plots):
    # Computes cumulative moisture index per plot (distractor logic)
    retention_scores = []
    for plot in plots:
        score = 0
        for moisture in plot:
            if moisture > 0.5:
                score += moisture * 1.2
            else:
                score += moisture * 0.8
        retention_scores.append(score)
    return retention_scores

def filter_viable_zones(plots, threshold=0.55):
    # Determines viability based on average condition (used in main logic)
    viable = []
    for plot in plots:
        avg_condition = sum([1 if x > threshold else 0 for x in plot]) / len(plot)
        viable.append(avg_condition > 0.7)
    return viable

def calculate_optimal_harvest(plots):
    # Main computation path
    total_yield = 0
    nutrient_status = analyze_soil_quality(plots)
    viability_mask = filter_viable_zones(plots)
    
    # Use itertools.compress to select only viable plots
    viable_plots = list(compress(plots, viability_mask))
    
    adjustment_factor = 0.0
    debug_logs = []
    
    # Irrelevant nested loop - simulates diagnostic scan
    for i, plot in enumerate(plots):
        for j, val in enumerate(plot):
            if val > 0.9:
                debug_logs.append(f"High reading at ({i},{j})")  # Dead code path
    
    # Actual yield calculation
    for idx, plot in enumerate(viable_plots):
        base_yield = 0
        for reading in plot:
            if reading > 0.7:
                base_yield += reading * 15
            elif reading > 0.4:
                base_yield += reading * 8
            else:
                base_yield += reading * 3
        
        # Apply nutrient bonus only if both conditions met
        if nutrient_status[idx] and sum(plot) / len(plot) > 0.65:
            base_yield *= 1.4
        
        total_yield += base_yield
    
    # Secondary adjustment using enumerate and zip (semi-relevant)
    multipliers = [1.1, 0.95, 1.05]
    for i, (plot, mult) in enumerate(zip(viable_plots, multipliers)):
        if i < len(multipliers):
            total_yield -= sum(plot) * 0.05  # Minor reduction

    final_adjustment = 0
    for x in range(3):
        final_adjustment += x ** 2  # Distractor: unused computation
    
    return int(total_yield)

# Simulated sensor data from agricultural drones (normalized readings)
land_plots = [
    [0.72, 0.68, 0.54, 0.81],
    [0.34, 0.45, 0.53, 0.62],
    [0.77, 0.81, 0.79, 0.83],
    [0.21, 0.33, 0.41, 0.29]
]

water_data = estimate_water_retention(land_plots)  # Called but not used

final_yield = calculate_optimal_harvest(land_plots)
print(f"Result: {final_yield}")