def calculate_temperature():
    readings = [23.5, 19.0, 27.3, 22.1, 18.9, 30.2, 25.4]
    filtered_readings = [temp for temp in readings if temp >= 20.0]
    total = sum(filtered_readings)
    count = len(filtered_readings)
    average = total / count
    adjustment_factor = 1.1 if average > 25 else 0.9
    adjusted_avg = average * adjustment_factor
    season = 'summer'
    is_summer = season == 'summer' or season == 'autumn'
    final_temperature = adjusted_avg + (2 if is_summer else -1)
    status = 'stable' if final_temperature > 24 else 'variable'
    outlier_count = sum(1 for t in readings if t < 19.5)
    return final_temperature
result = calculate_temperature()
print(f"Target result: {result}")