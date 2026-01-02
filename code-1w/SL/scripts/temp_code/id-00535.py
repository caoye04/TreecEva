from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant readings
data_stream = [
    {'sensor': 'temp', 'value': 23.5, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.1, 'status': 'ok'},
    {'sensor': 'humid', 'value': 45.2, 'status': 'ok'},
    {'sensor': 'temp', 'value': 22.9, 'status': 'ok'},
    {'sensor': 'pressure', 'value': 1013.2, 'status': 'ok'},
    {'sensor': 'humid', 'value': 46.0, 'status': 'ok'},
    {'sensor': 'temp', 'value': 24.3, 'status': 'error'},  # Invalid due to error
    {'sensor': 'pressure', 'value': 1012.8, 'status': 'ok'},
    {'sensor': 'humid', 'value': 44.7, 'status': 'ok'},
    {'sensor': 'temp', 'value': 23.8, 'status': 'ok'}
]

# Data aggregation structures
temp_readings = []
humid_readings = []
pressure_readings = []
sensor_count = defaultdict(int)
status_log = Counter()

# Preprocessing: filter valid readings and group by sensor
total_valid = 0
redundant_sum = 0.0
normalization_factor = 1.0
correction_offset = 0.3

for entry in data_stream:
    status_log[entry['status']] += 1
    if entry['status'] != 'ok':
        continue
    
    sensor_count[entry['sensor']] += 1
    total_valid += 1

    if entry['sensor'] == 'temp':
        temp_readings.append(entry['value'])
        redundant_sum += entry['value'] * 0.01  # Irrelevant accumulation
    elif entry['sensor'] == 'humid':
        humid_readings.append(entry['value'])
        normalization_factor *= 1.001  # Distractor computation
    elif entry['sensor'] == 'pressure':
        pressure_readings.append(entry['value'])

# Compute basic statistics
avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
avg_humid = sum(humid_readings) / len(humid_readings) if humid_readings else 0
avg_pressure = sum(pressure_readings) / len(pressure_readings) if pressure_readings else 0

# Intermediate scoring (some irrelevant)
raw_temp_score = avg_temp * 2.1
raw_humid_score = (100 - abs(avg_humid - 50)) * 1.5
raw_pressure_score = 10 - abs(avg_pressure - 1013.0) / 10

# Filler variables for distraction
drift_estimate = abs(avg_temp - temp_readings[0])
stability_ratio = len(temp_readings) / (drift_estimate + 1e-5)
phantom_correction = drift_estimate * correction_offset

# Weighted intermediate score (not final)
intermediate_score = raw_temp_score * 0.5 + raw_humid_score * 0.3 + raw_pressure_score * 0.2

# Processed data structure for main logic
processed_data = {
    'metrics': {
        'temperature': avg_temp,
        'humidity': avg_humid,
        'pressure': avg_pressure
    },
    'counts': dict(sensor_count),
    'total_valid': total_valid,
    'base_scores': {
        'temp': raw_temp_score,
        'humid': raw_humid_score,
        'pressure': raw_pressure_score
    }
}

# Main scoring function with conditional adjustments
def calculate_final_score(data):
    metrics = data['metrics']
    counts = data['counts']
    base_scores = data['base_scores']
    
    # Primary score components
    temp_component = base_scores['temp']
    humid_component = base_scores['humid']
    pressure_component = base_scores['pressure']
    
    # Conditional bonus/penalty based on balance
    balance_factor = 1.0
    if abs(metrics['temperature'] - 23.5) < 1.0:
        balance_factor += 0.1
    if abs(metrics['humidity'] - 45.0) < 2.0:
        balance_factor += 0.08
    if abs(metrics['pressure'] - 1013.0) < 1.0:
        balance_factor += 0.05
    
    # Red herring calculation
    hypothetical_max = (30 * 2.1 + 100 * 1.5 + 20)
    efficiency_ratio = intermediate_score / hypothetical_max if hypothetical_max > 0 else 0
    
    # Final composition
    raw_final = (temp_component + humid_component + pressure_component) * balance_factor
    
    # Apply fake normalization (effectively none)
    normalized_final = raw_final * (normalization_factor or 1.0)
    
    # Round to nearest integer as per system spec
    return round(normalized_final)

# Execution point of interest
final_score = calculate_final_score(processed_data)

# Print result as required
print(f"Result: {final_score}")