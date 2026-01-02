import math

# Simulated sensor array data (temperature in Celsius)
sensor_data = [23.5, 19.0, 25.3, -1.2, 30.1, 18.7, 27.4, 22.0, 16.5, 35.6, 24.8, 20.3]

# Irrelevant auxiliary data (distractor)
aux_metadata = {
    'device_id': 'SENS-ALPHA-9',
    'firmware': 'v2.4.1',
    'calibration_offset': 0.07,
    'last_sync': '2023-10-05T14:22:10Z'
}

# Decoy transformation functions (dead code path)
def transform_legacy(data):
    return [round(x * 1.02 + 0.5, 2) for x in data if x > 0]

def apply_smoothing(data):  # Unused function
    smoothed = []
    for i in range(len(data)):
        neighbors = data[max(0, i-1):min(i+2, len(data))]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smoothed

# Real processing begins here
valid_range = (-5.0, 35.0)

# Filter out-of-range sensor readings
filtered_data = [x for x in sensor_data if valid_range[0] <= x <= valid_range[1]]

# Distractor: irrelevant statistical computation
mean_temp = sum(sensor_data) / len(sensor_data)
std_dev = (sum((x - mean_temp) ** 2 for x in sensor_data) / len(sensor_data)) ** 0.5
normalized = [(x - mean_temp) / std_dev for x in sensor_data]

# Threshold logic using lambda (required feature)
thresh_cold = 18.0
thresh_hot = 27.0
threshold_func = lambda t: 'CRITICAL' if t >= thresh_hot else ('WARNING' if t < thresh_cold else 'NORMAL')

# Bit manipulation red herring (irrelevant to final result)
status_code = 0
for reading in filtered_data:
    if reading > thresh_hot:
        status_code |= 1 << 1
    if reading < thresh_cold:
        status_code ^= 1 << 4

# Another decoy structure (unused)
temp_categories = {
    'cold': [t for t in filtered_data if t < thresh_cold],
    'moderate': [t for t in filtered_data if thresh_cold <= t < thresh_hot],
    'hot': [t for t in filtered_data if t >= thresh_hot]
}

# Real diagnostic processor
risk_weights = {'CRITICAL': 3.0, 'WARNING': 1.5, 'NORMAL': 0.1}

# Complex list comprehension with nested logic (required feature)
severity_scores = [
    risk_weights[threshold_func(temp)] * (1 + 0.1 * math.sin(i)) 
    for i, temp in enumerate(filtered_data)
]

# Misleading aggregation (intermediate distraction)
avg_severity = sum(severity_scores) / len(severity_scores)
total_impact = sum(s ** 1.1 for s in severity_scores if s > 1.0)

# Core logic hidden among distractions
def process_readings(readings, classifier):
    classified = [classifier(r) for r in readings]
    counts = {key: classified.count(key) for key in risk_weights.keys()}
    
    # Real answer calculation buried in complex formula
    base_score = counts['CRITICAL'] * 17.3
    base_score += counts['WARNING'] * 8.7
    base_score -= len([r for r in readings if 20 <= r <= 24]) * 1.2  # ideal range bonus
    
    # Additional red herring: recursive decoy (never called)
    def recursive_dampen(val, depth):
        if depth <= 0 or val < 1:
            return val
        return 0.9 * recursive_dampen(val, depth - 1)
    
    return int(round(base_score))

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_func)

# Print required output
print(f"Target result: {final_diagnostic}")