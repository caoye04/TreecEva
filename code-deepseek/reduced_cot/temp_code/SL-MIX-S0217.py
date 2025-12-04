sensor_readings = [3, 7, 4, 9, 2, 6]
base_temperature = 20
temperature_adjustments = [adjust * 2 if adjust > 5 else adjust for adjust in sensor_readings]
final_temperature = base_temperature + sum(temperature_adjustments)
print(f"Result: {final_temperature}")