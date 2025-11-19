import math

class SensorDataManager:
    def __init__(self, base_coords):
        self.base_x, self.base_y = base_coords
        self.readings = []
    
    def add_sensor_data(self, offset_x, offset_y, measured_distance):
        sensor_x = self.base_x + offset_x
        sensor_y = self.base_y + offset_y
        # Using Pythagorean theorem to compute depth from horizontal distance and direct measurement
        horizontal_distance = math.sqrt(offset_x**2 + offset_y**2)
        if measured_distance > horizontal_distance:
            depth = math.sqrt(measured_distance**2 - horizontal_distance**2)
            self.readings.append(depth)
        else:
            self.readings.append(0.0)  # Invalid reading
    
    def get_average_depth(self):
        return sum(self.readings) / len(self.readings) if self.readings else 0.0

def process_vessel_survey():
    # Vessel's initial GPS coordinates (arbitrary units)
    vessel_position = (15.5, 22.8)
    
    # Context manager for data processing
    with SensorDataManager(vessel_position) as dm:
        pass  # Custom exit handling in __exit__
    
    # Manual creation since we need to access the object post-context
    dm = SensorDataManager(vessel_position)
    
    # Sensor deployment data: (offset_x, offset_y, measured_distance_to_seabed_point)
    sensor_deployments = [
        (-3.2, 4.7, 25.3),
        (5.1, -2.9, 30.7),
        (1.8, 6.4, 18.9),
        (-4.5, -3.3, 22.1)
    ]
    
    # List comprehension to filter valid deployments where measured distance > 20
    valid_deployments = [deployment for deployment in sensor_deployments if deployment[2] > 20]
    
    # Add valid sensor data
    for deployment in valid_deployments:
        dm.add_sensor_data(*deployment)
    
    # Generator expression to calculate squares of readings for variance computation (not used here but part of processing)
    _ = (reading**2 for reading in dm.readings)
    
    return dm.get_average_depth()

# Enable context manager protocol
SensorDataManager.__enter__ = lambda self: self
SensorDataManager.__exit__ = lambda self, *args: None

computed_average_depth = process_vessel_survey()
print(f"Result: {computed_average_depth}")