import math

# Simulated sensor array data with calibration offsets
data = {
    'temp_readings': [23.5, 24.1, 22.9, 25.0, 23.8],
    'pressure_raw': [1013, 1015, 1012, 1016, 1014],
    'humidity_seq': [45, 47, 44, 46, 48],
    'voltage_levels': [3.3, 3.4, 3.2, 3.5, 3.3]
}

# Weighting schema for diagnostic scoring (some are red herrings)
weights = {
    'thermal': 0.3,
    'atmospheric': 0.25,
    'moisture': 0.2,
    'power': 0.15,
    'legacy_mode': 0.1,  # unused weight - distractor
    'fallback_index': 0.05  # unused weight - distractor
}

# Irrelevant preprocessing: normalize voltages (not used in final calculation)
normalized_voltages = [round((v - 3.2) / 0.3, 3) for v in data['voltage_levels']]
decoys = {'x': sum(normalized_voltages), 'y': max(normalized_voltages)}

# Misleading auxiliary function that looks important but is never called
def calculate_stability_index(seq, factor=1.0):
    mean_val = sum(seq) / len(seq)
    variance = sum((x - mean_val) ** 2 for x in seq) / len(seq)
    return round(math.exp(-factor * variance), 3)

# Secondary transformation with slicing distraction
temp_window = data['temp_readings'][1:-1]  # middle values only
adjusted_temps = [t * 1.02 for t in temp_window]  # minor correction

# Pressure conversion with bit manipulation red herring
raw_pressures = data['pressure_raw']
shifted_pressure = [(p >> 2) ^ 25 for p in raw_pressures]  # irrelevant transformation
mean_shifted = sum(shifted_pressure) / len(shifted_pressure)

# Humidity baseline adjustment using dictionary operations
humidity_dict = {i: val for i, val in enumerate(data['humidity_seq'])}
baseline_humidity = sum(humidity_dict.values()) / len(humidity_dict)
adjusted_humidity = baseline_humidity * 1.08

# Real processing begins here — only these steps contribute to final result
def compute_thermal_score(readings):
    avg_temp = sum(readings) / len(readings)
    fluctuation = sum(abs(readings[i] - readings[i-1]) for i in range(1, len(readings)))
    return avg_temp - fluctuation * 0.5

def compute_atmospheric_score(pressures):
    sorted_p = sorted(pressures)
    median_p = sorted_p[len(sorted_p)//2]
    range_p = sorted_p[-1] - sorted_p[0]
    return median_p - range_p * 0.2

# Unused recursive decoy
def integrate_series(n):
    if n <= 1:
        return n
    return integrate_series(n-1) + integrate_series(n-2)

# Main scoring logic — this is the only path that matters
def process_metrics(sensor_data, config_weights):
    # Actual score components
    thermal_component = compute_thermal_score(sensor_data['temp_readings'])
    atmospheric_component = compute_atmospheric_score(sensor_data['pressure_raw'])
    moisture_component = adjusted_humidity  # uses earlier global computation
    
    # Power quality metric (simple accumulation)
    power_fluctuations = sum(
        abs(data['voltage_levels'][i] - data['voltage_levels'][i-1])
        for i in range(1, len(data['voltage_levels']))
    )
    power_component = 100 - (power_fluctuations * 10)  # inverse relationship
    
    # Final weighted combination (only first four weights are actually used)
    w_t = config_weights['thermal']
    w_a = config_weights['atmospheric']
    w_m = config_weights['moisture']
    w_p = config_weights['power']
    
    preliminary_score = (
        thermal_component * w_t +
        atmospheric_component * w_a +
        moisture_component * w_m +
        power_component * w_p
    )
    
    # Apply nonlinear scaling based on system stability (constant in this case)
    scaling_factor = 1.05
    final_score = round(preliminary_score * scaling_factor, 3)
    
    # Early return guard (never triggers due to clean input)
    if math.isnan(final_score):
        return -999
        
    return final_score

# Execute main logic
temp_diagnostic = [compute_thermal_score(data['temp_readings'])]  # singleton list - red herring
flag = (len(temp_window) > 3) and (baseline_humidity > 40)

# Critical execution point
final_score = process_metrics(data, weights)

# Print result as required
print(f"Target result: {final_score}")