import math

# Simulate sensor data with noise and valid readings
def generate_sensor_data():
    raw_readings = [12.5, 13.0, 11.8, 14.2, 9.5, 10.0, 13.7]
    timestamps = [1, 2, 3, 4, 5, 6, 7]
    return list(zip(raw_readings, timestamps))

# Filter out low-confidence readings below threshold
def filter_noisy_readings(data, threshold=10.0):
    filtered = [x[0] for x in data if x[0] >= threshold]
    return filtered

# Apply calibration factor using lambda
linear_calibrate = lambda val, f: round(val * f, 2)

def preprocess_readings(readings):
    calibrated = [linear_calibrate(r, 1.03) for r in readings]
    sorted_vals = sorted(calibrated, reverse=True)
    top_three_avg = sum(sorted_vals[:3]) / 3
    
    # Distractor: unused statistical measures
    squared_devs = [(x - top_three_avg)**2 for x in calibrated]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    entropy_proxy = -sum([math.log(x) for x in calibrated if x > 1])
    
    return {
        'calibrated': calibrated,
        'top_three_avg': top_three_avg,
        'diagnostics': {
            'variance': variance_estimate,
            'entropy': entropy_proxy
        }
    }

# Determine stability class based on range
def classify_stability(values):
    if not values:
        return 'UNSTABLE'
    data_range = max(values) - min(values)
    return 'STABLE' if data_range < 3.0 else 'FLUCTUATING'

# Main calculation with conditional logic and early exit
def calculate_final_score(processed_data):
    base_score = processed_data['top_three_avg'] * 10
    stability_flag = classify_stability(processed_data['calibrated'])
    
    # Irrelevant transformation chain (distractor)
    temp_str = ''.join([chr(int(x) % 26 + 97) for x in processed_data['calibrated'][:4]])
    hash_val = sum([ord(c) for c in temp_str])
    decoy_score = hash_val * 0.7
    
    if stability_flag == 'UNSTABLE':
        return 0
    elif stability_flag == 'STABLE':
        adjustment = 5
    else:
        adjustment = -2
    
    # Multiple contributing factors
    outlier_count = len([x for x in processed_data['calibrated'] if x > 13.5])
    penalty = outlier_count * 1.5
    
    final = base_score + adjustment - penalty
    
    # Early return based on threshold
    if final > 130:
        final = 130  # cap score
    
    return round(final, 2)

# Execution flow
sensor_data = generate_sensor_data()
filtered_data = filter_noisy_readings(sensor_data)
processed_data = preprocess_readings(filtered_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")