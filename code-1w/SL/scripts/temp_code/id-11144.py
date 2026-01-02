readings = [23.5, 24.1, 22.8, 25.0, 23.9]
valid_readings = [temp for temp in readings if 20 <= temp <= 30]
average_temp = sum(valid_readings) / len(valid_readings)
adjusted_readings = {}
adjusted_readings['offset'] = average_temp - 0.5
adjusted_readings['final'] = adjusted_readings['offset'] * 1.02
scale = 'Celsius'
conversion_factor = 1.8
final_temperature = adjusted_readings.get('final') * conversion_factor + (273.15 if scale == 'Celsius' else 459.67)
Result: final_temperature