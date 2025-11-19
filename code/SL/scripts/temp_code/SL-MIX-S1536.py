import itertools
import statistics

def process_sensor_data(readings):
    valid_readings = [x for x in readings if 0 <= x <= 100]
    if len(valid_readings) < 3:
        return 0
    
    # Compute base metric as mean of valid readings
    base_metric = statistics.mean(valid_readings)
    
    # Generate all combinations of 3 readings
    combinations = list(itertools.combinations(valid_readings, 3))
    
    # Find combination that minimizes variance
    min_variance = float('inf')
    optimal_combo = None
    
    for combo in combinations:
        var = statistics.variance(combo)
        if var < min_variance:
            min_variance = var
            optimal_combo = combo
    
    # Calculate optimized metric
    if optimal_combo:
        optimized_metric = base_metric * (1 + 1/(1 + min_variance))
    else:
        optimized_metric = base_metric
        
    return optimized_metric

# Sensor readings with some outliers
sensor_readings = [12, 45, 67, 23, 89, 102, -5, 56, 78, 34, 91, 12]

# Process the data
optimized_metric = process_sensor_data(sensor_readings)
print(f"Result: {round(optimized_metric, 2)}")