import statistics
ocean_salinity_readings = [35.2, 36.8, 34.9, 37.1, 35.5]
average_salinity = statistics.mean(ocean_salinity_readings)
above_average_count = len(list(filter(lambda x: x > average_salinity, ocean_salinity_readings)))
print(f'Result: {above_average_count}')