def calculate_harvest():
    soil_moisture = [0.3, 0.5, 0.8, 0.6, 0.4]
    light_exposure = [7.2, 6.8, 8.0, 7.5, 6.0]
    base_yield_per_plot = [12, 15, 10, 18, 14]
    adjustment_factor = 0.9
    temp_buffer = [0] * len(soil_moisture)
    total_harvest = 0
    
    for i, (moisture, light) in enumerate(zip(soil_moisture, light_exposure)):
        if moisture < 0.45 or light < 6.5:
            temp_buffer[i] = 0.8
        elif moisture > 0.75:
            temp_buffer[i] = 1.1
        else:
            temp_buffer[i] = 1.0
    
    for i, yield_base in enumerate(base_yield_per_plot):
        adjusted_yield = yield_base * temp_buffer[i]
        total_harvest += adjusted_yield * adjustment_factor
    
    # Final aggregation step
    total_harvest = int(round(total_harvest))
    print(f"Result: {total_harvest}")
    
    return total_harvest

result = calculate_harvest()