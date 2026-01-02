def analyze_sensor_data(temp_data, press_data):
    # Irrelevant transformation: normalize data (not used in final result)
    normalized_temps = [round((t - min(temp_data)) / (max(temp_data) - min(temp_data)), 3) for t in temp_data]
    stability_score = 0
    for i, (t, p) in enumerate(zip(temp_data, press_data)):
        if i > 0 and abs(t - temp_data[i-1]) > 5:
            stability_score += 2
    
    # Distractor: complex conditional that doesn't affect output
    alert_status = "GREEN"
    if sum(press_data) / len(press_data) > 100 or max(temp_data) > 85:
        alert_status = "YELLOW" if stability_score < 10 else "RED"

    # Core logic hidden among distractions
    adjusted_values = []
    for idx, (t, p) in enumerate(zip(temp_data, press_data)):
        adjustment_factor = 1 + (idx * 0.1)  # Increases slightly with index
        adjusted_value = (t * 0.7) + (p * 0.3) * adjustment_factor
        adjusted_values.append(adjusted_value)
    
    # Secondary distractor: unused recursive helper
    def predict_next(val_list, depth=2):
        if depth == 0 or len(val_list) == 0:
            return val_list[-1] if val_list else 0
        return predict_next([val_list[i+1] - val_list[i] for i in range(len(val_list)-1)], depth-1)

    # Actual computation path
    base_yield = 0
    for val in adjusted_values:
        if val > 60:
            base_yield += val * 0.15
        elif val > 45:
            base_yield += val * 0.10
        else:
            base_yield += val * 0.05
    
    # Final adjustment based on sensor correlation
    correlation_bonus = 0
    for t, p in zip(temp_data, press_data):
        if t > 70 and p > 90:
            correlation_bonus += 1.5
    
    return base_yield + correlation_bonus


def calculate_optimal_yield(temps, pressures):
    # Wrapper that performs additional irrelevant checks
    if len(temps) != len(pressures):
        raise ValueError("Sensor data length mismatch")
    
    # Dead code path: never executed under normal inputs
    if any(t < 0 for t in temps) and False:  # Unreachable due to constant condition
        temps = [abs(t) for t in temps]
    
    # Key processing call
    raw_output = analyze_sensor_data(temps, pressures)
    
    # Final scaling - actually used
    scaling_factor = 0.95
    final_result = raw_output * scaling_factor
    
    # Distractor: logging unrelated metrics
    avg_temp = sum(temps) / len(temps)
    peak_pressure = max(pressures)
    duration_cycles = len(temps) * 2  # Unused metric
    
    return final_result

# Sensor input data from experimental run
temperature_readings = [68, 72, 75, 63, 80, 77, 70]
pressure_readings = [88, 95, 102, 85, 110, 98, 90]

# Execute main computation
final_yield = calculate_optimal_yield(temperature_readings, pressure_readings)
print(f"Result: {final_yield}")