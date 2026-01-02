from itertools import compress

def calculate_performance(base, data):
    # Normalize readings relative to base
    normalized = [round((val - base) / base * 100, 2) for val in data]
    
    # Determine which readings are above threshold
    above_threshold = [val > 5.0 for val in normalized]
    
    # Use itertools.compress to extract performance outliers
    outliers = list(compress(normalized, above_threshold))
    
    # Compute final score as sum of outlier improvements
    return int(sum(outliers))

# Baseline calibration value
baseline = 74.0

# Sensor readings from performance test
readings = [78.5, 72.3, 80.1, 73.8, 76.2, 82.0, 70.5, 77.4]

# Irrelevant auxiliary variable (minimal distraction)
temp_log = 'calibration_complete'

final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")