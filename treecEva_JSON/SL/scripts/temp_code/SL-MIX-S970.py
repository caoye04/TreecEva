import itertools
import math

def compute_signal_coherence(readings):
    valid_readings = [r for r in readings if r > 0 and not math.isnan(r)]
    
    if not valid_readings or len(valid_readings) < 3:
        return 0
    
    # Apply logarithmic transformation
    log_values = [math.log(x) for x in valid_readings if x > 1]
    
    # Early return if insufficient data after transformation
    if len(log_values) < 2:
        return -1
    
    # Compute pairwise products using itertools
    pairwise_products = []
    for a, b in itertools.combinations(log_values, 2):
        product = a * b
        if product > 0:  # Short-circuit evaluation
            pairwise_products.append(product)
    
    if not pairwise_products:
        return -2
    
    # Calculate metric using lambda function
    transform = lambda x: x ** 1.5 if x > 1 else x * 2
    transformed_values = [transform(p) for p in pairwise_products]
    
    # Compute final metric
    final_metric = sum(transformed_values) / len(transformed_values)
    return final_metric

# Sensor readings with some invalid values
sensor_data = [2.7, 3.5, -1.2, 0, 4.8, float('nan'), 5.1, 1.5, 6.2]
final_metric = compute_signal_coherence(sensor_data)
print(f'Result: {final_metric}')