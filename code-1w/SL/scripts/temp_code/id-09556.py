def system_check(diagnostic_fn, readings):
    high_temp_count = 0
    for temp in readings:
        if diagnostic_fn(temp):
            high_temp_count += 1
    return high_temp_count

# Sensor readings in degrees Celsius
temperature_readings = [68, 72, 76, 81, 69, 77]
baseline_average = sum(temperature_readings) / len(temperature_readings)

# Secondary metric: deviation count
std_deviation = (sum((x - baseline_average) ** 2 for x in temperature_readings) / len(temperature_readings)) ** 0.5
deviation_count = sum(1 for x in temperature_readings if abs(x - baseline_average) > std_deviation)

# Key computation path
final_diagnostic = system_check(lambda x: x > 75, temperature_readings)
threshold_alert = final_diagnostic * 2 + deviation_count

Result: threshold_alert