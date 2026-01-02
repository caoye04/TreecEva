from itertools import combinations

# Simulate agricultural land plots with various soil quality, moisture, and size
land_plots = [
    {'size': 10, 'soil_quality': 0.8, 'moisture': 0.6},
    {'size': 15, 'soil_quality': 0.5, 'moisture': 0.9},
    {'size': 12, 'soil_quality': 0.7, 'moisture': 0.4},
    {'size': 8,  'soil_quality': 0.9, 'moisture': 0.7},
    {'size': 20, 'soil_quality': 0.6, 'moisture': 0.5}
]

# Irrelevant weather data (distractor)
weather_forecast = {
    'temperature': [22, 24, 19, 23],
    'humidity': [60, 65, 70, 68],
    'wind_speed': [10, 12, 8, 9]
}

# Historical yield average (semi-relevant but not used in final calculation)
historical_avg_yield_per_unit = 3.2

# Thresholds for optimal growth (used in filtering)
optimal_soil_threshold = 0.65
min_moisture_for_growth = 0.45

# Helper function to compute base yield for a plot
def compute_base_yield(plot):
    return plot['size'] * plot['soil_quality'] * plot['moisture'] * 10

# Function to find best combination of plots that maximizes yield under constraints
def calculate_optimal_harvest(plots):
    valid_combinations = []
    
    # Generate all possible non-empty combinations of plots (using itertools)
    for r in range(1, len(plots) + 1):
        for combo in combinations(plots, r):
            total_size = sum(p['size'] for p in combo)
            if total_size <= 30:  # Max area constraint
                valid_combinations.append(combo)
    
    best_yield = 0
    
    # Evaluate each valid combination
    for combo in valid_combinations:
        combo_yield = 0
        adjustment_factor = 1.0
        
        # Apply synergy bonus if all plots in combo have high moisture
        if all(p['moisture'] >= 0.6 for p in combo):
            adjustment_factor *= 1.15
        
        # Penalize if any plot has low soil quality
        if any(p['soil_quality'] < optimal_soil_threshold for p in combo):
            adjustment_factor *= 0.9
        
        # Compute base yields and apply adjustment
        for plot in combo:
            raw_yield = compute_base_yield(plot)
            combo_yield += raw_yield * adjustment_factor
        
        if combo_yield > best_yield:
            best_yield = combo_yield
    
    # Additional irrelevant post-processing (distractor)
    smoothed_yield = best_yield * 0.98  # hypothetical equipment loss
    reported_yield = round(smoothed_yield, 2)
    
    # Final adjustment based on government subsidy rule (not actually changing result)
    if best_yield > 100:
        compliance_tax = best_yield * 0.02
        net_return = best_yield - compliance_tax
    
    # But we still return the unadjusted best_yield (key insight)
    return best_yield

# Misleading initialization
initial_estimate = sum(compute_base_yield(plot) for plot in land_plots)
baseline_selection = [p for p in land_plots if p['soil_quality'] >= optimal_soil_threshold]

# Core execution point
temp_result = calculate_optimal_harvest(land_plots)
final_yield = temp_result

# Dead code path (distractor)
if __name__ == '__main__':
    debug_mode = False
    if debug_mode:
        print("Debug:", initial_estimate)

print(f"Result: {final_yield}")