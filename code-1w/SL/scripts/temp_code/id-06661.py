def analyze_crop_performance():
    # Simulated agricultural data
    base_yield_per_acre = 120
    soil_quality_index = [0.85, 0.92, 0.78, 0.95, 0.88]
    rainfall_mm = [88, 95, 76, 105, 91]
    temperature_celsius = [22, 24, 21, 25, 23]

    # Irrelevant processing: climate trend analysis (distractor)
    avg_temp = sum(temperature_celsius) / len(temperature_celsius)
    temp_deviation = [round(t - avg_temp, 2) for t in temperature_celsius]
    growth_potential = list(map(lambda x: round(x * 1.1, 1), soil_quality_index))

    # Real data: field productivity and irrigation
    field_ids = ['F1', 'F2', 'F3', 'F4', 'F5']
    field_area_acres = [45, 60, 30, 50, 40]
    irrigation_levels = [70, 85, 60, 90, 75]  # Percent coverage

    # Destructuring and enumeration usage
    field_data = []
    for i, fid in enumerate(field_ids):
        efficiency_factor = round(soil_quality_index[i] * (irrigation_levels[i] / 100), 3)
        adjusted_yield = base_yield_per_acre * efficiency_factor
        field_record = (fid, field_area_acres[i], adjusted_yield, rainfall_mm[i])
        field_data.append(field_record)

    # Helper function with nested logic
    def calculate_harvest_efficiency(fields, irrigation):
        total_production = 0
        total_efficiency_score = 0.0

        # Nested loop simulating micro-zones in each field (some dead complexity)
        for idx, record in enumerate(fields):
            field_id, area, yield_per_acre, rain = record
            zone_count = 0
            zone_yield_sum = 0.0

            # Simulate 3 sub-zones per field (artificial nesting)
            for z in range(1, 4):
                zone_rain_effect = 1 + (0.001 * (rain - 80))
                zone_irrigation_boost = irrigation[idx] / 100 + 0.1 * (z % 2)
                zone_efficiency = (yield_per_acre / base_yield_per_acre) * zone_irrigation_boost * zone_rain_effect
                zone_yield = base_yield_per_acre * zone_efficiency
                if z == 2:  # Only middle zone contributes (misleading condition)
                    zone_yield_sum += zone_yield
                    zone_count += 1

            # Actual contribution uses average of valid zones
            if zone_count > 0:
                avg_zone_yield = zone_yield_sum / zone_count
                total_production += avg_zone_yield * area

            # Accumulate efficiency score (not used in final answer - red herring)
            total_efficiency_score += sum([irrigation[idx], soil_quality_index[idx] * 100]) / 2

        # Final yield based on total production per total acre
        total_acres = sum([f[1] for f in fields])
        final_yield = total_production / total_acres
        return round(final_yield, 2)

    # Misleading intermediate calculation (dead end)
    projected_drought_loss = 0
    for r in rainfall_mm:
        if r < 80:
            projected_drought_loss += 5.5

    # Key statement
    final_yield = calculate_harvest_efficiency(field_data, irrigation_levels)
    
    # Print result as required
    print(f"Result: {final_yield}")
    
    return final_yield

# Execute
analyze_crop_performance()