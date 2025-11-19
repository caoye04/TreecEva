from collections import deque
from functools import reduce
from dataclasses import dataclass

def process_sensor_data():
    # Initialize sensor readings queue
    sensor_readings = deque([15, 28, 42, 9, 33])
    
    # Processing Node 1: Apply threshold and transform
    threshold = 25
    transformed = []
    while sensor_readings:
        reading = sensor_readings.popleft()
        adjusted = reading * 2 if reading > threshold else reading + 5
        transformed.append(adjusted)
    
    # Processing Node 2: Bitwise operations with accumulator
    @dataclass
    class Accumulator:
        value: int = 0
        
        def update(self, x):
            self.value = (self.value & x) | (self.value ^ x)
    
    acc = Accumulator()
    for val in transformed:
        acc.update(val)
    
    # Processing Node 3: Conditional aggregation
    high_values = list(filter(lambda x: x > 30, transformed))
    low_values = list(filter(lambda x: x <= 30, transformed))
    
    aggregate_high = reduce(lambda a, b: a + b, high_values, 0) if high_values else 0
    aggregate_low = reduce(lambda a, b: a * b, low_values, 1) if low_values else 1
    
    # Final computation with ternary operator
    final_output = aggregate_high if len(high_values) > len(low_values) else aggregate_low
    
    return final_output

# Execute the pipeline
final_output = process_sensor_data()
print(f'Result: {final_output}')