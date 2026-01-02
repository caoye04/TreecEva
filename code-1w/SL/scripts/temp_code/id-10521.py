def analyze_agricultural_output(temperature_data, rainfall_data, threshold=25):
    # Initialize key variables
    baseline_yield = 4200
    stress_days = 0
    total_rainfall = sum(rainfall_data)
    cumulative_heat = 0
    heat_wave_count = 0
    temp_anomalies = []

    # Analyze daily temperature for crop stress
    for temp in temperature_data:
        cumulative_heat += temp
        if temp > threshold:
            stress_days += 1
            temp_anomalies.append(temp)
        if temp > threshold + 5:
            heat_wave_count += 1

    # Compute derived metrics (some used, some not)
    average_temperature = cumulative_heat / len(temperature_data)
    drought_severity = stress_days * 3.5
    yield_reduction_estimate = stress_days * 8.2

    # Simulate sensor noise (irrelevant to final result)
    calibration_offset = 0.0
    for i in range(3):
        calibration_offset += 0.1 * (i % 2)

    # Rainfall efficiency calculation (semi-relevant)
    effective_rainfall = 0.0
    for rain in rainfall_data:
        if rain > 0:
            effective_rainfall += rain * 0.9 if rain < 10 else rain * 0.6
n
    # Determine forecast stability using set logic and slicing
    recent_temps = temperature_data[-7:]
    recent_rains = rainfall_data[-7:]
    high_variability = set(recent_temps) & {t for t in recent_temps if abs(t - average_temperature) > 8}
    forecast_stable = len(high_variability) < 3 and max(recent_rains) < 50

    # Crop production model with conditional expression
    base_production = baseline_yield - yield_reduction_estimate
    supplemental_irrigation = True if total_rainfall > 200 else False
    crop_production = base_production * 1.15 if supplemental_irrigation else base_production * 0.88

    # Adjustment factor based on multiple conditions
    adjustment_factor = 1.0
    if stress_days == 0:
        adjustment_factor = 1.2
    elif stress_days < 5:
        adjustment_factor = 1.05
    else:
        adjustment_factor = 0.8 - (stress_days * 0.02)

    # Final yield determination at critical execution point
    final_yield = crop_production * adjustment_factor if forecast_stable else baseline_yield

    # Dead code path - irrelevant logging simulation
    debug_mode = False
    if debug_mode:
        print(f'Stress days: {stress_days}, Anomalies: {len(temp_anomalies)}')
        print(f'Calibration offset: {calibration_offset}')

    print(f'Result: {final_yield}')
    return final_yield

# Input data
temps = [22, 24, 26, 28, 27, 30, 33, 25, 23, 24, 26, 29, 31, 32, 28]
rains = [5, 12, 0, 8, 15, 3, 0, 20, 25, 18, 50, 55, 40, 10, 0]
analyze_agricultural_output(temps, rains)