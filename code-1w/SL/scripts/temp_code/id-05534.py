def preprocess_vitals(vital_signs):
    # Irrelevant preprocessing: normalizes values that aren't used later
    normalized = {}
    for k, v in vital_signs.items():
        if v > 0:
            normalized[k] = round((v - 37) / 1.5, 2)  # Arbitrary normalization
        else:
            normalized[k] = v
    return normalized

# Misleading dataset with unused entries
temp_history = [36.5, 37.1, 38.3, 39.0, 37.8, 36.9, 40.2]
heart_rates = [72, 85, 93, 102, 88, 76, 115]
blood_pressure_readings = [(120, 80), (130, 85), (145, 90), (150, 95)]

patient_symptoms = {"fever": True, "cough": False, "fatigue": True, "headache": True}
symptom_score = 0
for symptom in patient_symptoms:
    if symptom == "fever":
        symptom_score += 3
    elif symptom == "cough":
        symptom_score += 1
    elif symptom == "fatigue":
        symptom_score += 2
    elif symptom == "headache":
        symptom_score += 1

# Dead code path: never called
def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 2)

unused_lab_results = {
    "wbc_count": 12.4,
    "rbc_count": 4.8,
    "hemoglobin": 14.2,
    "platelets": 220
}

# Distractor: complex but irrelevant transformation
transformed_labs = set()
for key, val in unused_lab_results.items():
    if 'count' in key:
        transformed_labs.add(int(val))

# Real data path begins here
vital_signs = {'temp': 38.7, 'hr': 98, 'rr': 20}
vital_flags = set()
if vital_signs['temp'] > 38:
    vital_flags.add('fever')
if vital_signs['hr'] > 95:
    vital_flags.add('tachycardia')
if vital_signs['rr'] > 20:
    vital_flags.add('tachypnea')

# Simulated lab markers
inflammatory_markers = [8.5, 12.1, 9.3, 14.0, 11.7]

# Red herring: sorting and searching unused data
inflammatory_markers.sort()  # Sort but not re-assigned visibly
high_markers = [m for m in inflammatory_markers if m > 10]
first_elevated_index = -1
for i in range(len(inflammatory_markers)):
    if inflammatory_markers[i] > 10:
        first_elevated_index = i
        break

# Actual diagnostic logic (obscured by noise)
def assess_inflammation_level(markers, threshold=10):
    count_above = sum(1 for m in markers if m > threshold)
    if count_above >= 4:
        return 3
    elif count_above >= 2:
        return 2
    elif count_above >= 1:
        return 1
    else:
        return 0

# Another decoy function
def evaluate_chronic_conditions(condition_list):
    risk_factors = set()
    chronic_diseases = ['diabetes', 'hypertension', 'asthma']
    for cond in condition_list:
        if cond in chronic_diseases:
            risk_factors.add(cond)
    return len(risk_factors)

# Core analysis
comorbidities = ['asthma']  # Used to influence final score indirectly

# Unused imaging data
chest_xray_findings = {"opacity": False, "effusion": False}

# Key logic buried in middle
base_risk = assess_inflammation_level(inflammatory_markers)

# Bit manipulation red herring
encoded_state = 0
for i, m in enumerate(inflammatory_markers):
    if m > 11:
        encoded_state |= (1 << i)

# Real calculation chain
inflammatory_risk = base_risk
symptom_severity = len(patient_symptoms)

# Conditional branching with early exit red herring
for bp in blood_pressure_readings:
    systolic, diastolic = bp
    if systolic > 140:
        # This block runs but doesn't affect final result
        inflammatory_risk += 1
        break  # Early exit, but only adds 1 once

# Critical logic step: set intersection determines actual weight
known_fever_causes = {'infection', 'inflammation', 'autoimmune'}
patient_clues = {'fever', 'tachycardia', 'inflammation'}
clinical_overlap = known_fever_causes.intersection({'inflammation'})  # Only one real match

overlap_bonus = len(clinical_overlap) * 2

# Final diagnosis score computation
final_diagnostic = 0
final_diagnostic += inflammatory_risk * 8
final_diagnostic += symptom_severity * 3
final_diagnostic += overlap_bonus

if 'tachycardia' in vital_flags:
    final_diagnostic += 5

# Decoy assignment below — does not overwrite
final_diagnostic_temp = final_diagnostic + 100

# The true final value
final_diagnostic = analyze_patient_data() if 'analyze_patient_data' in globals() else final_diagnostic

# Actual function definition at the end to confuse control flow
def analyze_patient_data():
    # Recomputes only essential parts
    reevaluated_inflammation = assess_inflammation_level(inflammatory_markers)
    fever_present = vital_signs['temp'] > 38
    tachycardia_present = vital_signs['hr'] > 95
    bonus = 2 if 'inflammation' in clinical_overlap else 0
    result = reevaluated_inflammation * 8
    result += 4  # Base from symptoms (fixed in this path)
    result += bonus
    if tachycardia_present and fever_present:
        result += 5
    return result

# Print final result as required
Target result: {analyze_patient_data()}