import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.9, 20.2]
humidity_readings = [45, 52, 61, 48, 55, 67, 73, 59]
pressure_readings = [1013, 1015, 1012, 1018, 1016, 1014, 1011, 1017]

# Irrelevant auxiliary data (distractor)
color_codes = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
user_preferences = {'theme': 'dark', 'units': 'metric', 'alerts': True}

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]  # Never used

# Actual processing function
def filter_outliers(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean_val) <= threshold * std_dev]

# Red herring function with unused result
def compute_entropy(data):
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * math.log(p) for p in probs if p > 0)

entropy_diagnostic = compute_entropy(humidity_readings)  # Distractor assignment

# Real pipeline starts here
filtered_temps = filter_outliers(temperature_readings, threshold=1.5)
filtered_humidity = filter_outliers(humidity_readings, threshold=1.8)

# Composite index calculation (relevant)
adjusted_index = []
for t, h in zip(filtered_temps, filtered_humidity):
    adjustment = (t - 20) * (h / 50)
    adjusted_index.append(round(adjustment, 2))

# Data structuring using dictionary (required feature)
processed_data = {
    'temperatures': filtered_temps,
    'humidity_levels': filtered_humidity,
    'adjustment_curve': adjusted_index,
    'metadata': {
        'station_count': len(filtered_temps),
        'version': '2.1',
        'calibrated': True
    }
}

# Decoy transformation chain
transform_queue = ['normalize', 'scale', 'encode']
for step in transform_queue:
    if step == 'normalize':
        processed_data['aux_norm'] = [x / max(processed_data['temperatures']) for x in processed_data['temperatures']]
    elif step == 'calibrate':  # Unreachable branch
        processed_data['calib_flag'] = True

# Core analysis logic
status_map = {0: 'stable', 1: 'moderate', 2: 'elevated', 3: 'critical'}

# Complex conditional with nesting and multiple concepts
def evaluate_risk_level(index_values):
    if len(index_values) < 3:
        return 0
    avg_index = sum(index_values) / len(index_values)
    high_stress = [x for x in index_values if x > 1.5]
    
    if avg_index < 0.8:
        risk = 1
    elif avg_index < 2.0:
        risk = 2
        if len(high_stress) >= 2:
            secondary_check = sum(1 for x in index_values if x > 2.0)
            if secondary_check > 0:
                risk = 3
    else:
        risk = 3
        
    # Additional validation layer
    if risk >= 2:
        volatility = max(index_values) - min(index_values)
        if volatility > 3.0:
            risk = min(risk + 1, 3)
    
    return risk

# Another irrelevant computation (distractor)
dataset_hash = sum([hash(str(v)) % 1000 for v in pressure_readings]) % 777

# Final analysis combining dictionary access, conditionals, and arithmetic
def analyze_readings(data_dict):
    curve = data_dict['adjustment_curve']
    raw_temps = data_dict['temperatures']
    
    base_risk = evaluate_risk_level(curve)
    
    # Secondary factor based on temperature spread
    temp_range = max(raw_temps) - min(raw_temps)
    range_factor = 1 if temp_range > 5 else 0
    
    # Tertiary check using dictionary metadata
    sample_size = data_dict['metadata']['station_count']
    size_bonus = 1 if sample_size >= 5 else 0
    
    # Final diagnostic score (this is the answer)
    final_score = (base_risk * 17) + (range_factor * 5) + (size_bonus * 3)
    
    # Dead code block with misleading variables
    if False:
        debug_trace = []
        for k, v in data_dict.items():
            debug_trace.append(f'{k}: {len(str(v))}')
    
    return final_score

# Execution point of interest
final_diagnostic = analyze_readings(processed_data)
print(f"Target result: {final_diagnostic}")