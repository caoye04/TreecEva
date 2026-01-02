def preprocess_vitals(vital_signs):
    # Irrelevant transformation: normalizes values that aren't used later
    normalized = {k: round((v - 37) / 0.5, 2) for k, v in vital_signs.items() if 'temp' in k}
    return normalized


def compute_bmi(height_cm, weight_kg):
    # Distractor function: BMI is calculated but not part of final logic
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def assess_risk(age, has_comorbidity):
    # Misleading risk score with dead-end logic
    base_risk = 5 if age > 60 else 2
    if has_comorbidity:
        base_risk += 4
    risk_category = 'high' if base_risk >= 7 else 'moderate'
    return risk_category  # Not used in final path


def filter_abnormal_reads(readings):
    # Real processing: filters and aggregates EEG spike counts
    spikes = [r['spike_count'] for r in readings if r['quality'] == 'valid']
    threshold = 15
    abnormal = [s for s in spikes if s > threshold]
    return len(abnormal), sum(spikes) // len(spikes) if spikes else 0


def analyze_patient_data():
    # Main data structure with multiple irrelevant fields
    patient = {
        'name': 'John Doe',
        'age': 68,
        'weight_kg': 76.5,
        'height_cm': 174,
        'has_comorbidity': True,
        'temperature_c': 36.8,
        'blood_pressure': '142/90',
        'allergies': [],
        'medications': ['statin']
    }

    vitals = {
        'temp_core': 37.1,
        'temp_surface': 36.8,
        'heart_rate': 74,
        'respiratory_rate': 16,
        'o2_saturation': 97
    }

    # EEG readings – actual source of answer-related data
    eeg_readings = [
        {'timestamp': '13:01', 'spike_count': 12, 'quality': 'valid'},
        {'timestamp': '13:02', 'spike_count': 18, 'quality': 'valid'},
        {'timestamp': '13:03', 'spike_count': 5, 'quality': 'invalid'},  # filtered out
        {'timestamp': '13:04', 'spike_count': 21, 'quality': 'valid'},
        {'timestamp': '13:05', 'spike_count': 8, 'quality': 'valid'},
        {'timestamp': '13:06', 'spike_count': 19, 'quality': 'valid'}
    ]

    # Irrelevant preprocessing
    processed_vitals = preprocess_vitals(vitals)
    bmi = compute_bmi(patient['height_cm'], patient['weight_kg'])
    risk_level = assess_risk(patient['age'], patient['has_comorbidity'])

    # Set operation distractor: computes unique timestamps (not used)
    valid_times = {r['timestamp'] for r in eeg_readings if r['quality'] == 'valid'}
    time_count = len(valid_times)

    # String method distractor: analyzes medication names
    med_analysis = ''.join(patient['medications']).upper().replace('IN', 'IN-')

    # Core logic embedded among distractions
    abnormal_count, avg_spike = filter_abnormal_reads(eeg_readings)
    
    # Decision logic based on EEG data
    if abnormal_count >= 3:
        severity = 85
    elif abnormal_count == 2:
        severity = 45
    else:
        severity = 15
    
    # Final computation using average spike count as modifier
    adjustment = (avg_spike - 10)  # Base adjustment from empirical norm
    final_diagnostic = severity + adjustment
    
    # Dead code path: never executed due to fixed conditions above
    if patient.get('fake_flag', False):
        final_diagnostic *= -1
    
    return final_diagnostic

# Execution point
final_diagnostic = analyze_patient_data()
print(f"Result: {final_diagnostic}")