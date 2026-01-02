def analyze_agricultural_output(land_plots, weather_data):
    base_yield_per_plot = 12.5
    stress_threshold = 70
    cumulative_rainfall = sum(weather_data)
    avg_temperature = sum([wd * 0.3 for wd in weather_data]) / len(weather_data) if weather_data else 0

    # Irrelevant climate metrics (distractor)
    wind_chill_factor = 0.5 * avg_temperature - 3.2
    humidity_index = (cumulative_rainfall / 100) * 1.8

    high_stress_count = 0
    total_viable_area = 0
    temp_analysis_log = []

    for plot in land_plots:
        elevation = plot['elevation']
        soil_quality = plot['soil']
        temperature_stress = plot.get('temp_stress', 0)

        # Simulate conditional viability
        if soil_quality >= 4 and elevation < 800:
            total_viable_area += plot['size']
            if temperature_stress > stress_threshold:
                high_stress_count += 1
            temp_analysis_log.append(elevation * 0.1)

    # Misleading intermediate calculation (not used in final result)
    theoretical_max_yield = total_viable_area * base_yield_per_plot * 1.2

    # Core logic: crop production depends on viable area and stress levels
    stress_penalty = 0.1 * high_stress_count
    crop_production = total_viable_area * base_yield_per_plot
    crop_production -= crop_production * stress_penalty

    # Resilience factor based on rainfall patterns (uses slicing)
    recent_rainfall = weather_data[-3:]  # last 3 days
    baseline_rainfall = weather_data[:len(weather_data)//2]  # first half
    if sum(recent_rainfall) > sum(baseline_rainfall) * 0.4:
        resilience_factor = 1.15
    else:
        resilience_factor = 0.9

    # Final yield computation (target line)
    final_yield = crop_production * resilience_factor

    # Dead code path (distractor)
    if wind_chill_factor < 0:
        final_yield *= 1.05

    # Unused diagnostic
    diagnostics = {
        'plots_analyzed': len(land_plots),
        'total_rainfall': cumulative_rainfall,
        'high_stress_zones': high_stress_count
    }

    print(f"Result: {final_yield}")
    return final_yield

# Input data
plots = [
    {'size': 10, 'elevation': 600, 'soil': 5, 'temp_stress': 75},
    {'size': 8, 'elevation': 850, 'soil': 3, 'temp_stress': 65},
    {'size': 12, 'elevation': 500, 'soil': 4, 'temp_stress': 80},
    {'size': 15, 'elevation': 700, 'soil': 5, 'temp_stress': 68}
]

weather = [10, 12, 8, 15, 20, 25, 18]

result = analyze_agricultural_output(plots, weather)