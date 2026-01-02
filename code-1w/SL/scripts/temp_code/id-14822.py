from itertools import combinations

def analyze_risk_factors(temperatures, thresholds):
    high_risk_count = 0
    temp_alerts = []
    for t in temperatures:
        if t > thresholds[1]:
            temp_alerts.append(t)
            if t > thresholds[2]:
                high_risk_count += 1
    return len(temp_alerts), high_risk_count

def calculate_stability_index(base, readings):
    stability = base
    fluctuation_penalty = 0
    for i in range(1, len(readings)):
        diff = abs(readings[i] - readings[i-1])
        if diff > 5:
            fluctuation_penalty += diff * 0.1
    stability -= fluctuation_penalty
    return max(stability, 0)

def evaluate_performance(sensor_data, config):
    # Extract relevant data
    main_readings = sensor_data['core_temperatures']
    aux_readings = sensor_data['aux_voltages']
    
    # Misleading computation - not used in final result
    avg_voltage = sum(aux_readings) / len(aux_readings) if aux_readings else 0
    voltage_peaks = [v for v in aux_readings if v > 12.5]
    peak_ratio = len(voltage_peaks) / len(aux_readings) if aux_readings else 0
    
    # Real logic begins
    threshold_levels = config['temp_thresholds']
    alert_count, critical_count = analyze_risk_factors(main_readings, threshold_levels)
    
    # Simulate correction factor based on pattern density
    valid_combinations = 0
    for combo in combinations(main_readings, 3):
        if all(t > threshold_levels[0] for t in combo):
            valid_combinations += 1
    
    # Distractor: unused intermediate
    adjusted_combinations = valid_combinations * 0.9 if valid_combinations > 10 else valid_combinations
    
    base_score = 100
    if critical_count > 2:
        base_score -= 40
    elif critical_count > 0:
        base_score -= 20
    
    if alert_count > 5:
        base_score -= 15
    
    stability = calculate_stability_index(50, main_readings)
    
    # Another distractor: complex but unused structure
    diagnostics = {
        'anomalies': [],
        'flags': set(),
        'metadata': {'version': '2.1', 'mode': 'diagnostic'}
    }
    for idx, temp in enumerate(main_readings):
        if temp > threshold_levels[2]:
            diagnostics['anomalies'].append((idx, temp))
            diagnostics['flags'].add('CRITICAL_TEMP')
    
    # Final score calculation
    final_score = base_score - (alert_count * 2) + int(stability)
    
    # Irrelevant transformation
    final_score_normalized = round(final_score / 150 * 100, 2)
    
    return int(final_score)

# Main execution
sensor_input = {
    'core_temperatures': [78, 85, 91, 95, 88, 96, 99, 87, 90, 94],
    'aux_voltages': [11.2, 12.1, 13.4, 11.8, 12.6, 10.9, 13.1]
}

config_params = {
    'temp_thresholds': [70, 85, 95]  # mild, high, critical
}

result = evaluate_performance(sensor_input, config_params)
print(f"Result: {result}")