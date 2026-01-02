from collections import defaultdict

# Simulate sensor data aggregation and weighted scoring in an environmental monitoring system
def collect_sensor_data():
    raw_readings = [
        ('temp', 23.5), ('humidity', 65), ('co2', 410),
        ('temp', 24.1), ('humidity', 63), ('light', 870),
        ('co2', 405), ('pm25', 12), ('temp', 22.9)
    ]
    
    grouped = defaultdict(list)
    for sensor, value in raw_readings:
        grouped[sensor].append(value)
    
    averaged = {}
    for sensor in grouped:
        averaged[sensor] = round(sum(grouped[sensor]) / len(grouped[sensor]), 2)
    
    return averaged

def normalize readings(readings):
    # Misleading function - never called
    pass

def preprocess_data(data):
    # Add baseline corrections (some irrelevant)
    corrections = {'temp': -1.0, 'humidity': 0, 'co2': -40, 'pm25': 0, 'light': -100}
    corrected = {}
    for k, v in data.items():
        corrected[k] = v + corrections.get(k, 0)
    
    # Derived metrics (only some used later)
    if 'temp' in corrected:
        corrected['feels_like'] = corrected['temp'] * 1.1
    if 'co2' in corrected and 'humidity' in corrected:
        corrected['air_quality_index'] = (corrected['co2'] / 10) + (corrected['humidity'] / 2)
    
    # Dead code branch - misleading
    if 'pressure' in corrected:
        corrected['altitude'] = 44330 * (1 - (corrected['pressure']/1013.25)**(1/5.255))
    
    return corrected

def calculate_stability_score(processed):
    # Assess temporal stability across sensors (not directly used)
    keys_of_interest = ['temp', 'humidity', 'co2']
    stability = 0
    for key in keys_of_interest:
        if key in processed:
            stability += abs(processed[key]) % 7
    return round(stability, 2)
def calculate_final_score(processed, weights):
    base_components = ['temp', 'humidity', 'co2', 'pm25']
    score = 0.0
    
    # Only these contribute to final score
    relevant_weights = {k: v for k, v in weights.items() if k in base_components}
    
    for component in base_components:
        raw_val = processed.get(component, 0)
        weight = relevant_weights.get(component, 0)
        contribution = raw_val * weight
        score += contribution
    
    # Distraction: unused derived values
    if 'feels_like' in processed:
        adjusted_temp = processed['feels_like'] * 0.95
    
    # Final nonlinear scaling
    if score > 0:
        score = (score ** 0.95) * 1.05
    
    return round(score, 4)

# Main execution flow
data_raw = collect_sensor_data()
data_processed = preprocess_data(data_raw)

# Weight configuration (domain-specific tuning)
weights_config = {
    'temp': 0.8,
    'humidity': 0.6,
    'co2': 0.9,
    'pm25': 1.2,
    'light': 0.3  # Not used in final score
}

# Irrelevant intermediate calculation
stability_metric = calculate_stability_score(data_processed)
scaling_factor = len(data_processed) * 0.7  # Unused distraction

final_score = calculate_final_score(data_processed, weights_config)

# Red herring variable
auxiliary_result = [x for x in range(5) if x % 2 == 0]

print(f"Result: {final_score}")