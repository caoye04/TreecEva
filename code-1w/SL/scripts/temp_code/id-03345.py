def simulate_agricultural_cycle():
    # Environmental constants
    base_rainfall = 120
    temperature_factor = 0.88
    soil_quality_index = 92

    # Crop parameters
    crop_types = ['wheat', 'barley', 'oats']
    planting_density = {
        'wheat': 250,
        'barley': 200,
        'oats': 180
    }
    
    # Simulated growth stages (days)
    germination_days = {
        'wheat': 12,
        'barley': 14,
        'oats': 10
    }

    # Distractor: unused pest resistance data
    pest_resistance_levels = {
        'wheat': 0.76,
        'barley': 0.81,
        'oats': 0.69
    }

    # Field layout and area calculations
    field_dimensions = [(15, 20), (10, 30), (25, 12)]
    total_area = sum([length * width for length, width in field_dimensions])

    # Intermediate efficiency modifiers
    irrigation_efficiency = 0.93
    sunlight_exposure_ratio = 0.97

    # Distractor: dummy function that's defined but not used
    def calculate_pest_spread_rate(risk_factor):
        return risk_factor * 0.3 + 0.1

    # Growth modifier based on environmental factors
    growth_multiplier = (base_rainfall / 100) * temperature_factor * (soil_quality_index / 100)

    # Yield accumulator
    cumulative_yield = 0
    yield_contributions = []

    # Lambda for dynamic adjustment
    adjust_for_conditions = lambda base, days: base * (1 + 0.01 * (21 - days))

    for crop in crop_types:
        density = planting_density[crop]
        days_to_germinate = germination_days[crop]
        
        # Apply adjustment function
        adjusted_density = adjust_for_conditions(density, days_to_germinate)
        
        # Calculate potential yield per hectare
        raw_yield = adjusted_density * growth_multiplier
        
        # Efficiency losses
        harvesting_loss_rate = 0.05
        effective_yield = raw_yield * (1 - harvesting_loss_rate)
        
        # Accumulate
        cumulative_yield += effective_yield
        yield_contributions.append(effective_yield)

    # Distractor: irrelevant cost calculation
    fertilizer_cost_per_hectare = 150
    total_fertilizer_budget = fertilizer_cost_per_hectare * len(crop_types)

    # Final harvest efficiency calculation
    total_possible_yield = sum([planting_density[c] * growth_multiplier for c in crop_types])
    actual_total_yield = cumulative_yield
    
    # Key result variable
    final_yield = actual_total_yield * irrigation_efficiency * sunlight_exposure_ratio

    # Print target result
    print(f"Result: {final_yield}")

    return final_yield

# Execute simulation
simulate_agricultural_cycle()