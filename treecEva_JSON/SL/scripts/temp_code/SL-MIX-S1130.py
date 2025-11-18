import itertools

temperature_readings = [
    [23.5, 24.0, 22.8, 23.9],
    [25.1, 24.7, 25.3, 24.9],
    [22.0, 21.5, 22.3, 21.9]
]

calibration_factor = 1.02
calibrate = lambda x: x * calibration_factor

adjusted_readings = [
    list(map(calibrate, station)) 
    for station in temperature_readings
]

station_averages = [
    sum(reading_group) / len(reading_group)
    for reading_group in adjusted_readings
]

first_station_average = station_averages[0]

print(f"Result: {first_station_average}")