def preprocess_vitals(vital_signs):
    # Irrelevant transformation: normalize values (not used in final logic)
    normalized = {k: round(v / max(vital_signs.values()), 3) for k, v in vital_signs.items()}
    return normalized


def compute_urgency_index(temp, hr, rr):
    # Distractor function: computes an index never used
    score = 0.3 * (temp - 98.6) + 0.2 * (hr - 75) + 0.5 * (rr - 20)
    return round(score, 3)


def filter_abnormal_entries(records, limits):
    # Dead code path — this function is defined but not invoked
    filtered = {}
    for patient_id, readings in records.items():
        if any(readings[k] < limits[k][0] or readings[k] > limits[k][1] for k in readings):
            filtered[patient_id] = readings
    return filtered

# Simulated patient data (real input)
patient_records = {
    'P001': {'temperature': 101.3, 'heart_rate': 110, 'respiratory_rate': 24, 'systolic_bp': 145},
    'P002': {'temperature': 98.7, 'heart_rate': 88, 'respiratory_rate': 22, 'systolic_bp': 138},
    'P003': {'temperature': 96.4, 'heart_rate': 55, 'respiratory_rate': 16, 'systolic_bp': 110},
    'P004': {'temperature': 102.1, 'heart_rate': 122, 'respiratory_rate': 30, 'systolic_bp': 158}
}

# Thresholds for analysis (used in actual logic)
thresholds = {
    'fever': (100.4, float('inf')),
    'tachycardia': (100, float('inf')),
    'tachypnea': (20, float('inf')),
    'hypertension': (140, float('inf'))
}

# Misleading intermediate variables (distractors)
mock_analysis = [compute_urgency_index(p['temperature'], p['heart_rate'], p['respiratory_rate']) 
                   for p in patient_records.values()]
baseline_stats = {'avg_temp': sum(p['temperature'] for p in patient_records.values()) / len(patient_records)}

# Auxiliary diagnostic mapping (used in real logic)
diagnostic_map = {
    0: 'stable',
    1: 'monitored',
    2: 'elevated',
    3: 'critical'
}

# Real processing begins here
abnormal_flags = []
for pid, vitals in patient_records.items():
    flag_count = 0
    if thresholds['fever'][0] <= vitals['temperature']:
        flag_count += 1
    if thresholds['tachycardia'][0] <= vitals['heart_rate']:
        flag_count += 1
    if thresholds['tachypnea'][0] <= vitals['respiratory_rate']:
        flag_count += 1
    if thresholds['hypertension'][0] <= vitals['systolic_bp']:
        flag_count += 1
    abnormal_flags.append(flag_count)

# Linear search for maximum severity index (actual relevant step)
max_severity = 0
for i in range(len(abnormal_flags)):
    if abnormal_flags[i] > max_severity:
        max_severity = abnormal_flags[i]

# Tuple unpacking - irrelevant to outcome
(_, _, last_temp, last_bp) = tuple(patient_records['P004'].values())

# Set operations: collect unique severity levels (red herring)
severity_set = set(abnormal_flags)
high_risk_count = len([f for f in abnormal_flags if f >= 2])

# Actual key computation
severity_code = len(severity_set) * max_severity

def analyze_patient_data(records, config):
    # Core logic hidden among distractions
    total_critical = 0
    for data in records.values():
        conditions_met = 0
        if data['temperature'] >= config['fever'][0]:
            conditions_met += 1
        if data['heart_rate'] >= config['tachycardia'][0]:
            conditions_met += 1
        if data['respiratory_rate'] >= config['tachypnea'][0]:
            conditions_met += 1
        if data['systolic_bp'] >= config['hypertension'][0]:
            conditions_met += 1
        if conditions_met >= 3:
            total_critical += 1
    category_index = diagnostic_map.get(total_critical, 'unknown')
    # Final result derived from count and mapping
    lookup_value = list(diagnostic_map.keys())[list(diagnostic_map.values()).index(category_index)]
    return severity_code + lookup_value

# Execute main logic
temp_snapshot = preprocess_vitals(patient_records['P001'])
final_diagnostic = analyze_patient_data(patient_records, thresholds)
print(f"Target result: {final_diagnostic}")