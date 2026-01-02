def preprocess_vitals(vital_signs):
    # Irrelevant preprocessing: Normalize values (not used in final logic)
    normalized = [(v - min(vital_signs)) / (max(vital_signs) - min(vital_signs)) for v in vital_signs]
    return [round(n * 100) for n in normalized]


def compute_risk_score(age, history):
    # Distractor function: Computes a risk score but it's not used in final path
    base_risk = 0.5
    if age > 60:
        base_risk += 0.3
    if 'diabetes' in history:
        base_risk += 0.2
    if 'hypertension' in history:
        base_risk += 0.25
    return round(base_risk * 100)


def evaluate_organ_stress(heart_rate, resp_rate, temp):
    # Misleading intermediate calculation
    stress_index = (heart_rate * 0.4) + (resp_rate * 0.3) + (abs(temp - 98.6) * 10)
    category = 'low'
    if stress_index > 60:
        category = 'high'
    elif stress_index > 40:
        category = 'moderate'
    return stress_index, category  # Not used directly


def filter_artifacts(sensor_data):
    # Real but obfuscated relevant processing
    filtered = [x for x in sensor_data if 0 <= x <= 200 and x % 2 == 1]  # Only odd values in range
    return [x for x in filtered if x > 50]  # Further filter above threshold


def calculate_metabolic_load(filtered_readings, duration_hours):
    # Relevant transformation
    total_load = 0
    for r in filtered_readings:
        if r < 100:
            total_load += r * 0.7
        else:
            total_load += r * 1.1
    return total_load / duration_hours


def derive_biomarker_signature(load, age, markers):
    # Complex but partially irrelevant transformation
    signature = load * 0.3
    if age % 5 == 0:
        signature += 12.5
    # Decoy logic with dictionary that isn't fully used
    profile = {m: signature + (i * 3.2) for i, m in enumerate(markers)}
    profile['adjusted'] = signature * 1.4
    return profile['adjusted']  # Only this value is carried forward


def analyze_patient_data():
    # Patient data input
    age = 47
    vital_signs = [72, 18, 97.1, 128, 88, 99.5]  # HR, RR, Temp, BP, SpO2, Temp
    lab_results = [110, 134, 95, 142, 88, 105, 155, 76, 160, 112]
    medical_history = ['asthma']
    biomarkers = ['crp', 'il6', 'tnf']
    monitoring_duration = 6  # hours

    # Distractor: Unused derived values
    risk_level = compute_risk_score(age, medical_history)
    _, organ_risk = evaluate_organ_stress(vital_signs[0], vital_signs[1], vital_signs[2])
    processed_vitals = preprocess_vitals(vital_signs)

    # Core diagnostic chain
    cleaned_data = filter_artifacts(lab_results)
    
    # Intermediate result that looks important but is only partially relevant
    metabolic_load = calculate_metabolic_load(cleaned_data, monitoring_duration)
    
    # Final computation path
    signature_value = derive_biomarker_signature(metabolic_load, age, biomarkers)
    
    # Key decision logic with red herring condition
    if signature_value > 100:
        severity = 'critical'
        adjustment_factor = 0.85
    elif signature_value > 70:
        severity = 'elevated'
        adjustment_factor = 0.9
    else:
        severity = 'normal'
        adjustment_factor = 1.0

    # Dead code branch — never executed due to age
    compensation_bonus = 0
    if age < 30 and 'athlete' in medical_history:
        compensation_bonus = 15

    # Final diagnostic calculation — only this matters
    base_diagnostic = signature_value * adjustment_factor
    final_diagnostic = int(base_diagnostic - 17.3)  # Final deterministic result

    # Print required at end
    print(f"Target result: {final_diagnostic}")
    
    return final_diagnostic

# Execution entry point
result = analyze_patient_data()