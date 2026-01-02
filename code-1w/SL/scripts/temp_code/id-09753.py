def compute_neural_activation(inputs):
    weights = [0.5, -1.2, 0.8, -0.3, 1.0]
    bias = 0.25
    
    # Compute weighted sum using list comprehension
    weighted_inputs = [inp * w for inp, w in zip(inputs, weights)]
    pre_activation = sum(weighted_inputs) + bias
    
    # Apply sigmoid-like activation
    activation = 1 / (1 + 2.718 ** (-pre_activation))
    
    return round(activation, 3)

# Simulate batch input from sensors
sensor_readings = [(1.0, 0.5, 0.8, 1.2, 0.9), (0.4, 0.7, 0.6, 0.5, 1.1), (1.3, 0.2, 0.9, 0.8, 0.6)]

# Process each reading tuple
activation_levels = [compute_neural_activation(reading) for reading in sensor_readings]

# Scaling factor based on safety margin
scaling_factor = 0.85

# Critical assignment point
energy_threshold = max(activation_levels) * scaling_factor

# Irrelevant debug variable (minimal distraction)
dummy_test = len(sensor_readings) > 0

print(f"Result: {energy_threshold}")