def preprocess_sensor(readings):
    smoothed = [(readings[i-1] + readings[i] + readings[i+1]) / 3 
                 for i in range(1, len(readings)-1)]
    return [x * 1.05 for x in smoothed if x > 0]

# Simulate correction factor drift (irrelevant but plausible)
def compute_drift_compensation(values):
    base = sum(values) / len(values)
    drift = [base * (1 + 0.01 * i) for i in range(len(values))]
    return [v - d for v, d in zip(values, drift)]

# Core calculation
def calculate_process_efficiency(temps, pressures):
    efficiency_map = {}
    for t, p in zip(temps, pressures):
        key = round(t)
        if key not in efficiency_map:
            efficiency_map[key] = []
        efficiency_map[key].append(p / (t + 273.15))
    
    # Extract average efficiencies per temperature bucket
    avg_efficiencies = {k: sum(v)/len(v) for k, v in efficiency_map.items()}
    return avg_efficiencies

# Determine optimal yield based on constrained thresholds
def calculate_optimal_yield(temp_input, press_input):
    # Preprocess raw sensor data
    filtered_temps = preprocess_sensor(temp_input)
    filtered_press = preprocess_sensor(press_input)
    
    # Normalize lengths (distractor: extra processing)
    min_len = min(len(filtered_temps), len(filtered_press))
    trimmed_temps = filtered_temps[:min_len]
    trimmed_press = filtered_press[:min_len]
    
    # Compute efficiency map (core logic)
    eff_dict = calculate_process_efficiency(trimmed_temps, trimmed_press)
    
    # Irrelevant transformation (distractor)
    squared_pairs = [{"temp": k, "value_sq": v**2} for k, v in eff_dict.items()]
    total_sq = sum(item["value_sq"] for item in squared_pairs)  # unused
    
    # Real computation path
    valid_keys = [k for k in eff_dict.keys() if 20 < k < 80]
    if not valid_keys:
        return 0
    
    selected_effs = [eff_dict[k] for k in valid_keys]
    mean_eff = sum(selected_effs) / len(selected_effs)
    
    # Apply physical constraint and scaling
    max_pressure_inlet = max(trimmed_press) * 0.9  # safety margin
    scaling_factor = 1 + (max_pressure_inlet / 100)
    
    # Final yield calculation
    final_yield = int(mean_eff * scaling_factor * 1000)  # scale to engineering units
    
    # Dead code branch (distractor)
    if final_yield < 0:
        backup = [x for x in trimmed_temps if x > 50]
        final_yield = len(backup) * 100
    
    return final_yield

# Input data from lab experiment
temperature_data = [25.0, 26.5, 28.0, 30.5, 33.0, 36.0, 40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0]
pressure_data = [101.3, 102.1, 103.5, 105.0, 107.2, 110.0, 113.5, 117.0, 120.0, 122.5, 125.0, 127.5, 130.0, 132.0, 134.0]

# Execute main logic
final_yield = calculate_optimal_yield(temperature_data, pressure_data)
print(f"Result: {final_yield}")