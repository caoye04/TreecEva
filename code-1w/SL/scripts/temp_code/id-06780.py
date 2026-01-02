def analyze_vital(vital, baseline):
    if vital < baseline * 0.8:
        return 'LOW'
    elif vital > baseline * 1.2:
        return 'HIGH'
    return 'NORMAL'


def compute_risk_score(age, markers):
    base_score = age / 100
    modifier = sum([1 for m in markers if m == 'ELEVATED']) * 0.1
    return round(base_score + modifier, 4)

# Irrelevant helper (distractor)
def decrypt_code(token):
    return sum(ord(c) * i for i, c in enumerate(token)) % 1000

current_token = 'X9F2M1'
decrypted_key = decrypt_code(current_token)

# Simulated patient health data
vital_signs = [
    {'hr': 72, 'bp': 120, 'temp': 36.8},
    {'hr': 84, 'bp': 138, 'temp': 37.5},
    {'hr': 63, 'bp': 112, 'temp': 36.1}
]

# Unused alternate data structure (dead path)
patient_matrix = [[72, 120], [84, 138]]

baseline_standards = {
    'hr': 75,
    'bp': 130,
    'temp': 36.6
}

risk_markers = []
status_log = []

for i, reading in enumerate(vital_signs):
    hr_status = analyze_vital(reading['hr'], baseline_standards['hr'])
    bp_status = analyze_vital(reading['bp'], baseline_standards['bp'])
    temp_status = analyze_vital(reading['temp'], baseline_standards['temp'])
    
    # Accumulate real risk markers
    if hr_status != 'NORMAL' or bp_status != 'NORMAL':
        risk_markers.append('ELEVATED')
    else:
        risk_markers.append('STABLE')
        
    # Log status (distractor output)
    status_log.append(f"Patient {i+1}: HR={hr_status}, BP={bp_status}")

# Decoy accumulation (red herring)
summary_hash = 0
for char in 'health_summary':
    summary_hash += ord(char) % 17

# Real threshold logic
thresholds = {
    'age_cutoff': 65,
    'marker_count_critical': 2
}

patient_age = 68

# Simulated secondary system check (irrelevant)
def validate_device(signal_strength, calibration):
    return signal_strength > 5 and calibration in ['OK', 'CALIBRATED']

device_status = validate_device(7, 'OK')
device_id = 'VITAL-SCAN-02'

# Core aggregation function

def aggregate_metrics(data, config):
    critical_count = 0
    temp_anomalies = 0
    
    # Process each entry
    for idx, record in enumerate(data):
        # Only temp used here (misleading: others seem relevant)
        deviation = abs(record['temp'] - baseline_standards['temp'])
        if deviation > 0.4:
            temp_anomalies += 1
        
        # Real logic: count abnormal temps
        if record['temp'] < 36.3 or record['temp'] > 37.2:
            critical_count += 1

    # Secondary condition based on risk markers
    high_risk_episodes = len([m for m in risk_markers if m == 'ELEVATED'])
    
    # Main diagnostic score
    base_diagnostic = critical_count * 100
    
    # Age adjustment
    if patient_age >= config['age_cutoff']:
        base_diagnostic += 50
    
    # Final nonlinear adjustment
    if high_risk_episodes >= config['marker_count_critical']:
        base_diagnostic *= 1.2
    
    return int(round(base_diagnostic))

# Execution point of interest
final_diagnostic = aggregate_metrics(vital_signs, thresholds)

# Print required result
print(f"Result: {final_diagnostic}")