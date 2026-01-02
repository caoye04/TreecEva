def calculate_harvest(yields, moisture_levels):
    total_harvest = 0
    adjustment_factor = 1.0
    
    for i, yield_val in enumerate(yields):
        moisture = moisture_levels[i]
        
        if moisture < 12:
            adjustment_factor = 0.8
        elif moisture > 18:
            adjustment_factor = 0.6
        else:
            adjustment_factor = 1.0
        
        adjusted_yield = yield_val * adjustment_factor
        total_harvest += adjusted_yield
        
        # Early exit if optimal conditions met
        if adjusted_yield >= 95 and moisture == 15:
            break
            
    return total_harvest

# Input data
crop_yields = [80, 94, 96, 88]
soil_moisture = [10, 16, 15, 20]

result = calculate_harvest(crop_yields, soil_moisture)
print(f"Result: {result}")