from collections import defaultdict, Counter

# Simulated medical diagnostic system with red herrings and complex logic
def process_vitals(vital_signs):
    # Irrelevant transformation (distraction)
    transformed = {k: v * 1.05 for k, v in vital_signs.items()}
    adjusted = {}
    for key, value in transformed.items():
        if key == 'temperature':
            adjusted[key] = value - 0.5
        elif key == 'heart_rate':
            adjusted[key] = value + 3
        else:
            adjusted[key] = value
    return adjusted

def compute_risk_score(age, biomarkers):
    # Misleading risk model with unused branches
    base_score = 0
    if age > 65:
        base_score += 20
    elif age > 40:
        base_score += 10
    else:
        base_score += 5

    flag = False
    if 'glucose' in biomarkers and biomarkers['glucose'] > 140:
        base_score += 15
        flag = True  # Dead assignment

    # Complex but irrelevant scoring branch
    if 'cholesterol' in biomarkers:
        if biomarkers['cholesterol'] > 240:
            base_score += 25
        elif biomarkers['cholesterol'] > 200:
            pass  # Red herring logic

    # Decoy calculation
    temp_score = 0
    for marker in ['creatinine', 'alt', 'ast']:
        if marker in biomarkers:
            temp_score += biomarkers[marker] // 10

    return base_score  # temp_score never used

def validate_symptoms(symptoms):
    # Unused validation function (dead code path)
    critical = ['chest_pain', 'shortness_of_breath', 'dizziness']
    count = sum(1 for s in symptoms if s in critical)
    return count >= 2

def normalize_lab_values(labs):
    # Distractor normalization
    norms = {}
    for test, val in labs.items():
        if test == 'wbc':
            norms[test] = round(val / 4.5, 2)
        elif test == 'rbc':
            norms[test] = round(val * 0.88, 2)
        else:
            norms[test] = val
    return norms

def analyze_patient_data(record):
    # Core logic embedded in noise
    vitals = record.get('vitals', {})
    labs = record.get('labs', {})
    history = record.get('history', [])
    
    # Key processing step (obscured)
    processed_vitals = process_vitals(vitals)
    temperature_status = processed_vitals['temperature'] > 37.5
    heart_rate_status = processed_vitals['heart_rate'] > 100
    
    # Real condition check (hidden among distractions)
    acute_flags = 0
    if temperature_status:
        acute_flags += 1
    if heart_rate_status:
        acute_flags += 1
    
    # Lab-based detection
    infection_markers = defaultdict(int)
    for test, value in labs.items():
        test_lower = test.lower()
        if 'crp' in test_lower or 'esr' in test_lower:
            infection_markers['inflammatory'] += 1
        if value > 180 and test_lower == 'procalcitonin':
            infection_markers['sepsis_indicator'] = value
    
    # Critical decision logic (non-obvious)
    sepsis_risk = 0
    if infection_markers['inflammatory'] >= 1:
        sepsis_risk += 30
    if 'sepsis_indicator' in infection_markers:
        sepsis_risk += 70  # Only triggered if procalcitonin > 180
    
    # Final determination based on multiple layers
    comorbidities_score = len([h for h in history if h in ['diabetes', 'immunocompromised']])
    
    # Primary answer derivation
    if sepsis_risk >= 70 and acute_flags >= 1:
        final_level = 3
    elif sepsis_risk >= 50 or (acute_flags >= 1 and comorbidities_score > 0):
        final_level = 2
    elif acute_flags >= 1:
        final_level = 1
    else:
        final_level = 0
    
    # Decoy aggregations
    summary_stats = Counter(['low', 'medium', 'high'])
    for _ in range(3):
        summary_stats['medium'] -= 1  # Irrelevant mutation
    
    # Actual output variable
    final_diagnostic = final_level * 250 + (sepsis_risk // 10)
    
    # Print required for traceability
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated patient data
patient_record = {
    'vitals': {
        'temperature': 38.2,
        'heart_rate': 112,
        'blood_pressure': 130
    },
    'labs': {
        'wbc': 14.5,
        'crp': 45,
        'procalcitonin': 210  # Triggers high sepsis risk
    },
    'history': ['diabetes']
}

# Execution point
final_diagnostic = analyze_patient_data(patient_record)