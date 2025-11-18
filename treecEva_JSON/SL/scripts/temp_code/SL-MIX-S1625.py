import math
import itertools

# Sensor readings from distributed network
sensor_readings = [12.5, 8.3, 15.7, 6.2, 22.1]

# Calculate pairwise signal ratios using list comprehension
signal_ratios = [
    reading1 / reading2 
    for reading1, reading2 in itertools.combinations(sensor_readings, 2)
    if reading2 != 0
]

# Apply logarithmic transformation with ternary operator for error handling
log_ratios = [
    math.log(ratio) if ratio > 0 else 0 
    for ratio in signal_ratios
]

# Weight factor based on number of valid readings
weight_factor = len([r for r in sensor_readings if r > 0])

# Compute entropy contribution using lambda function
entropy_func = lambda x: -x * math.log(x) if x > 0 else 0
entropy_components = [entropy_func(r/sum(log_ratios)) for r in log_ratios if sum(log_ratios) != 0]

# Final signal entropy index calculation
signal_entropy_index = weight_factor * sum(entropy_components) if entropy_components else 0

print(f"Result: {round(signal_entropy_index, 6)}")