def preprocess_vitals(vital_signs):
    # Irrelevant transformation (distractor)
    normalized = {k: v / 100.0 for k, v in vital_signs.items()}
    adjusted = {}
    for k, v in normalized.items():
        if 'heart' in k:
            adjusted[k] = v * 1.05
        elif 'temp' in k:
            adjusted[k] = v * 0.98
    return adjusted

# Decoy data structures (red herring)
diseases_db = {
    'hypertension': {'severity': 3, 'thresholds': [140, 90]},
    'fever': {'severity': 2, 'thresholds': [38, 40]},
    'bradycardia': {'severity': 4, 'thresholds': [50, 60]}
}

# Unused function (dead code path)
def compute_body_mass_index(weight_kg, height_m):
    return round(weight_kg / (height_m ** 2), 2)

# Misleading intermediate calculation (distractor)
suspicious_pattern_count = 0
for i in range(1, 100):
    if i % 7 == 0 and i % 3 != 0:
        suspicious_pattern_count += 1

# Primary patient dataset (relevant)
patient_readings = [
    {'heart_rate': 72, 'temp_c': 36.8, 'systolic': 120, 'oxygen_sat': 98},
    {'heart_rate': 76, 'temp_c': 37.1, 'systolic': 124, 'oxygen_sat': 97},
    {'heart_rate': 80, 'temp_c': 37.3, 'systolic': 128, 'oxygen_sat': 96}
]

# Auxiliary analysis with bit manipulation red herring
status_flags = 0b0
for reading in patient_readings:
    if reading['oxygen_sat'] < 95:
        status_flags |= 0b1000
    if reading['temp_c'] > 38:
        status_flags |= 0b0100

# Unused flag computation (distractor)
extreme_cases = sum(1 for r in patient_readings if r['heart_rate'] > 100 or r['temp_c'] > 39)

# Core diagnostic logic (key path)
def evaluate_stability(readings):
    baseline = readings[0]
    deviations = 0
    for r in readings[1:]:
        if abs(r['heart_rate'] - baseline['heart_rate']) > 5:
            deviations += 1
        if abs(r['temp_c'] - baseline['temp_c']) > 0.5:
            deviations += 1
    return deviations < 3

# Data aggregation using sets (required Python feature)
recorded_metrics = set()
for reading in patient_readings:
    recorded_metrics.update(reading.keys())
expected_metrics = {'heart_rate', 'temp_c', 'systolic', 'oxygen_sat'}
missing_metrics = expected_metrics - recorded_metrics  # Empty set (truth)

# Character counting distractor
metric_chars = sum(len(m) for m in recorded_metrics)

# Modular arithmetic in decoy scoring
pseudo_score = (metric_chars * 17) % 13

# Dictionary-based severity mapper (relevant but indirect)
severity_map = {
    0: 1,
    1: 2,
    2: 3,
    3: 4,
    4: 5
}

# Main analysis function combining multiple concepts
def analyze_patient_data():
    # Step 1: Check metric completeness
    if missing_metrics:
        return -1
    
    # Step 2: Evaluate temporal stability
    stable = evaluate_stability(patient_readings)
    
    # Step 3: Compute average vitals
    avg_heart_rate = sum(r['heart_rate'] for r in patient_readings) / len(patient_readings)
    avg_temp = sum(r['temp_c'] for r in patient_readings) / len(patient_readings)
    
    # Step 4: Apply thresholds
    fever_present = avg_temp >= 37.5
    tachycardia_risk = avg_heart_rate >= 75
    
    # Step 5: Combine into diagnostic index
    diagnostic_index = 0
    if not stable:
        diagnostic_index += 1
    if fever_present:
        diagnostic_index += 1
    if tachycardia_risk:
        diagnostic_index += 1
    
    # Step 6: Map to severity level
    base_severity = severity_map.get(diagnostic_index, 5)
    
    # Step 7: Apply oxygen trend adjustment
    oxygen_trend = [r['oxygen_sat'] for r in patient_readings]
    decompensating = any(oxygen_trend[i] > oxygen_trend[i+1] + 1 for i in range(len(oxygen_trend)-1))
    
    # Step 8: Final adjustment
    final_severity = base_severity + (1 if decompensating else 0)
    
    # Step 9: Cross-check with set cardinality (subtle relevance)
    metric_count_factor = len(recorded_metrics & expected_metrics)  # 4
    
    # Step 10: Final diagnostic computation
    final_diagnostic = (final_severity * 100) + metric_count_factor
    
    return final_diagnostic

# Execute main logic
temp_log = preprocess_vitals({'heart_rate': 75, 'temp_c': 37.0})  # Unused result

final_diagnostic = analyze_patient_data()
print(f"Result: {final_diagnostic}")