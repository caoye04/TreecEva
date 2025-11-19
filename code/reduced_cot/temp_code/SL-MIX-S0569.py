from functools import reduce
from contextlib import contextmanager
import math

def calculate_variance(values):
    if len(values) < 2:
        return 0
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / (len(values) - 1)

@contextmanager
def sensor_context(sensor_id):
    print(f"Initializing sensor {sensor_id}")
    try:
        yield sensor_id
    finally:
        print(f"Deactivating sensor {sensor_id}")

class TelemetryProcessor:
    def __init__(self):
        self.state = 'IDLE'
        self.readings_buffer = []
        self.valid_readings = []
    
    def process_reading(self, value):
        if self.state == 'IDLE':
            if value >= 0 and value <= 100:
                self.state = 'ACTIVE'
                self.readings_buffer.append(value)
        elif self.state == 'ACTIVE':
            if value < 0 or value > 100:
                self.state = 'ERROR'
            else:
                self.readings_buffer.append(value)
                if len(self.readings_buffer) >= 5:
                    self.valid_readings.extend(self.readings_buffer)
                    self.readings_buffer.clear()
        elif self.state == 'ERROR':
            if value >= 0 and value <= 100:
                self.state = 'ACTIVE'
                self.readings_buffer.append(value)
    
    def get_valid_readings(self):
        return self.valid_readings[:]

# Main processing
processor = TelemetryProcessor()
sensor_data = [23.5, 45.2, -5.0, 67.8, 89.1, 12.3, 105.0, 34.7, 56.9, 78.2, 25.0, 91.4]

with sensor_context('TEMP_01') as sensor:
    for reading in sensor_data:
        processor.process_reading(reading)
    
    valid_values = processor.get_valid_readings()
    processed_mean = sum(valid_values) / len(valid_values) if valid_values else 0
    
    # Apply transformation using functional programming
    transformed_values = list(map(lambda x: x * 1.8 + 32, filter(lambda x: x > processed_mean, valid_values)))
    
    # Calculate final statistics
    if len(transformed_values) > 1:
        processed_variance = calculate_variance(transformed_values)
    else:
        processed_variance = 0

print(f"Result: {processed_variance}")