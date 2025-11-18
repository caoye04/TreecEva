from functools import reduce

# Sensor readings from 3 different sensors
sensor_readings = [
    [12, -5, 8, -3, 17],
    [4, 9, -2, 15, -7],
    [-6, 11, 3, -9, 13]
]

# Initialize stability index
stability_index = 0

# Process each sensor's readings
for readings in sensor_readings:
    # Apply modular transformation to each reading (mod 10)
    mod_readings = list(map(lambda x: x % 10, readings))
    
    # Filter out zero values
    filtered_readings = list(filter(lambda x: x != 0, mod_readings))
    
    # If no readings remain after filtering, skip this sensor
    if not filtered_readings:
        continue
    
    # Create a set of unique readings and a frozenset for comparison
    unique_readings = set(filtered_readings)
    frozen_readings = frozenset(filtered_readings)
    
    # Check if the set and frozenset have the same number of elements
    if len(unique_readings) == len(frozen_readings):
        # Calculate product of unique readings using reduce
        product = reduce(lambda a, b: a * b, unique_readings, 1)
        
        # Apply modular arithmetic (mod 7) to the product
        mod_product = product % 7
        
        # Update stability index with the modular product
        stability_index += mod_product
    else:
        # If duplicate elements exist, break out of the loop
        break

# Apply final adjustment to stability index
stability_index = (stability_index * 3) - 2

print(f"Result: {stability_index}")