import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.7, 25.3, 26.0, 24.8, 23.9]
humidity_readings = [45, 48, 50, 44, 47, 49, 51]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017]

# Irrelevant backup data (distractor)
backup_temperatures = [22.1, 23.0, 21.9]  
backup_humidity = [55, 53, 57]

# Weight configuration for data fusion (critical)
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'pressure': 0.2,
    'altitude': 0.1  # unused but looks relevant
}

# Decoy function - appears useful but not used in main logic
def calculate_average_raw(data_list):
    total = 0
    count = 0
    for item in data_list:
        total += item
        count += 1
    return total / count if count else 0

# Auxiliary transformation (red herring)
adjusted_humidity = []
for h in humidity_readings:
    adjusted_humidity.append(max(0, min(100, h + 2)))  # clamped adjustment

# Fake anomaly detection (dead code path)
anomalies_detected = False
critical_thresholds = {'temp_high': 30, 'humid_high': 80}
for t in temperature_readings:
    if t > critical_thresholds['temp_high']:
        anomalies_detected = True

# Real processing begins here
aggregated_data = []
for i in range(len(temperature_readings)):
    # Composite index calculation with normalization
    norm_temp = (temperature_readings[i] - 20) / 10
    norm_humid = humidity_readings[i] / 100
    norm_press = (pressure_readings[i] - 1000) / 100
    composite_index = (norm_temp * 0.5) + (norm_humid * 0.3) + (norm_press * 0.2)
    aggregated_data.append(composite_index)

# Secondary transformation - smoothing filter (partially relevant)
smoothed_indices = []
for j in range(len(aggregated_data)):
    if j == 0:
        smoothed_indices.append(aggregated_data[j])
    else:
        smoothed_val = 0.7 * aggregated_data[j] + 0.3 * smoothed_indices[j-1]
        smoothed_indices.append(smoothed_val)

# Data structure mix: using dictionary to repackage (required feature)
data = {
    'indices': smoothed_indices,
    'count': len(smoothed_indices),
    'version': '2.1',
    'calibration': {'offset': 0.05, 'active': True}
}

# Unused complex object (distractor)
class DataProcessor:
    def __init__(self, factor):
        self.factor = factor
        self.history = []
    
    def transform(self, x):
        return x * self.factor + 2

    def log(self, value):
        pass  # dead method

# Decoy instantiation (misleading)
processor_v1 = DataProcessor(1.1)
processor_v2 = DataProcessor(0.9)

# Core metric computation (key logic)
def compute_base_metric(log_data):
    total = 0.0
    for idx, val in enumerate(log_data['indices']):
        if idx % 2 == 0:
            total += val * math.sin(idx + 1)
        else:
            total += val * math.cos(idx + 1)
    return total

# Higher-order weighting and combination
def process_metrics(sensor_data, weight_map):
    raw_metric = compute_base_metric(sensor_data)
    
    # Apply actual weights (despite some being unused)
    temp_weight = weight_map['temp']
    humid_weight = weight_map['humidity']
    press_weight = weight_map['pressure']
    
    # Dummy operations to obscure logic
    dummy_sum = temp_weight + humid_weight + press_weight
    scale_factor = math.sqrt(dummy_sum) if dummy_sum > 0 else 1
    
    # Actual contribution weights (only temp and pressure matter)
    effective_weight = temp_weight + press_weight
    
    # Final nonlinear transformation
    result = (raw_metric * scale_factor * effective_weight) + 10.5
    
    # Inject constant offset that affects final answer
    if len(sensor_data['indices']) >= 5:
        result -= 3.2  # correction term
    
    return result

# Trigger point: this assignment produces the target variable
final_score = process_metrics(data, weights)

# Output requirement
print(f"Target result: {final_score}")