def analyze_patient_vitals(vital_signs, baseline):
    # Irrelevant transformation (distractor)
    normalized = {k: (v - 50) / 10 for k, v in vital_signs.items()}
    deviation_score = 0
    for k, v in vital_signs.items():
        if k in baseline:
            deviation_score += abs(v - baseline[k])
    
    # Dead code path - never used (red herring)
    def stress_index(x):
        return x * 1.5 if x > 75 else x * 0.8

    # Misleading intermediate metric
    temp_risk = deviation_score * 2.3
    return deviation_score

# Unused auxiliary function (decoy)
def compute_thermoregulation_efficiency(temp_readings):
    avg_temp = sum(temp_readings) / len(temp_readings)
    variance = sum((t - avg_temp) ** 2 for t in temp_readings)
    return variance / avg_temp

# Simulated sensor data with noise flags
sensor_metadata = {
    'device_01': {'calibration': 1.02, 'noise_floor': 0.05},
    'device_02': {'calibration': 0.98, 'noise_floor': 0.07}
}

# Real processing begins here
raw_readings = [
    [72, 120, 95],
    [68, 118, 94],
    [74, 125, 96],
    [70, 119, 95]
]

# Extract heart rate (index 0), blood pressure (index 1), oxygen (index 2)
heart_rates = [row[0] for row in raw_readings]
blood_pressures = [row[1] for row in raw_readings]
oxygen_levels = [row[2] for row in raw_readings]

# Distractor: complex zip + enumerate usage with irrelevant computation
offset_analysis = {}
for i, (hr, bp) in enumerate(zip(heart_rates, blood_pressures)):
    if i % 2 == 0:
        offset_analysis[f'even_{i}'] = (hr * 1.01) + (bp * 0.03)

# Real signal cleaning
filtered_o2 = [o for o in oxygen_levels if 90 <= o <= 100]
mean_o2 = sum(filtered_o2) / len(filtered_o2)

# Set operations for anomaly detection (required python feature)
expected_range = set(range(70, 76))
observed_hr_set = set(heart_rates)
anomalies = observed_hr_set.symmetric_difference(expected_range)

# Boolean logic chain with short-circuiting
baseline_ok = len(anomalies) < 5 and (mean_o2 > 92 or True) and not False

# Conditional expression with distractor
risk_factor = 1.5 if mean_o2 < 94 else 0.8

# Multiple simultaneous assignments (variable assignment concept)
status_code, severity_level, adjustment = 200, 'moderate', 0.0

# Bit manipulation red herring (irrelevant to final result)
encoded_status = status_code ^ 0xFF & 0x1F

# Health data structure construction (relevant)
health_data = {
    'vitals': {
        'heart_rate_avg': sum(heart_rates) / len(heart_rates),
        'blood_pressure_trend': blood_pressures[-1] - blood_pressures[0],
        'oxygen_stability': max(filtered_o2) - min(filtered_o2)
    },
    'metrics': {
        'anomaly_count': len(anomalies),
        'baseline_match': baseline_ok,
        'risk_adjustment': adjustment
    }
}

# Threshold definitions
thresholds = {
    'critical_anomalies': 10,
    'oxygen_threshold': 1.5,
    'pressure_warning': 3
}

# Core logic nested in dependency chain
prev_result = analyze_patient_vitals(
    {'hr': health_data['vitals']['heart_rate_avg']},
    {'hr': 72}
)

# Final aggregation function with multiple concepts
def aggregate_metrics(data, limits):
    score = 0
    vitals = data['vitals']
    metrics = data['metrics']
    
    # Nested conditional logic (3 levels deep)
    if metrics['baseline_match']:
        if vitals['oxygen_stability'] < limits['oxygen_threshold']:
            score += 40
            if vitals['blood_pressure_trend'] < limits['pressure_warning']:
                score += 30
        else:
            score += 10
    else:
        score -= 20
    
    # Additional arithmetic path
    anomaly_penalty = max(0, 5 * (limits['critical_anomalies'] - metrics['anomaly_count']))
    score += anomaly_penalty
    
    # Irrelevant bitwise operation inside function (distraction)
    masked_score = score & 0xFFFF
    
    # Decoy dictionary update
    data['diagnostics'] = 'completed'
    
    # Final computation
    final_value = int(masked_score + prev_result * 1.2)
    return final_value

# Execution point of interest
final_diagnostic = aggregate_metrics(health_data, thresholds)
print(f"Result: {final_diagnostic}")