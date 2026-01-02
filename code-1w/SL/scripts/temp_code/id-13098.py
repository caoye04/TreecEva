def analyze_symptoms(history, vitals):
    # Diagnostic thresholds
    fever_threshold = 38.0
    pressure_low = 90
    pressure_high = 140

    # Extract data
    temperature = vitals.get('temperature')
    systolic = vitals.get('systolic')
    diastolic = vitals.get('diastolic')
    heart_rate = vitals.get('heart_rate')

    # Secondary vitals (distractor variables)
    respiratory_rate = vitals.get('respiratory_rate')  # Not used in final logic
    oxygen_sat = vitals.get('oxygen_sat')              # Distractor
    cholesterol = vitals.get('cholesterol')           # Irrelevant metric

    # Historical symptom tracking (semi-relevant)
    prior_fever_days = 0
    for entry in history:
        if entry['symptom'] == 'fever' and entry['severity'] > 2:
            prior_fever_days += 1

    # Current symptom flags
    has_fever = temperature > fever_threshold
    has_hypertension = systolic > pressure_high or diastolic > 90
    has_tachycardia = heart_rate > 100

    # Distractor loop: counts unrelated symptoms (not impacting diagnosis)
    chronic_conditions = set()
    for record in history:
        if record['duration_days'] > 90:
            chronic_conditions.add(record['symptom'])
    
    # Additional unused computation: misleading complexity
    avg_severity = sum([r['severity'] for r in history]) / len(history) if history else 0
    max_duration = max([r['duration_days'] for r in history], default=0)

    # Medication interference check (dead code path - never called)
    def check_interactions(meds):
        interactions = []
        for m in meds:
            if 'antibiotic' in m:
                interactions.append('caution')
        return interactions  # Never invoked

    # Core diagnostic logic (only this affects final answer)
    risk_factors = 0
    if has_fever:
        risk_factors += 1
    if has_hypertension:
        risk_factors += 2
    if has_tachycardia:
        risk_factors += 3

    # Use dictionary to map risk level to diagnostic code
    risk_map = {0: 100, 1: 205, 2: 310, 3: 415, 4: 415, 5: 520}
    base_diagnostic = risk_map.get(risk_factors, 100)

    # Minor adjustment using set difference (real but subtle use)
    new_symptoms = set([r['symptom'] for r in history]) - {'fatigue', 'headache'}
    if 'chest_pain' in new_symptoms:
        base_diagnostic += 50

    # Final computation
    adjustment = len(new_symptoms) % 4
    final_diagnostic = base_diagnostic + adjustment

    # Output result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Patient data
patient_history = [
    {'symptom': 'fever', 'severity': 3, 'duration_days': 3},
    {'symptom': 'cough', 'severity': 2, 'duration_days': 5},
    {'symptom': 'fatigue', 'severity': 4, 'duration_days': 10},
    {'symptom': 'chest_pain', 'severity': 5, 'duration_days': 2}
]

vital_signs = {
    'temperature': 38.6,
    'systolic': 144,
    'diastolic': 88,
    'heart_rate': 108,
    'respiratory_rate': 18,
    'oxygen_sat': 97,
    'cholesterol': 210
}

# Execute
final_diagnostic = analyze_symptoms(patient_history, vital_signs)