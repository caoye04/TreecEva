from collections import defaultdict, Counter
import math

# Simulated patient health monitoring system with diagnostic scoring
def analyze_vital_signs(vitals):
    score = 0
    if 'heart_rate' in vitals:
        hr = vitals['heart_rate']
        if hr > 100:
            score += 2
        elif hr < 60:
            score += 1
    
    # Irrelevant respiratory pattern analysis (distractor)
    if 'respiration' in vitals:
        resp = vitals['respiration']
        for i in range(3):
            resp = max(12, min(20, resp + (-1)**i * 2))  # Noise loop
    
    if 'temperature' in vitals:
        temp = vitals['temperature']
        if temp > 38.0:
            score += 2
    return score

# Out-of-scope utility (dead code path)
def calculate_bmi(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 2)

# Data transformation pipeline with red herrings
def normalize_readings(readings):
    normalized = {}
    factor_map = {'glucose': 0.95, 'cholesterol': 1.03, 'uric_acid': 0.88}
    
    for key, val in readings.items():
        if isinstance(val, str) and 'N/A' in val:
            continue
        if key in factor_map:
            normalized[key] = val * factor_map[key]
        else:
            normalized[key] = val * 1.0  # Identity transform (misleading)
    
    # Decoy computation on stringified data
    checksum = sum(ord(c) for c in str(normalized)) % 1000
    return normalized

# Main processing logic
def evaluate_risk_level(metrics):
    risk = 0
    decoy_sum = 0
    
    for k, v in metrics.items():
        if 'pressure' in k:
            if isinstance(v, tuple) and len(v) == 2:
                systolic, diastolic = v
                if systolic > 140 or diastolic > 90:
                    risk += 3
        elif k == 'hemoglobin':
            if v < 12:
                risk += 2
    
    # Complex irrelevant aggregation (distractor)
    temp_counter = Counter([math.ceil(v) for v in metrics.values() if isinstance(v, (int, float))])
    for val, cnt in temp_counter.items():
        decoy_sum += val * cnt * (cnt % 2)
    
    return risk

# Core diagnostic engine
def process_metrics(data, limits):
    base_score = analyze_vital_signs(data.get('vitals', {}))
    readings = data.get('lab_results', {})
    
    # Normalize lab results (contains distractors)
    cleaned = normalize_readings(readings)
    
    # Key risk evaluation
    risk_level = evaluate_risk_level(cleaned)
    
    # Conditional override logic based on age (partially relevant)
    age = data.get('age', 0)
    modifier = -1 if age < 30 and risk_level > 2 else (1 if age > 65 else 0)
    
    # Integration with decoy variables
    intermediate_flag = False
    accumulator = 0
    for reading in readings.values():
        if isinstance(reading, (int, float)):
            accumulator += abs(reading) % 7
    
    # Red herring: unused complex structure
    patient_profile = defaultdict(lambda: 'unknown')
    patient_profile.update({
        'metabolic_score': sum(cleaned.values()) // (1 + len(cleaned)),
        'toxic_load': math.log(accumulator + 1),
        'stress_index': base_score * 2 + modifier
    })
    
    # Final calculation — only this matters
    final_diagnostic = (base_score * 10) + risk_level + modifier
    
    # Misleading print simulation
    debug_trace = f"Diag-{final_diagnostic % 11}".replace('0', 'X')
    
    return final_diagnostic

# Input data with mixed types and noise
thresholds = {'critical': 5, 'warning': 3}
health_data = {
    'patient_id': 'P-7812',
    'age': 72,
    'vitals': {
        'heart_rate': 108,
        'temperature': 38.7,
        'respiration': 18
    },
    'lab_results': {
        'cholesterol': 240,
        'glucose': 110,
        'blood_pressure': (148, 88),
        'hemoglobin': 11.5,
        'uric_acid': 7.1
    },
    'notes': 'Patient reports fatigue'.upper()
}

# Execute main logic
final_diagnostic = process_metrics(health_data, thresholds)
print(f"Target result: {final_diagnostic}")