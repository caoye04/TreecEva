def calculate_water_level(rainfall, evaporation):
    # Initialize tracking variables
    initial_level = 100  # Starting water level in reservoir
    water_level = initial_level
    historical_levels = []
    max_recorded = -float('inf')
    min_recorded = float('inf')
    
    # Process rainfall data
    for day, amount in rainfall.items():
        # Apply rainfall effect
        water_level += amount
        
        # Record historical data for analytics (not used in final calculation)
        historical_levels.append(water_level)
        max_recorded = max(max_recorded, water_level)
        min_recorded = min(min_recorded, water_level)
        
        # Apply daily evaporation
        daily_evaporation = amount * evaporation if amount > 0 else 5
        water_level -= daily_evaporation
        
        # Safety check - water level cannot go below 0
        water_level = max(0, water_level)
    
    # Calculate average level (not used in final result)
    avg_level = sum(historical_levels) / len(historical_levels) if historical_levels else 0
    
    # Apply seasonal adjustment factor
    season_factor = 0.8 if min_recorded < 50 else 1.2
    
    # Final water level calculation with conditional adjustment
    return water_level * (season_factor if max_recorded > 150 else 1.0)

# Rainfall data: {day: amount in mm}
rainfall_data = {
    'Monday': 25,
    'Tuesday': 0,
    'Wednesday': 15,
    'Thursday': 30,
    'Friday': 10
}

# Evaporation factor (fraction of rainfall that evaporates)
evaporation_factor = 0.4

# Calculate the final water level
final_water_level = calculate_water_level(rainfall_data, evaporation_factor)

# Some additional calculations that don't affect the result
water_surplus = final_water_level - 100
water_status = "Excess" if water_surplus > 0 else "Deficit"
conservation_needed = water_surplus < -20

print(f"Result: {final_water_level}")