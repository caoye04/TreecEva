import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [45, 48, 52, 58, 61, 57, 54, 49, 47]
pressure_readings = [1013, 1012, 1015, 1018, 1020, 1017, 1014, 1011, 1009]

# Irrelevant calibration coefficients (distractor)
calibration_a = 0.987
kalman_gain = 0.05
offset_matrix = [[0.1, -0.2], [0.3, 0.15]]

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [0.5 * (x - mean_val) for x in data]  # Unused function

# Real preprocessing
processed_temps = [round(t ** 1.05 - 2.0, 2) for t in temperature_readings]
processed_humidity = [h + 2 if h < 50 else h - 3 for h in humidity_readings]

# Combined data structure with slicing distraction
all_data = [processed_temps[i:i+3] for i in range(0, len(processed_temps), 3)]
flattened_humidity = [val for sublist in all_data for val in sublist]  # Reuse of all_data for confusion

# Decoy transformation (irrelevant)
decoherence_factor = sum([math.sin(i) for i in range(len(humidity_readings))])
entropy_proxy = math.log(len(pressure_readings) + 1) * decoherence_factor

# Real signal filter using set operations (core logic)
outlier_indices = set()
for i, temp in enumerate(processed_temps):
    if temp > 25.5 or temp < 22.0:
        outlier_indices.add(i)

valid_indices = set(range(len(processed_temps))) - outlier_indices
filtered_temps = [processed_temps[i] for i in valid_indices]

# Construct composite dataset (key step)
processed_data = {
    'temps': processed_temps,
    'humidity': processed_humidity,
    'indices': valid_indices
}

# Threshold configuration map (used in analysis)
threshold_map = {
    'temp_high': 25.5,
    'temp_low': 22.0,
    'humidity_stable': 50,
    'weighting': (0.7, 0.3)  # weights for temp and humidity
}

# Auxiliary diagnostic tool (misleading)
def compute_stability_index(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs) if diffs else 0.0

stability_score = compute_stability_index(pressure_readings)  # Irrelevant result

# Core analysis function with conditional branching and tuple unpacking
def analyze_readings(data, thresholds):
    temp_vals = data['temps']
    hum_vals = data['humidity']
    active_indices = data['indices']
    
    high_temp_count = 0
    stable_humidity_count = 0
    
    # Complex conditional evaluation with nesting
    for idx in sorted(active_indices):
        if idx < len(temp_vals):  # Redundant check (distractor)
            if temp_vals[idx] > thresholds['temp_high']:
                high_temp_count += 1
            elif temp_vals[idx] < thresholds['temp_low']:
                high_temp_count += 0.5  # Partial increment (subtle)
            
        if idx < len(hum_vals):
            hum_condition = (
                hum_vals[idx] >= thresholds['humidity_stable'] - 5 and 
                hum_vals[idx] <= thresholds['humidity_stable'] + 5
            )
            if hum_condition:
                stable_humidity_count += 1
    
    # Weighted diagnostic calculation (actual answer source)
    w1, w2 = thresholds['weighting']
    raw_score = (w1 * high_temp_count) + (w2 * stable_humidity_count)
    
    # Final nonlinear transformation
    final_score = int((raw_score ** 2) + 17.3)
    
    # Decoy output variables (distraction)
    diagnostic_token = hash('ENV_MON_2024') % 1000
    fallback_code = math.ceil(stability_score * 10)
    
    return final_score

# Trigger key computation
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")