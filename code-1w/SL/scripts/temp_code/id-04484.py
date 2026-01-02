from collections import defaultdict, Counter
import math

# Simulated patient diagnostic system with noise and red herrings
def collect_vitals():
    return {
        'heartrate': 78,
        'bp_systolic': 124,
        'bp_diastolic': 82,
        'temperature': 36.8,
        'respiration': 16
    }

def collect_lab_results():
    # Irrelevant lab data (distractor)
    return {
        'cholesterol': 198,
        'vitamin_d': 32,
        'iron_level': 67,
        'wbc_count': 7.2
    }

def preprocess_data(raw_vitals):
    processed = defaultdict(float)
    for k, v in raw_vitals.items():
        if 'bp_' in k:
            processed[k] = v + 5  # Artificial adjustment (red herring)
        else:
            processed[k] = v
    # Extra transformation that isn't used later (dead code path)
    processed['fake_index'] = (processed['bp_systolic'] + processed['bp_diastolic']) / 20
    return processed

def extract_symptom_score(vitals):
    # Real logic: compute a hidden symptom severity score
    hr = vitals['heartrate']
    temp = vitals['temperature']
    resp = vitals['respiration']
    
    base_score = hr * 0.1
    if temp > 37.0:
        base_score += 8.5
    elif temp < 36.0:
        base_score += 6.2
    else:
        base_score += 4.3

    # Respiratory adjustment
    if resp > 20 or resp < 12:
        base_score += 7.1
    else:
        base_score += 3.4

    # Bit manipulation distraction (not actually affecting result)
    magic_flag = (hr ^ 17) & 7
    if magic_flag > 4:
        base_score += 1.5  # This always triggers but is part of misdirection

    return round(base_score, 4)

def generate_fallback_profile(labs):
    # Unused function - dead code path (decoy)
    profile = Counter()
    for test, value in labs.items():
        if value < 50:
            profile['deficiency'] += 1
        elif value > 200:
            profile['elevated'] += 1
    return profile

def evaluate_stress_markers(vitals):
    # Distractor function: looks important but not used in final chain
    stress_index = 0
    if vitals['heartrate'] > 80:
        stress_index += 10
    if vitals.get('fake_index', 0) > 10:
        stress_index += 5
    return stress_index * 1.5

def analyze_symptoms(data, threshold_config):
    # Core logic hidden among distractions
    raw_vitals = data['vitals']
    symptoms = data['presenting_symptoms']  # cough, fatigue, etc.
    
    # Preprocess (includes irrelevant modifications)
    vitals = preprocess_data(raw_vitals)
    
    # Real calculation begins here
    score = extract_symptom_score(vitals)
    
    # Conditional logic with short-circuiting red herring
    adjustment = 0
    if 'fever' in symptoms and vitals['temperature'] > 37.5:
        adjustment += 12.0
    elif 'fatigue' in symptoms or 'headache' in symptoms:
        adjustment += 5.0  # This applies
    else:
        adjustment += 2.0
    
    # Multiple assignments distraction
    a, b, c = 3.1, 6.2, 9.3
    temp_var = (a * b) / c  # 2.0, irrelevant
    
    # Real adjustment uses bitwise logic disguised as noise
    flags = 0
    if vitals['bp_systolic'] > 120: flags |= 1
    if vitals['bp_diastolic'] > 80: flags |= 2
    if flags == 3:  # Both high → hypertension flag
        adjustment += 8.0  # This applies

    total_risk = score + adjustment
    
    # Final threshold comparison (key logic)
    if total_risk >= threshold_config['critical']:
        diagnosis_code = 9
    elif total_risk >= threshold_config['moderate']:
        diagnosis_code = 6
    else:
        diagnosis_code = 3
    
    # The actual answer is derived from bit operation on diagnosis code
    # Hidden relationship: final_diagnostic = diagnosis_code << 2 (i.e., *4)
    final_diagnostic = diagnosis_code << 2  # Equivalent to *4
    
    # Decoy print and unused variables
    debug_snapshot = f"Risk={total_risk:.2f}, Code={diagnosis_code}"
    dummy_array = [0] * 5
    for i in range(len(dummy_array)):
        dummy_array[i] = i * final_diagnostic // 2  # Dead computation
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Gather real and fake data
    raw_vitals = collect_vitals()
    lab_results = collect_lab_results()  # Collected but not used
    
    # Build patient data structure
    patient_data = {
        'vitals': raw_vitals,
        'presenting_symptoms': ['fatigue', 'cough'],
        'age': 47,
        'weight': 72.5
    }
    
    # Threshold configuration (only these matter)
    thresholds = {
        'mild': 10.0,
        'moderate': 15.0,
        'critical': 25.0
    }
    
    # Execute key statement
    final_diagnostic = analyze_symptoms(patient_data, thresholds)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")