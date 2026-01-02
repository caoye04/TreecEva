def preprocess_vitals(vital_signs):
    # Irrelevant transformation: normalizes values that aren't used later
    normalized = {k: round((v - 37) / 0.5, 2) for k, v in vital_signs.items() if 'temp' in k}
    return normalized

# Decoy patient data with multiple unused fields
temp_readings = {'temp_morning': 36.8, 'temp_noon': 37.2, 'temp_evening': 37.5}
blood_pressure = [120, 80]
heart_rates = [70, 72, 68, 74, 71]

# Unused function simulating misleading analysis
def compute_risk_score(data):
    score = 0
    for val in data:
        if val > 70:
            score += 0.3
        else:
            score -= 0.1
    return round(score, 2)

# Real processing begins here
symptom_severity = {
    'fever': 2,
    'cough': 3,
    'fatigue': 4,
    'headache': 1
}

# Conditional expression used in logic
base_risk = 5 if sum(symptom_severity.values()) >= 8 else 2

# Set operations: tracking affected systems
respiratory_symptoms = {'cough', 'shortness_of_breath'}
digestive_symptoms = {'nausea', 'abdominal_pain'}
current_presentations = {'cough', 'fatigue', 'fever', 'headache'}

# Cross-reference sets to determine system involvement
overlapping_systems = len(current_presentations & respiratory_symptoms) + len(current_presentations & digestive_symptoms)

# Dictionary-based triage protocol
triage_protocol = {
    0: 'monitor',
    1: 'evaluate',
    2: 'urgent',
    3: 'immediate'
}

# Simulated lab results (some irrelevant)
labs = {
    'wbc_count': 11.2,  # above normal
    'rbc_count': 4.7,
    'platelets': 220,
    'crp_level': 18.5  # elevated inflammation marker
}

# Boolean logic chain with short-circuiting and red herrings
has_infection_marker = labs['wbc_count'] > 10.0 or labs['crp_level'] > 10.0 and symptom_severity['fever'] > 0
is_stable = heart_rates[-1] < 75 and not any(hr > 100 for hr in heart_rates[:3])
requires_intervention = has_infection_marker and not is_stable or overlapping_systems >= 2

# Dead code path - never called but looks important
def generate_report():
    return "Comprehensive diagnostic report generated."

# Key logic hidden among distractions
comorbidities = ['hypertension', 'diabetes']
chronic_count = len([cond for cond in comorbidities if cond in ['asthma', 'hypertension']])

# Main analysis function
def analyze_patient_data():
    # Step 1: base score from symptoms
    total_severity = sum(val for key, val in symptom_severity.items() if key in current_presentations)
    
    # Step 2: adjust by lab markers (only crp_level actually used)
    inflammation_bonus = labs['crp_level'] * 0.3 if labs['crp_level'] > 15.0 else 0
    
    # Step 3: set-derived modifier
    system_modifier = len(current_presentations | respiratory_symptoms) % 4
    
    # Step 4: complex conditional expression
    age_factor = 1.4 if 65 <= 72 < 80 else 1.0  # hardcoded patient age = 72
    
    # Step 5: combine into diagnostic score
    raw_score = total_severity * 2.5 + inflammation_bonus + system_modifier * chronic_count * age_factor
    
    # Step 6: apply triage mapping via dictionary lookup
    urgency_level = triage_protocol.get(min(overlapping_systems + int(inflammation_bonus > 0), 3), 'monitor')
    
    # Step 7: final diagnostic computation (this is the answer)
    final_diagnostic = int(raw_score * 10) if urgency_level == 'urgent' or requires_intervention else int(raw_score)
    
    # Step 8: red herring - this print is irrelevant
    _ = [print(f'Red flag: {key}') for key in labs.keys() if labs[key] > 15.0]
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_patient_data()
print(f"Target result: {final_diagnostic}")