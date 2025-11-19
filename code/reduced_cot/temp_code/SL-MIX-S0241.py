import math
from statistics import variance
from functools import wraps

def track_processing_stats(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        wrapper.total_processed += len(result) if isinstance(result, list) else 1
        return result
    wrapper.call_count = 0
    wrapper.total_processed = 0
    return wrapper

class SensorDataValidator:
    def __enter__(self):
        self.valid_readings = []
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def add_reading(self, temp, humidity, pressure):
        # Data validation with early return
        if not (temp >= -50 and temp <= 60):
            return False
        if not (humidity >= 0 and humidity <= 100):
            return False
        if not (pressure >= 900 and pressure <= 1100):
            return False
        
        # Apply sensor correction factors
        corrected_temp = temp * (1 + humidity * 0.001) if humidity > 50 else temp * (1 - humidity * 0.0005)
        self.valid_readings.append(corrected_temp)
        return True

@track_processing_stats
def process_station_batch(station_data):
    with SensorDataValidator() as validator:
        for reading in station_data:
            temp, humidity, pressure = reading
            validator.add_reading(temp, humidity, pressure)
        return validator.valid_readings

# Sensor data from 3 monitoring stations
station_a_readings = [(25.3, 45.2, 1013.2), (26.1, 48.7, 1012.8), (24.8, 52.1, 1013.5)]
station_b_readings = [(22.7, 65.3, 1015.1), (23.4, 67.8, 1014.9), (21.9, 70.2, 1015.3)]
station_c_readings = [(27.8, 35.6, 1010.7), (28.2, 38.4, 1010.3), (26.9, 41.2, 1011.0)]

# Process all stations
processed_a = process_station_batch(station_a_readings)
processed_b = process_station_batch(station_b_readings)
processed_c = process_station_batch(station_c_readings)

# Combine all valid readings
all_valid_readings = processed_a + processed_b + processed_c

# Calculate spatial adjustment based on station positions
station_positions = [(0, 0), (3, 4), (6, 0)]  # Coordinates in km
adjusted_temperatures = []

for i, temp in enumerate(all_valid_readings):
    x, y = station_positions[i % len(station_positions)]
    distance_from_origin = math.sqrt(x**2 + y**2)
    
    # Apply spatial adjustment: temperature decreases 0.5°C per km from origin
    adjustment = distance_from_origin * 0.5
    adjusted_temp = temp - adjustment
    
    # Ternary operator for extreme value handling
    adjusted_temp = adjusted_temp if adjusted_temp > 0 else 0
    adjusted_temperatures.append(adjusted_temp)

# Calculate final spatial variance
final_temperature_variance = variance(adjusted_temperatures) if len(adjusted_temperatures) > 1 else 0

print(f"Result: {final_temperature_variance}")