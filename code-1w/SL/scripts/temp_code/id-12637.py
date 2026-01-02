def simulate_growth_cycle():
    # Environmental parameters
    base_temperature = 22.5
    rainfall_mm = 86
    daylight_hours = 14

    # Crop characteristics
    germination_rate = 0.88
    max_capacity = 5000
    stress_factor = 0.0

    # Simulate soil nutrient depletion over time
    nutrient_levels = [95, 87, 76, 68, 62, 55]
    avg_nutrients = sum(nutrient_levels) / len(nutrient_levels)
    depletion_penalty = (95 - avg_nutrients) * 0.01

    # Calculate photosynthesis efficiency
    photo_efficiency = min(1.0, (daylight_hours / 16) * (base_temperature / 25))
    
    # Irrelevant health metrics for neighboring crops (distractor)
    neighbor_crop_health = [0.7, 0.92, 0.68, 0.77]
    avg_neighbor_health = sum(neighbor_crop_health) / len(neighbor_crop_health)
    stability_score = avg_neighbor_health * 1.5  # Unused metric

    # Water stress calculation
    if rainfall_mm < 60:
        water_stress = 0.3
    elif rainfall_mm > 120:
        water_stress = 0.2
    else:
        water_stress = 0.05

    # Temperature stress check
    if base_temperature < 18 or base_temperature > 30:
        stress_factor += 0.15
    if abs(base_temperature - 22.5) < 2:
        stress_factor -= 0.05  # Optimal range bonus

    # Germination projection with environmental modifiers
    effective_germination = germination_rate * (1 - depletion_penalty) * (1 - water_stress)
    initial_plants = int(max_capacity * effective_germination)

    # Growth phase losses due to compounded stresses
    total_loss_factor = stress_factor + depletion_penalty + water_stress
    survival_rate = max(0.4, 1 - total_loss_factor)

    # Final yield calculation per plant
    base_yield_per_plant = 12.5
    yield_bonus = photo_efficiency * 0.3
    final_yield_per_plant = base_yield_per_plant * (1 + yield_bonus)

    # Compute total harvest
    total_harvest = initial_plants * final_yield_per_plant

    # Efficiency normalization against theoretical maximum
    theoretical_max = max_capacity * (base_yield_per_plant * 1.3)
    final_yield = (total_harvest / theoretical_max) * 100  # Percentage efficiency

    # Red herring: unused data transformation
    normalized_data = [x / 100 for x in nutrient_levels if x > 60]
    adjusted_scores = [round(x * final_yield, 2) for x in normalized_data]  # Not used

    return final_yield

# Entry point
final_yield = simulate_growth_cycle()
print(f"Target result: {final_yield}")