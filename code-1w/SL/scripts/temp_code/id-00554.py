temperature_celsius = 37
humidity_percent = 35
temperature_fahrenheit = (temperature_celsius * 9/5) + 32
is_summer = True

temperature_status = temperature_fahrenheit > 98.6
humidity_level = humidity_percent if is_summer else max(humidity_percent - 10, 0)

# Key statement
threshold_flag = temperature_status and (humidity_level < 40)

# Additional but relevant logic to maintain context
dew_point_approx = temperature_celsius - ((100 - humidity_percent) / 5)
comfort_index = "High" if threshold_flag else "Moderate"

Result: threshold_flag