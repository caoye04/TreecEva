import math
import re
from collections import defaultdict

def process_sensor_data(readings_batch):
    # Step 1: Apply logarithmic smoothing to all readings
    smoothed = [math.log(abs(temp) + 1) if temp != 0 else 0 for temp in readings_batch]
    
    # Step 2: Identify potential outliers using a ternary condition
    mean_val = sum(smoothed) / len(smoothed)
    deviations = [(val - mean_val) ** 2 for val in smoothed]
    std_dev = math.sqrt(sum(deviations) / len(deviations))
    
    # Step 3: Flag values that deviate by more than 1.5 standard deviations
    outlier_flags = [abs(val - mean_val) > 1.5 * std_dev for val in smoothed]
    
    # Step 4: Pattern matching for specific temperature signatures
    signature_matches = [bool(re.match(r'^-?\d+\.\d{2,}$', str(temp))) for temp in readings_batch]
    
    # Step 5: Calculate anomaly score using logical operations and exponentiation
    base_score = sum([smoothed[i] ** 2 if outlier_flags[i] and signature_matches[i] else 0 for i in range(len(smoothed))])
    
    # Step 6: Apply corrective factor using a ternary operator
    correction_factor = 1.2 if base_score > 10 else 0.8
    
    # Step 7: Final anomaly score calculation
    anomaly_score = round(base_score * correction_factor, 2) if base_score > 0 else 0
    
    return anomaly_score

# Sensor readings from a monitoring station
sensor_readings = [23.45, -15.67, 0, 120.89, -98.77, 24.12, 25.00, -22.33]

# Execute processing pipeline
anomaly_score = process_sensor_data(sensor_readings)
print(f"Result: {anomaly_score}")