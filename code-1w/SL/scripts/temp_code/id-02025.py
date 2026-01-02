import itertools

# Agricultural yield simulation with environmental adjustments
soil_quality = {'loam': 0.8, 'clay': 0.5, 'sand': 0.3}
crop_data = {
    'wheat': {
        'base_yield': 3.2,
        'nutrient_req': 0.7,
        'water_optimal': 600,
        'yield': 0
    },
    'corn': {
        'base_yield': 4.1,
        'nutrient_req': 0.9,
        'water_optimal': 750,
        'yield': 0
    }
}

# Simulate growth cycles over multiple plots
plots = ['plot_A', 'plot_B', 'plot_C']
weather_factors = [0.95, 1.02, 0.88]
soil_types = ['loam', 'clay', 'sand']

# Initialize tracking variables (some are distractions)
total_irrigation = 0
unused_metric = 0
simulation_cycles = 0

for plot, weather in itertools.product(plots, repeat=2):
    # Misleading counter that doesn't affect final result
    unused_metric += len(plot) * 2

    # Select soil type based on plot index (cyclic)
    soil_idx = ord(plot[-1]) % 3
    soil_type = soil_types[soil_idx]
    base_soil_factor = soil_quality[soil_type]

    # Water availability varies by iteration
    water_avail = 580 + (ord(plot[0]) % 40)

    # Calculate wheat yield with multiple adjustment factors
    water_ratio = min(water_avail / crop_data['wheat']['water_optimal'], 1.1)
    nutrient_factor = 0.85  # Simulated fertilizer application

    # Primary yield calculation
    raw_yield = crop_data['wheat']['base_yield'] * base_soil_factor * weather
    intermediate_yield = raw_yield * water_ratio * nutrient_factor

    # Additional adjustment for growth cycle
    if simulation_cycles % 3 == 0:
        intermediate_yield *= 1.05

    # Assign back to crop data (only last assignment matters due to loop)
    crop_data['wheat']['yield'] = intermediate_yield

    # Update other tracking variables (distractions)
    total_irrigation += water_avail
    simulation_cycles += 1

    # Dead code path - never executed but adds cognitive load
    if False:
        crop_data['corn']['yield'] = 0.0

# Final adjustment factor based on market conditions (independent of loop)
economic_index = 1.1
market_volatility = 0.05
trend_factor = economic_index - market_volatility
adjustment_factor = trend_factor * 0.9

# Critical statement: final yield computation
final_yield = crop_data['wheat']['yield'] * adjustment_factor

# Print result for evaluation
print(f"Result: {final_yield}")