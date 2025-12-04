# Temperature monitoring for weather analysis
base_readings = [22.5, 18.3, 25.1, 16.8, 20.7, 24.9]
max_temp = max(base_readings)
min_temp = min(base_readings)
final_temperature = round((max_temp + min_temp) / 2, 1)
print(f"Result: {final_temperature}")