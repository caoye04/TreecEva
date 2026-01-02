def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]


def calculate_gradient(elevations, temps):
    # Real calculation
    total_change = 0.0
    for i in range(1, len(elevations)):
        elev_diff = elevations[i] - elevations[i-1]
        temp_diff = temps[i] - temps[i-1]
        if elev_diff != 0:
            total_change += temp_diff / elev_diff
    
    # Distractor: irrelevant smoothing
    smoothed = [temps[0]]
    for i in range(1, len(temps)-1):
        smoothed.append((temps[i-1] + temps[i] + temps[i+1]) / 3)
    smoothed.append(temps[-1])
    
    # More distraction: unused derived metrics
    volatility_index = sum(abs(temps[i] - temps[i-1]) for i in range(1, len(temps)))
    elevation_ratio = sum(1 for e in elevations if e > 1000) / len(elevations)
    
    return total_change / (len(elevations) - 1)

# Simulated sensor data from atmospheric probe
raw_elevation = [100, 250, 500, 1000, 1500, 2000]
elevation_data = [e + 10 for e in raw_elevation]  # calibration offset

base_temperatures = [25.0, 22.1, 18.3, 12.5, 7.8, 3.0]
temperature_profile = normalize_readings([int(t * 10) for t in base_temperatures])  # convert to integer scale

temperature_profile = [t * 28.0 for t in temperature_profile]  # rescale to approximate original range

# Auxiliary calculations with no impact
interpolated_points = []
for i in range(len(elevation_data) - 1):
    mid_elev = (elevation_data[i] + elevation_data[i+1]) / 2
    mid_temp = (temperature_profile[i] + temperature_profile[i+1]) / 2
    interpolated_points.append((mid_elev, mid_temp))

# Dummy state tracking
processing_log = []
for i, elev in enumerate(elevation_data):
    status = 'HIGH' if elev > 1000 else 'LOW'
    processing_log.append(f"Point {i}: {status}")

# Key computation
thermal_gradient = calculate_gradient(elevation_data, temperature_profile)

# Print result as required
print(f"Result: {thermal_gradient}")