def analyze_plant_efficiency(readings):
    adjusted_readings = []
    correction_factor = 1.07
    baseline = sum(readings[:3]) / 3
    
    # Irrelevant transformation (distractor)
    normalized = [round(x / max(readings) * 100) for x in readings]
    outliers = [i for i, x in enumerate(readings) if x > 1.5 * baseline]
    
    for i, val in enumerate(readings):
        if i % 2 == 0:
            adjusted = val * correction_factor
        else:
            adjusted = val * (1 + 0.01 * i)
        if i > 0 and readings[i] < readings[i-1]:
            adjusted *= 0.98  # decay adjustment
        adjusted_readings.append(int(adjusted))
    
    # Dead code path (never executed due to logic)
    if len(outliers) > 10:
        safety_margin = 0
        for idx in outliers:
            safety_margin += normalized[idx]
        baseline -= safety_margin

    # Core data used for answer
    thermal_loads = []
    for x in adjusted_readings:
        if x % 4 == 0:
            thermal_loads.append(x + 12)
        elif x % 3 == 0:
            thermal_loads.append(x + 8)
        else:
            thermal_loads.append(x + 5)
    
    # Red herring: complex but unused calculation
    cumulative_stress = 0
    stress_weights = [0.1, 0.3, 0.6]
    for j in range(len(adjusted_readings) - 2):
        window = adjusted_readings[j:j+3]
        weighted = sum(window[k] * stress_weights[k] for k in range(3))
        cumulative_stress += weighted ** 0.5

    # Key computation path
    temp_buffer = [thermal_loads[i] for i in range(0, len(thermal_loads), 2)]
    avg_midsection = sum(temp_buffer[2:7]) / 5
    
    # Decoy assignment (misleading intermediate)
    peak_capacity = int(avg_midsection * 1.15)
    
    # Actual key statement
    peak_capacity = max(thermal_loads[-5:])
    
    # Unused variable cluster (distraction)
    final_metrics = {
        'stability': len(outliers),
        'efficiency_ratio': baseline / (sum(normalized[:10]) / 10),
        'peak_capacity_debug': int(cumulative_stress / 10)
    }
    
    # Output required result
    print(f"Result: {peak_capacity}")

# Input data
sensor_data = [86, 94, 77, 81, 90, 76, 88, 95, 73, 82, 91, 79, 87, 93, 75]
analyze_plant_efficiency(sensor_data)