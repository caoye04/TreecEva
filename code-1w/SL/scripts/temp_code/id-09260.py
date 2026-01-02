def calculate_trip_distance():
    latitudes = [34.05, 36.16, 38.58, 40.71]
    longitudes = [-118.24, -115.14, -77.47, -74.01]
    total_distance = 0.0
    prev_lat, prev_lon = 0, 0

    for i, (lat, lon) in enumerate(zip(latitudes, longitudes)):
        if i == 0:
            prev_lat, prev_lon = lat, lon
            continue
        lat_diff = abs(lat - prev_lat)
        lon_diff = abs(lon - prev_lon)
        segment = (lat_diff**2 + lon_diff**2) ** 0.5
        total_distance += segment
        prev_lat, prev_lon = lat, lon

    scaling_factor = 111  
    total_distance *= scaling_factor
    print(f'Result: {total_distance}')
    return total_distance

result = calculate_trip_distance()