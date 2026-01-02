from itertools import combinations

# Sensor readings from two environmental monitoring stations
east_station_data = {12, 15, 18, 21, 24, 27, 30, 33}
west_station_data = {18, 21, 24, 27, 33, 36, 39}

# Find overlapping valid measurements between stations
common_elements = east_station_data.intersection(west_station_data)

# Irrelevant distraction: generate pairs (not used in final computation)
distinct_pairs = list(combinations(east_station_data, 2))

total_sensors_east = len(east_station_data)
total_sensors_west = len(west_station_data)

# Final computation
result = sum(common_elements)
print(f"Target result: {result}")