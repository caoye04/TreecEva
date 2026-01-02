from itertools import compress

def calculate_efficiency(logs):
    # Extract performance flags and values
    thresholds = [85, 90, 75, 95, 80]
    readings = [88, 92, 70, 96, 82]
    
    # Determine valid performances
    success_mask = [reading >= threshold for reading, threshold in zip(readings, thresholds)]
    
    # Use list comprehension to get high-performance values
    high_performers = [x for x in compress(readings, success_mask)]
    
    # Irrelevant distraction: unused variable
    baseline_average = sum(thresholds) / len(thresholds)
    
    # Compute efficiency score using lambda
    scaler = lambda val: val * 1.1 if val > 90 else val * 1.05
    adjusted = sum(scaler(value) for value in high_performers)
    
    return int(adjusted)

# Main data input
metrics = {'system_id': 'X7', 'readings': [88, 92, 70, 96, 82], 'version': 2.1}

# Critical computation point
energy_output = calculate_efficiency(metrics)

print(f"Result: {energy_output}")