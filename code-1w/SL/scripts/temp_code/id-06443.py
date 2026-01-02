def preprocess_vitals(vital_set):
    # Irrelevant transformation: normalizes values but not used in final path
    normalized = {k: round(v / max(vital_set.values()), 2) for k, v in vital_set.items()}
    return normalized


def compute_organ_risk(age, organ_scores):
    # Distractor function: computes risk but not used in final logic
    base_risk = sum(organ_scores.values()) * 0.1
    age_factor = 1 + (age - 50) * 0.02 if age > 50 else 1
    return round(base_risk * age_factor, 3)


def evaluate_symptom_history(symptoms):
    # Dead code path: looks useful but unused
    severity_map = {'fever': 2, 'cough': 1, 'fatigue': 1, 'shortness_of_breath': 3}
    total_severity = sum(severity_map.get(s, 0) for s in symptoms)
    return total_severity


def filter_critical_indicators(labs):
    # Relevant: extracts critical lab anomalies using set operations
    critical_markers = {'troponin', 'creatinine', 'bilirubin', 'INR'}
    detected = set(labs.keys())
    critical_hits = detected.intersection(critical_markers)
    flag_count = len(critical_hits)
    
    # Decoy calculation
    decoy_score = sum([labs[m] * 2 for m in critical_hits if m != 'INR']) if 'INR' in labs else 0
    
    # Only this matters
    if 'troponin' in critical_hits and labs['troponin'] > 0.04:
        flag_count += 2  # cardiac alert increases flags
    
    return flag_count


def assess_hydration_status(na_level, urine_concentration):
    # Misleading intermediate result
    if na_level > 145:
        return "hyper"
    elif na_level < 135:
        return "hypo"
    return "normal"

# Main data -- contains red herrings
patient_record = {
    'demographics': {
        'age': 68,
        'height_cm': 174,
        'weight_kg': 82,
        'blood_type': 'A+',
        'smoker': False
    },
    'vitals': {
        'temperature_c': 37.8,
        'heart_rate_bpm': 92,
        'systolic_bp': 148,
        'diastolic_bp': 90,
        'respiratory_rate': 18
    },
    'lab_results': {
        'hemoglobin': 13.4,
        'wbc_count': 9.6,
        'platelets': 210,
        'glucose': 167,
        'sodium': 142,
        'potassium': 4.1,
        'creatinine': 1.9,
        'eGFR': 48,
        'troponin': 0.08,
        'INR': 1.3,
        'bilirubin': 1.7
    },
    'symptoms': ['chest_pain', 'dizziness', 'nausea'],
    'medications': ['atorvastatin', 'lisinopril', 'aspirin']
}

# Irrelevant preprocessing steps
vital_norms = preprocess_vitals(patient_record['vitals'])
symptom_burden = evaluate_symptom_history(patient_record['symptoms'])
organ_risk_score = compute_organ_risk(patient_record['demographics']['age'], patient_record['lab_results'])

# Key variables intermixed with decoys
hydration_status = assess_hydration_status(patient_record['lab_results']['sodium'], 800)
decoy_aggregate = sum(patient_record['vitals'].values()) + sum(patient_record['lab_results'].values())

# Character counting distractor: counts letters in medication names
med_char_count = sum(len(med) for med in patient_record['medications'])

# Central diagnostic logic chain
flag_counter = 0

# Step 1: Age-based baseline risk
if patient_record['demographics']['age'] > 65:
    flag_counter += 1

# Step 2: Blood pressure evaluation
bp_flags = 0
if patient_record['vitals']['systolic_bp'] > 140:
    bp_flags += 1
if patient_record['vitals']['diastolic_bp'] > 90:
    bp_flags += 1
if bp_flags >= 1:
    flag_counter += bp_flags  # two points if both elevated

# Step 3: Use of set operation to detect critical labs (REAL USE)
labs = patient_record['lab_results']
critical_flag_boost = filter_critical_indicators(labs)
flag_counter += critical_flag_boost

# Step 4: eGFR check for kidney function
if labs['eGFR'] < 60:
    flag_counter += 2

# Step 5: Glucose level screening
if labs['glucose'] > 126:
    flag_counter += 1
    if labs['glucose'] > 200:
        flag_counter += 1

# Step 6: Medication interaction side effect check (decoy logic)
interactions = 0
if 'lisinopril' in patient_record['medications'] and labs['potassium'] > 5.0:
    interactions += 1  # not triggered

# Final computation
baseline = 5
multiplier = 3
adjustment = -4

# Complex expression with irrelevant terms
final_diagnostic = baseline + (multiplier * flag_counter) + adjustment
final_diagnostic -= med_char_count * 0  # neutralized term (red herring)

# Output result
print(f"Result: {final_diagnostic}")