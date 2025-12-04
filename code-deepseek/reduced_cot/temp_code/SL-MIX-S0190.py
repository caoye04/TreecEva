def analyze_climate_data(readings_dict, base_temp):
    temp_deviations = [reading - base_temp for reading in readings_dict.values()]
    seasonal_pattern = {city: temp * 1.05 for city, temp in readings_dict.items()}
    deviation_sum = sum(temp_deviations)
    count_dev = len(temp_deviations)
    irrelevant_calc = deviation_sum * 0.1
    filtered_deviations = [dev for dev in temp_deviations if dev > 0]
    avg_deviation = sum(filtered_deviations) / len(filtered_deviations) if filtered_deviations else 0
    seasonal_adjust = sum(seasonal_pattern.values()) / len(seasonal_pattern)
    adjusted_trend = avg_deviation + (seasonal_adjust - base_temp) * 0.8
    return round(adjusted_trend, 2)

city_readings = {'Tokyo': 18.5, 'London': 12.3, 'Sydney': 22.1, 'Moscow': 8.7, 'Rio': 26.4}
baseline_temp = 15.0
climate_coefficient = 1.2
redundant_metric = sum([temp * 0.5 for temp in city_readings.values()])

# Main execution point
seasonal_factor = climate_coefficient * 0.9
temperature_trend = analyze_climate_data(city_readings, baseline_temp)
regional_variance = redundant_metric - baseline_temp

print(f"Target result: {temperature_trend}")