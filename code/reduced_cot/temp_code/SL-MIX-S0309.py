import math
from collections import defaultdict

# Sensor readings: each sublist represents readings from one sensor
sensor_readings = [
    [12, 28, 35, 42],
    [7, 15, 23, 31],
    [5, 18, 29, 38]
]

# Initialize a dictionary to store transformed readings
transformed_signals = defaultdict(list)

# Process each sensor's readings
for sensor_id, readings in enumerate(sensor_readings):
    for reading in readings:
        # Apply modular arithmetic with a prime base
        mod_value = (reading ** 2) % 17
        
        # Apply logarithmic transformation if mod_value is non-zero
        if mod_value > 0:
            log_value = math.log(mod_value)
            # Apply exponential transformation
            exp_value = math.exp(log_value / 2)
            transformed_signals[sensor_id].append(exp_value)
        else:
            transformed_signals[sensor_id].append(0)

# Calculate aggregate signal strength
aggregate_signal_strength = 0
for sensor_id, signals in transformed_signals.items():
    # Apply nested loops to compute pairwise products
    for i in range(len(signals)):
        for j in range(i+1, len(signals)):
            product = signals[i] * signals[j]
            # Conditional branch based on product value
            if product > 10:
                aggregate_signal_strength += product * 0.5
            else:
                aggregate_signal_strength += product * 0.1

# Final adjustment using modular arithmetic
aggregate_signal_strength = int(aggregate_signal_strength) % 100

print(f"Result: {aggregate_signal_strength}")