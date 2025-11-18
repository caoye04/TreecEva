import bisect

# Sensor positions along migration route (sorted)
migration_sensors = [12, 28, 34, 47, 59, 63, 78, 85, 91, 104]

# Bird resting point of interest
resting_point = 50

def find_closest_sensor(sensors, target):
    # Binary search for insertion point
    pos = bisect.bisect_left(sensors, target)
    
    # Check edge cases
    if pos == 0:
        return sensors[0]
    if pos == len(sensors):
        return sensors[-1]
    
    # Compare distances to adjacent sensors
    left_sensor = sensors[pos - 1]
    right_sensor = sensors[pos]
    
    if abs(target - left_sensor) <= abs(target - right_sensor):
        return left_sensor
    else:
        return right_sensor

# Find closest sensor to resting point
closest_sensor_position = find_closest_sensor(migration_sensors, resting_point)
print(f'Result: {closest_sensor_position}')