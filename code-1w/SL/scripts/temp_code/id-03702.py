def analyze_patient_vitals():
    heart_rate = 76
    oxygen_saturation = 97
    energy_level = 89.5
    base_metabolism = 78.2
    
    # Primary diagnostic thresholds
    threshold = 85
    patient_stable = 1
    critical_condition = -1
    
    # Secondary checks (not used in final decision)
    respiratory_rate = 18
    blood_pressure_systolic = 120
    
    # Conditional expression determining final diagnosis
    final_diagnostic = patient_stable if energy_level > threshold else critical_condition
    
    # Additional unrelated metric
    bmi = 22.4
    
    # Energy threshold adjusted based on protocol
    energy_threshold = int(energy_level * 0.9) if final_diagnostic == patient_stable else int(energy_level * 0.5)
    
    return energy_threshold

result = analyze_patient_vitals()
print(f"Result: {result}")