import math
from collections import defaultdict

def process_sensor_data():
    # Simulated sensor readings (in Celsius)
    raw_readings = [23.5, 19.2, 25.8, 21.0, 27.3]
    
    # State machine for processing phases
    state = 'INIT'
    calibration_factors = {}
    adjusted_values = []
    
    # Phase 1: Compute calibration factors using logarithms
    if state == 'INIT':
        for i, temp in enumerate(raw_readings):
            # Logarithmic calibration factor based on sensor position
            calibration_factors[i] = math.log(temp + 10)  # Avoid log(0)
        state = 'CALIBRATED'
    
    # Phase 2: Apply calibration and exponential adjustment
    if state == 'CALIBRATED':
        for i, temp in enumerate(raw_readings):
            # Apply calibration and exponential boost
            adjusted_temp = temp * calibration_factors[i] + math.exp(i * 0.1)
            adjusted_values.append(adjusted_temp)
        state = 'ADJUSTED'
    
    # Phase 3: Sort using greedy selection (largest first)
    sorted_values = []
    temp_copy = adjusted_values[:]
    
    while temp_copy:
        max_val = max(temp_copy)
        sorted_values.append(max_val)
        temp_copy.remove(max_val)
    
    # Phase 4: Calculate final adjustment using nested loop accumulation
    final_adjustment = 0.0
    for i in range(len(sorted_values)):
        inner_sum = 0.0
        for j in range(i+1):
            inner_sum += sorted_values[j] * (0.9 ** j)  # Exponential decay weight
        final_adjustment += inner_sum
    
    return final_adjustment

# Execute processing
final_adjustment = process_sensor_data()
print(f"Result: {final_adjustment}")