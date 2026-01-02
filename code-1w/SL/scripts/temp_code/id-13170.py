def analyze_symptoms(temp, heart_rate):
    # Irrelevant computation - distractor
    risk_score = (temp * 1.8 + 32) / heart_rate * 100
    
    # Real logic: classify fever severity
    if temp > 39.0:
        severity = 'high'
    elif temp > 38.0:
        severity = 'moderate'
    else:
        severity = 'low'
    
    return severity, risk_score

def compute_recovery_index(age, days_ill):
    # Misleading intermediate calculation
    base_index = 100 - age + days_ill
    adjustment = 0
    if age < 30:
        adjustment = 15
    elif age > 60:
        adjustment = -20
    final_index = base_index + adjustment
    
    # Dead code path - never used in main flow
    if final_index > 90:
        prognosis = 'excellent'
    else:
        prognosis = 'guarded'
    
    return final_index  # Unused return

def assess_vital_stability(blood_pressure, oxygen_levels):
    # Complex but irrelevant logic chain
    systolic, diastolic = blood_pressure
    mean_pressure = (systolic + 2 * diastolic) / 3
    
    # Stability conditions
    pressure_stable = 70 <= mean_pressure <= 110
    o2_stable = oxygen_levels >= 94
    
    stability_set = {pressure_stable, o2_stable}
    
    # Distractor: unused transformation
    stability_report = {
        'mean_pressure': round(mean_pressure, 2),
        'o2_level': oxygen_levels,
        'stable': pressure_stable and o2_stable
    }
    
    return pressure_stable and o2_stable

def calculate_lab_trend(initial_wbc, current_wbc):
    # White blood cell trend analysis
    change_rate = (current_wbc - initial_wbc) / initial_wbc * 100
    
    if change_rate > 20:
        trend = 'increasing'
    elif change_rate < -20:
        trend = 'decreasing'
    else:
        trend = 'stable'
    
    # Decoy function output
    confidence = 'high' if abs(change_rate) > 10 else 'medium'
    
    return trend

def evaluate_patient_outcome():
    # Primary patient data
    temperature = 38.6
    heart_rate = 110
    age = 45
    days_ill = 3
    blood_pressure = (130, 85)
    oxygen_saturation = 92
    wbc_initial = 9.0
    wbc_current = 11.7
    
    # Irrelevant variables - red herrings
    hydration_status = 'adequate'
    nutrition_score = 7.8
    sleep_quality = 6.5
    stress_index = 4.2
    inflammation_marker = 18.3
    
    # Step 1: Analyze symptoms
    symptom_severity, _ = analyze_symptoms(temperature, heart_rate)
    
    # Step 2: Assess vital stability
    vitals_stable = assess_vital_stability(blood_pressure, oxygen_saturation)
    
    # Step 3: Calculate lab trend
    wbc_trend = calculate_lab_trend(wbc_initial, wbc_current)
    
    # Step 4: Compute recovery index (unused but looks important)
    recovery_index = compute_recovery_index(age, days_ill)
    
    # Step 5: Evaluate comorbidities (distractor with set operations)
    preexisting_conditions = {'hypertension', 'asthma'}
    high_risk_conditions = {'diabetes', 'heart_disease', 'immunodeficiency'}
    moderate_risk = {'obesity', 'chronic_kidney'}
    
    has_high_risk = not preexisting_conditions.isdisjoint(high_risk_conditions)
    has_moderate_risk = not preexisting_conditions.isdisjoint(moderate_risk)
    
    # Step 6: Determine treatment response
    responded_to_treatment = (
        symptom_severity == 'moderate' and 
        wbc_trend == 'decreasing'
    )
    
    # Step 7: Final outcome logic
    if symptom_severity == 'high':
        base_outcome = 3
    elif symptom_severity == 'moderate':
        base_outcome = 2
    else:
        base_outcome = 1
    
    # Step 8: Adjust for vitals
    if not vitals_stable:
        base_outcome += 1
    
    # Step 9: Adjust for risk factors
    risk_penalty = 0
    if has_high_risk:
        risk_penalty += 2
    elif has_moderate_risk:
        risk_penalty += 1
    
    # Step 10: Treatment response bonus
    treatment_bonus = 1 if responded_to_treatment else 0
    
    # Step 11: Final diagnostic score
    raw_diagnostic = base_outcome + risk_penalty - treatment_bonus
    
    # Step 12: Apply scaling and type conversion
    final_diagnostic = int(round(raw_diagnostic * 250 + 75))
    
    # Output the target result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute
final_diagnostic = evaluate_patient_outcome()